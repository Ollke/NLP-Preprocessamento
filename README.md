# Preprocessamento de Texto com FastAPI e SpaCy em um Contêiner Docker

Este é um script que implementa um serviço de pré-processamento de texto usando FastAPI e SpaCy. Ele oferece a capacidade de realizar várias etapas de pré-processamento de texto, como remoção de caracteres especiais, lematização e remoção de stopwords em um texto de entrada. Abaixo estão as instruções de uso e uma descrição detalhada das funcionalidades deste script.

## Uso
* Abra o terminal e navegue até o diretório que contém o Dockerfile e o código main.py.
* Construa a imagem Docker usando o seguinte comando (substitua nome-da-imagem pelo nome que você deseja dar à imagem):

```
docker build -t nome-da-imagem .
```
* Uma vez que a imagem seja construída com sucesso, você pode executar um contêiner baseado nessa imagem com o seguinte comando:
```
docker run -p 3000:3000 nome-da-imagem
```

Agora, o serviço estará disponível em http://localhost:3000.

POST /: Este endpoint aceita uma solicitação JSON com o seguinte formato:
```
{
  "text": "Texto de exemplo para pré-processamento.",
  "model": "en",
  "remove_special_chars": true,
  "lemmatize": true,
  "remove_stopwords": true
}
```
* texto (obrigatório): O texto a ser pré-processado.
* model (opcional): O código do modelo a ser utilizado ("en" - Inglês, "pt" - português). 
* remove_special_chars (opcional): Um sinalizador booleano que determina se os caracteres especiais devem ser removidos. Se definido como true, os caracteres especiais serão removidos.
* lemmatize (opcional): Um sinalizador booleano que determina se a lematização deve ser aplicada. Se definido como true, a lematização será aplicada aos tokens do texto.
* remove_stopwords (opcional): Um sinalizador booleano que determina se as stopwords devem ser removidas. Se definido como true, as stopwords serão removidas do texto.

## Exemplo de Solicitação
Aqui está um exemplo de solicitação para o endpoint:

```
{
  "texto": "The quick brown fox jumps over the lazy dog.",
  "model": "en",
  "remove_special_chars": true,
  "lemmatize": true,
  "remove_stopwords": true
}
```

Esta solicitação irá processar o texto de entrada, remover caracteres especiais, aplicar lematização e remover as stopwords. O texto pré-processado será retornado na resposta.

## Exemplo de Resposta
A resposta será um JSON que inclui os atributos enviados e o texto pré-processado:


```
{
  "texto": "The quick brown fox jumps over the lazy dog.",
  "model": "en",
  "remove_special_chars": true,
  "lemmatize": true,
  "remove_stopwords": true
  "response": "quick brown fox jump lazy dog"
}
```

* O texto pré-processado é fornecido como "response".
* Você pode fazer solicitações para o endpoint diretamente a partir do seu ambiente de desenvolvimento ou de qualquer cliente HTTP.
*Isso conclui as instruções para criar e executar um contêiner Docker com o serviço de pré-processamento de texto com FastAPI e SpaCy. Este contêiner pode ser facilmente implantado em qualquer ambiente compatível com Docker.
