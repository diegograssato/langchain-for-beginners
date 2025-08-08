import streamlit as st
import agent as Agente


agent = Agente.Agente()

def retonar_simple_chain(question: str):

    resultado = agent.simple_chain(question)

    st.write("🔍 Resposta para o termo encontrado...")
    st.success("Resposta:")
    st.write(resultado["text"])

    with st.expander("📚 Termos utilizados"):
        st.write(resultado["termo"] + "...")


def retonar_retrival_response(question: str):

    resultado = agent.retrival_response(question)

    st.write("🔍 Resposta para o termo encontrado...")
    st.success("Resposta:")
    st.write(resultado["result"])

    with st.expander("📚 Fontes utilizadas"):
        for i, doc in enumerate(resultado["source_documents"]):
            st.markdown(f"**Fonte {i+1}:**")
            st.write(doc.page_content[:500] + "...")



# Configuração da página
st.set_page_config(page_title="Assistente Booking.com", layout="centered")
st.title("📄 Assistente Booking com RAG")
st.markdown("Faça uma pergunta sobre o conteúdo do PDF do Booking.com.")

pergunta = st.text_input("Digite sua pergunta:")
# Botão para enviar a pergunta
if st.button("Responder") and pergunta:
    # with st.spinner("🔍Consultando termos..."):
    #     retonar_simple_chain(pergunta)

    with st.spinner("Consultando documentos..."):
        retonar_retrival_response(pergunta)

