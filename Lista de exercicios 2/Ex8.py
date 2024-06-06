#Construa um script em linguagem Python que utilize um dicionáriocujas chaves são os códigos do produto e os valores são o nome doproduto, o preço unitário e a quantidade comprada
# A partir dodicionário, o programa deve imprimir os itens da compra e calcular osubtotal de cada um deles, ou seja, quantidade * preço unitário. 
# Por fim,o programa deve apresentar o valor total da compra.

produtos = {}

while True:
    cod = int(input('Código: '))
    nome = input('Nome: ')
    preco = float(input('R$: '))
    qtde = int(input('Qtde: '))
    prod = []
    prod.append(nome)
    prod.append(preco)
    prod.append(qtde)
    produtos.update({cod: prod})
    resp = input('Deseja continuar [S/N]? ')
    if resp == 'N' or resp == 'n':
        break