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

## Variáveis de Ambiente
[Documentação oficial do python-dotenv](https://pypi.org/project/python-dotenv/)

1. **Instalação do python-dotenv**  
  ```bash
   pip install python-dotenv
   ```

2. **Arquivos de Ambiente (.flaskenv e .env)**  
   - **.flaskenv:**  
      - Armazena variáveis específicas para o Flask (ex: FLASK_APP, FLASK_ENV)
      - usado para rodar o ambiente de desenvolvimento com `flask run`.
     
   - **.env:**  
     Contém variáveis sensíveis e configurações gerais (secrets, DB, etc).  
     - Crie uma pasta `settings` com um arquivo `env.py` para declarar essas variáveis.
     - Carregue o `env.py` no `app.py` logo após instanciar o Flask, para o reconhecimento das variáveis.
     - Extração de variáveis com acesso direto à instância `app` do Flask:   
          Como no próprio arquivo de entrada `app.py`.
          ```bash
          ENV_VAR = app.config['ENV_VAR']
          ```
     - Extração de variáveis sem acesso direto à instância `app` do Flask:   
          Como em blueprints ou migrations.
          ```bash
          from flask import current_app
          .
          .
          .
          ENV_VAR = current_app.config.get('ENV_VAR')
          ```

3. **Observação:**  
   É comum que algumas variáveis se repitam entre os arquivos `.flaskenv` e `.env`.  
