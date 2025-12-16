# Local QWEN 2.5 3B Deployment

This project deploys the Qwen2.5-3B language model locally using FastAPI, with GPU acceleration on Nvidia Geforce 1060ti.

## Requirements

- Python 3.12
- Nvidia GPU with CUDA support
- At least 6GB VRAM, 16GB RAM

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
   pip install transformers fastapi uvicorn bitsandbytes accelerate python-multipart
   ```

4. Download model: `python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='Qwen/Qwen2.5-3B')"`

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

### Example Usage in Python

```python
import requests

response = requests.post("http://127.0.0.1:8000/generate", json={"prompt": "Explain quantum computing"})
print(response.json()["response"])
```

See `example_usage.py` for a complete script that demonstrates how to integrate the API into your AI Agent.

## Notes

- The model uses 4-bit quantization to optimize memory usage and fit within the 6GB VRAM limit.
- Generation parameters: max_new_tokens=100, temperature=0.7, do_sample=True
- For implementing AI Agents, integrate this API into your agent framework by sending POST requests with prompts and processing the responses.