# chatgpt-clone-Langchain

## Overview
ChatGPT-Langchain is a Python-based chatbot that emulates the functionality of OpenAI's ChatGPT using the Langchain library. This script integrates GPT-3.5-turbo model to provide a responsive and interactive chat experience, backed by an efficient retrieval system.

This is my mini project where I watched TechLead videos to learn how to use openai API and create a custom ChatGPT usinng Langchain.

## Features
- Leverages GPT-3.5-turbo model for generating human-like text responses.
- Uses Langchain's ConversationalRetrievalChain for integrating document-based information into responses.
- Maintains a history of the conversation to provide context-aware responses.
- Option to persist indexed data for efficient reloading in future sessions.

## Requirements
- Python 3.x
- OpenAI API Key
- Langchain library and additional package below
```pip install langchain openai chromadb tiktoken unstructured```

## Usage
Run the script from the command line:
```python chatbot.py "Hello, how are you?"```

To exit the chat, type 'q' or 'quit'.