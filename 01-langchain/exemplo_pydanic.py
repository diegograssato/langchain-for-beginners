from pydantic import BaseModel, EmailStr

usuario = {
    "nome": "João",
    "idade": 30,
    "email": "joao@example.com"
}

# print(usuario)

# usuario["idade"] += 10

# print(usuario)

class Usuario(BaseModel):
    nome: str
    idade: int
    email: EmailStr

usuario_model = Usuario(nome="João",
                        idade="1000",
                        email="joao@example.com")

print(type(usuario_model))
usuario_model.idade += 10
print(usuario_model.model_dump_json(indent=4))
