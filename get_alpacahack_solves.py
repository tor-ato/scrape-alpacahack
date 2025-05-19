import requests
from bs4 import BeautifulSoup

def get_alpacahack_solves(user):
    response = requests.get(f"https://alpacahack.com/users/{user}")
    soup = BeautifulSoup(response.content, features="html.parser")
    tbody = soup.find("tbody",class_="MuiTableBody-root")
    print({user})
    print(f"{'CHALLENGE':20}{'SOLVES':20}{'SOLVED AT':20}")
    for i in tbody.find_all("tr"):
        data = i.find_all("td")
        challenge = data[0].find("a").text
        solves = data[1].find("p").text
        solve_at = data[2].find("p").text
        print(f"{challenge:20}{solves:20}{solve_at:20}")
