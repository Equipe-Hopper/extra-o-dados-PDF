import requests


class Llama:
    url = "http://localhost:1234/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama-3.2-3b-instruct",
        "messages": [
            {"role": "system", "content": "Você vai escrever em apenas um paragrafo mensagens prontas de emails relacionados ao envio de uma planilha excel (essa planilha ja está anexada no email) com apenas numeros de telefone, nao precisa especificar nome de empresa ou qualquer outro destinatario, o destinatario ja espera receber esse email, pois é um email recorrente, tambem so quero que voce retorne apenas o conteudo da mensagem."},

            {"role": "user",
                "content": "Escreva uma mensagem de envio de email sobre uma planilha excel que contem apenas numeros de telefone (nao precisar especificar nome de empresa ou qualquer outro destinatario), Meu nome é Armando Neto e estou enviando esse email"}
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }
    

    def api_get(self):
        # Fazendo a requisição POST
        response = requests.post(
            Llama.url, headers=Llama.headers, json=Llama.data)
        content = response.json()
        content = content.get('choices')[0].get('message').get('content')
        # Verificando e exibindo a resposta
        if response.status_code == 200:
            return content
        else:
            print("Erro:", response.status_code, response.text)


