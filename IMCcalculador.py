import PySimpleGUI  as sg 
sg.theme("TanBlue")

Layout = [
    [sg.Text('IMC')],
    [sg.Text('massa '),sg.Input(key='-MASS-',size=(5,1))],
    [sg.Text('altura '),sg.Input(key='-HIGH-',size=(5,1))],
    [sg.Push(),sg.Button('calcular'),sg.Push()]
]

window = sg.Window('IMC',layout=Layout,font='Monaco 18')

while True:
    event, value = window.read()
    print(event,value)
    massa=float(value['-MASS-'])
    altura=float(value['-HIGH-'])
    imc = massa / (altura**2)
    sg.Popup(f' seu resultado é {imc:.2f}')
    if event == 'QUIT' or event == sg.WIN_CLOSED:
        break
