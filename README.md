# Project Name

A brief description of your project.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Plunnnnn/Down <your-folder>
    cd <your-folder>
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - **On Windows**:
      ```bash
      venv\Scripts\activate
      ```

    - **On macOS and Linux**:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the Flask application**:

    - On Windows, use `set` instead of `export`:
      ```bash
      set FLASK_APP=run.py
      set FLASK_ENV=development
      ```

    - On macOS and Linux:
      ```bash
      export FLASK_APP=run.py
      export FLASK_ENV=development
      ```

## Usage

1. **Run the Flask application**:
    ```bash
    flask run
    ```

2. **Open your web browser and go to** `http://127.0.0.1:5000`.

3. Use the search bar to search for games. Click on a game to view detailed information.

## Project Structure

- `app/`: Contains the main application code.
  - `__init__.py`: Initializes the Flask app.
  - `game.py`: Contains the `Game` class and related methods.
  - `routes.py`: Defines the routes for the Flask app.
  - `scrape.py`: Contains the scraping logic.
- `static/`: Contains static files (e.g., CSS, JavaScript).
- `templates/`: Contains HTML templates.
  - `game_detail.html`: Template for game detail page.
  - `index.html`: Template for the main search page.
- `run.py`: Entry point for running the Flask app.
- `requirements.txt`: Lists the Python dependencies.

## Preview
 
https://github.com/user-attachments/assets/757fd742-5831-440f-bedd-633c3f3b8fa9

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
