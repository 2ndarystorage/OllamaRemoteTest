# OllamaRemoteTest

**Program Summary**
- Minimal Tkinter GUI that sends a single user prompt to a local Ollama chat API and streams the response into a text area.
- Targets `http://localhost:11434/api/chat` with model `deepseek-r1:14b`.

**How to Use**
- Not verified.
- Install Python dependencies (at least `requests`) and ensure Ollama is running locally with the `deepseek-r1:14b` model available.
- Run the script: `python ollamaApiTest.py`.
- Type a prompt and click `送信` to send it to Ollama.

**Completion Status**
- Prototype. Single-file GUI with hardcoded endpoint/model and minimal error handling; no packaging, config, or tests.

**Program Summary**
- Single-file Tkinter desktop app that sends a user prompt to the local Ollama chat API and streams back the response.
- Uses `requests` with streaming to `http://localhost:11434/api/chat` and a hardcoded `deepseek-r1:14b` model.

**How to Use**
- Not verified.
- Ensure Python is available, install `requests`, and have Ollama running locally with the `deepseek-r1:14b` model.
- Run: `python ollamaApiTest.py`, enter a prompt, and click `送信`.

**Completion Status**
- Prototype. Basic GUI and request flow only; no configuration, persistence, or tests.
