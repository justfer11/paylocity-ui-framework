import re

def parse_currency(text: str) -> float:
    # Remove currency symbols and commas, but keep the decimal point
    cleaned = re.sub(r"[^\d.]", "", text)
    try:
        return float(cleaned)
    except ValueError:
        return 0.0