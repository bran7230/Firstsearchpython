import requests
from bs4 import BeautifulSoup

user_input = input("Enter website: ")

response = requests.get(user_input)

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

paragraphs = soup.find_all()

for idx, paragraph in enumerate(paragraphs, start=1):
        print(f"Paragraph {idx}: {paragraph.text}\n")
    

    