import pandas as pd

from llm_utils import call_llm
from prompts import SYSTEM_PROMPT
from prompts import PROMPT_TEMPLATE


df = pd.read_csv("cleaned_data.csv")

record = df.iloc[0].to_json(indent=2)

prompt = PROMPT_TEMPLATE.replace(

    "{}",

    record

)

print("Temperature = 0\n")

print(

    call_llm(

        SYSTEM_PROMPT,

        prompt,

        temperature=0

    )

)

print("\n")

print("=" * 60)

print("\n")

print("Temperature = 0.7\n")

print(

    call_llm(

        SYSTEM_PROMPT,

        prompt,

        temperature=0.7

    )

)