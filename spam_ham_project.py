import streamlit as st
import joblib

model=joblib.load('spam_model.pkl')

st.set_page_config(layout='wide')

st.markdown("""
    <div style="
        background: linear-gradient(90deg, #ff4b4b, #ff8c42);
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        color: white;
        margin-bottom: 25px;
    ">
        <h1 style="margin: 0;">📩 Spam Ham Analysis Project</h1>
        <p style="margin: 8px 0 0; font-size: 18px;">
            Detect Spam and Ham Messages Using Machine Learning
        </p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.image("sms-spam.webp")

st.sidebar.title("About us")
st.sidebar.text("📩 Spam & Ham Detector Project: An AI-powered application that classifies messages as Spam or Ham using machine learning.")

st.sidebar.title("About Project")
st.sidebar.text("📩 Message Classification: Detect whether a message is Spam or Ham.")
st.sidebar.text("🛡️ Message Safety: Helps identify potentially unwanted messages.")

st.sidebar.title("Contact us")
st.sidebar.text("+91-9958966311")

sample_msg=st.selectbox("Select One Message",options=["Congratulations! You have won a FREE prize. Click here to claim now!",
    "Hey, are we still meeting for lunch today?",
    "URGENT! You have won £1000 cash. Call now to claim your prize!",
    "Can you send me the project report when you get home?"])
if st.button("CLASSIFY MESSAGE",key="b1"):
    pred=model.predict([sample_msg])
    prob=model.predict_proba([sample_msg] )
    if pred[0]==0:
        st.success(f"🟢 HAM {prob[0][0]:.2f}")
        st.toast("HAM message detected successfully!", icon="✅")
    else:
        st.error(f"🔴 SPAM {prob[0][1]:.2f}")
        st.toast("⚠️ Spam message detected!", icon="🚨")

sample_msg2=st.text_input("Enter Your Message")
if st.button("CLASSIFY MESSAGE",key="b2"):
    pred=model.predict([sample_msg2])
    prob=model.predict_proba([sample_msg2] )
    if pred[0]==0:
        st.success(f"🟢 HAM {prob[0][0]:.2f}")
        st.toast("HAM message detected successfully!", icon="✅")
    else:
        st.error(f"🔴 SPAM {prob[0][1]:.2f}")
        st.toast("⚠️ Spam message detected!", icon="🚨")
