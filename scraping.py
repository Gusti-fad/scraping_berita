from bs4 import BeautifulSoup
import requests

source = requests.get('https://techcrunch.com/').text

soup = BeautifulSoup(source, 'html.parser')

def news_scraper(keyword):
    total_headlines = []
    no_of_keyword_headlines = 0
    keyword_title = []

    for headline in soup.findAll('a', class_='post-block__title__link'):
        news_headline = headline.get_text(strip=True)

        if news_headline not in total_headlines:
            total_headlines.append(news_headline)

    for i, title in enumerate(total_headlines):
        text = ''
        if keyword in title:
            text = '\033(KEYWORD)\033'
            no_of_keyword_headlines += 1
            keyword_title.append(title)

        print(f'{i + 1} - {title} {text}')   

    print(f'\n-------------- HASIL BERDASARKAN KATA KUNCI "{keyword}" = {no_of_keyword_headlines} --------------')
    for i, title in enumerate(keyword_title):
        print(f'{i + 1} - {title}')
news_scraper('AI')