# AgeCategory.py

import streamlit as st
import time
import streamlit.components.v1 as components

def determine_age_category(age):
    if age < 0:
        return "❌", "Invalid age. Age cannot be negative."
    elif age <= 12:
        return "🧒", "Child"
    elif age <= 19:
        return "🧑", "Teenager"
    elif age <= 59:
        return "🧔", "Adult"
    else:
        return "👴", "Senior"

def reveal_result(emoji, category):
    html_code = f"""
    <style>
    .reveal {{
        opacity: 0;
        transform: scale(0.9);
        animation: fadeIn 1s forwards ease-in-out;
        animation-delay: 0.3s;
    }}

    @keyframes fadeIn {{
        to {{
            opacity: 1;
            transform: scale(1);
        }}
    }}

    .emoji-highlight {{
        font-size: 100px;
        display: inline-block;
        padding: 20px;
        border-radius: 50%;
        background-color: #ffffff10;
        animation: glow 1.5s ease-in-out forwards;
    }}

    @keyframes glow {{
        0% {{
            box-shadow: 0 0 0px #4CAF50;
        }}
        50% {{
            box-shadow: 0 0 40px #4CAF50, 0 0 20px #4CAF50 inset;
        }}
        100% {{
            box-shadow: 0 0 20px #4CAF50, 0 0 10px #4CAF50 inset;
        }}
    }}
    </style>

    <div class='reveal' style='text-align: center; margin-top: 30px;'>
        <div class='emoji-highlight'>{emoji}</div>
        <div style='font-size: 36px; font-weight: bold; color: #4CAF50; margin-top: 15px;'>You are classified as: {category}</div>
    </div>
    """
    components.html(html_code, height=350)

def main():
    st.set_page_config(page_title="Age Category Classifier", page_icon="📊")
    st.title("📊 Age Category Classifier")
    st.markdown("### Enter your age to find out your category:")

    age = st.number_input("Enter Age", min_value=-1, max_value=120, value=25, step=1)

    if st.button("🎯 Check Category"):
        with st.spinner("Analyzing..."):
            time.sleep(1.5)
        emoji, category = determine_age_category(age)
        reveal_result(emoji, category)

if __name__ == "__main__":
    main()
