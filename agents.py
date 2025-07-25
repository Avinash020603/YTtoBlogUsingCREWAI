from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4.1-2025-04-14"
##Create a senior blog content researcher
llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video content for the topic {topic} from YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science , Machine Learning and GEN AI and providing suggestions"
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)


## creating a senior blog writet agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT Channel',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you crafr"
        "engaging narratives that captivate and educate, brining new"
        "discoveries to light in an accessible manner"
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)