from rich.console import Console
from rich.table import Table

from azuresoc_agent.agent.orchestrator import Orchestrator

console = Console()
orchestrator = Orchestrator()

console.print("[bold green]AzureSOC-Agent[/bold green]")
console.print("Type exit to quit.\n")

while True:

    question = input("AzureSOC> ")

    if question.lower() == "exit":
        break

    result = orchestrator.process(question)

    if not result["success"]:
        console.print(f"[red]{result.get('message', 'Something went wrong.')}[/red]")
        continue

    console.print(f"[dim]Intent:[/dim] {result['intent']}")

    columns = result.get("columns") or []
    rows = result.get("rows") or []

    if not rows:
        console.print("[yellow]No results.[/yellow]")
        continue

    table = Table(show_header=True, header_style="bold cyan")

    for column in columns:
        table.add_column(str(column))

    for row in rows:
        table.add_row(*[str(value) for value in row])

    console.print(table)
