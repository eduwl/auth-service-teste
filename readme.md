# Auth Service Teste

Gera token com as credenciais corretas e valida acesso a endpoints em que determinada role é necessaria.

## Dependências
- `fastapi`
- `httpx`
- `pydantic`
- `pydantic-settings`
- `python-dotenv`
- `PyJWT`
- `pytest`
- `uvicorn`

## Configurando

Tenha na raiz do projeto um arquivo `.env`

```.env
SECRETY_KEY="SUPER_SUPER_SECRET"
```

## Makefile

O projeto contem um `Makefile` para agilizar comandos comuns, execute os comandos abaixo na raiz do projeto.

### Teste
- Para realizar os testes unitarios presentes no projeto use o seguinte comando.
```bash
make test
```

### DEV
- Para iniciar a aplicação diretamente da pasta do projeto use o seguinte comando.
```bash
make dev
```

### Run com Docker
- Para iniciar e rodar o projeto em um container docker use o seguinte comando para gerar a imagem e subir um container com o projeto.
```bash
make run
```

### Remover container docker
- Use o seguinte comando para remover o container docker do projeto.
```bash
make down
```

