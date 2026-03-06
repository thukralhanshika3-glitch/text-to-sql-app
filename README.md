# Text-to-SQL App

A simple Text-to-SQL application built using **Streamlit**, **LangChain**, and **Ollama** (Llama 3 locally).
This app takes your queries in plain English, translates them into SQL using an LLM, and retrieves the specific data from a local SQLite database.

## Features
- **Local LLM**: Uses Local Llama 3 via Ollama to generate queries.
- **Easy UI**: A fast web UI built with Streamlit.
- **SQLite Database**: Comes with a simple sample database script containing student grades.

## Getting Started

### 1. Prerequisites
- Python 3.9+ installed
- [Ollama](https://ollama.com/) installed and running locally
- Pull the model before running:
  ```bash
  ollama pull llama3
  ```

### 2. Setup Database
Run the startup script to create `student_grades.db` populated with some initial data.
```bash
python create_db.py
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Make sure `ollama serve` is active in the background, then launch Streamlit:
```bash
streamlit run app.py
```

The app will become available in the browser at `http://localhost:8501`.
