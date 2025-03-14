import PySimpleGUI as sg


#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key= 'usuario', size=(20,1)), ],
    [sg.Text('Senha'), sg.Input(key= 'senha', password_char= '*',size=(20,1))],
    [sg.Checkbox('Mantenha-me conectado')],
    [sg.Button('Entrar')]
]
#Janela

janela = sg.Window('Tela de Login', layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'ticy' and valores['senha'] == '123':
            print('Bem-vinda a Dev Aprender!')