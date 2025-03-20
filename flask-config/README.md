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

## Conexão com o Banco de Dados via SQLAlchemy

Utilização de um container para rodar o banco de dados localmente, por meio do `docker-compose.yml`.

__SGBD__: MySQL

__URI__: `"mysql://user:password@mysql_db:3306/test_db"`  
   - Variáveis de ambiente configuradas no `docker-compose.yml`. 
   - _mysql_db_:
      - nome do serviço definido no `docker-compose.yml`. 
      - Pode funcionar se colocar `localhost` em seu lugar, se estiver rodando o flask no modo de desenvolvimento.

Configuração no código:

[Documentação oficial do Flask-SqlAlchemy](https://flask-sqlalchemy.readthedocs.io/en/stable/)   

[Documentação oficial do MySqlClient](https://pypi.org/project/mysqlclient/)   

1. **Pacotes Necessários**  
   - **Flask-SQLAlchemy** (já inclui o SQLAlchemy):  
     ```bash
     pip install Flask-SQLAlchemy
     ```
   - **Driver do Banco:**  
     Para o MySQL, por exemplo, instale o `mysqlclient`.
     ```bash
     pip install mysqlclient
     ```

2. **Conexão com o Banco**  
   - Crie um arquivo `database/connection.py` para centralizar a conexão com o banco.  
   - Nesse arquivo, importe e instancie o SQLAlchemy.
     
3. **Models**  
   - **Estrutura:**  
     Crie a pasta `models` para abrigar cada model.
   - **Timestamp Model:**:
      - Importe a instância `db` de `database/connection.py`.
      - Crie a classe abstrata `TimestampModel` configurando as propriedades `created` e `updated`.
   - **Os demais models:**  
     - Em cada model, importe `TimestampModel`.
     - Cada classe representa uma tabela, elas devem herdar de `TimestampModel`.
        - Assim, todo model também terá `created` e `updated`.
     - Defina o nome da tabela com `__tablename__`.
     - Cada propriedade da classe é uma coluna da tabela definida por `mapped_column`.
       - O primeiro argumento geralmente é o tipo (ex: `Integer`, `String`, etc).
       - As constraints (como `primary_key=True`, `nullable=False`, `unique=True`) são passadas como kwargs.
   - **Facilidade de Importação:**  
        - Crie um arquivo `models/__init__.py` que importe todos os models para facilitar o acesso em outras partes do projeto.
        - O `TimestampModel` não precisa ser importado.

4. **Conexão do DB no `app.py`**  
   - Configure as variáveis de ambiente do SqlAlchemy antes de inicializar o app.
      - `SQLALCHEMY_DATABASE_URI`
      - `SQLALCHEMY_TRACK_MODIFICATIONS`
   - A inicialização do DB com `db.init_app(app)` deve ocorrer após a definição das variáveis de ambiente.

## Migrations

[Documentação oficial do flask-migrate](https://flask-migrate.readthedocs.io/en/latest/)

1. **Instalação do Flask-Migrate**  
   ```bash
   pip install Flask-Migrate
   ```

2. **Configuração das Migrations**  
   - Importe e inicialize o `Migrate` no `app.py` após a conexão com o DB.
   - **IMPORTANTE:** Os models devem estar importados no `app.py`, senão as migrations não conseguem detectá-los.

3. **Comandos da CLI do Flask para Migrations**

   - **Inicializar as migrations** (Criação da pasta `database/migrations`):
     ```bash
     flask db init -d database/migrations
     ```

   - **Criar novas migrations** (Baseado nas alterações nos models):
     ```bash
     flask db migrate -d database/migrations
     ```
     - Se um **model for novo** → `CREATE TABLE`
     - Se um **model for alterado** → `ALTER TABLE`

   - **Aplicar as migrations ao banco de dados**:
     ```bash
     flask db upgrade -d database/migrations
     ```

4. **Verificando migrations aplicadas**
   - Última migration aplicada:
     ```bash
     flask db current -d database/migrations
     ```
   - Últimas migrations aplicadas:
     ```bash
     flask db heads -d database/migrations
     ```
   - Histórico completo das migrations:
     ```bash
     flask db history -d database/migrations
     ```

5. **Rollback (Reverter migrations)**
   - **Reverter a última migration**:
     ```bash
     flask db downgrade -d database/migrations
     ```
   - **Reverter para um ID específico** (Dica: verifique as migrations aplicadas):
     ```bash
     flask db downgrade <id_migration> -d database/migrations
     ```
   - **Reverter todas as migrations (reset do DB)**:
     ```bash
     flask db downgrade base -d database/migrations
     ```