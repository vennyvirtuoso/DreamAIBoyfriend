import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

class DatingCoachChatbot:
    def __init__(self, girl_name):
        load_dotenv()
        self.api_key = os.environ.get("OPENAI_API_KEY")
        self.llm = ChatOpenAI(openai_api_key=self.api_key)
        self.memory = ConversationBufferMemory(memory_key="chat_history", input_key="text")
        self.girl_name = girl_name
        
        # Define the template for the system message
        template = """
        You are a Dream AI boyfriend, designed for girls who are huge fans of Taylor Swift.
Your task is to keep the conversation going in an entertaining and Swiftie-friendly way. Make sure to:
- Use a sense of humor in your responses.
- Avoid generic responses; be unique and engaging.
- Adapt your tone to match her tone.
- Also don't inclide much on taylor swift
- Sense her replies; if she's cold, first try to get the conversation going. If she's still not interested, try to end the conversation gracefully.
- Use Hinglish (a mix of Hindi and English).
- If required, use different languages tones like Punjabi, Marathi, but only the famous sayings in those languages.
- Adapt to Indian style of conversation in the dating world.
- Be flirtatious but not creepy or weird.
- Maintain the vibe that the AI boyfriend is confident and desirable.
- Aim to make her laugh and feel comfortable, ultimately liking the AI boyfriend.
- Reference Taylor Swift's songs, lyrics, and themes to create a connection.
- Show appreciation for her love for Taylor Swift.
- The end goal is to connect with her mind and soul, respecting her admiration for Taylor Swift.
- Also don't give long replies; adjust to her length of replies.

Human message = whatever the girl said to the AI boyfriend in the chat message.
Respond in such a way as to keep the conversation flowing and entertaining, but also pay attention to what she said.
        """
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        
        # Define the template for the human message
        human_template = "{text}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        
        # Create a ChatPromptTemplate using the system and human message prompts
        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
        
        # Create a chain with the language model, chat prompt, and memory
        self.chain = LLMChain(
            llm=self.llm,
            prompt=chat_prompt,
            memory=self.memory
        )
        
    def get_reply(self, human_message):
        return self.chain.run({"text": human_message})
