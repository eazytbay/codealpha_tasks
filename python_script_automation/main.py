import requests
from bs4 import BeautifulSoup

def scrape_jumia_products():
    # URL of the Jumia Nigeria website
    url = 'https://www.jumia.com.ng/'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the product titles and links
        products = soup.find_all('div', class_='info')

        # Loop through each product and extract the title and link
        for product in products:
            title = product.find('a', class_='title').text.strip()
            link = product.find('a', class_='core')['href']
            print(f'Title: {title}')
            print(f'Link: {link}')
            print('---')

    else:
        print('Failed to retrieve data. Check the URL or your internet connection.')

if __name__ == "__main__":
    scrape_jumia_products()
