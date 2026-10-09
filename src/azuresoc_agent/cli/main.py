from rich.console import Console

from azuresoc_agent.agent.orchestrator import Orchestrator

console = Console()
orchestrator = Orchestrator()

console.print("[bold green]AzureSOC-Agent[/bold green]")
console.print("Type exit to quit.`n")

while True:

    question = input("AzureSOC> ")

    if question.lower() == "exit":
        break

    result = orchestrator.process(question)

    console.print(result)
