from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import AzureChatOpenAI, AzureOpenAI, ChatOpenAI, OpenAI, OpenAIEmbeddings

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["AZURE_API_KEY"] = ''
os.environ["AZURE_API_BASE"] = ''
os.environ["AZURE_API_VERSION"] = '2025-01-01-preview'

default_llm = AzureChatOpenAI(model=os.environ['AZURE_OPENAI_DEPLOYMENT_MODEL'], temperature=0.1)
@CrewBase
class GameBuilderCrew:
    """GameBuilder crew"""
    agents_config = './config/agents.yaml'
    tasks_config = './config/tasks.yaml'

    @agent
    def senior_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_engineer_agent'],
            allow_delegation=False,
            llm="azure/chat-deployment",
            provider="azure_openai",
            verbose=True
        )

    @agent
    def qa_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_engineer_agent'],
            allow_delegation=False,
            llm="azure/chat-deployment",
            provider="azure_openai",
            verbose=True
        )

    @agent
    def chief_qa_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_qa_engineer_agent'],
            allow_delegation=True,
            llm="azure/chat-deployment",
            provider="azure_openai",
            verbose=True
        )


    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_task'],
            agent=self.senior_engineer_agent()
        )

    @task
    def review_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_task'],
            agent=self.qa_engineer_agent(),
            #### output_json=ResearchRoleRequirements
        )

    @task
    def evaluate_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_task'],
            agent=self.chief_qa_engineer_agent()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the GameBuilderCrew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            llm=default_llm,
            verbose=True,
        )
