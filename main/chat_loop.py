from openai import OpenAI

client = OpenAI()

PLACEHOLDER = "You are an expert tutor who explains concepts simply and clearly."

def chat_loop(initial_prompt: str, turns: int = 3):
    """Iteratively feed ChatGPT’s answer back as the next prompt."""
    messages = [
        {"role": "system", "content": PLACEHOLDER},
        {"role": "user", "content": initial_prompt}
    ]

    for i in range(turns):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        reply = response.choices[0].message.content
        print(f"\nTurn {i+1} (Assistant):\n{reply}\n")

        # Append assistant reply
        messages.append({"role": "assistant", "content": reply})

        # Use assistant reply as next user input
        messages.append({"role": "user", "content": reply})

# Example usage
if __name__ == "__main__":
    chat_loop("Explain quantum entanglement like I'm 10 years old.", turns=3)
