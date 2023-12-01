from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Bot')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

trainer = ListTrainer(chatbot)

trainer.train([
        "Hello there. Tell me how are you feeling today?",
        "Hi there. What brings you here today?",
        "Hi there. How are you feeling today?",
        "Great to see you. How do you feel currently?",
        "Hello there. Glad to see you're back. What's going on in your world right now?"
      ])

request = input("User: ")

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response(request)

print(response)