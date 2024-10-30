# Chatbot Langchain Mark One

Welcome to the Chatbot Langchain Mark One project! This interactive chatbot leverages Langchain and Streamlit to provide a seamless user experience for answering questions through real-time web searches while maintaining conversation context.

## Features

- **Interactive Q&A**: Accepts questions from users.
- **Web Search Integration**: Conducts web searches to provide accurate answers.
- **Contextual Conversations**: Keeps track of conversation history for follow-up questions.
- **Real-time Responses**: Streams responses as they are generated.

## Requirements

To get started, you'll need the following:

- Necessary API keys for OpenAI, Google API, Gustomer Search Engine ID - GOOGLE_CSE_ID

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/chatbot-langchain-markone.git
cd chatbot-langchain-markone
```

### Set Up Environment Variables
1. Create `.env` file in the root of the project
2. Copy of the contents from the `.env.sample` file and update it with your API keys.

### Running the project locally
1. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
2. install the required packages:
```bash
pip install -r requirements.txt
```
3. Run the Streamlit app:
```bash
streamlit run bot/app.py
```

### Running with Docker
If you prefer using Docker, you can build and run the application with the following commands:
```bash
docker build -t chatbot-langchain-markone .
```

2. Run the Docker container:
```bash
docker run -p 8501:8501 chatbot-langchain-markone
```

### Usage
Once the application is running, navigate to `http://localhost:8501` in your browser to start chatting with the bot.


