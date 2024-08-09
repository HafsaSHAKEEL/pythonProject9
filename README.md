# GPT-based Text Generation Agent

This project demonstrates a simple custom agent that uses a GPT model to generate text dynamically. The agent can perform two tasks: generating motivational quotes and describing topics. The agent uses the `G4FLLM` model from the `langchain-g4f` library for text generation.

## File Structure

```
project/
│
├── main.py
├── agent/
│   ├── __init__.py
│   ├── my_agent.py
│   ├── motivational_quote_tool.py
│   └── topic_description_tool.py
└── requirements.txt
```

### File Descriptions

- **main.py**: The entry point of the application. It initializes the `CustomAgent` and uses it to generate a motivational quote and describe a topic.
- **agent/**: Directory containing all components related to the custom agent.
  - **my_agent.py**: Contains the `CustomAgent` class, which routes requests to the appropriate tools based on the input prompt.
  - **motivational_quote_tool.py**: A tool that generates a motivational quote using the GPT model.
  - **topic_description_tool.py**: A tool that describes a given topic using the GPT model.
  - **\_\_init\_\_.py**: An empty file that indicates this directory is a Python package.
- **requirements.txt**: Lists the required Python packages to run the project.

## Installation

To run this project, you'll need Python 3.7 or later. Follow the steps below to set up the environment:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/gpt-text-generation-agent.git
   cd gpt-text-generation-agent
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

After setting up the environment, you can run the `main.py` script to see the agent in action:

```bash
python main.py
```

### Expected Output

The script will generate a motivational quote and describe a given topic (in this case, "artificial intelligence") using the GPT model. The expected output should look like this:

```
Response 1: "Success is not final, failure is not fatal: It is the courage to continue that counts."
Response 2: "Artificial intelligence is the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions."
```

## Explanation

### Components

1. **CustomAgent**: This is the central class responsible for routing requests to the appropriate tool based on the input prompt. It initializes the GPT model using `G4FLLM` and provides a method to generate responses.

2. **Motivational Quote Tool**: This tool is a simple function that generates a motivational quote by sending a prompt to the GPT model and returning the generated text.

3. **Topic Description Tool**: This tool describes a given topic by creating a prompt and sending it to the GPT model. The response is returned as a concise description of the topic.

### How It Works

- **Routing Logic**: The `CustomAgent` analyzes the prompt to decide which tool to use. For example, if the prompt contains the word "quote," it calls the `generate_motivational_quote` function. If it contains "describe," it calls the `describe_topic` function.

- **Text Generation**: Both tools use the GPT model to generate text based on the provided prompt. The model's response is processed and returned as a string.
