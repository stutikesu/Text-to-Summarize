import os
import click
import requests
import json
from dotenv import load_dotenv

#environment set
load_dotenv()

#apiset
API_URL = os.getenv('http://localhost:11434/api/generate')

def pullmodel(model_name_):

    url = 'http://localhost:11434/api/pull'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "model": model_name_
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"Failed to pull model: {response.status_code} {response.text}")

@click.command()
@click.option('-t', '--file', type=click.File('r'), help='Path to the text file to be summarized')
@click.argument('text', required=False)
def summarize(file, text):
    

    # reading the content after file is being provided
    if file:
        text = file.read()

    
    if text:
        try:
            pullmodel("qwen2:0.5b")  
            summary = summarize_text(text)
            click.echo(f"Summary: {summary}")
        except requests.exceptions.RequestException as e:
            click.echo(f"Error: {e}")
        except json.JSONDecodeError as e:
            click.echo(f"JSON Decode Error: {e}")
        except Exception as e:
            click.echo(f"Error: {e}")
    else:
        click.echo("Please provide a text file with -t option.")

def summarize_text(text):
   

    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "model": "qwen2:0.5b",  #it can be llama3, llama2
        "prompt": text,         # Prompt
        "stream": False         
    }

    # for debugging
    print(f"Sending request to URL: {'http://localhost:11434/api/generate'}")
    print(f"Payload: {payload}")

    #postrequest
    response = requests.post('http://localhost:11434/api/generate', headers=headers, json=payload)

    if response.status_code == 200:
        try:
            summary = ""
            for line in response.iter_lines():
                try:
                    response_json = json.loads(line.decode('utf-8'))
                    summary += response_json.get("response", "")
                    if response_json.get("done", False):
                        break
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    continue

            return summary
        except json.JSONDecodeError as e:
            raise Exception(f"JSON Decode Error: {e} - Response: {response.text}")
    else:
        raise Exception(f"Failed to summarize: {response.status_code} {response.text}")

if __name__ == '__main__':
    summarize()
