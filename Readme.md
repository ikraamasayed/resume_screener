# Resume Screener

An experimental Python project that explores using a locally hosted LLM to compare a candidate's resume against a job description.

## Overview

The current prototype uses **LangChain** and **Ollama (Gemma 3 4B)** to pass resume and job-description text to a language model and print its assessment.

The goal is to explore how LLMs can assist with preliminary resume-to-job matching without depending on paid cloud APIs.

## Tech Stack

- Python
- LangChain
- Ollama
- Gemma 3 4B
- `langchain-ollama`
- `langchain-core`

## Current Features

- Reads resume and job-description text files.
- Constructs a comparison prompt using LangChain.
- Runs inference using a locally hosted Gemma 3 4B model.
- Prints the generated response.

## Project Structure

```text
resume_screener/
├── DATA/
│   └── books/
│       ├── dummy_resume.txt
│       └── dummy_jd.txt
├── app.py
├── utils.py
├── doc_rag.py
├── rag_followup.py
├── test.py
└── requirement.txt
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/ikraamasayed/resume_screener.git
cd resume_screener
```

### 2. Create a virtual environment

```bash
uv venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
uv pip install -r requirement.txt
```

### 4. Install and run Ollama

Install Ollama and pull the model:

```bash
ollama pull gemma3:4b
```

Ensure the Ollama service is running before executing the Python script.

### 5. Run the application

```bash
python app.py
```

**Note:** The current script expects `dummy_resume.txt` and `dummy_jd.txt` in the working directory, whereas the committed sample files are in `DATA/books/`. Update the paths in `app.py` before running it.

## Current Limitations

- No PDF or DOCX resume upload.
- No web interface in the verified implementation.
- No structured scoring or candidate ranking.
- No database or user management.
- No automated tests.
- RAG implementation is unfinished.

## Potential Improvements

1. Support PDF and DOCX resume extraction.
2. Accept job descriptions and resumes through an API.
3. Return structured JSON containing matched skills, missing skills, and evidence.
4. Add explainable scoring instead of relying on a free-form LLM response.
5. Add input validation and automated tests.
6. Evaluate the model's consistency against a small set of labelled examples.

## Learning Objectives

This project explores local LLM inference, prompt construction, LangChain model integration, and the early stages of document-processing workflows.

## Status

Experimental prototype. Not intended for production recruitment decisions.
