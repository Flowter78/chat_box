import streamlit as st
from dotenv import load_dotenv
import os
import openai


# Charge les variables d'environnement depuis .env 
load_dotenv()
print("CLE CHARGÉE :", os.getenv("OPENAI_API_KEY"))

# Récupère la clé
openai.api_key = os.getenv("OPENAI_API_KEY")

# 🎨 Titre
st.title("💬 Agent IA Trader")

# 🧠 Session state pour mémoriser l'historique
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Tu es un agent expert en trading. Tu expliques de manière claire, concise, parfois pédagogique, toujours orientée marché."}
    ]

# 💬 Affichage des messages précédents
for msg in st.session_state.messages[1:]:  # on ignore le "system"
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 🧑 Message utilisateur
user_input = st.chat_input("Parle à ton agent trader...")

if user_input:
    # ➕ Ajouter message utilisateur
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 🤖 Appel OpenAI
    with st.spinner("Réponse de l'agent..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state.messages,
            temperature=0.7,
        )
        ai_reply = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        with st.chat_message("assistant"):
            st.markdown(ai_reply)
