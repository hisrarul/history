import random

def handler(event, context):
    quotes = [ "Life is good everyday!",
        "Be humble and conquer", "learn, learn and grow!"
    ]
    ran_quote = random.sample(quotes, 1)[0]
    print(ran_quote)
