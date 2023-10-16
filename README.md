# Langchain playground

## Purpose

The purpose of this project is to demonstrate the usage of the LangChain library in conjunction with the OpenAI GPT language model to perform structured conversations and calculations. 
Specifically, it showcases how to create an agent that can answer questions and perform calculations using a structured tool, in this case, a multiplier function.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.10 (tested)
- Access to the OpenAI API (You can request access through the Scott Logic organization)

### Installation

```bash
pip install -r requirements.txt
```

### Configuration
To use this project, you need to configure it with your OpenAI API Key. Follow these steps:

1. Create a `.env` file in the project root directory. Alternatively rename the `.env.example` file.
2. Open the `.env` file and add your OpenAI API Key like this:
plaintext
```
OPENAI_API_KEY=your-api-key-here
```
3. Save and close the `.env` file.

## Structure

The project is organised as follows:

- `main.py`: The main script that sets up the LangChain agent and executes a conversation.
- `tools/multiplier.py`: Contains the `multiplier` tool, which can be provided to an agent to perform multiplication.
- `.env.example`: An example `.env` file template. Copy and rename it to `.env` to configure your API Key.
