# Configuração de um projeto Flask

Doc de como configurar e manter um ambiente de desenvolvimento do projeto.

Rodar em DEV: `flask run`

---

## Gerenciamento de Pasta

````
meu_app/
├── middlewares
├── models -> Entidades 
├── services -> Regras de negócio 
├── controllers -> Blueprints 
└── database
    ├── connection -> conexão com SQLAlchemy
    ├── migrations -> gerenciado pelo Flask-Migrate 
    └── seeds -> gerenciado pelo Flask-Seeder 
└── settings
    └── env.py -> Declaração de variáveis de ambiente 
├── app.py -> arquivo de entrada
├── .flaskenv -> .env de DEV
├── .env
├── requirements.txt
├── Dockerfile 
├── docker-compose -> DEV
├── .dockerignore
└── .gitignore
````

## Venv - Ambiente Virtual

- **Criar:**  
  `python -m venv env`

- **Ativar:**  
  - Windows: `env\Scripts\activate`  
  - Linux/MacOS: `source env/bin/activate`  

- **Desligar:**  
  `deactivate`

### Dependências

- **OBS:** Após ativação, as dependências instaladas ficam isoladas no ambiente virtual.

- **Salvar Dependências no requirements.txt:**  
  `pip freeze > requirements.txt`  
  _Boa prática: executar este comando a cada instalação para manter o requirements.txt atualizado._

- **Instalar Dependências do requirements.txt:**  
  `pip install -r requirements.txt`