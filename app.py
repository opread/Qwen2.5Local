from fastapi import FastAPI, Form
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = FastAPI()
model_name = "Qwen/Qwen2.5-3B"

quantization_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, quantization_config=quantization_config, device_map="auto")



@app.post("/generate")
async def generate(prompt: str = Form(...)):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=2048, do_sample=True, temperature=0.2)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}

@app.post("/generate_gemini")
async def generate_gemini(
    prompt: str = Form(...),
    model_name: str = Form("gemini-1.5-flash"),
    temperature: float = Form(0.7),
    max_tokens: int = Form(1000)
):
    generation_config = {
        "temperature": temperature,
        "max_output_tokens": max_tokens,
    }
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt, generation_config=generation_config)
    return {"response": response.text}