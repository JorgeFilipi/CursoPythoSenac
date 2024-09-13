# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e
# altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas
# paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa de
# azulejos possui 1,5 m2


comp = float(input('Informe o comprimento da cozinha: '))
larg = float(input('Informe a largura da cozinha: '))
altu = float(input('Informe a autura da cozinha: '))

azul = (2*((comp*altu)+(larg*altu)))/1.5

print('Para cobrir as paredes com azulejos, serão necessários',
      azul, 'metros quadrados de azulejos.')
