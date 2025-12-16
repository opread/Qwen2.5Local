@echo off
echo Setting up QWEN 2.5 3B Local Deployment
echo.

echo Creating virtual environment...
"C:\Users\oprea\AppData\Local\Programs\Python\Python312\python.exe" -m venv venv
if %errorlevel% neq 0 (
    echo Failed to create virtual environment.
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    pause
    exit /b 1
)

echo Installing PyTorch with CUDA...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
if %errorlevel% neq 0 (
    echo Failed to install PyTorch.
    pause
    exit /b 1
)

echo Installing other dependencies...
pip install transformers fastapi uvicorn bitsandbytes accelerate python-multipart
if %errorlevel% neq 0 (
    echo Failed to install dependencies.
    pause
    exit /b 1
)

echo Downloading Qwen2.5-3B model (this may take several minutes)...
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='Qwen/Qwen2.5-3B')"
if %errorlevel% neq 0 (
    echo Failed to download model.
    pause
    exit /b 1
)

echo.
echo Setup complete!
echo To start the server, run: venv\Scripts\activate && uvicorn app:app --host 127.0.0.1 --port 8000
echo.
pause