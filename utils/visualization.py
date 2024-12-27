from tabulate import tabulate
from rich.console import Console

console = Console()


def visualize_countries(countries):

    console.print("[bold blue]\nVisualizing First 10 Country Data...[/bold blue]")

    table_data = [
        [
            country.get("name", "Unknown"),
            country.get("capital", "Unknown"),
            country.get("currency", "Unknown"),
        ]
        for country in countries[:10]  # Display only the first 10 countries
    ]
    headers = ["Name", "Capital", "Currency"]

    # Display the table
    console.print(tabulate(table_data, headers=headers, tablefmt="grid"))
