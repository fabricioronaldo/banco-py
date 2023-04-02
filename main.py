import PySimpleGUI as sg
import janelas

janela_principal, janela_clientes, janela_cad_cliente = janelas.menu_principal(), None,None

while True:
    window, event, values = sg.read_all_windows()

    # Quando a janela for fechada
    if window == janela_principal and event == sg.WIN_CLOSED:
        break

    # Quando queremos ir para próxima janela

    if window == janela_principal and event == 'Clientes':
        janela_clientes = janelas.menu_cliente()
        janela_principal.hide()
    elif event == sg.WIN_CLOSED:
        break 
    
    if window == janela_clientes and event == 'Cadastrar Cliente':
        janela_cad_clientes = janelas.cadastrar_cliente()
        janela_clientes.hide()
    elif window == janela_clientes and event == 'Voltar':
        janela_clientes.hide()
        janela_principal.un_hide()
    elif event == sg.WIN_CLOSED:
        break

    if window == janela_cad_cliente and event == 'Voltar':
        janela_cad_clientes.hide()
        janela_clientes.un_hide()


arquivo = open('clientes.txt','a')
arquivo.write(f"{values['cpf']},{values['nome']},{values['telefone']} \n")
arquivo.close()






