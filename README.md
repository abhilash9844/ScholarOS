# ScholarOS

ScholarOS is a local-first AI learning platform that transforms educational content into searchable knowledge.

## Features

- 🎥 YouTube transcript ingestion
- 📄 PDF ingestion (planned)
- 🔍 Semantic search
- 🧠 AI-generated notes
- 📝 Flashcards
- ❓ Quiz generation
- 🔁 Revision mode

## Installation

```bash
git clone https://github.com/<your-username>/ScholarOS.git
cd ScholarOS
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage

```bash
scholar --help
```

Example:

```bash
scholar ingest https://youtu.be/<video-id>
```

## Roadmap

- [x] Project setup
- [ ] YouTube transcript ingestion
- [ ] LanceDB integration
- [ ] Semantic search
- [ ] AI notes
- [ ] Flashcards
- [ ] Quiz generation
- [ ] Revision mode

## License

MIT License