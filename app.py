import streamlit as st
from assistant import SafetySupportAssistant

# Initialize backend
assistant = SafetySupportAssistant()

# Page setup
st.set_page_config(page_title="🛡️ Saheli Scam Detector", page_icon="📱")
st.title("🛡️ Saheli: Scam Detection & Women's Safety Support")

st.markdown("""
👋 **Welcome!** This tool helps you detect **scammy, phishing, or fake loan** messages.  
It also connects you with **verified women's helplines and NGOs** across India.  

---

📩 **Paste a suspicious message (SMS, WhatsApp, ad, etc.) below to analyze:**
""")

# Message input
message = st.text_area("✍️ Enter message here:", height=150)

# Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔍 Analyze"):
        if message.strip() == "":
            st.warning("Please paste a message to analyze.")
        else:
            result = assistant.analyze_message_for_scam(message)
            st.subheader("📊 Analysis Result")
            st.json(result)

with col2:
    if st.button("📞 Helplines & NGOs"):
        st.subheader("📍 Verified Women's Helplines")
        st.json(assistant.get_ngo_helpline_info())

with col3:
    if st.button("📈 Scam Check Analytics"):
        st.subheader("📊 Scam Detection Stats")
        st.json(assistant.get_scam_analytics())
