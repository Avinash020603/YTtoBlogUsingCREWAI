from crewai import Crew,Process
from agents import blog_writer,blog_researcher
from tasks import research_task,write_task

crew=Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

##start the task execution process with the enhanced feedback

result=crew.kickoff(inputs={'topics':'AI VS ML VS DL VS data Science'})
print(result)