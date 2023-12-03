from time import sleep
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
from pathlib import Path

'''empty list for to store urls'''
visited = set()

def web_crawler(unique_urls):
    '''Large websites is hard to crawl and can take a lot of time 
    for educational purposes it limited to 3000 visited links'''
    while(len(unique_urls) >  len(visited) and len(unique_urls) < 3000):

        print(f'Unique links number {len(unique_urls)}')
        print(f'Visited links  numbers {len(visited)}')
        current_url = unique_urls.pop()

        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}
        try:
            page = requests.get(current_url, headers=headers)
            soup = BeautifulSoup(page.content, "html.parser")
            save_page(page, soup)
            sleep(1)

            '''Loop reads all urls on curreent page'''
            for node in soup.find_all('a'):
                '''Get href attribute with link to other pages'''
                href= node.get('href')
                full_url = urljoin(current_url, href)
                if full_url not in visited and full_url not in unique_urls:
                    unique_urls.add(full_url)
                else:
                    visited.add(full_url)
        except Exception:
            pass

def save_page(page, soup):
    '''Check if directory for saving scraped pages exist'''
    storage_directory = os.path.expanduser('~/storage')
    if not os.path.exists(storage_directory):
        os.mkdir(storage_directory)
    '''Save html pages to storage directory'''
    try:
        home_dir = os.path.expanduser('~')
        filename = f"html_{soup.find('title').text}.html"
        filename = os.path.join(home_dir, 'storage' , filename)
        print(filename)
        with open(filename, 'w') as f:
            f.write(page.text)
            f.close()
        sleep(1)
    except Exception:
        pass

'''This application is demo web scraping application creeated which
working in the way of webcrawler and using Beautiful soup to travel 
through links and save html pages on user machine'''
def main():

    base_url = input("Enter URL to start scraping web site: \n")
    '''Create empty storage for non veseted unique links'''
    unique_urls = {base_url}
    web_crawler(unique_urls)

if __name__ == "__main__":
    main()