import json
import os
import pandas as pd

from jsonschema import validate
from jsonschema.exceptions import ValidationError

from llm_utils import call_llm
from prompts import SYSTEM_PROMPT
from prompts import PROMPT_TEMPLATE
from schema import SCHEMA
from guardrails import contains_pii

df = pd.read_csv("cleaned_data.csv")

results = []

records = df.head(3)

for i, row in records.iterrows():

    record = row.to_json(indent=2)

    if contains_pii(record):
        print(f"Record {i+1} skipped due to PII.")
        continue

    prompt = PROMPT_TEMPLATE.replace("{}", record)

    response = call_llm(
        SYSTEM_PROMPT,
        prompt,
        temperature=0
    )

    try:

        parsed = json.loads(response)

        validate(
            instance=parsed,
            schema=SCHEMA
        )

        parsed["record_number"] = i + 1

        results.append(parsed)

        print(f"Record {i+1} processed successfully.")

    except ValidationError:

        print(f"Record {i+1} failed schema validation.")

    except Exception:

        print(f"Record {i+1} contains invalid JSON.")

os.makedirs("outputs", exist_ok=True)

with open("outputs/results.json", "w") as f:
    json.dump(results, f, indent=4)

print("\nFinished.")
print("Results saved to outputs/results.json")