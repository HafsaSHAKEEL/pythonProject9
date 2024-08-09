from agent.my_agent import CustomAgent


def main():
    agent = CustomAgent()  # Initialize the custom agent

    response_1 = agent.generate_response("give me motivational quote")  # generating motivational quote
    print("Response 1:", response_1)

    # Example 2: Describe a topic
    response_2 = agent.generate_response("Describe human")
    print("Response 2:", response_2)


if __name__ == "__main__":
    main()
