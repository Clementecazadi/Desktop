import PySimpleGUI as sg
sg.theme('DarkTeal9')
layout = [[sg.Text('Digite a chave:'), sg.InputText('', border_width=0)],
          [sg.Text('Digite algo:'), sg.InputText('', border_width=0)],
          [sg.Button('Criptografar', border_width=0, size=(42, 1))],
          [sg.Text('Crytography:'), sg.InputText('', border_width=0)],
          [sg.Text('Decryption ?'), sg.Button('Sim', border_width=0, size=(10, 1)),
           sg.Button('Não', border_width=0, size=(10, 1))],
          [sg.InputText('', border_width=0)]]
window = sg.Window('Criptografia', layout, font='123 12', size=(400, 193))
while True:
    button, values = window.read()
    if button == sg.WIN_CLOSED:
        break

