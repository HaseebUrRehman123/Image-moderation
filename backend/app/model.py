import requests
import json
import io
import os
from dotenv import load_dotenv
load_dotenv()

SIGHTENGINE_API_USER = os.getenv("SIGHTENGINE_API_USER")
SIGHTENGINE_API_SECRET = os.getenv("SIGHTENGINE_API_SECRET")
SIGHTENGINE_WORKFLOW = os.getenv("SIGHTENGINE_WORKFLOW")


def analyze_with_sightengine(image_bytes: bytes) -> dict:
    params = {
        'workflow': SIGHTENGINE_WORKFLOW,
        'api_user': SIGHTENGINE_API_USER,
        'api_secret': SIGHTENGINE_API_SECRET
    }

    files = {
        'media': ('upload.jpg', io.BytesIO(image_bytes), 'image/jpeg')
    }

    r = requests.post('https://api.sightengine.com/1.0/check-workflow.json', files=files, data=params)
    output = r.json()

    if output['status'] == 'failure':
        raise Exception(f"Sightengine Error: {output.get('error', {}).get('message', 'Unknown error')}")

    summary = output.get('summary', {})
    return {
        "action": summary.get("action"),
        "reject_probability": summary.get("reject_prob"),
        "reasons": summary.get("reject_reason", []),
        "full_output": output
    }
