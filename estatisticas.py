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

print('Total de Likes:', total_likes)
print('Total de Posts:', total_posts)
print('Média de Likes por Posts:', average_likes_per_post)
