# Bloxs

Full-Stack Developer (Python/Flask) - Bloxs Challenge


First of all, create an environment with ```python3 -m venv .venv```, active with ```source .venv/bin/activate``` then install the dependencies ```pip install -r requirements.txt```

Start the container with database:
```docker-compose up -d```

To acess the container, run:
```docker exec -it flask_app bash```


# Database

To create the database, run this command:
```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```


# TODOs

Implementar os endpoints listados abaixo

### Endpoints

- [x] Criação de uma conta;
- [x] Depósito em uma conta;
- [x] Consulta de saldo em determinada conta;
- [x] Saque em uma conta;
- [x] Bloqueio de uma conta;
- [ ] Extrato de transações de uma conta;

### Testes

- [x] Criação de uma conta;
- [x] Depósito em uma conta;
- [x] Consulta de saldo em determinada conta;
- [ ] Saque em uma conta;
- [ ] Bloqueio de uma conta;
- [ ] Extrato de transações de uma conta;
- [ ] Fix pytest configuration to load env with ENVIRONMENT=test
 