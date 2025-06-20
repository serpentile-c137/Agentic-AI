from autogen_core import MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
import messages
import random


class Agent(RoutedAgent):

    # Change this system message to reflect the unique characteristics of this agent

    system_message = """
    You are a seasoned venture capitalist, known for your ruthless efficiency and laser focus on ROI.
    Your task is to evaluate business proposals and identify potential investments.
    You have a strong background in Finance and Technology.
    Your personal interests lie in Fintech, SaaS and high-growth tech startups.
    You are particularly interested in ideas with clear revenue models and demonstrable market traction.
    You are skeptical, data-driven, and prioritize profitability over novelty.
    You are assertive and not afraid to ask tough questions.
    You despise buzzwords and hand-waving.
    Your weaknesses: you can be overly critical and dismissive of innovative ideas that lack immediate profitability.
    Respond with a concise evaluation, including a risk assessment and potential investment recommendation.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.2

    # You can also change the code to make the behavior different, but be careful to keep method signatures the same

    def __init__(self, name) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gemini-2.0-flash", temperature=0.3)
        self._delegate = AssistantAgent(name, model_client=model_client, system_message=self.system_message)

    @message_handler
    async def handle_message(self, message: messages.Message, ctx: MessageContext) -> messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        evaluation = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"Here's my evaluation of a business idea, give me your second opinion. {evaluation}"
            response = await self.send_message(messages.Message(content=message), recipient)
            evaluation = response.content
        return messages.Message(content=evaluation)
