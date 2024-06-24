import requests
from bs4 import BeautifulSoup
import os

def fetch_web_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: Received status code {response.status_code}"
    except requests.RequestException as e:
        return f"An exception occurred: {str(e)}"

def parse_web_content(page):
    if page:
        soup = BeautifulSoup(page, 'html.parser')
        articles = soup.find_all('article')
        return articles
    else:
        return None

def extract_article_info(articles):
    extracted_articles = []
    for article in articles:
        title_element = article.find('h1')
        if not title_element:
            continue
        title = title_element.get_text(strip=True)
        
        date_element = article.find('time')
        date = date_element.get_text(strip=True) if date_element else 'No date'
        
        author_element = article.find('span', class_='typography__body--5')
        author = author_element.get_text(" ", strip=True) if author_element else 'No author'
        
        disclaimer_element = article.find('div', class_='single__disclaimer')
        disclaimer = disclaimer_element.get_text(" ", strip=True) if disclaimer_element else 'No disclaimer'
        
        content_elements = article.find_all(['p', 'div'])
        content = ' '.join([element.get_text(" ", strip=True) for element in content_elements if element.get_text(strip=True)])
        
        article_info = {
            'Title': title,
            'Date': date,
            'Author': author,
            'Disclaimer': disclaimer,
            'Content': content
        }
        extracted_articles.append(article_info)
    
    return extracted_articles

def extract_images_from_articles(articles):
    extracted_images = []
    for article in articles:
        try:
            img_element = article.find('img')
            if img_element and img_element.has_attr('src'):
                img_url = img_element['src']
                extracted_images.append(img_url)
        except AttributeError:
            continue
    return extracted_images    

def display_article_info(extracted_articles):
    if extracted_articles:
        for i, article in enumerate(extracted_articles, start=1):
            print(f"Article {i}:")
            for key, value in article.items():
                print(f"{key}: {value}")
            print()  # Blank line for readability
    else:
        print("No articles to display.")

def save_articles_to_file(extracted_articles, filename):
    if extracted_articles:
        try:
            # Retrieve the path to the directory containing this script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # Construct the path to the text folder
            text_folder = os.path.join(script_dir, 'text_folder')
            # Create the text folder if it doesn't exist
            os.makedirs(text_folder, exist_ok=True)
            # Construct the file path within the text folder
            filepath = os.path.join(text_folder, filename)
            # Open the file in write mode with UTF-8 encoding
            with open(filepath, 'w', encoding='utf-8') as file:
                for i, article in enumerate(extracted_articles, start=1):
                    file.write(f"Article {i}:\n")
                    for key, value in article.items():
                        file.write(f"{key}: {value}\n")
                    if i < len(extracted_articles):
                        file.write('\n')  # Blank line for readability except last line
            print(f"Articles have been saved successfully to {filepath}.")
        except Exception as e:
            print(f"An error occurred while saving articles: {str(e)}")
    else:
        print("No articles to save.")
    
def main():
    url = 'https://www.infomoney.com.br/colunistas/convidados/de-faamg-para-sete-maravilhas-ou-quarteto-fantastico-afinal-as-big-techs-estao-mesmo-caras/'
    page = fetch_web_content(url)
    if "Error" not in page and "An exception occurred" not in page:
        articles = parse_web_content(page)
        if articles:
            extracted_articles = extract_article_info(articles)
            display_article_info(extracted_articles)
            extracted_images = extract_images_from_articles(articles)
            if extracted_images:
                print("Extracted Image URLs:")
                for img_url in extracted_images:
                    print(img_url)
            else:
                print("No images extracted.")
            # Save articles to file
            save_articles_to_file(extracted_articles, 'articles.txt')
        else:
            print("No articles found on the page.")
    else:
        print(page)

if __name__ == "__main__":
    main()