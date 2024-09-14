# Simples Sistema Bancário - Desafio DIO/NTT DATA

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## Descrição

Este projeto consiste em um **sistema bancário simples** criado como parte do desafio da trilha de Engenharia de Dados com Python, promovida pela **NTT Data** em parceria com a **DIO**. O sistema permite depósitos, saques e exibição de extrato bancário de forma simples e prática, aplicando regras como:

- **Depósito**: Apenas valores positivos são aceitos.
- **Saque**: Até 3 saques diários, com um limite de R$ 500 por saque.
- **Extrato**: Exibe todos os depósitos e saques realizados, bem como o saldo final da conta.

## Funcionalidades

- **Depósito**: Permite realizar depósitos de valores positivos, que são refletidos no saldo e no extrato.
- **Saque**: Limita a quantidade de saques a 3 por dia, com um valor máximo de R$ 500 por saque. O saldo disponível é atualizado automaticamente.
- **Extrato**: Lista todas as operações (depósitos e saques) realizadas, mostrando o saldo final ao final do extrato.

## Requisitos

- Python 3.8+
- Módulo `datetime` (disponível na biblioteca padrão do Python)

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do sistema.
- **VSCode**: Editor de código recomendado para trabalhar no projeto.

## Como Executar o Projeto

1. Clone este repositório:
    ```bash
    git clone git@github.com:theophiloweb/DIO-Desafio-Sistema-Bancario-2024.git
    ```

2. Acesse o diretório do projeto:
    ```bash
    cd nome-do-repositorio
    ```

3. Execute o script Python:
    ```bash
    python sistema_bancario.py
    ```

## Contato

- E-mail: [teophilo@gmail.com](mailto:teophilo@gmail.com)
- LinkedIn: [Teophilo Silva](https://www.linkedin.com/in/teophilo-silva-dev)

## Exemplo de Código

Aqui está um trecho do código para ilustrar a funcionalidade de saque do sistema:

```python
def saque(valor):
    if valor > 0:
        global saldo
        global count
        if valor <= saldo and count < 3:
            saldo -= valor
            count += 1
            msg.append(f'{dt_operacao.strftime("%d/%m/%Y %H:%M")}: Saque de R$ {valor}.')
            return f'Saque de R$ {valor} realizado com sucesso. Operação {count}/{QTD_SAQUE_DIARIO} restante(s).'
        else:
            if saldo < valor:
                return f'Saldo insuficiente. Tente novamente. {QTD_SAQUE_DIARIO - count} saques restantes.'
            else:
                return f'Limite de saques por dia atingido. Tente novamente. {QTD_SAQUE_DIARIO - count} saque(s) restante(s).'
    else:
        return 'Valor inválido.'
```


## Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.



