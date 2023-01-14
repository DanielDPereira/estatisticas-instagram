#Relatório para Instagram

nome_relatorio = str(input("Digite o nome do relatório: "))

seguidores = int(input("Digite a quantidade de seguidores: "))

likes_input = input('Insira os likes dos posts (separe com uma ","): ')

# Transformando os likes em um array de string (que vai ser convertido pra número depois)
likes_list_string = likes_input.split(',')

# Passando por cada elemento da lista, transformando em números e adicioando
# à uma nova lista que só vai ter números
likes_list = []

for elemento in likes_list_string:
    likes_convertido_em_numero = float(elemento)

    # adicionando o numero de likes do post no array
    likes_list.append(likes_convertido_em_numero) 
    
# Estatísticas
total_likes = sum(likes_list)
total_posts = len(likes_list) # Tamanho da lista (quantos elementos tem) é o número de posts
average_likes_per_post = total_likes / total_posts

#Código data - Início

#Use o modelo DD/MM/AAAA

def dia_no_ano(dia, mes, ano):
  numero_de_dias = dia
  contador_meses = 1
  while contador_meses < mes:
    if contador_meses in (1, 3, 5, 7, 8, 10, 12):
      numero_de_dias += 31
    elif contador_meses in (4, 6, 9, 11):
      numero_de_dias += 30
    elif contador_meses == 2:
      numero_de_dias += 28
    contador_meses += 1
  return numero_de_dias

def bissexto(ano):
  return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

def validar_data(dia, mes, ano):
  if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1583:
    return False
  if mes in (4, 6, 9, 11) and dia == 31:
    return False
  if mes == 2 and dia >= 30:
    return False
  if mes == 2 and dia == 29 and not bissexto(ano):
    return False
  return True

def diferenca_data(data1, data2):

  # Separa os dados adequadamente e trata entradas mal-formadas.
  try:
    dia1, mes1, ano1 = [int(datando) for datando in data1.split("/")]
  except ValueError:
    raise ValueError('Data inválida: ' + data1)

  try:
    dia2, mes2, ano2 = [int(datador) for datador in data2.split("/")]
  except ValueError:
    raise ValueError('Data inválida: ' + data2)

  # Verifica se as datas entradas são válidas:
  if not validar_data(dia1, mes1, ano1):
    raise ValueError('Data inválida: ' + data1)
  if not validar_data(dia2, mes2, ano2):
    raise ValueError('Data inválida: ' + data2)

  # Inverte as datas se a data2 anteceder a data1.
  if ano2 < ano1 or (ano2 == ano1 and (mes2 < mes1 or (mes2 == mes1 and dia2 < dia1))):
    return -diferenca_data(data2, data1)

  # Calcula o número de dias nos anos incompletos.
  dias_ano1 = dia_no_ano(dia1, mes1, ano1)
  dias_ano2 = dia_no_ano(dia2, mes2, ano2)

  # Calcula o número de dias totais, considerando os anos incompletos e anos completos de 365 dias.
  dias_total = dias_ano2 - dias_ano1 + (ano2 - ano1) * 365

  # Considera anos começando em 01/03 para poder fazer a correção dos anos bissextos.
  ano1b = ano1
  if mes1 < 3:
    ano1b -= 1

  ano2b = ano2
  if mes2 < 3:
    ano2b -= 1

  # Soma os dias dos anos bissextos. São os divisíveis por 4 que ocorrem entre ano1b e ano2b.
  dias_total += int(ano2b / 4) - int(ano1b / 4)

  # Subtrai os dias dos anos bissextos que não existiram na etapa anterior. São os divisíveis por 100.
  dias_total -= int(ano2b / 100) - int(ano1b / 100)

  # Soma de volta os dias dos anos bissextos que foram removidos a mais na etapa anterior. São os divisíveis por 400.
  dias_total += int(ano2b / 400) - int(ano1b / 400)

  # Resultado da função.
  return dias_total

####### Início do programa. #######

# Lê a entrada do usuário.
x = input(("Digite a data do primeiro post: "))
y = input(("Digite a data do último post: "))

# Calcula a diferença.
diferenca = diferenca_data(x, y)

#Código data - Fim

#Print dos resultados - Início

print(nome_relatorio)
print("Total de seguidores:", seguidores)
print("Total de Likes:", total_likes)
print("Total de Posts:", total_posts)
print("Média de Likes por Posts:", average_likes_per_post)
print("Período: "+str(diferenca)+" dias")
print("Em média, posts a cada "+str(diferenca/total_posts)+" dias")
#Print dos resultados - Fim

#Só para não fechar o cmd
input()

