# Teste em python para criptografia

## Criando ambiente
Esse repositório utiliza Poetry para gerir o projeto. Caso não tenha:

```
pip install poetry
```

## Instalando as dependências

Para isso, com o poetry já instlado, pasta acessa-lo:

```
poetry shell
```

Instale as dependências 

```
poetry install
```

Nesse ponto podemos rodar os testes de cobertura, basta no terminal já dentro do ambiente virtual digitar:

```
task test
```

Assim será possivel ver os testes escritos

Para ver a cobertura dos testes no codigo, podemos visualmente atraves de um navegaor, no meu caso firefox:

```
firefox htmlcov/index.html
```