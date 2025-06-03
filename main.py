# main.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List, Dict
import json # Importar para lidar com JSON

app = FastAPI()

# Uma lista para armazenar as conexões ativas, agora com o nome do usuário
# Será uma lista de dicionários: {"websocket": WebSocket, "username": str}
active_connections: List[Dict] = []

@app.get("/")
async def get_root():
    return {"message": "Servidor de chat rodando!"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # Temporariamente adiciona a conexão sem nome de usuário
    # O nome de usuário será recebido na primeira mensagem
    active_connections.append({"websocket": websocket, "username": "Anônimo"})
    current_user_info = None # Para armazenar as informações deste usuário

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data) # Tenta parsear a mensagem como JSON

            if message.get("type") == "username":
                # Se for a primeira mensagem e contiver o nome de usuário
                new_username = message.get("username", "Anônimo")
                # Encontra a conexão atual e atualiza o nome de usuário
                for conn_info in active_connections:
                    if conn_info["websocket"] == websocket:
                        conn_info["username"] = new_username
                        current_user_info = conn_info
                        print(f"Usuário conectado: {new_username} ({websocket.client.host}:{websocket.client.port})")
                        await websocket.send_text(f"Bem-vindo(a) ao chat, {new_username}!")
                        # Notifica outros usuários que alguém entrou (opcional)
                        # for conn in active_connections:
                        #     if conn["websocket"] != websocket:
                        #         await conn["websocket"].send_text(f"<em>{new_username} entrou no chat.</em>")
                        break
            elif message.get("type") == "chat_message":
                chat_message = message.get("message")
                sender_username = "Anônimo"
                if current_user_info:
                    sender_username = current_user_info["username"]

                # Prepara a mensagem para broadcast (agora como JSON)
                response_message = {
                    "type": "chat_message",
                    "sender": sender_username,
                    "message": chat_message
                }

                # Envia a mensagem para todos os clientes conectados
                for connection_info in active_connections:
                    try:
                        await connection_info["websocket"].send_text(json.dumps(response_message))
                    except RuntimeError: # Lida com casos onde a conexão pode ter sido fechada
                        print(f"Erro ao enviar para {connection_info['username']}, removendo.")
                        active_connections.remove(connection_info)

    except WebSocketDisconnect:
        # Encontra e remove a conexão desconectada
        if current_user_info:
            active_connections.remove(current_user_info)
            print(f"Usuário desconectado: {current_user_info['username']} ({websocket.client.host}:{websocket.client.port})")
            # Notifica outros usuários que alguém saiu (opcional)
            # for conn in active_connections:
            #     await conn["websocket"].send_text(f"<em>{current_user_info['username']} saiu do chat.</em>")
        else:
            print(f"Cliente anônimo desconectado: {websocket.client.host}:{websocket.client.port}")


# Para rodar o servidor, execute no terminal:
# uvicorn main:app --reload