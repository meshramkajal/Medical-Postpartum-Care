import openai
import random
from flask import Flask, jsonify, request, redirect, render_template

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'


# Define the types and techniques of prompts
PROMPT_TYPES = [
    "Open ended",
    "Instruction",
    "Multiple Choice",
    "Fill in the blank",
    "Binary",
    "Ordering",
    "Prediction",
    "Explanation",
    "Opinion",
    "Scenario",
    "Comparative"
]

PROMPT_TECHNIQUES = [
    "Role play",
    "Chained",
    "Linked",
    "Tree of thought",
    "Instructional",
    "Add Examples",
    "Style",
    "Temperature"
]

history = ["Bot: Hello, how can I help you today? I am a chatbot designed to assist with a variety of tasks and answer questions. You can ask me about anything from general knowledge to specific topics, and I will do my best to provide a helpful and accurate response. Please go ahead and ask me your first question.\n"]

@app.route('/')
def index():
    return render_template('index.html', history=history)

@app.route('/chat', methods=['POST'])
def chat():
    input_string = request.form['input_text']
    response = chatbot_pipeline(input_string)
    history.append("User: " + input_string)
    history.append("Bot: " + response)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    global history
    history = ["Bot: Hello, how can I help you today? I am a chatbot designed to assist with a variety of tasks and answer questions. You can ask me about anything from general knowledge to specific topics, and I will do my best to provide a helpful and accurate response. Please go ahead and ask me your first question.\n"]
    return redirect('/')

def chatbot_pipeline(input_text):
    if "medical postpartum" in input_text.lower():
        # If the user's query is related to medical postpartum, use OpenAI to answer
        return get_openai_response(input_text)
    else:
        # If the user's query is not related to medical postpartum, provide a default response
        return "I am sorry, I don't have information for medical postpartum care."

def get_openai_response(user_input):
    # Select a type and technique randomly from the available prompts
    prompt_type = random.choice(PROMPT_TYPES)
    prompt_technique = random.choice(PROMPT_TECHNIQUES)

    # Generate the prompt based on the selected type and technique
    prompt = generate_prompt(prompt_type, prompt_technique, user_input)
 # Send the prompt to the OpenAI API for response generation
    response = openai.Completion.create(
        engine='gpt-3.5-turbo',  # Specify the language model engine
        prompt=prompt,
        max_tokens=50,  # Set the maximum number of tokens for the generated response
        temperature=0.8,  # Adjust the temperature to control response randomness
        n=1  # Generate a single response
    )

    return response.choices[0].text.strip()


   
#def chatbot_pipeline(user_input):
    # Select a type and technique randomly from the available prompts
    prompt_type = random.choice(PROMPT_TYPES)
    prompt_technique = random.choice(PROMPT_TECHNIQUES)

    # Generate the prompt based on the selected type and technique
    prompt = generate_prompt(prompt_type, prompt_technique, user_input)
    print("Response", prompt)

    # Send the prompt to the OpenAI API for response generation
    response = openai.Completion.create(
        engine='gpt-3.5-turbo',  # Specify the language model engine
        prompt=prompt,
        max_tokens=50,  # Set the maximum number of tokens for the generated response
        temperature=0.8,  # Adjust the temperature to control response randomness
        n=1  # Generate a single response
    )
    print("Response3", response)

#     # return response.choices[0].text.strip()
# set = ["Open ended","Instruction","Multiple Choice", "Fill in the blank","Binary","Ordering","Prediction", "Explanation","Opinion", "Scenario", "Comparative",
# "Role play", "Chained", "Linked",  "Tree of thought", "Instructional", "Add Examples", "Style","Temperature"]

def generate_prompt(prompt_type, prompt_technique, user_input):
    if prompt_type == "postpartum":
        prompt = f"Tell me about {user_input}"
    elif prompt_type == "Instruction":
        prompt = f"Provide instructions on {user_input}"
    elif prompt_type == "Multiple Choice":
        prompt = f"What are the options for {user_input}? A) Option 1 B) Option 2 C) Option 3"
    elif prompt_type == "Fill in the blank":
        prompt = f"Complete the following sentence: {user_input} is important for ____. "
    elif prompt_type == "Binary":
        prompt = f"Is {user_input} true or false?"
    elif prompt_type == "Ordering":
        prompt = f"Arrange the following in order of {user_input}: A) Option 1 B) Option 2 C) Option 3"
    elif prompt_type == "Prediction":
        prompt = f"Predict what will happen next in relation to {user_input}."
    elif prompt_type == "Explanation":
        prompt = f"Explain the concept of {user_input}."
    elif prompt_type == "Opinion":
        prompt = f"What is your opinion on {user_input}?"
    elif prompt_type == "Scenario":
        prompt = f"Imagine a scenario where {user_input}. Describe how you would handle it."
    elif prompt_type == "Comparative":
        prompt = f"Compare and contrast {user_input} and another similar concept or object."

    # Apply the selected technique to the prompt
    if prompt_technique == "Role play":
        prompt = f"Acting as a {user_input}, perform a task in the required format."
    elif prompt_technique == "Chained":
        prompt = f"Build on the previous response and provide a response to {user_input}."
    elif prompt_technique == "Linked":
        prompt = f"Link the concept of {user_input} to a related topic or idea."
    elif prompt_technique == "Tree of thought":
        prompt = f"Create a tree of thought around {user_input}, exploring different aspects and subtopics."
    elif prompt_technique == "Instructional":
        prompt = f"Provide step-by-step instructions on {user_input}."
    elif prompt_technique == "Add Examples":
        prompt = f"Give examples of {user_input} to illustrate its meaning or application."
    elif prompt_technique == "Style":
        prompt = f"Write a {prompt_technique} response to {user_input}, using a {prompt_technique} writing style."
    elif prompt_technique == "Temperature":
        prompt = f"Generate a response to {user_input} with a temperature of {prompt_technique}."

    return prompt

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5001)
# chat("Hello, I want you help on medical issues?")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)