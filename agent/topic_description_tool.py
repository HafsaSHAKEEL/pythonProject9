def describe_topic(topic: str, llm):
    prompt = f"Describe the topic '{topic}' informatively."
    response = llm.generate([prompt])
    return response.generations[0][0].text.strip()
