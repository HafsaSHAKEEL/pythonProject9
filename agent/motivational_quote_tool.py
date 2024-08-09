def generate_motivational_quote(llm):
    prompt = "Generate a motivational quote ensuring positivity"
    response = llm.generate([prompt])
    return response.generations[0][0].text.strip()
