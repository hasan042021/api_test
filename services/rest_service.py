import time
import requests
from rich.console import Console
from rich.prompt import Prompt

console = Console()


def post_country_details(country):
    rest_url = "https://jsonplaceholder.typicode.com/posts"

    console.print("\n[bold blue]--- Preparing to Post Country Details ---[/bold blue]")

    # Display the country details
    console.print(f"[bold green]Name:[/bold green] {country['name']}")
    console.print(f"[bold green]Capital:[/bold green] {country['capital']}")
    console.print(f"[bold green]Currency:[/bold green] {country['currency']}")

    # Take UserID from the user
    while True:
        try:
            user_id = int(
                Prompt.ask("[bold cyan]Enter User ID (integer only):[/bold cyan]")
            )
            break
        except ValueError:
            console.print(
                "[bold red]Invalid input. Please enter an integer for User ID.[/bold red]"
            )

    # Create the payload
    payload = {
        "title": f"Country: {country['name']}",
        "body": f"Capital: {country['capital']}, Currency: {country['currency']}",
        "userId": user_id,
    }

    # Hiting the server 3 times if it fails attempts
    retries = 3
    for attempt in range(retries):
        try:
            response = requests.post(rest_url, json=payload)

            if response.status_code == 403:
                console.print("[bold red]403 Forbidden:[/bold red] Skipping request.")
                return None
            elif response.status_code == 500:
                console.print(
                    f"[bold yellow]500 Internal Server Error:[/bold yellow] Retrying..."
                )
                time.sleep(2**attempt)  # Exponential backoff
                continue
            else:
                response.raise_for_status()
                console.print(
                    f"\n[bold green]Successfully posted:[/bold green]\n {response.json()}"
                )
                return response.json()

        except requests.exceptions.RequestException as e:
            console.print(f"[bold red]Request error:[/bold red] {e}")

    console.print("[bold red]Failed to post after retries.[/bold red]")
    return None
