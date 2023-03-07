import requests
from bs4 import BeautifulSoup

# URL da página da Wikipedia
url = "https://pt.wikipedia.org/wiki/Catedral_Metropolitana_de_S%C3%A3o_Paulo"

try:
    # Fazendo uma requisição HTTP à página
    with requests.get(url) as response:
        # Verificando se a requisição foi bem-sucedida
        response.raise_for_status()
        
        # Extraindo apenas o texto visível da página
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text(separator='\n', strip=True)
        
        # Salvando o texto em um arquivo .txt
        with open("texto_wikipedia.txt", "w", encoding='utf-8') as file:
            file.write(text)
            
except requests.exceptions.HTTPError as error:
    print("Não foi possível acessar a página:", error)