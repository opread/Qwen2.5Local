# Local AI Model Deployment

This project deploys the Qwen2.5-3B language model locally using FastAPI, with GPU acceleration on Nvidia Geforce 1060ti. It also includes integration with Google's Gemini API for cloud-based AI generation.

## Requirements

- Python 3.12
- Nvidia GPU with CUDA support
- At least 6GB VRAM, 16GB RAM
- Google AI API key (for Gemini integration)

## Setup

### Automated Setup

Run the installation script: `install.bat`

This will create the virtual environment, install dependencies, and download the model.

### Manual Setup

See `install_instructions.txt` for detailed installation steps.

Use Command Prompt (cmd.exe) for the following commands.

1. Create virtual environment: `"C:\Users\[username]\AppData\Local\Programs\Python\Python312\python.exe" -m venv venv`

2. Activate: `venv\Scripts\activate`

3. Install dependencies:
   ```
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
   pip install transformers fastapi uvicorn bitsandbytes accelerate python-multipart google-generativeai python-dotenv
   ```

4. Download model: `python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='Qwen/Qwen2.5-3B')"`

5. Set up Google API key:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a `.env` file in the project root with `GOOGLE_API_KEY=your_google_ai_api_key`

## Running the Web App

Run the server: `uvicorn app:app --host 127.0.0.1 --port 8000`

The web app will load the model on GPU and start listening on http://127.0.0.1:8000

## API Usage

The API provides an endpoint for generating responses from prompts.

### Endpoint: POST /generate

- **Request Body**: JSON with `prompt` field
  ```json
  {
    "prompt": "Hello, how are you?"
  }
  ```

- **Response**: JSON with `response` field
  ```json
  {
    "response": "Hello! I'm doing well, thank you for asking. How can I assist you today?"
  }
  ```

### Endpoint: POST /generate_gemini

- **Request Body**: Form data with `prompt`, `model_name` (optional, default: "gemini-1.5-flash"), `temperature` (optional, default: 0.7), `max_tokens` (optional, default: 1000)
  ```
  prompt=Hello, how are you?
  model_name=gemini-1.5-flash
  temperature=0.7
  max_tokens=1000
  ```

- **Response**: JSON with `response` field
  ```json
  {
    "response": "Hello! I'm doing well, thank you for asking. How can I assist you today?"
  }
  ```

### Example Usage in Python

```python
import requests

# For local Qwen model
response = requests.post("http://127.0.0.1:8000/generate", data={"prompt": "Explain quantum computing"})
print(response.json()["response"])

# For Gemini API
response = requests.post("http://127.0.0.1:8000/generate_gemini", data={
    "prompt": "Explain quantum computing",
    "model_name": "gemini-1.5-flash",
    "temperature": 0.7,
    "max_tokens": 1000
})
print(response.json()["response"])
```

See `example_usage.py` for a complete script that demonstrates how to integrate the API into your AI Agent.

## Notes

- The Qwen model uses 4-bit quantization to optimize memory usage and fit within the 6GB VRAM limit.
- Qwen generation parameters: max_new_tokens=2048, temperature=0.2, do_sample=True
- Gemini API requires a valid Google AI API key set in the `.env` file
- For implementing AI Agents, integrate this API into your agent framework by sending POST requests with prompts and processing the responses.