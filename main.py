import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# ORM
# CREATE DATABASE meubanco;

# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela.

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    # Definindo campos da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

# Salvar no banco de dados.
os.system("cls || clear")

# Create 
print("Solicitando dados para o usuário")
inserir_nome = input("Digite o seu nome: ")
inserir_email = input("Digite o seu email: ")
inserir_senha = input("Digite a sua senha: ")

usuario = Usuario(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(usuario)
session.commit()

# Delete
print("\nExcluindo um  usuário.")
email_usuario = input("Informe o email do usuário para ser excluído: ")

usuario = session.query(Usuario).filter_by(email = email_usuario).first()
session.delete(usuario)
session.commit()
print("Usuário excluído com sucesso.")

# Listando todos os usuários do banco de dados.
print("\nExibindo todos os usuários do banco de dados.")
lista_usuarios = session.query(Usuario).all()

# Read
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

# Update
print("\nAtualizando dados do usuário.")
usuario = session.query(Usuario).filter_by(email = email_usuario).first()

novos_dados = Usuario(
    nome = input("Digite seu nome: "),
    email = input("Digite seu e-mail: "),
    senha = input("Digite sua senha: ")
)

usuario = novos_dados
session.add(usuario)
session.commit()


# Fechando conexão.
session.close()