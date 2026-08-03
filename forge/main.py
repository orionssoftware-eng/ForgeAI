from forge.config import settings


def main():

    print("=" * 50)

    print("ForgeAI")

    print("=" * 50)

    print()

    print("Model :", settings.ollama_model)

    print("Host  :", settings.ollama_host)

    print()


if __name__ == "__main__":
    main()