# import openai library
import openai

# Set up the OpenAI API client
openai.api_key = "YOUR-API-KEY"  # Replace with your new API key

# This loop will let us ask questions continuously and behave like ChatGPT
while True:
    # Set up the model and prompt
    model_engine = "gpt-3.5-turbo-instruct"  # Updated to the latest model version
    
    prompt = input('Enter new prompt: ')

    if 'exit' in prompt or 'quit' in prompt:
        break

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extracting useful part of response
    response = completion.choices[0].text
    
    # Printing response
    print(response)
