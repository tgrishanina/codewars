import urllib.request
from bs4 import BeautifulSoup

def get_member_since(username):
    url = f"https://www.codewars.com/users/{username}"
    response = urllib.request.urlopen(url)
    html_content = response.read()  
    soup = BeautifulSoup(html_content, 'html.parser')
    stats = soup.find_all('div', class_='stat')
    for stat in stats:
        if 'Member Since' in stat.get_text():
            member_since = stat.get_text().replace('Member Since:', '').strip()
            return member_since