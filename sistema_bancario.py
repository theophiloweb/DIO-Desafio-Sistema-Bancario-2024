'''
Depósito: Somente valores positivos. Deve ser retornado em extrato
Saques: Somente 3 por dia. Máximo de 500 por saque. Caso não tenha saldo o sistema exibe uma mensagem. Deve ser retornado os saques em extrato
Extrato: Depósitos e Saques e no fim da listagem o saldo da conta. Deve-se usar o R$.

'''
from datetime import datetime

LIMITE_DIARI0 = 500
QTD_SAQUE_DIARIO = 3
saldo = 0
msg = []
dt_operacao = datetime.now()
count = 0


def deposito(valor):
    if valor > 0:
       global saldo
       saldo += valor
       msg.append(f'{dt_operacao.strftime("%d/%m/%Y %H:%M")}: Depósito de R$ {valor}.')
       return f'Depósito de R$ {valor} realizado com sucesso.'
    else:
        return 'Valor inválido.'
    
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
        return False

def extrato():
    if len(msg) > 0:
        for value in msg:
            print(value, end='\n')
        print(f'\nSaldo total: R$ {saldo}')    
    else:
        print('Sem operações para o momento.')   


while True:
        print(
            """
            ######MENU######

            Selecione uma Opção:
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [4] Sair

            """ 
        ) 

        option = int(input("Opção: "))

        if option == 4:
            print('Saindo...')
            break
        elif option == 1:
            valor = float(input('Digite o valor para depósito: ')) 
            print(deposito(valor))
        elif option == 2:
            valor = float(input('Digite o valor para saque: '))
            print(saque(valor))      
        elif option == 3:
            extrato()
        else:
            print('Opção inválida. Tente novamente.')                
         
