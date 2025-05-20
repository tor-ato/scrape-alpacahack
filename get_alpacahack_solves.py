import requests
from bs4 import BeautifulSoup

def get_alpacahack_solves(user):
    response = requests.get(f"https://alpacahack.com/users/{user}")
    soup = BeautifulSoup(response.content, features="html.parser")
    tbody = soup.find("tbody", class_="MuiTableBody-root")
    column_width = 15
    print({user})
    print(f"{'CHALLENGE':{column_width}}{'SOLVES':{column_width}}{'SOLVED AT':{column_width}}")
    for i in tbody.find_all("tr"):
        data = i.find_all("td")
        challenge = data[0].find("a").text
        solves = data[1].find("p").text
        solve_at = data[2].find("p").text
        print(f"{challenge:{column_width}}{solves:{column_width}}{solve_at:{column_width}}")
