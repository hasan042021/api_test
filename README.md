# GraphQL REST Automation

This project automates the process of fetching country data from a GraphQL API, posting selected details to a REST API, handling errors, and saving data to a CSV file. It also includes basic visualization of the data.

## Project Structure

- **api_test/**
  - **scripts.py**: Entry point of the project
  - **services/**
    - **graphql_service.py**: Functions related to GraphQL operations
    - **rest_service.py**: Functions related to REST API interactions
    - **file_service.py**: Functions for CSV file handling
  - **utils/**
    - **visualization.py**: Functions for visualization
  - **.gitignore**: Git ignore file (used to ignore `api_env`)
  - **requirements.txt**: List of dependencies
  - **README.md**: Instructions and project description


## Requirements

### Python version

- Python 3.x

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/hasan042021/api_test
   cd api_test
   ```

2. Install the dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:

   ```bash
   python scripts.py
   ```

## How It Works

1. **Fetch Countries (GraphQL)**: The `fetch_countries()` function sends a request to the GraphQL API and retrieves the list of countries with their name, capital, and currency.
2. **Post Country Details (REST)**: The `post_country_details()` function posts the country details to a REST API (https://jsonplaceholder.typicode.com/posts). It handles errors like 403 Forbidden and retries in case of 500 Internal Server Error with exponential backoff.
3. **Save to CSV**: The `save_to_csv()` function saves the country data to a CSV file.
4. **Visualization**: The `visualize_countries()` function displays a table of the first 10 countries with their name, capital, and currency.

## Error Handling

- **403 Forbidden**: The request is skipped, and no further action is taken.
- **500 Internal Server Error**: The request is retried with exponential backoff (2, 4, 8 seconds).
- **Other Errors**: Any other request errors are logged to the console.

## Saving Report

- **Data Transformation**: All countries are saved to a CSV file in the format:
  - `Country Name`, `Capital`, `Currency`.
