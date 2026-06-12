import json
import sys
from json.decoder import JSONDecodeError

string = '{"status":"healthy","uptime":3600'

fallback_dictionary = {
    "status": "unknown",
    "uptime": 0
}

metrics = {}

try:
    json.loads(string)
except JSONDecodeError as err:
    print(f"{err} String is not a Valid JSON")
    print("Falling Back to Hardcoded Metrics")
finally:
    metrics = fallback_dictionary

print(f"Metrics State: {metrics}")
sys.exit(0)