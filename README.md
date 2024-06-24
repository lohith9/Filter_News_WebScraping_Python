# Filter News Web Scraping in Python

This project involves web scraping to fetch and filter news articles from a specified URL using Python. The script retrieves web content, parses the HTML, extracts relevant article information, and saves the extracted data to a file.

## Features

- Fetch web content from a specified URL
- Parse HTML content using BeautifulSoup
- Extract article information including title, date, author, disclaimer, and content
- Extract image URLs from articles
- Display extracted article information
- Save extracted articles to a text file

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/lohith9/Filter_News_WebScraping_Python.git
   cd Filter_News_WebScraping_Python
   ```

2. **Install the required libraries:**

   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

1. **Configure the URL in the `main` function:**

   Open the `news_magnet.py` file and update the `url` variable with the desired news article URL.

2. **Run the script:**

   ```bash
   python news_magnet.py
   ```

   The script will fetch the content from the specified URL, extract the articles, display the extracted information, and save the articles to a file named `articles.txt` in the `text_folder` directory.

## Code Structure

- `news_magnet.py`: The main script containing functions to fetch web content, parse HTML, extract article information, extract image URLs, display articles, and save articles to a file.

## Functions

- `fetch_web_content(url)`: Fetches web content from the specified URL.
- `parse_web_content(page)`: Parses HTML content to extract articles.
- `extract_article_info(articles)`: Extracts essential information from the list of parsed articles.
- `extract_images_from_articles(articles)`: Extracts image URLs from the list of parsed articles.
- `display_article_info(extracted_articles)`: Displays the extracted article information in a readable format.
- `save_articles_to_file(extracted_articles, filename)`: Saves the extracted article information to a file.

## Example

Here is an example of how the extracted information is displayed:

```
Article 1:
Title: De FAAMG para Sete Maravilhas ou Quarteto Fantástico: afinal, as big techs estão mesmo caras?
Date: 17 mar 2024 09h30
Author: Por Matheus Popst
Disclaimer: info_outline Importante: os comentários e opiniões contidos neste texto são responsabilidade do autor e não necessariamente refletem a opinião do InfoMoney ou de seus controladores
Content: The Magnificent Seven é um filme de faroeste de 1960 dirigido por John Sturges – mas o termo voltou à cena no ano passado em um contexto bem diferente...
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.

## Contact

For any questions or suggestions, please contact Lohith Andra at lohith@example.com.
```

Feel free to customize this `README.md` file as needed for your project.
