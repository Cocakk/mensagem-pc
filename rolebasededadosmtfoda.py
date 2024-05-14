# calculador de lucros dinero denero lucros
from twilio.rest import Client


import pandas as pd

account_sid = ' '
auth_token = ' '
client = Client(account_sid, auth_token)
# abrir arquivos em excel 

listaM = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho'] 


for mes in listaM:
    tabelaVA = pd.read_excel(f'{mes}.xlsx')

    # analisa as data base do excel procurando o vendedor que atingiu a meta (55 mil)

    if (tabelaVA[ 'Vendas' ] > 55000).any():
        vendedor = tabelaVA.loc[tabelaVA[ 'Vendas' ] > 55000 ,'Vendedor'].values[0]
        lucro = tabelaVA.loc[tabelaVA['Vendas'] > 55000 , 'Vendas'].values[0]
        print(f'no mes de {mes} o {vendedor} gerou o total de {lucro} deneros')

        #escreve e envia a mensagem quando encontra o vendedor

        from twilio.rest import Client
        message = client.messages.create(
            from_=' ',
            to=' ',
            body = f'no mes de {mes} encontrou {vendedor} com o total de {lucro} deneros')
        

print(message.sid)


# verificar cada arquivo e ver se tem algum valor na coluna de vendas é maior que 55 mil

# se for maior que 55 mil -> envia um sms pro meu numero
# se nn, fodase
