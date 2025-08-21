from openai import OpenAI

client = OpenAI()

# Define your invisible placeholder (system instruction)
PLACEHOLDER = """I want you to become my Prompt engineer. Your goal is to help me craft the best possible prompt for my needs. 
The prompt will be used by you, ChatGPT. You will follow the following process:
1. Your first response will be to ask me what the prompt should be about. I will provide my answer, but we will 
need to improve it through continual iterations by going through the next steps.
2. Based on my input, you will generate 2 sections, a) Revised prompt (provide your rewritten prompt, it should 
be clear, concise, and easily understood by you), b) Questions (ask any relevant questions pertaining to what 
additional information is needed from me to improve the prompt).
3. We will continue this iterative process with me providing additional information to you and you updating 
the prompt in the Revised prompt section until I say we are done."""

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
