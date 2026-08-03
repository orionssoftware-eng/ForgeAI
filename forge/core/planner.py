class Planner:

    SIMPLE_COMMANDS = [
        "cubo",
        "sfera",
        "cono",
        "cilindro",
        "piano",
        "luce",
        "camera"
    ]

    def plan(self, prompt: str):

        text = prompt.lower()

        for cmd in self.SIMPLE_COMMANDS:

            if cmd in text:

                return [prompt]

        return self.decompose(prompt)

    def decompose(self, prompt):

        return [
            prompt
        ]