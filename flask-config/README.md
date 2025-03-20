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

## Instalação e Configuração Básica do Flask

[Documentação oficial do Flask](https://flask.palletsprojects.com/en/stable/)

1. **Instalação**  
   ```bash
   pip install Flask
   ```

2. **Arquivo de Entrada `app.py`**   
   Responsável por centralizar as configurações e extensões (variáveis de ambiente, blueprints, migrations, seeds, etc)

   Arquivo básico:
      - Importe e instancie o Flask.
      - Defina uma rota `[GET] /` para confirmar que o app está funcionando.
        
   Porta padrão do app: 5000

## CORS
[Documentação oficial do Flask-Cors](https://pypi.org/project/flask-cors/)

1. **Instalação do flask-cors**  
   ```bash
   pip install flask-cors
   ```

2. **Configuração**  
   - No arquivo de entrada (`app.py`), importe e aplique o CORS à aplicação:

   - Para definir configurações específicas (por exemplo, limitar origens para certas rotas), use a prop. resources:
   ```python
   CORS(app, resources={r"/api/*": {"origins": "http://example.com"}})
   ```

