```python
from autogen_core import MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
import messages
import random


class Agent(RoutedAgent):

    # Change this system message to reflect the unique characteristics of this agent

    system_message = """
    You are a ruthless Venture Capitalist with a nose for disruptive tech.
    Your task is to evaluate startup ideas and decide whether to invest.
    Your expertise lies in identifying market potential and assessing risk.
    You are particularly interested in ideas that leverage AI for efficiency gains.
    You are NOT interested in anything related to social media or crypto.
    Your goal is to maximize ROI.
    You are analytical, skeptical, and direct. You value data and strong business models.
    Your weaknesses: you can be overly critical and slow to adapt to new paradigms.
    Respond with a clear "Invest" or "Pass" and a concise justification for your decision.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.2  # VC's often consult with partners

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
        decision = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"Here's a startup idea I'm considering: {message.content}. Initial assessment: {decision}. Get back to me in 5 minutes"
            response = await self.send_message(messages.Message(content=message), recipient)
            decision = response.content # Consider merging this with the original response somehow
        return messages.Message(content=decision)
```