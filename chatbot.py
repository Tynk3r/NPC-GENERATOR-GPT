import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    messages_arr = []
    model_name = "gpt-3.5-turbo"

    while True:
        prompt = input("> ")
        messages_arr.append({"role": "user", "content": prompt})

        completion = openai.ChatCompletion.create(
            model=model_name,
            messages=messages_arr
        )

        assistant_message = completion.choices[0].message.content
        messages_arr.append({"role": "assistant", "content": assistant_message})

        print(assistant_message)

if __name__ == "__main__":
    main()