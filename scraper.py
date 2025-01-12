import requests
from bs4 import BeautifulSoup
from config import URL, HEADERS

def obter_preco():
    try:
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        preco = soup.find("span", class_="andes-money-amount__fraction").get_text()
        preco_atual = float(preco.replace(".", "").replace(",", "."))
        return preco_atual
    except Exception as e:
        print(f"Erro ao obter o preço: {e}")
        return None
