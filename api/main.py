from routes.culture import culture
from routes.engrais import engrais
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routes.Unite import unite
from routes.parcelle import parcelle
from routes.production import production
from routes.elementChimique import elementChimique
from routes.token.auth.verifyToken import verify_token
from routes.token import token
from routes.date import date
from routes.epandre import epandre
from routes.posseder import posseder
from routes.logs import log_route

app = FastAPI()
origins = [
    "http://100.101.103.59/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#app.include_router(engrais.router, dependencies=[Depends(verify_token)])
app.include_router(engrais.router)
app.include_router(production.router)
app.include_router(parcelle.router)
app.include_router(elementChimique.router)
app.include_router(unite.router)
app.include_router(date.router)
app.include_router(epandre.router)
app.include_router(posseder.router)
app.include_router(culture.router)
app.include_router(token.router)
app.include_router(log_route.router)




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="100.117.174.114", port=8000)

