import re


def contains_pii(text):

    patterns = [

        r"\b\d{10}\b",                     # Phone number

        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",  # Email

        r"\b\d{12}\b"                      # 12-digit number (simple Aadhaar check)

    ]

    for pattern in patterns:

        if re.search(pattern, text):

            return True

    return False