SYSTEM_PROMPT = """
You are an AI assistant that evaluates housing records.

Return ONLY valid JSON.

Do not explain your answer.

Do not use markdown.
"""

PROMPT_TEMPLATE = """
Analyse the following housing record.

{}

Return ONLY this JSON structure:

{{
    "predicted_price_level": "Low | Medium | High",
    "overall_condition": "Poor | Average | Good | Excellent",
    "reason": "One short sentence"
}}
"""