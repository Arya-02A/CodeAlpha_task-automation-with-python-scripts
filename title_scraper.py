import requests
from bs4 import BeautifulSoup

def save_title(url, output_file):
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    title_tag = soup.title
    if title_tag and title_tag.string:
        title = title_tag.string.strip()
    else: "NO TITLE FOUND"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(title + '\n')
    print(f"Saved title: {title}")


website_url = input("Enter the url of the website: ")
save_title(website_url, "title.txt")
