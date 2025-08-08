import streamlit as st
import agent as Agente


agent = Agente.Agente()

import streamlit as st

st.set_page_config(page_title="Assistente Booking.com", layout="centered")
st.title("💬 Assistente Booking com RAG")

# Campo para nome do usuário
if "nome_usuario" not in st.session_state:
    with st.form("form_nome"):
        nome = st.text_input("Digite seu nome para iniciar a conversa:")
        submitted = st.form_submit_button("Entrar no chat")
        if submitted and nome:
            st.session_state.nome_usuario = nome.strip()

# Garante que nome seja preenchido antes de prosseguir
if "nome_usuario" not in st.session_state:
    st.stop()

# Usa o nome como session_id
session_id = st.session_state.nome_usuario

# Inicializa o histórico de mensagens no Streamlit
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Exibe histórico
for role, mensagem in st.session_state.chat_history:
    display_name = session_id if role == "user" else "Assistente"
    with st.chat_message(role):
        st.markdown(display_name + ": " + mensagem)

# Entrada tipo chat
prompt = st.chat_input(f"{session_id}, escreva sua pergunta...")

if prompt:
    # Mostra a pergunta do usuário
    with st.chat_message("user"):
        st.markdown(session_id + ": " + prompt)
    st.session_state.chat_history.append(("user", prompt))

    # Consulta o agente com o histórico persistido via SQLite
    with st.spinner("Consultando documentos..."):
        resposta = agent.retrival_response_with_historical(prompt, session_id)
        resposta_texto = resposta["result"]
        fontes = resposta.get("source_documents", [])

    # Mostra a resposta do assistente
    with st.chat_message("assistant"):
        st.markdown("Assistente: " + resposta_texto)

        if fontes:
            with st.expander("📚 Fontes utilizadas"):
                for i, doc in enumerate(fontes):
                    st.markdown(f"**Fonte {i+1}:**")
                    st.write(doc.page_content[:500] + "...")

    st.session_state.chat_history.append(("assistant", resposta_texto))
