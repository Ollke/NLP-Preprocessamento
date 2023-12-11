import os
import string
import spacy
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from spacy.lang.en.stop_words import STOP_WORDS as STOP_WORDS_EN
from spacy.lang.pt.stop_words import STOP_WORDS as STOP_WORDS_PT

app = FastAPI()

# Carregua os modelos de idioma
nlp_en = spacy.load("en_core_web_sm")
nlp_pt = spacy.load("pt_core_news_sm")


# Modelo de dados Pydantic para a entrada JSON
class JSONRequest(BaseModel):
    text: str
    model: str = "en"
    remove_special_chars: bool = False
    lemmatize: bool = False
    remove_stopwords: bool = False

@app.post("/")
async def root(json: JSONRequest):
    text = json.text

    # Remove caracteres especiais usando string.punctuation (opcional)
    if json.remove_special_chars:
        text = "".join([char for char in text if char not in string.punctuation])

    # Carregue o modelo de idioma
    if(json.model.lower() == "en"):
        doc = nlp_en(text)
    elif(json.model.lower() == "pt"):
        doc = nlp_pt(text)
    else:
        raise HTTPException(status_code=406, detail="Model not found")

    # Lematização (opcional)
    if json.lemmatize:
        tokens = [token.lemma_ for token in doc]
    else:
        tokens = [token.text for token in doc]

    # Remoção de stopwords (opcional)
    if json.remove_stopwords:
        if(json.model.lower() == "en"):
            tokens = [token for token in tokens if token.lower() not in STOP_WORDS_EN]
        elif(json.model.lower() == "pt"):
            tokens = [token for token in tokens if token.lower() not in STOP_WORDS_PT]
        

    # Retorne o texto pré-processado como uma string
    return JSONResponse(content={
        "text": json.text,
        "model": json.model,
        "remove_special_chars": json.remove_special_chars,
        "lemmatize": json.lemmatize,
        "remove_stopwords": json.remove_stopwords,
        "response": " ".join(tokens)
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
