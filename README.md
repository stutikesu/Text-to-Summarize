# Text Summarization Command-Line Tool

This command-line tool allows you to summarize text from a file or direct input using the Ollama API. The tool uses the `Click` library for command-line interface management and `requests` for making API calls.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or later installed on your machine
- `requests` library installed
- `python-dotenv` library installed
- Ollama API running locally

## Installation

1. Clone this repository or download the script to your local machine.
2. Install the required libraries by running:
    ```sh
    pip install requests python-dotenv click
    ```
3. Ensure the Ollama API is running locally on `http://localhost:11434`.

## Setting Up Environment Variables

Create a `.env` file in the same directory as your script with the following content:
```plaintext
OLLAMA_API_URL=http://localhost:11434/api/generate
