import streamlit as st
import openai

st.set_page_config(page_title="Business Strategy Coach Bot", layout="centered")

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🧠 Business Strategy Coach Bot")
st.write("Welcome! I can help you build SWOT analyses, craft business pitches, and plan your strategy.")

task = st.selectbox(
    "What would you like help with?",
    [
        "SWOT Analysis",
        "Business Pitch",
        "Growth Strategy",
        "Target Market Definition",
        "Ask a Custom Strategy Question"
    ]
)

user_input = st.text_area("Describe your business or ask your question:")

if st.button("Generate Strategy Advice"):
    if user_input.strip() == "":
        st.warning("Please enter a business description or question.")
    else:
        prompt = f"You are a helpful business strategy coach. The user wants help with: {task}. Here is their description: {user_input}. Provide clear, structured advice."

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a business strategy advisor."},
                {"role": "user", "content": prompt}
            ]
        )

        output = response['choices'][0]['message']['content']
        st.success("Here’s what I recommend:")
        st.write(output)
