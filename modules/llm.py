import requests


class Llama:
    url = "http://localhost:1234/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama-3.2-3b-instruct",
        "messages": [
            {"role": "system", "content": "Você vai escrever em apenas um paragrafo bem generico como: 'aqui está a planilha recorrente sobre numeros de telefone' (essa planilha ja está anexada no email, NÃO escreva nada como [Planilha anexada no email]) nao precisa especificar nome de empresa ou qualquer outro destinatario, o destinatario ja espera receber esse email, pois é um email recorrente, tambem so quero que voce retorne apenas o conteudo da mensagem."},

            {"role": "user",
                "content": "Escreva um parágrafo generico sobre uma planilha recorrente com informações de números de telefone, indicando que a planilha está anexada ao email e não é necessário incluir conteudo repetido."}
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }

    def api_get(self):
        # Fazendo a requisição POST
        print("Consumindo LLM...")
        response = requests.post(
            Llama.url, headers=Llama.headers, json=Llama.data)
        content = response.json()
        content = content.get('choices')[0].get('message').get('content')
        # Verificando e exibindo a resposta
        if response.status_code == 200:
            return content
        else:
            print("Erro:", response.status_code, response.text)


