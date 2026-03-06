import streamlit as st
import os
from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Page Setup
st.set_page_config(page_title="Text-to-SQL App", layout="centered")
st.title("📊 Talk to Your Database")
st.write("Ask questions about the student grades database in plain English.")

# API Key Input
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", type="password")
    st.markdown("[Get your Groq API key here](https://console.groq.com/keys)")

# Database Connection
db = SQLDatabase.from_uri("sqlite:///student_grades.db")

if not groq_api_key:
    st.info("🚨 Please add your Groq API key in the sidebar to continue.")
    st.stop()

# Fast Cloud LLM (Groq)
llm = ChatGroq(
    model="llama3-8b-8192", # Faster Llama 3 running on Groq LPU
    temperature=0,
    api_key=groq_api_key
)

# Prompt (LCEL Style)
prompt = ChatPromptTemplate.from_template("""
You are a senior data analyst and SQL expert.

Given the database schema below, write a correct SQL query
that answers the user's question.

Rules:
- Use only the tables and columns in the schema
- Do NOT explain anything
- Return ONLY the SQL query

Schema:
{schema}

Question:
{question}
""")

# LCEL Runnable Pipeline
sql_chain = (
    prompt
    | llm
    | StrOutputParser()
)

schema = db.get_table_info()

# UI Input
question = st.text_input(
    "Enter your question:",
    placeholder="e.g., Who scored the highest in Math?"
)

# Execution
if question:
    try:
        sql_query = sql_chain.invoke(
            {"schema": schema, "question": question}
        ).strip()

        st.subheader("🧠 Generated SQL")
        st.code(sql_query, language="sql")

        st.subheader("📈 Result")
        result = db.run(sql_query)
        st.write(result)

    except Exception as e:
        st.error(f"❌ Error: {e}")

# Footer
st.markdown("---")
st.caption("Powered by LangChain • Groq LPU • Llama 3 • Streamlit")
