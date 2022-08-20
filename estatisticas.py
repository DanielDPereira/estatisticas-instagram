#

númerodelikes = []

print("Insira os likes de cada post, colocando uma , depois de cada elemento ")
likes = input().split(",")

likes = int(likes)
númerodelikes.extend(likes)
númerodelikes = str(númerodelikes)

print("Média de likes por post = ")

print(sum(númerodelikes) / len(númerodelikes))

print("Quantidade de posts = ", len(númerodelikes))