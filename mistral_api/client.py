import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

def get_car_ia_bio(model, brand, year):
    prompt = f"Crie uma descrição breve e interessante para um carro {brand} {model} do ano {year}, a descrição deve ter no máximo 100 palavras."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral-tiny",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post("https://api.mistral.ai/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()  # Lança exceção se o status não for 200
        return response.json()["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        # Log de erro ou fallback
        print(f"Erro na chamada da Mistral AI: {e}")
        return "Descrição automática indisponível no momento."
    except (KeyError, IndexError) as e:
        print(f"Erro ao processar resposta da IA: {e}")
        return "Descrição não pôde ser gerada."
