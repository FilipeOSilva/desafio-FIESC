# Teste de Docker com ROS

## Criando Docker
Esse repositório utilizar Docker para gerir o ambiente, caso não tenha:

```
sudo apt install docker
```

## Montando (build) o container
Com o docker já instalado:

```
sudo docker build -t ros2_desafio .
```


## Executando o container
Basta no terminal executar o comando a seguir e já será impressa as mensagens referente a memória:

```
sudo docker run -it --rm ros2_desafio
```
