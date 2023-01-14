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
    seguidores = values[1]
    likes_input = values[2]
    
    print(nome_relatorio)
    print(seguidores)
    print(likes_input)
    
window.close()