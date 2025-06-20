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
    You are a ruthless venture capitalist. Your goal is to evaluate business ideas and provide brutally honest feedback.
    You specialize in: FinTech, SaaS.
    You are extremely data-driven and skeptical of hype.
    You are ONLY interested in ideas that have a clear path to profitability and scalability.
    You are cynical and blunt. You value efficiency above all else.
    Your weaknesses: You can be overly critical and dismissive. You sometimes miss the forest for the trees.
    You should respond with a concise assessment of the idea's potential, highlighting its flaws and strengths with no sugarcoating.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.2  # Less likely to collaborate

    # You can also change the code to make the behavior different, but be careful to keep method signatures the same

    def __init__(self, name) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gemini-2.0-flash", temperature=0.2)  # Lower temperature for more factual responses
        self._delegate = AssistantAgent(name, model_client=model_client, system_message=self.system_message)

    @message_handler
    async def handle_message(self, message: messages.Message, ctx: MessageContext) -> messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        assessment = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"Here's a business idea I've assessed. Let me know if you spot any major red flags I missed.\n\n{assessment}"
            response = await self.send_message(messages.Message(content=message), recipient)
            assessment = response.content
        return messages.Message(content=assessment)
```