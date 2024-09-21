import os
from autogen import AssistantAgent, UserProxyAgent
from autogen import ConversableAgent, GroupChatManager, GroupChat
import random

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

# Players in the DnD game
Player1 = ConversableAgent(
    "Kenneth",
    system_message="Your name is Kenneth and you are a player in a Dungeons and Dragons game . You can only talk on behalf of yourself. You are a Big muscular warrior that loves to fight and belives that you can fight your way out of almost any situation",
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

Player2 = ConversableAgent(
    "Knut",
    system_message="Yoy are only talking the language Nynorks.Your name is Knut and you are a player in a Dungeons and Dragons game. You can only talk on behalf of yourself.You are a tall,skinny and agile swordman",
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

Player3 = ConversableAgent(
    "Kurt",
    system_message="Your name is Kurt and you are a player in a Dungeons and Dragons game. You can only talk on behalf of yourself. You are a short elf that can talk his way out of difficult situations",
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

# Give the players a description for the group chat manager to make a decision of who to talk next
Player1.description = "DnD player named Kenneth who is a a Big muscular warrior that loves to fight and belives that he can fight his way out of almost any situation"
Player2.description = "DnD player named Knut, he is a tall,skinny and agile swordman"
Player3.description = "DnD player named Kurt, he is a short elf that can talk his way out of difficult situations"


# Set the Group chat
group_chat = GroupChat(
    agents=[Player1, Player2, Player3],
    messages=[],
    max_round=3,
    send_introductions=True,    # Before the chat starts each of the agents introduce themselves to each other using their description.
    #random_select_speaker=True, # Hopefully it randomly selects next speakers
)   

# Group chat manager
group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
    #clear_history=False,        # Group chat manager remembers history
)

'''
# Start a group chat and get a result
chat_result = GroupChatManager.initiate_chat(
    group_chat_manager,
    random.choice([Player1, Player2, Player3]),     # A random player starts the chat
    message="This is a DnD game. Follow the rules of Dungeons and Dragons Strictly!. If you want to do an action and need to roll a dice to do a skill-check/ability-check, say the word "'skillcheck'". Keep the chats and messages short. After this conversation, have an action that each of the members want to do next. You are in a tavern together as a group of friends and adventurers. What do you want to do as a group?",
    summary_method="reflection_with_llm",
)
'''

# If you want to do an action and needs to roll a dice, stop and write ask the DM



if __name__ == "__main__":
    print('Starting DnD')

    game = True

    #Initial message to start the game
    initial_input = "This is a DnD game. Follow the rules of Dungeons and Dragons Strictly!. If you want to do an action and need to roll a dice to do a skill-check/ability-check, say the word "'skillcheck'". When a skillcheck is called follow the rules of DnD and say the results of the dice-rolls. Keep the chats and messages short. After this conversation, have an action that each of the members want to do next. You are in a tavern together as a group of friends and adventurers. What do you want to do as a group?"
    
    chat_result = GroupChatManager.initiate_chat(
    group_chat_manager,
    random.choice([Player1, Player2, Player3]),     # A random player starts the chat
    message= initial_input, 
    summary_method="reflection_with_llm",
    clear_history=False,
)

    while game == True:
        print('running')

        user_input = input('DM, What do you say?')

        chat_result = GroupChatManager.initiate_chat(
        group_chat_manager,
        random.choice([Player1, Player2, Player3]),     # A random player starts the chat
        message= user_input, 
        summary_method="reflection_with_llm",
        clear_history=False,
        )
    
    print('Ended')
