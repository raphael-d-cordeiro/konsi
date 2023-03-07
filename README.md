<h3 align="center">Konsi</h3>

---

<p align="center"> Desafio Python API
</p>
<p>
A Konsi coleta uma variedade de dados que não são facilmente acessíveis, para propor melhores opções de créditos para seus clientes. Um dos tipos de dados coletados é o número da matrícula do aposentado ou pensionista.

O desafio é fazer uma API que busque e retorne a matrícula do servidor em um determinado portal.

Será necessário desenvolver um crawler para coletar esse dado no portal e uma API para fazer input e buscar o resultado depois.

Requisitos

● Organização do código

● Testes

● Facilidade ao rodar o projeto

● Facilidade ao rodar o projeto

● Performance: aqui avaliaremos o tempo para crawlear o dado.

</p>


##  Execução do Projeto

### Pré-requisitos

What things you need to install the software and how to install them.

```
Python 3.10+
Rabbitmq 
Redis
Postgresql
```

### Instalação

Uma série passo a passo de exemplos que informam como executar um ambiente de desenvolvimento.


1. Clonar o repositório Git

```
git clone https://github.com/raphael-d-cordeiro/konsi.git
cd konsi
```
##### Sem Docker

2. Instalar as dependências(virtualenv recomendado)

```
pip install -r konsi_api/requirements.txt
pip install -r konsi_worker/requirements.txt
```
3. Configurar env file

```
cp .env.example .env

# preencher .env variaveis
```

4. Executar servidor API

```
python konsi_api/src/main.py
```

5. Executar Worker

```
cd konsi_worker
celery -A src.celery_worker worker -E --loglevel=INFO --concurrency=1 -Ofair
```

6. Testar as rotas pela Documentação

```
http://127.0.0.1:8000/docs/

```

##### Com Docker Compose (recommended)

1. build & run

```
docker-compose up -d
```

## Executando os testes

Para executar os testes de unidade com PyTest após a instalação, execute na pasta do projeto

```
pytest -v
```

## Built Using 

- [FastApi](https://fastapi.tiangolo.com/) - REST API Framework
- [Sqlalchemy](https://www.sqlalchemy.org/) - Database ORM
- [PyTest](https://pytest.org/) - Test Tools