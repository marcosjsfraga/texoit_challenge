
#### Como instalar com Pyenv
```bash
$ pyenv virtualenv 3.11.2 venv-python-3.11.2
$ pyenv activate venv-python-3.11.2
$ pip install -r requirements.txt
$ python scr/main.py
```

#### Como executar o projeto
```bash
$ python scr/main.py
```

#### URL do endpoint que verifica status da API
http://localhost:8000/apistatus


#### URL do endpoint que retorna os produtores
http://localhost:8000/producers_by_prize_ranges


#### Como executar os testes:
```bash
$ pytest -v
```
