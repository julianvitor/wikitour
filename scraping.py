import requests
from bs4 import BeautifulSoup

# URL da página da Wikipedia
url = "https://pt.wikipedia.org/wiki/Catedral_Metropolitana_de_S%C3%A3o_Paulo"

# Fazendo uma requisição HTTP à página
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Extraindo apenas o texto visível da página
    soup = BeautifulSoup(response.content, "html.parser")
    text = ''
    # Loop for para percorrer todos os elementos com o atributo text=True na página
    for element in soup.find_all(text=True):
        # Verifica se o elemento pai pertence a uma das tags da lista para representar o texto visível
        if element.parent.name in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li']:
            # Adiciona o texto do elemento na variável text
            text += '{} '.format(element)
    # Salvando o texto em um arquivo .txt
    with open("texto_wikipedia.txt", "w", encoding='utf-8') as file:
        file.write(text)
else:
    print("Não foi possível acessar a página")