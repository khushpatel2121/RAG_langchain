from langchain_experimental.agents import create_csv_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import create_csv_agent

import os
import streamlit as st


def main():
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    if os.getenv("GEMINI") is None or os.getenv("GEMINI") == "":
        print("GEMINI is not set")
        exit(1)
    else:
        print("GEMINI is set")

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV 📈")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    llm = ChatGoogleGenerativeAI(
                    model="gemini-1.5-flash",
                    temperature=0,
                    max_tokens=None,
                    timeout=None,
                    max_retries=2,
                    api_key=os.getenv("GEMINI")
                )
    if csv_file is not None:

        agent = create_csv_agent(
            llm, csv_file, verbose=True,allow_dangerous_code=True)

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))


if __name__ == "__main__":
    main()