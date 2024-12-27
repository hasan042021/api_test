from services.graphql_service import fetch_countries
from services.rest_service import post_country_details
from services.file_service import save_to_csv
from utils.visualization import visualize_countries
from rich.console import Console
from rich.prompt import Prompt

console = Console()


def main():
    countries = []  # Initialize an empty list for storing countries

    # Starting the Menu
    while True:
        # Menu option details
        console.print("\n[bold blue]--- Main Menu ---[/bold blue]")
        console.print("[bold green]1.[/bold green] Fetch countries from GraphQL API")
        console.print(
            "[bold green]2.[/bold green] Save countries to CSV (requires fetching countries first)"
        )
        console.print(
            "[bold green]3.[/bold green] Visualize countries (requires fetching countries first)"
        )
        console.print(
            "[bold green]4.[/bold green] Post a country to REST API (requires fetching countries first)"
        )
        console.print("[bold green]5.[/bold green] Exit")

        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4", "5"])

        # Menu actions based on choice
        if choice == "1":
            console.print(
                "[bold blue]Fetching countries from GraphQL API...[/bold blue]"
            )
            countries = fetch_countries()
            if countries:
                console.print(
                    f"[bold green]Successfully fetched {len(countries)} countries![/bold green]"
                )
                console.print("[bold blue]Saving all countries to CSV...[/bold blue]")
                save_to_csv(countries)
            else:
                console.print(
                    "[bold red]Failed to fetch countries or no data available.[/bold red]"
                )

        elif choice == "2":
            if not countries:
                console.print(
                    "[bold red]You must fetch countries before saving to a CSV file![/bold red]"
                )
            else:
                console.print("[bold blue]Saving all countries to CSV...[/bold blue]")
                save_to_csv(countries)

        elif choice == "3":
            if not countries:
                console.print(
                    "[bold red]You must fetch countries before visualizing them![/bold red]"
                )
            else:
                console.print("[bold blue]Visualizing countries...[/bold blue]")
                visualize_countries(countries)

        elif choice == "4":
            if not countries:
                console.print(
                    "[bold red]You must fetch countries before posting a country to the REST API![/bold red]"
                )
            else:
                while True:
                    # Select a country
                    selected_index = Prompt.ask(
                        "[bold yellow]Enter the index of the country to post (starting from 0)[/bold yellow]",
                        choices=[str(i) for i in range(len(countries))],
                    )
                    selected_country = countries[int(selected_index)]

                    # Display the selected country details
                    console.print("\n[bold blue]Selected Country Details:[/bold blue]")
                    console.print(
                        f"[bold green]Name:[/bold green] {selected_country['name']}"
                    )
                    console.print(
                        f"[bold green]Capital:[/bold green] {selected_country['capital']}"
                    )
                    console.print(
                        f"[bold green]Currency:[/bold green] {selected_country['currency']}"
                    )

                    # Confirm if the user wants to post this country
                    confirm = Prompt.ask(
                        "\n[bold cyan]Do you want to post this country? Type 'yes' or 'no': [/bold cyan]",
                        choices=["yes", "no"],
                    )

                    if confirm == "yes":
                        console.print(
                            "[bold blue]Posting the selected country...[/bold blue]"
                        )
                        post_country_details(selected_country)
                        break
                    else:
                        console.print(
                            "[bold red]Selection cleared. Please choose another country.[/bold red]"
                        )
        elif choice == "5":
            console.print("[bold blue]Exiting the program. Goodbye![/bold blue]")
            break

        else:
            console.print(
                "[bold red]Invalid choice. Please select a valid option.[/bold red]"
            )


if __name__ == "__main__":
    main()
