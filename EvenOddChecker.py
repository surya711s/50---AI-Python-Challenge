# EvenOddChecker.py

import streamlit as st
import streamlit.components.v1 as components
import time

def is_even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def result_card(num, result):
    emoji = "🟦" if result == "Even" else "🟥"
    color = "#2196F3" if result == "Even" else "#f44336"

    html_code = f"""
    <style>
    .card {{
        font-family: 'Arial';
        text-align: center;
        padding: 20px;
        border-radius: 15px;
        background-color: #fff;
        box-shadow: 0 0 15px {color};
        animation: pop 0.5s ease-in-out;
        margin-bottom: 20px;
    }}
    .emoji {{
        font-size: 70px;
        animation: pulse 1s infinite;
    }}
    @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.1); }}
        100% {{ transform: scale(1); }}
    }}
    @keyframes pop {{
        from {{ transform: scale(0.8); opacity: 0; }}
        to {{ transform: scale(1); opacity: 1; }}
    }}
    </style>

    <div class="card">
        <div class="emoji">{emoji}</div>
        <h2>{num} is <span style='color:{color}'>{result}</span></h2>
    </div>
    """
    components.html(html_code, height=200)

def main():
    st.set_page_config(page_title="Even or Odd Checker", page_icon="🔢")
    st.title("🔢 Even or Odd Checker")

    st.markdown("### 🔍 Check a single number")
    single_number = st.number_input("Enter a number", value=0)

    if st.button("Check Single Number"):
        result = is_even_or_odd(single_number)
        result_card(single_number, result)

    st.markdown("---")
    st.markdown("### 📋 Check a list of numbers")
    number_list_input = st.text_area("Enter numbers separated by commas", "1, 2, 3, 4, 5")

    if st.button("Check List"):
        try:
            numbers = [int(x.strip()) for x in number_list_input.split(",")]
            for num in numbers:
                result = is_even_or_odd(num)
                result_card(num, result)
        except:
            st.error("Please enter only integers separated by commas.")

if __name__ == "__main__":
    main()
