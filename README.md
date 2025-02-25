# Python-Mental-Health-Chatbot(Web-based)

## Languages/Components Used

- Frontend: Python
- Backend: Python
- Database: SQLite
- Model: Ollama(qwen 0.5b)#you can change as per your gpu

## Step 1: Download and Install Ollama

- Visit the official Ollama website: https://ollama.ai
- Download the installer for your OS (Windows, macOS, or Linux)
- Follow the on-screen instructions to install Ollama
- Verify installation by running:
```
ollama --version
```

## Step 2: Download the Qwen-0.5B Model

Open a terminal or command prompt

Run the following command to download and set up the Qwen-0.5B model:

```
ollama pull qwen:0.5b
```

Check available models to confirm installation:

```
ollama list
```

## before run
- chaange the path in chatbotwebsite -> config.py
- chaange the path in chatbotwebsite -> Chatbot -> chatbot.py
- to update model. chaange the path in chatbotwebsite -> Chatbot -> chatbot.py line 35 currently using qwen 0.5b

## Installation

```
git clone
```
Note: Configure your application in the `config.py` and database and make sure the database and URI are set up correctly
```
pip install -r requirements1.txt
```

```
python run.py
```

## Functions
- Register, Login, and Continue as a Guest (For privacy reasons)
- Chat with the chatbot
- Select a specific topic
- Conduct a mental health test
- Mindfulness Exercises
- Journalling for manual tracking
- SOS Hotline (Only Malaysia) #based on info collected, you can change
- Edit profile
- Add patient History (pdf)
- chat about patient history

## Technical Domain
- Create using Python
- Flask for the Web
- SQLAlchemy for Database
- Bootstrap for the UI
- TensorFlow and NLTK for the machine learning model
- Other Library like Flask-login, Flask-bcrypt
- LLM model customised QA for patient history
