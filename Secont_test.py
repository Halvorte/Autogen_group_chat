import os
from autogen import AssistantAgent, UserProxyAgent
from autogen import ConversableAgent


os.environ["API_KEY"] = ""
os.environ["BASE_URL"] = ""

# Update the configuration for Azure OpenAI
llm_config = {
    "config_list" :
            [
                {
                    "model": "gpt-4o", 
                    "base_url": os.getenv('BASE_URL'),
                    "api_type": "azure",
                    "api_version": "2024-02-01",
                    "api_key": os.getenv('API_KEY')
                 }
            ],
}

# Two players. One asking the other to tell a joke. /
# The second player is told to tell a joke, and end the message with good bye. /
# The first player terminates when it reads good bye.


Player1 = ConversableAgent(
    "Kenneth",
    system_message="Your name is Kenneth and you are a part of a duo of comedians.",
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
    is_termination_msg=lambda msg: "good bye" in msg["content"].lower(),
)

Player2 = ConversableAgent(
    "Knut",
    system_message="Your name is Knut and you are a part of a duo of comedians.",
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)


# Player1 asks Player2 a question
result = Player1.initiate_chat(Player2, message="Knut, tell me a joke, then say Good Bye", max_turns=2)

