from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

import os
from tools.multiplier import multiplier
from tools.substractor import substractor

OpenAI.api_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(temperature=0)

# Structured tools are compatible with the STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION agent type.
agent_executor = initialize_agent(
    [multiplier, substractor],
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

agent_executor.run("What is 1 multiplied by 10 and then to the result subtract 7")

