# Ollama Local Setup

This repository contains the steps I followed to set up Ollama on my Windows system and run a local Large Language Model (LLM) using the Command Prompt. I also created a Python virtual environment and verified that Python scripts run successfully inside it.

## Project Details

- Operating System: Windows
- Ollama Version: 0.32.1
- Model Used: Llama 3.2
- Python Virtual Environment: venv

## Steps Performed

### 1. Verified Ollama Installation

```bash
ollama --version
```

### 2. Downloaded the Llama 3.2 Model

```bash
ollama pull llama3.2
```

### 3. Verified the Installed Model

```bash
ollama list
```

### 4. Ran the Model Locally

```bash
ollama run llama3.2
```

Example:

```
>>> hiii
How's it going? Is there something I can help you with or would you like to chat?
```

## Python Virtual Environment

Created a virtual environment using:

```bash
python -m venv venv
```

Activated the virtual environment:

```bash
venv\Scripts\activate
```

Created a simple Python file (`app.py`) to verify that Python was working correctly inside the virtual environment.

Run the program:

```bash
python app.py
```

Example Output:

```
Virtual Environment is Working!
Enter your name: tusha
Welcome, tusha!
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

## Git Commands Used

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/tushachauhan19/Tusha_drdo.git
git push -u origin main
```

## Conclusion

This project demonstrates:

- Installation of Ollama on Windows.
- Downloading and running the Llama 3.2 model locally.
- Creating and activating a Python virtual environment.
- Running a Python script successfully.
- Uploading the project to GitHub using Git.