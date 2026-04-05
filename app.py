import streamlit as st
import pandas as pd
import json
import requests

# Configuração de Interface de Alto Nível - Onyx & Bronze
st.set_page_config(page_title="Edu - Elite Financial Mentor", page_icon="🏛️")

# Estética Personalizada: Fundo Preto Puro e Ouro/Bronze
st.markdown("""
    <style>
    .main { background-color: #000000; color: #CD7F32; }
    .stMetric { 
        background-color: #1a1a1a; 
        padding: 20px; 
        border-radius: 15px; 
        border: 1px solid #CD7F32; 
    }
    h1, h2, h3 { color: #FFD700 !important; }
    .stButton>button { 
        background-color: #CD7F32; 
        color: white; 
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def carregar_contexto():
    try:
        # Busca os dados na pasta que você criou
        with open('Dados/perfil_investidor.json', 'r') as f:
            perfil = json.load(f)
        df = pd.read_csv('Dados/transacoes.csv')
        total_despesas = df[df['tipo'] == 'despesa']['valor'].sum()
        return perfil, total_despesas
    except:
        return None, 0

# --- INTERFACE ---
st.title("🏛️ Edu: Mentoria Financeira de Elite")
perfil, gastos = carregar_contexto()

if perfil:
    c1, c2 = st.columns(2)
    c1.metric("Patrimônio Sob Gestão", f"R$ {perfil['patrimonio_total']:.2f}")
    c2.metric("Fluxo de Saída Mensal", f"R$ {gastos:.2f}")

    st.markdown("---")
    prompt = st.chat_input("Solicite uma análise técnica ao Edu...")
    
    if prompt:
        st.chat_message("user").write(prompt)
        with st.chat_message("assistant"):
            st.write("Analisando dados locais com RAG... (Certifique-se que o Ollama está ativo).")
else:
    st.error("Erro: Base de Dados não encontrada na pasta /Dados.")
