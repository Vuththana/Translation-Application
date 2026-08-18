## Translation Application (Education Purpose)
This application used **Qwen/Qwen2.5-0.5B-Instruct** for translating input text to the targeted language. I have also implemented guardrails to check for prompt injecting by using **qualifire/prompt-injection-sentinel** to scan for both input inside the application for vulnerabilities, lastly for inappropriate content I use **unitary/toxic-bertunitary/toxic-bert**.



### Requirements
It is required that your laptop/PC have a GPU that supports CUDA and a good amount of VRAM, at least 6GB.

### Setup
Firstly, you have to setup a virtual environment before installing the packages syncing the project with `pyproject.toml`, follow this command to get setup
```
python3 venv <anyname>
```
After creating the virtual environment, use this following command
```
source <your-venv-name>/bin/activate
```

Run `uv sync` to sync the project with `pyproject.toml`

### Running the application
To run the application use the following commands:

For Linux and MacOS
```
python3 main.py
```
For Window
```
python main.py
```