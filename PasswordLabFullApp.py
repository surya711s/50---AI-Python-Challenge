import streamlit as st
import re
from streamlit_lottie import st_lottie
import requests

# Load Lottie animation from URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Evaluate password strength
def evaluate_password(password):
    has_length = len(password) >= 8
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_symbol = bool(re.search(r"[!@#$%^&*()_+{}\[\]:;\"'<>,.?/~\\|-]", password))

    score = sum([has_length, has_upper, has_digit, has_symbol])
    return score, has_length, has_upper, has_digit, has_symbol

# Strength label and color
def get_strength(score):
    if score <= 1:
        return "Weak", "red", "😓"
    elif score == 2 or score == 3:
        return "Medium", "orange", "😐"
    else:
        return "Strong", "green", "😎"

# Suggestion for weak passwords
def password_suggestions(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append("🔹 Use at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("🔹 Add uppercase letters.")
    if not re.search(r"\d", password):
        suggestions.append("🔹 Include numbers.")
    if not re.search(r"[!@#$%^&*()_+{}\[\]:;\"'<>,.?/~\\|-]", password):
        suggestions.append("🔹 Add special characters.")
    return suggestions

# UI setup
st.set_page_config(page_title="🔐 Password Strength Checker", page_icon="🔐")
st.title("🔐 AI-Powered Password Strength Checker")

# Optional animation
lottie_animation = load_lottie_url("https://lottie.host/1c4305f7-1263-4346-a661-3b898e8ee003/aK6UIU0EJN.json")
if lottie_animation:
    st_lottie(lottie_animation, height=150)

# Password input
show_password = st.checkbox("👁 Show password", value=False)
password = st.text_input("Enter your password:", type="default" if show_password else "password")

if st.button("Check Password"):
    if not password:
        st.warning("⚠️ Please enter a password.")
    else:
        score, has_length, has_upper, has_digit, has_symbol = evaluate_password(password)
        strength, color, face = get_strength(score)

        st.markdown(f"### Strength: <span style='color:{color}'>{strength} {face}</span>", unsafe_allow_html=True)
        st.progress(score / 4)

        # Requirements check
        st.markdown("### ✅ Requirements Check")
        st.write(f"- Minimum Length (8): {'✅' if has_length else '❌'}")
        st.write(f"- Contains Uppercase: {'✅' if has_upper else '❌'}")
        st.write(f"- Contains Number: {'✅' if has_digit else '❌'}")
        st.write(f"- Contains Symbol: {'✅' if has_symbol else '❌'}")

        # Suggestions
        if score < 4:
            st.markdown("### 💡 Suggestions to improve:")
            for suggestion in password_suggestions(password):
                st.write(suggestion)

        # Fun reaction
        if score == 4:
            st.balloons()
