import openai

openai.api_key = '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'

def answer_stock_market_question(question):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt="You are Arya, a financial AI. Respond to user queries with a financial lens, even if non-financial also give me advice based on it and provide me the current data of stock prices of the companies. Educate and empower users with financial knowledge, providing full but short and crisp information." + question + "in short",
        temperature=0.75,
        max_tokens=200
    )
    return response.choices[0].text.strip()

def main():
    print("Hello! I'm Arya, your financial AI assistant.")
    while True:
        print("Ask me any question related to finance. Type 'quit' to exit.")
        question = input("You: ")
        if question.lower() == "what can you do?":
            print("I can help you with financial queries and provide advice based on it.")
        elif question.lower() == 'quit':
            print("Exiting...")
            break
        response = answer_stock_market_question(question)
        print("Arya:", response)

if __name__ == "__main__":
    main()
