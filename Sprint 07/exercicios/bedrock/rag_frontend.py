import streamlit as st 
import rag_backend as demo  # Substitua "rag_backend" pelo nome do arquivo do backend

st.set_page_config(page_title="HR Q and A with RAG")  # Define o título da página

# Define um título estilizado usando HTML
new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">HR Q & A with RAG 🎯</p>'
st.markdown(new_title, unsafe_allow_html=True)  # Exibe o título na página

# Verifica se o índice vetorial já foi carregado na sessão
if 'vector_index' not in st.session_state: 
    with st.spinner("💀 Aguarde a mágica... Todas as coisas bonitas na vida levam tempo :-)"):
        st.session_state.vector_index = demo.hr_index()  # Chama a função que carrega o índice vetorial

# Cria uma área de texto para entrada do usuário
input_text = st.text_area("Input text", label_visibility="collapsed") 

# Cria um botão personalizado
go_button = st.button("📌Aprenda GenAI com Rahul Trisal", type="primary")  

# Se o botão for pressionado
if go_button: 
    with st.spinner(" 📢 Sempre que alguém me diz que não posso fazer algo, eu quero fazer ainda mais - Taylor Swift"):
        response_content = demo.hr_rag_response(index=st.session_state.vector_index, question=input_text)  # Chama a função do backend para obter a resposta
        st.write(response_content)  # Exibe a resposta na tela
