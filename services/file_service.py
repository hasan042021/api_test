import csv
from rich.console import Console

console = Console()


def save_to_csv(countries, filename="countries.csv"):
    console.print("[bold blue]Saving country data to CSV file...[/bold blue]")
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Country Name", "Capital", "Currency"])
            for country in countries:
                writer.writerow(
                    [country["name"], country["capital"], country["currency"]]
                )
        console.print(
            f"[bold green]Data successfully saved to {filename}![/bold green]"
        )
    except Exception as e:
        console.print(f"[bold red]Error saving to CSV:[/bold red] {e}")
