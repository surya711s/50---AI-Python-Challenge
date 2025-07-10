# CountNumbersApp.py
import streamlit as st
import matplotlib.pyplot as plt
import time

def count_numbers(numbers):
    positive = sum(1 for n in numbers if n > 0)
    negative = sum(1 for n in numbers if n < 0)
    zero = sum(1 for n in numbers if n == 0)
    return positive, negative, zero

# Streamlit config
st.set_page_config(page_title="Count Numbers", page_icon="🔢")
st.title("🔢 Count Positive, Negative & Zero Numbers")

# Input
user_input = st.text_input("Enter numbers separated by spaces (e.g. 3 -2 0 5 -7 0 1)")

# Button
if st.button("✅ Check Numbers"):
    if user_input:
        try:
            with st.spinner("Analyzing your numbers..."):
                progress = st.progress(0)
                for i in range(1, 101):
                    time.sleep(0.005)
                    progress.progress(i)

                numbers = list(map(int, user_input.strip().split()))
                pos, neg, zero = count_numbers(numbers)

            st.success("🎉 Analysis Complete!")

            # Animated metrics
            st.subheader("📊 Results")
            col1, col2, col3 = st.columns(3)
            col1.metric("✅ Positive", pos)
            col2.metric("❌ Negative", neg)
            col3.metric("⭕ Zeros", zero)

            # Chart data
            labels = ['Positive', 'Negative', 'Zero']
            values = [pos, neg, zero]
            colors = ['#4CAF50', '#F44336', '#9E9E9E']

            # Pie and Bar side by side
            col4, col5 = st.columns(2)

            with col4:
                fig_pie, ax_pie = plt.subplots(facecolor='white')
                ax_pie.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
                ax_pie.axis('equal')
                ax_pie.set_title("Distribution Pie Chart")
                st.pyplot(fig_pie)

            with col5:
                fig_bar, ax_bar = plt.subplots(facecolor='white')
                ax_bar.bar(labels, values, color=colors)
                ax_bar.set_title("Number Count Comparison")
                ax_bar.set_ylabel("Count")
                ax_bar.set_xlabel("Category")
                for i, v in enumerate(values):
                    ax_bar.text(i, v + 0.1, str(v), ha='center', fontweight='bold')
                st.pyplot(fig_bar)

        except ValueError:
            st.warning("⚠️ Please enter only valid integers separated by spaces. Example: `1 2 -3 0`")
    else:
        st.warning("⚠️ Input field is empty. Please enter some numbers.")
