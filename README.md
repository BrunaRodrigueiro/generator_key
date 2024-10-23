# Gerador de Senhas em Python

Este projeto é um **gerador de senhas** desenvolvido em Python, criado como uma forma de **praticar lógica de programação**. O código utiliza funções integradas da linguagem para gerar senhas aleatórias que combinam letras maiúsculas, minúsculas, números e caracteres especiais.

## Funcionalidades

- Geração de senhas com um número de caracteres especificado.
- Utilização de letras (maiúsculas e minúsculas), números e símbolos.
- Uso de bibliotecas padrão como `random` e `string` para gerar os caracteres aleatórios.

## Como funciona

O gerador de senhas escolhe aleatoriamente caracteres de três grupos: letras, dígitos e caracteres especiais. O comprimento da senha é determinado pelo valor que o usuário passa como argumento na função `password_generator()`. A senha gerada é então exibida no console.

### Estrutura do Código

1. **Importação de módulos**:
   - `random`: Utilizado para gerar a escolha aleatória de caracteres.
   - `string`: Fornece constantes como letras (`ascii_letters`), dígitos (`digits`) e caracteres especiais (`punctuation`).

2. **Função `password_generator(key)`**:
   - Gera uma senha de acordo com o número de caracteres (key) fornecido.
   - Escolhe caracteres aleatórios do conjunto `string.ascii_letters`, `string.digits` e `string.punctuation`.

3. **Exemplo de Execução**:
   - O código gera uma senha de 12 caracteres aleatórios e a exibe no console.

## Como Executar

Para executar o gerador de senhas, siga os seguintes passos:

1. Clone este repositório ou copie o código para seu ambiente local.
2. Certifique-se de que você tem o Python instalado. Se não tiver, baixe e instale [Python](https://www.python.org/downloads/).
3. Execute o script Python.

### Exemplo de execução

```bash
$ python password_generator.py
```

No console, o resultado será algo parecido com:

```
Senha gerada: A7f!vG$2k&J#
```


## Objetivo do Projeto

Este projeto foi criado com o objetivo de **praticar conceitos de lógica de programação** em Python, como:
- Manipulação de strings.
- Uso de funções.
- Geração de números aleatórios.
- Manipulação de listas e loops.

## Aprendizados

Ao desenvolver este gerador de senhas, você aprenderá a:
- Trabalhar com a biblioteca `random` para gerar resultados aleatórios.
- Utilizar a biblioteca `string` para acessar caracteres alfabéticos e especiais.
- Escrever funções em Python e retornar resultados.
- Utilizar o método `''.join()` para concatenar strings de forma eficiente.

## Requisitos

- Python 3.x

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request com melhorias no código ou na documentação.

## Licença

Este projeto é de código aberto e está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
