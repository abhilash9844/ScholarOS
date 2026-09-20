<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,24&height=120&text=ScholarOS&fontSize=42&fontColor=fff&desc=Local-First%20AI%20Learning%20Platform&descSize=15&descAlignY=75&fontAlignY=38" width="100%"/>

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![AI](https://img.shields.io/badge/AI%20Powered-FF6F00?style=flat-square&logo=openai&logoColor=white)](https://github.com/abhilash9844/ScholarOS)
[![Local First](https://img.shields.io/badge/Local--First-Privacy_Friendly-4CAF50?style=flat-square)](https://github.com/abhilash9844/ScholarOS)
[![Stars](https://img.shields.io/github/stars/abhilash9844/ScholarOS?style=flat-square&color=gold)](https://github.com/abhilash9844/ScholarOS)

</div>

---

## What is ScholarOS?

**ScholarOS** is a local-first AI learning platform that transforms educational content into searchable knowledge — running entirely on your machine, with no data sent to the cloud.

> Feed it a YouTube lecture or a PDF textbook. It turns it into smart notes, flashcards, quizzes, and a searchable knowledge base you can revisit forever.

---

## Features

| Feature | Description |
|:--------|:------------|
| 🎥 **YouTube Transcript Ingestion** | Automatically extracts and processes video transcripts |
| 📄 **PDF Ingestion** *(planned)* | Parse and index PDF documents |
| 🔍 **Semantic Search** | Find concepts across all your ingested content |
| 🧠 **AI-Generated Notes** | Summarize and structure content automatically |
| 📝 **Flashcards** | Auto-generated spaced-repetition cards |
| ❓ **Quiz Generation** | Test your understanding with generated questions |
| 🔁 **Revision Mode** | Structured review sessions |

---

## Architecture Overview

```
Input (YouTube / PDF)
        │
        ▼
  Transcript Parser
        │
        ▼
   Chunking Engine
        │
        ├──► Semantic Embedding → Vector Store
        │                              │
        │                              ▼
        │                       Semantic Search
        │
        ├──► AI Summarizer → Smart Notes
        │
        └──► Quiz / Flashcard Generator
```

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Transformers](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

---

## Installation

```bash
git clone https://github.com/abhilash9844/ScholarOS.git
cd ScholarOS
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running

```bash
python app.py
# or if Streamlit-based:
streamlit run app.py
```

---

## Why Local-First?

Most AI tools send your study material to external servers. **ScholarOS** runs entirely offline:
- ✅ Your notes stay on your machine
- ✅ Works without internet after setup
- ✅ No usage limits or API costs

---

<div align="center">

**[⬅ Back to Profile](https://github.com/abhilash9844)**

*Learn smarter, not harder.*

</div>
