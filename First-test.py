import os
from autogen import AssistantAgent, UserProxyAgent

# Set up your environment variables
#os.environ["API_KEY"] = ""
#os.environ["BASE_URL"] = ""


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

assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

# Start the chat
user_proxy.initiate_chat(
    assistant,
    message="Tell me a joke about NVDA and TESLA stock prices.",
)
