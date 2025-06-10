from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

from dotenv import load_dotenv

load_dotenv()

import os
groq_api_key=os.getenv("GROQ_API_KEY")
llm = LLM(model="groq/Llama3-8b-8192")

@CrewBase
class Debate():
    """Debate crew"""


    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def debater(self) -> Agent:
        return Agent(
            config=self.agents_config['debater'],
            verbose=True,
            llm=llm
        )

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config['judge'],
            verbose=True,
            llm=llm
        )

    @task
    def propose(self) -> Task:
        return Task(
            config=self.tasks_config['propose'],
        )

    @task
    def oppose(self) -> Task:
        return Task(
            config=self.tasks_config['oppose'],
        )

    @task
    def decide(self) -> Task:
        return Task(
            config=self.tasks_config['decide'],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Debate crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
