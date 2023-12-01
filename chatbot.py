# https://datasciencedojo.com/blog/rule-based-chatbot-in-python/#

# Importing modules
import json
import re
import random


def extract_from_dataset():
    with open('./dataset.json', 'r') as f:
        data = json.load(f)


    # Building a list of Keywords
    keywords={}
    keywords_dict={}
    responses={}
    for intent in data['intents']:
        word = intent['tag']
        list_syn={}

        # Building dictionary of Intents & Keywords
        synonyms=[]
        for syn in intent['patterns']:
            # Remove any special characters from synonym strings
            lem_name = re.sub('^a-zA-Z0-9 \n\.]', ' ', syn)
            synonyms.append(lem_name.lower())
        list_syn[word]=set(synonyms)

        
        # Defining a new key in the keywords dictionary
        keywords[word]=[]

        # Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters
        for synonym in list(list_syn[word]):
            keywords[word].append('.*\\b'+synonym+'\\b.*')

        # Defining a new key in the response dictionary
        responses[word]=[]

        # Building a dictionary of responses
        for response in intent['responses']:
            responses[word].append(response)


    for intent, keys in keywords.items():
        # Joining the values in the keywords dictionary with the OR (|) operator updating them in keywords_dict dictionary
        keywords_dict[intent]=re.compile('|'.join(keys))

    return {
        'keywords_dict': keywords_dict,
        'responses' : responses,
    }


def initiate_bot(keywords_dict, responses):
    continue_dialogue = True
    print ("Hello, I am your friend HealthyRobo. You can ask me any question regarding mental health")
    # While loop to run the chatbot indefinetely
    while (continue_dialogue == True):  

        # Takes the user input and converts all characters to lowercase
        user_input = input('You: ').lower()

        # Defining the Chatbot's exit condition
        if user_input == 'quit': 
            print ("Thank you for visiting.")
            break
        matched_intent = None 

        for intent,pattern in keywords_dict.items():

            # Using the regular expression search function to look for keywords in user input
            if re.search(pattern, user_input): 
                # if a keyword matches, select the corresponding intent from the keywords_dict dictionary
                matched_intent=intent 

                if matched_intent == 'night' or matched_intent == 'goodbye' or matched_intent == 'thanks':
                    continue_dialogue = False                
                break

        
        key = None
        if matched_intent in responses:
            # If a keyword matches, the no-response intent is replaced by the matched intent as the key for the responses dictionary
            key = matched_intent

        # The chatbot prints the response that matches the selected intent
        if key in responses:
            print('Bot: '+random.choice(responses[key]))
            if continue_dialogue == False:
                break
        else:
            print('Bot: I am sorry, I could not understand you')
        

data = extract_from_dataset()
initiate_bot(data['keywords_dict'], data['responses'])




