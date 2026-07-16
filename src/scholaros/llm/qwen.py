import ollama

MODEL = "qwen3:8b"


def generate(prompt: str) -> str:
    print(f"Using model: {MODEL}")

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    print("Received response from Ollama.")

    return response["message"]["content"]