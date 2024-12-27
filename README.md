
# Gerar Embeddings com Ollama

Este repositório fornece um script em Python para conectar-se ao servidor Ollama, processar um texto e obter os embeddings correspondentes. Ele também exibe um resumo dos embeddings gerados.

## Requisitos

- **Python 3.7+**
- **Servidor Ollama** executando localmente em `http://localhost:11434`

## Instalação

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/ollama_embeddings.git
   cd ollama_embeddings
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Certifique-se de que o servidor Ollama está em execução localmente. Você pode iniciá-lo com o comando:
   ```bash
   ollama serve
   ```

2. Execute o script Python:
   ```bash
   python ollama_embeddings.py
   ```

3. O script processará o texto fornecido e exibirá:
   - O tamanho do vetor de embeddings gerado.
   - Os 10 primeiros valores do vetor.

## Exemplo de Saída

Ao processar o texto `"Esta é uma frase de teste para geração de embeddings."`, a saída pode ser algo como:

```
Resumo dos Embeddings:
Tamanho do vetor: 4096
Primeiros 10 valores: [0.123, 0.456, 0.789, ...]
```

## Personalização

- Você pode alterar o texto processado modificando a variável `texto` no script:
  ```python
  texto = "Seu texto aqui."
  ```

- Altere o modelo utilizado no Ollama ajustando a variável `model` no script:
  ```python
  model = "llama2"
  ```

## Problemas Conhecidos

- **Erro de conexão com o Ollama:** Verifique se o servidor está em execução e acessível em `http://localhost:11434`.
- **Embeddings não retornados:** O modelo precisa estar configurado para suportar a geração de embeddings.

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou correções.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

