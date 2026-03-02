# Import necessary libraries
# No changes needed in this cell
from openai import OpenAI
from IPython.display import Markdown, display
import os

# If using the Vocareum API endpoint
# TODO: Fill in the missing parts marked with **********


api_key=os.getenv("OPENAI_API_KEY")

# If using OpenAI's API endpoint
client = OpenAI(api_key=api_key)

# No changes needed in this cell
from enum import Enum


class OpenAIModels(str, Enum):
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_41_MINI = "gpt-4.1-mini"
    GPT_41_NANO = "gpt-4.1-nano"


MODEL = OpenAIModels.GPT_41_NANO


def get_completion(system_prompt, user_prompt, model=MODEL):
    """
    Function to get a completion from the OpenAI API.
    Args:
        system_prompt: The system prompt
        user_prompt: The user prompt
        model: The model to use (default is gpt-4.1-mini)
    Returns:
        The completion text
    """
    messages = [
        {"role": "user", "content": user_prompt},
    ]
    if system_prompt is not None:
        messages = [
            {"role": "system", "content": system_prompt},
            *messages,
        ]
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"


'''def display_responses(*args):
    """Helper function to display responses as Markdown, horizontally."""
    markdown_string = "<table><tr>"
    # Headers
    for arg in args:
        markdown_string += f"<th>System Prompt:<br />{arg['system_prompt']}<br /><br />"
        markdown_string += f"User Prompt:<br />{arg['user_prompt']}</th>"
    markdown_string += "</tr>"
    # Rows
    markdown_string += "<tr>"
    for arg in args:
        markdown_string += f"<td>Response:<br />{arg['response']}</td>"
    markdown_string += "</tr></table>"
    display(Markdown(markdown_string))'''

# ...existing code...
def display_responses(*args):
    """Helper function to display responses as Markdown in notebooks, or plain text in terminal."""
    try:
        # detect IPython environment
        from IPython import get_ipython
        if get_ipython() is None:
            raise RuntimeError("Not in IPython")
        markdown_string = "<table><tr>"
        # Headers
        for arg in args:
            markdown_string += f"<th>System Prompt:<br />{arg['system_prompt']}<br /><br />"
            markdown_string += f"User Prompt:<br />{arg['user_prompt']}</th>"
        markdown_string += "</tr>"
        # Rows
        markdown_string += "<tr>"
        for arg in args:
            markdown_string += f"<td>Response:<br />{arg['response']}</td>"
        markdown_string += "</tr></table>"
        display(Markdown(markdown_string))
    except Exception:
        # fallback for plain Python: print readable text
        for i, arg in enumerate(args, start=1):
            print(f"\n--- Response {i} ---")
            print("System Prompt:", arg.get("system_prompt"))
            print("User Prompt:", arg.get("user_prompt"))
            print("Response:\n", arg.get("response"))
# ...existing code...


# No changes needed in this cell
plain_system_prompt = "You are a helpful assistant."  # A generic system prompt
user_prompt = "Give me a simple plan to declutter and organize my workspace."

print(f"Sending prompt to {MODEL} model...")
baseline_response = get_completion(plain_system_prompt, user_prompt)
print("Response received!\n")

display_responses(
    {
        "system_prompt": plain_system_prompt,
        "user_prompt": user_prompt,
        "response": baseline_response,
    }
)

# TODO: Write a system prompt starting with "You are..." replacing the ***********
role_system_prompt = "You are an expert professional organizer and productivity coach"

print("Sending prompt with professional role...")
role_response = get_completion(role_system_prompt, user_prompt)
print("Response received!\n")

# Show last two prompts and responses
display_responses(
    {
        "system_prompt": plain_system_prompt,
        "user_prompt": user_prompt,
        "response": baseline_response,
    },
    {
        "system_prompt": role_system_prompt,
        "user_prompt": user_prompt,
        "response": role_response,
    },
)

# TODO: Write a constraints system prompt replacing the ***********
constraints_system_prompt = f""" {role_system_prompt}. The plan must be achievable in one hour and require no purchases, using only existing household items."""

print("Sending prompt with constraints...")
constraints_response = get_completion(constraints_system_prompt, user_prompt)
print("Response received!\n")

# Show last two prompts and responses
display_responses(
    {
        "system_prompt": role_system_prompt,
        "user_prompt": user_prompt,
        "response": role_response,
    },
    {
        "system_prompt": constraints_system_prompt,
        "user_prompt": user_prompt,
        "response": constraints_response,
    },
)


# TODO: Ask the LLM to explain its reasoning step by step, replacing the ***********
reasoning_system_prompt = (
    f"{constraints_system_prompt}. Explain your reasoning for each step of the plan in a thoughtful way before presenting the final checklist."
)

print("Sending prompt with reasoning request...")
reasoning_response = get_completion(reasoning_system_prompt, user_prompt)
print("Response received!\n")

# Display the last two prompts and responses
display_responses(
    {
        "system_prompt": constraints_system_prompt,
        "user_prompt": user_prompt,
        "response": constraints_response,
    },
    {
        "system_prompt": reasoning_system_prompt,
        "user_prompt": user_prompt,
        "response": reasoning_response,
    },
)