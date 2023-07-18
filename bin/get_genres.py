import requests, os.path
from bs4 import BeautifulSoup

genre_list_path = os.path.expandvars(os.path.join(".", "lists", "genre_list.txt"))

# https://github.com/coco-zxc/charting-sounds/blob/f509338eb0ee3ba9b0e06d732c9a360791d5f363/Scripts/every_noise_at_once.py
def get_genre_list_base():
    '''
    This funtion returns a list of genres in Every Noise at Once by Glenn McDonald. 
    The list contains all genres sorted by popularity (Descending)
    '''
    url = "https://everynoise.com/everynoise1d.cgi?scope=all"
    html = requests.get(url).text
    soup = BeautifulSoup(html,"html.parser")
    rows = soup.find_all("tr")

    genre_list_by_popularity=[]

    for row in rows:
        genre_name = row.find_all('td')[2].text
        genre_list_by_popularity.append(genre_name)

    return genre_list_by_popularity

def write_genre_list():
    if not os.path.exists(os.path.dirname(genre_list_path)):
        os.makedirs(os.path.dirname(genre_list_path))
    if not os.path.exists(genre_list_path):
        with open(genre_list_path, "x", encoding="utf-8") as genre_list:
            for genre in get_genre_list_base():
                genre_list.write(f"{genre}\n")
    else:
        with open(genre_list_path, "w+", encoding="utf-8") as genre_list:
            for genre in get_genre_list_base():
                genre_list.write(f"{genre}\n")