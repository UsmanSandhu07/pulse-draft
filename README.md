# Pulse Draft

ReAct agent that looks up live examples for a topic, then drafts a professional-network post. Groq handles generation; Tavily is the search tool. Streamlit is the front end.

## Pieces

```
pulse-draft/
├── app/streamlit_app.py   # simple UI
├── src/agent.py           # ReAct init
├── src/tools.py           # search helpers
├── src/prompts.py         # writer persona
├── pulse_draft_advanced.py
└── requirements.txt
```

## Run

Python 3.11+.

```bash
pip install -r requirements.txt
copy .env.example .env   # if present; otherwise use the sidebar
streamlit run app/streamlit_app.py
```

Need `GROQ_API_KEY` and `TAVILY_API_KEY`.

## Flow

1. Search recent high-performing posts in the niche
2. Note hook / body / CTA patterns
3. Draft
4. Tighten the opening line and close

Always edit the output before publishing. Follow the platform’s terms; this tool does not post for you.

```bash
pytest tests/   # if tests are present
ruff check .
```
