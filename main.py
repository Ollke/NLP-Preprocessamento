import os
import string
import spacy
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from spacy.lang.en.stop_words import STOP_WORDS

app = FastAPI()

# Carregue o modelo de idioma
nlp = spacy.load("en_core_web_sm")

# Modelo de dados Pydantic para a entrada JSON
class JSONRequest(BaseModel):
    texto: str
    remove_special_chars: bool = False
    lemmatize: bool = False
    remove_stopwords: bool = False

@app.post("/")
async def root(json: JSONRequest):
    texto = json.texto

    # Remove caracteres especiais usando string.punctuation (opcional)
    if json.remove_special_chars:
        texto = "".join([char for char in texto if char not in string.punctuation])

    # Processamento de texto
    doc = nlp(texto)

    # Lematização (opcional)
    if json.lemmatize:
        tokens = [token.lemma_ for token in doc]
    else:
        tokens = [token.text for token in doc]

    # Remoção de stopwords (opcional)
    if json.remove_stopwords:
        tokens = [token for token in tokens if token.lower() not in STOP_WORDS]

    # Retorne o texto pré-processado como uma string
    return JSONResponse(content={
        "TextoBase": json.texto,
        "TextoPreProcessado": " ".join(tokens)
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
