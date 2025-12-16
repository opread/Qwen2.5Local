import requests

# Example script to use the local QWEN API

def generate_response(prompt):
    url = "http://127.0.0.1:8000/generate"
    data = {"prompt": prompt}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    prompt = "Hello, what is the capital of France?"
    result = generate_response(prompt)
    print(f"Prompt: {prompt}")
    print(f"Response: {result}")

    # For AI Agent integration, call generate_response with your prompts