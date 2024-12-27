import requests
import numpy as np
import json

# Função para conectar ao Ollama e processar a saída
def get_embeddings(text, model="llama2", host="http://localhost:11434"):
    """
    Conecta ao Ollama local para processar o texto e gerar saída.

    Args:
        text (str): Texto para o qual será gerada a saída.
        model (str): Nome do modelo utilizado no Ollama.
        host (str): URL do servidor Ollama.

    Returns:
        str: Texto completo gerado pelo Ollama.
    """
    url = f"{host}/api/generate"
    payload = {"model": model, "prompt": text}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers, stream=True)
        response.raise_for_status()
        
        full_response = ""
        for line in response.iter_lines():
            if line:
                # Decodificar cada linha e agregar o texto
                line_data = json.loads(line)
                full_response += line_data.get("response", "")
        
        return full_response
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar ao Ollama: {e}")
        return None

# Fornecer texto simples
texto = "Como posso para de perder cabelo?.(em português)"

# Obter resposta do Ollama
output = get_embeddings(texto)

# Exibir a saída completa
if output is not None:
    print("\nSaída completa do Ollama:")
    print(output)

    print("\n \t  Resumo dos Embeddings:")
    print(f"Tamanho do vetor: {len(output)}")
    print(f"Primeiros 10 valores: {output[:10]}")
else:
    print("Falha ao processar o texto.")
