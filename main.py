from fastapi import FastAPI
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI(
    title="My fastAPI API", version="1.0.0", description="API de exemplo FastAPI"
)

# declarando usuarios teste
users = {"user1": "password1", "user2": "password2"}

security = HTTPBasic()

# Criação do metodo basico de autenticação
def verify_password(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    if username in users and users[username] == password:
        return username
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais invalidas",
        headers={"WWW-Authenticate": "Basic"},
    )


@app.get("/hello")
async def home(username: str = Depends(verify_password)):
    return "Hello, FastAPI"

@app.get("/")
async def home():
    return "Hello, FastAPI"