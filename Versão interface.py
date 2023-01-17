import PySimpleGUI as sg

sg.theme('DarkPurple1')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Relatório Instagram')],
            [sg.Text('Insira o nome do relatório'), sg.InputText()],
            [sg.Text('Insira a quantidade de seguidores'), sg.InputText()],
            [sg.Text('Insira os likes dos posts (separe com uma ",")'), sg.InputText()],
            [sg.Text('Digite a data do primeiro post'), sg.InputText()],
            [sg.Text('Digite a data do último post'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Relatório', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    #Programa - início
        
    #Caputurando inputs    
    nome_relatorio = values[0]
    seguidores = int(values[1])
    likes_input = values[2]
    
    # Transformando os likes em um array de string (que vai ser convertido pra número depois)
    likes_list_string = likes_input.split(',')
    
    # Passando por cada elemento da lista, transformando em números e adicioando
    # à uma nova lista que só vai ter números
    likes_list = []
    
    for elemento in likes_list_string:
        likes_convertido_em_numero = int(elemento)

        # adicionando o numero de likes do post no array
        likes_list.append(likes_convertido_em_numero) 
        
    # Estatísticas
    total_likes = sum(likes_list)
    total_posts = len(likes_list) # Tamanho da lista (quantos elementos tem) é o número de posts
    average_likes_per_post = total_likes / total_posts
    
    print(nome_relatorio)
    print(seguidores)
    print(likes_list)
    print(sum(likes_list))
    
window.close()