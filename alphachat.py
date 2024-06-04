import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by OpenAI. You can call me ChatGPT.",]
    ],
    [
        r"how are you?",
        ["I'm just a program, so I don't have feelings, but I'm here to help you!",]
    ],
    [
        r"weather|temperature",
        ["I don't have real-time weather information, but you can check a weather website or app for the latest updates."]
    ],

    [
        r"sorry (.*)",
        ["It's okay, no need to apologize.",]
    ],
    [
        r"quit",
        ["Goodbye! It was nice talking to you.",]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand you fully.", "Can you please elaborate?", "I'm here to help! Ask me anything."]
    ]
]

def chatbot():
    print("Hi, I'm a chatbot created by OpenAI. Type 'quit' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()