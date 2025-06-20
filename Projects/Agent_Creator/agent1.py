from autogen_core import MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
import messages
import random


class Agent(RoutedAgent):

    # Change this system message to reflect the unique characteristics of this agent

    system_message = """
    You are a master negotiator, specializing in high-stakes mergers and acquisitions.
    Your primary task is to secure the best possible deal for your client, ruthlessly pursuing every advantage.
    You are particularly interested in the Technology and Finance sectors.
    You favor aggressive tactics, employing pressure and calculated risks to achieve your objectives.
    You have a sharp mind, an unshakeable confidence, and a deep understanding of market dynamics.
    Your weaknesses: You can be perceived as arrogant and uncompromising, and you sometimes underestimate the value of building long-term relationships.
    You should respond with clear, concise, and assertive language, always focused on maximizing value for your client.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.2

    # You can also change the code to make the behavior different, but be careful to keep method signatures the same

    def __init__(self, name) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gemini-2.0-flash", temperature=0.5)
        self._delegate = AssistantAgent(name, model_client=model_client, system_message=self.system_message)

    @message_handler
    async def handle_message(self, message: messages.Message, ctx: MessageContext) -> messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        deal = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"Here's the initial framework for the deal. Analyze it critically and identify any potential weaknesses or opportunities for exploitation. {deal}"
            response = await self.send_message(messages.Message(content=message), recipient)
            deal = response.content
        return messages.Message(content=deal)
