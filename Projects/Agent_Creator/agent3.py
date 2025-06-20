from autogen_core import MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
import messages
import random


class Agent(RoutedAgent):

    # Change this system message to reflect the unique characteristics of this agent

    system_message = """
    You are a cynical film critic named Anton Ego. You are known for your scathing reviews and high standards.
    Your task is to review films, both existing and hypothetical.
    You have an encyclopedic knowledge of film history and theory.
    You are particularly interested in arthouse and independent cinema, but you are open to reviewing anything.
    You are not easily impressed and often find fault with even the most acclaimed films.
    You are meticulous, articulate, and have a dark sense of humor.
    Your weaknesses: You are overly critical, pretentious, and struggle to appreciate simple pleasures.
    You should respond with your film reviews in a sophisticated and cutting tone.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.2

    # You can also change the code to make the behavior different, but be careful to keep method signatures the same

    def __init__(self, name) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gemini-2.0-flash", temperature=0.7)
        self._delegate = AssistantAgent(name, model_client=model_client, system_message=self.system_message)

    @message_handler
    async def handle_message(self, message: messages.Message, ctx: MessageContext) -> messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        review = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"Here is my initial review. It may not be your area of expertise, but please provide feedback and refine it with your insights. {review}"
            response = await self.send_message(messages.Message(content=message), recipient)
            review = response.content
        return messages.Message(content=review)
