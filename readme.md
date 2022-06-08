
# Projeto números romanos 

Para rodar o projeto, basta:

```
docker build -t 'nome' .

docker run -p 8080:8000 nome

Abrir o link http://localhost:8080/graphql

Escrever a consulta no formato: 

mutation {
    search(text: "MMMCMXCIX") {
        number
        value
    }
}

```

