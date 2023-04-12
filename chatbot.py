import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    messagesArr = []

    while True :
        prompt = input("> ")

        messagesArr.append({"role": "user", "content": prompt})

        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=messagesArr
        )

        messagesArr.append({"role": "assistant", "content": completion.choices[0].message.content})

        print(completion.choices[0].message.content)