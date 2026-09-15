import re


def clean_text(text):
    text = text.lower()

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Keep important technical symbols like C++, C#, .NET
    text = re.sub(r"[^a-zA-Z0-9+#./\-\s]", "", text)

    return text.strip()