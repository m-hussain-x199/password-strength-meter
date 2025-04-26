import random
import string
import re
import streamlit as st

blacklist = ["password", "123456", "123456789", "12345678", "12345", "1234567", "qwerty", "abc123", "password1", "111111", "123123", "admin", "welcome", "1234", "qwertyuiop"]

def check_password_strength(password):
    score = 0
    feedback = []
    if password.lower() in blacklist:
        return 1, ["Your password is too common and easy to guess. Choose a different one!"]
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")
    if re.search(r'[@#$%&*+=!]', password):
        score += 1
    else:
        feedback.append("Please add at least one more special character. (!@#$%^&*)")        
    return score, feedback

def generate_strong_password(length = 12):
    if length < 8:
        length = 8
    characters = string.ascii_letters + string.digits + "!@#$%^&*" 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

st.title("🔐 Password Strength Meter")
st.write("Check how strong your password is and get suggestions to make it more stronger!")

password_input = st.text_input("Enter your password: ", type = "password")
if password_input:
    score, feedback = check_password_strength(password_input)
    st.subheader("🔎 Analysis Result:")
    if score <= 2:
        st.error("Strength: Weak ❌")
        for f in feedback:
            st.write("- " + f)
    elif score <= 4:
        st.warning("Strength: Moderate ⚠️")
        for f in feedback:
            st.write("- " + f)
    else:
        st.success("Strength: Strong ✅")
        st.write("Great! Your password meets all the recommended criteria.")
    st.subheader("💡Ideas for Strong Password")
    if st.button("Generate Strong Password"):
        st.info(generate_strong_password())           

st.markdown(
    """
    <hr style="margin-top: 50px;">
    <div style='text-align: center; font-size: 20px; color: white; animation: fadeIn 7s;'>
        Created by Muhammad Hussain <br>
        <a href='https://github.com/m-hussain-x199' target='_blank' style='color: gray; text-decoration: none;'>
            <img src='https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/github.svg' width='20' style='vertical-align: middle; margin-right: 5px;'> GitHub
        </a> |
        <a href='https://www.linkedin.com/in/where-is-hussain' target='_blank' style='color: gray; text-decoration: none;'>
            <img src='https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/linkedin.svg' width='20' style='vertical-align: middle; margin-right: 5px;'> LinkedIn
        </a>
    </div>

    <style>
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)
