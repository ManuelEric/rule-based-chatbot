from openai import OpenAI

client = OpenAI(
    api_key='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'
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = [ 
        {"role": "system", "content": "You are a professional in mental wellness"},
        {"role": "user", "content": "Who want to check in her/his mental wellness"}, 
    ]
)



while True:
    message = input("User: ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )


    reply = chat.choices[0].message.content
    print(f"Bot: {reply}")

    # to make chatbot keep track of the context of the communication
    messages.append({"role": "assistant", "content": reply})