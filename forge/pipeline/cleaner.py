import re


class CodeCleaner:

    @staticmethod
    def clean(text: str) -> str:

        text = re.sub(r"```python", "", text)
        text = re.sub(r"```", "", text)

        return text.strip()