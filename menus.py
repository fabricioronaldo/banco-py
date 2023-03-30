import PySimpleGUI as sg

def janela_principal():
    sg.theme('Reddit') 
    layout = [
            [sg.Text('Escolha uma Operação:', font=('Helvetica', 20),pad=(0,20))],
            [sg.Button('Cliente', size=(50,0))],
            [sg.Button('Conta', size=(50,0))]
        ]
    return sg.Window('Menu Principal', layout=layout, finalize=True)



