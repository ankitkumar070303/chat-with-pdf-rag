from dotenv import load_dotenv
import os
import sys
from google import genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("ERROR: GOOGLE_API_KEY not set in environment")
    sys.exit(1)

client = genai.Client(api_key=api_key)

try:
    resp = client.models.list()
    # Try to print model ids/names in a friendly way
    if hasattr(resp, 'models'):
        models = resp.models
    else:
        models = resp

    print("Available models:")
    for m in models:
        # m might be a dict-like or object
        try:
            mid = m.get('name') if isinstance(m, dict) else getattr(m, 'name', None)
        except Exception:
            mid = str(m)
        print('-', mid)
except Exception as e:
    print('Error listing models:', e)
    sys.exit(2)
