from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from rich.console import Console

console = Console()


def fetch_countries():
    graphql_url = "https://countries.trevorblades.com/"

    console.print(
        "[bold blue]Fetching country data from the GraphQL API...[/bold blue]"
    )

    # preparation for graphql
    transport = RequestsHTTPTransport(url=graphql_url)
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # graphql query
    query = gql(
        """
        query {
          countries {
            name
            capital
            currency
          }
        }
        """
    )

    try:
        response = client.execute(query)
        console.print("[bold green]Successfully fetched countries![/bold green]")
        return response["countries"]
    except Exception as e:
        console.print(f"[bold red]Error fetching countries:[/bold red] {e}")
        return []
