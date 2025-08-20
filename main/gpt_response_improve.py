from openai import OpenAI

client = OpenAI()

# Define your invisible placeholder (system instruction)
PLACEHOLDER = "You are an expert tutor who explains concepts simply and clearly."

def chat_with_placeholder(user_prompt: str):
    """Send a prompt to ChatGPT with an invisible system-level placeholder."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # choose your model
        messages=[
            {"role": "system", "content": PLACEHOLDER},  # invisible to user
            {"role": "user", "content": user_prompt}      # user’s input only
        ]
    )
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    user_prompt = "Explain quantum entanglement like I'm 10 years old."
    answer = chat_with_placeholder(user_prompt)
    print(answer)
