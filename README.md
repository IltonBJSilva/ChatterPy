
# 🚀 Chat em Tempo Real com Python e WebSockets

Bem-vindo ao projeto de um chat em tempo real simples, construído com  **Python** , **FastAPI** e  **WebSockets** ! Este projeto foi desenvolvido com foco em aprendizado e serve como uma base robusta para entender os fundamentos da comunicação bi-direcional em tempo real na web.

---

## 🎯 Sobre o Projeto

Este projeto implementa um sistema de chat básico onde múltiplos usuários podem se conectar e trocar mensagens instantaneamente. Ele demonstra o poder dos **WebSockets** para criar experiências interativas, indo além do tradicional modelo de requisição/resposta do HTTP.

**Funcionalidades Atuais:**

* **Conexão em Tempo Real:** Utiliza WebSockets para uma comunicação persistente e instantânea entre cliente e servidor.
* **Múltiplos Usuários:** Suporta a conexão de diversos clientes simultaneamente.
* **Identificação de Usuário:** Cada usuário pode inserir um nome de sua escolha ao entrar no chat.
* **Broadcast de Mensagens:** Mensagens enviadas por um usuário são retransmitidas para todos os outros usuários conectados.

---

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **FastAPI:** Framework web moderno e de alta performance para construir a API e o servidor WebSocket.
* **Uvicorn:** Servidor ASGI (Asynchronous Server Gateway Interface) para rodar a aplicação FastAPI.
* **WebSockets (JavaScript API):** No lado do cliente (navegador) para estabelecer e gerenciar a conexão com o servidor.
* **HTML, CSS, JavaScript:** Para o desenvolvimento do frontend simples do chat.

---

## 📦 Como Rodar o Projeto (Passo a Passo)

Siga estes passos para configurar e executar o chat em sua máquina local:

### 1. Pré-requisitos

Certifique-se de ter o **Python 3.7+** instalado em seu sistema.

### 2. Configuração do Ambiente

1. **Clone este repositório (se ainda não o fez):**

   **Bash**

   ```
   git clone [LINK_DO_SEU_REPOSITORIO]
   cd chat_websocket_py
   ```

   *(**Nota:** Substitua `[LINK_DO_SEU_REPOSITORIO]` pelo link real do seu repositório Git, se estiver usando um.)*
2. **Crie um ambiente virtual (altamente recomendado):**

**    python -m venv venv

```**


**
**3. **
   ****Ative o ambiente virtual:**


   **
   *** **No Windows:**
     **Bash**


     ```
     .\venv\Scripts\activate
     ```

   * **No macOS/Linux:**
     **Bash**


     ```
     source venv/bin/activate
     ```

3. **
   ****Instale as dependências^^ do projeto:**


   **Bash**


```

   pip install fastapi uvicorn websockets

```

### 3. Executando o Servidor

1. Com o ambiente virtual ativado, execute o servidor FastAPI usando Uvicorn:

   **Bash**


```

   uvicorn main:app --reload

```





   *O flag `--reload` é útil durante o desenvolvimento, pois o servidor será reiniciado automaticamente a cada alteração no código.*

   Você verá uma mensagem indicando que o servidor está rodando, geralmente em `http://127.0.0.1:8000` ou `http://localhost:8000`.

### 4. Abrindo o Cliente no Navegador

1. Abra o arquivo `index.html` em seu navegador web preferido. Você pode simplesmente arrastar e soltar o arquivo na janela do navegador ou abrir via `Ctrl+O`/`Cmd+O`.
1. Você verá uma tela de login simples. Digite o nome de usuário que deseja usar e clique em "Entrar no Chat".
1. Para testar com múltiplos usuários, abra `index.html` em outras abas do navegador ou em diferentes navegadores, usando nomes de usuário distintos.

---

## 💡 Próximos Passos e Desafios

Este projeto é um ponto de partida. Há muitas melhorias e funcionalidades que podem ser adicionadas para aprofundar o aprendizado:

* **Salas de Chat:** Implementar a capacidade de criar e entrar em salas de chat diferentes.
* **Mensagens Privadas:** Permitir que usuários enviem mensagens diretamente para um usuário específico.
* **Persistência de Dados:** Salvar o histórico de mensagens em um banco de dados.
* **Notificações de Entrada/Saída:** Exibir mensagens quando um usuário entra ou sai do chat.
* **Gerenciamento de Conexões:** Melhorar a forma como o servidor lida com conexões ativas e inativas.
* **Tratamento de Erros:** Adicionar tratamento mais robusto para mensagens inválidas ou desconexões inesperadas.

---

## 🤝 Contribuição

Este é um projeto de estudo pessoal. Sinta-se à vontade para explorar o código, adaptá-lo e usá-lo como base para seus próprios experimentos. Se tiver sugestões ou ideias, pode registrar uma issue.

---

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.
```
