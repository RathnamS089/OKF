import requests
import json
from history import getrecentdata
from main import savetookf
def run_tool():
    print("Reading exhaust from zsh history file...")
    exhaust=getrecentdata(40)
    if not exhaust or not exhaust.strip():
        print("No exhaust or history found")
        return
    print("sending data to model for analysis...")
    prompt=f"""You are Chronos, an automated developer knowledge assistant.
    Read the following raw developer terminal logs and extract the single most valuable technical concept, tool used, or bug fixed.
    Return ONLY a valid JSON object with these exact keys:
    - "title": A short, clean title for the file (string)
    - "category": Choose one of: 'BugFix', 'Tooling', or 'Concept' (string)
    - "tags": A list of 2-3 relevant topic strings (list)
    - "body_content": A clean Markdown explanation of what the developer was doing (string)
    Raw Developer Exhaust:
    {exhaust}"""
    try:
        response=requests.post("http://localhost:11434/api/generate",json={
            "model":"llama3.2",
            "prompt":prompt,
            "format":"json",
            "stream":False
        })
        results=json.loads(response.json()["response"])
        print(f"Model analysis complete! Generating OKF format for {results['title']}")
        savetookf(
            title=results['title'],
            category=results['category'],
            tags=results['tags'],
            body_content=results['body_content']
        )
    except Exception as e:
        print(f"Fk up in model analysis:{e}")
if __name__=="__main__":
     run_tool()