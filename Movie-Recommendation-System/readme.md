# IMDb Movie Recommendations Scraper

This Python script uses Selenium to scrape IMDb for movie recommendations based on genre tags. It fetches information such as title, year, and runtime.

## Prerequisites

- Python 3.x
- ChromeDriver (included for Windows, for other platforms download and set the path)

## Installation

1. Clone the repository:

    ```bash
    git clonehttps://github.com/shrey141102/PythonProjects.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Download ChromeDriver:

    - It is already included in the repository
    - Link for chromedriver if you want manually download: https://sites.google.com/chromium.org/driver/
    - Make sure to place the `chromedriver.exe` in the project directory.

## Usage

1. Run the script:

    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to enter movie genre tags.

3. View the recommendations displayed in a tabular format.

## Troubleshooting

If you encounter any issues, consider checking the following:

- Ensure you have a stable internet connection.
- Verify that the tags are separated by spaces and are valid genres.
- Check for any typos in the tags.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

