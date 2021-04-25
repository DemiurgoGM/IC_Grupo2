# Código Fonte - IC Grupo 2

## Instalação 

##### Docker

A instalação desse projeto requer [docker](https://docs.docker.com/engine/install/) e o [compose](https://docs.docker.com/compose/install/) 

## Execução

##### Via docker-compose

Para instalar todas as dependências do projeto, fazer binding das portas localmente e executar o servidor django, basta executar, a partir da raíz do projeto:

```
    docker-compose -f docker/docker-compose.yml up
```