# Multimodal Personal Knowledge Base Agent

A Docker-compatible, full-stack application that allows you to upload, organize, and query your personal knowledge base with support for notes, diagrams, papers, and code snippets. Ask questions like:

> “What was my last project’s evaluation metric and what was the score?”

## Features

- **Upload**: Drag and drop notes (.md, .txt), diagrams (.png, .jpg, .svg), papers (.pdf), code snippets (.py, .js, .java, etc.)
- **Semantic Search**: Ask natural language questions about your uploads.
- **Project Tracking**: Keep track of projects, evaluation metrics, and results.
- **Multimodal**: Handles text, images, and PDFs.
- **API & Web UI**: REST API and simple React-based UI.

## Tech Stack

- Python FastAPI (backend)
- PostgreSQL (database)
- LangChain & OpenAI (embeddings & LLM, optional local fallback)
- React (frontend)
- Docker Compose

## Quickstart

```bash
git clone https://github.com/Ahmad-Khalil-LEEA/multimodal-pkb-agent.git
cd multimodal-pkb-agent
docker compose up --build
