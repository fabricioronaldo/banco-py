import PySimpleGUI as sg
from telas import Telas
import menus
import janelas

#janela_principal, janela_clientes = janelas.menu_principal(), None

# Criar um loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()

    # Quando a janela for fechada
    if window == janelas.janela_principal and event == sg.WIN_CLOSED:
        break

    # Quando queremos ir para próxima janela

    if window == janelas.janela_principal and event == 'Menu Cliente':
        janela.janela_clientes = janelas.menu_cliente()
        janela.janela_principal.hide()

    #if window == janela_c and event == 'Enviar':
     #   cc = {'numero':values['conta'],'titular':values['titular'],'saldo':values['saldo'],'limite':values['limite']}
      #  conta = Conta(cc['numero'],cc['titular'],cc['saldo'],cc['limite'])
       # print(conta)
    #elif window == janela_c and event == 'Voltar':
     #   janela_c.hide()
      #  janela_p.un_hide()

    #if window == janela_p and event == 'Extrato':
     #   janela_e = janela_extrato()
      #  janela_p.hide()

    #if window == janela_e and event == 'Voltar':
     #   janela_e.hide()
      #  janela_p.un_hide()

    #if window == janela_p and event == 'Depositar':
     #   janela_d = janela_depositar()
      #  janela_p.hide()

    #if window == janela_d and event == 'Voltar':
     #   janela_d.hide()
      #  janela_p.un_hide()






#j1 = menus.janela_principal()
#tela = Telas()
#dados = tela.Iniciar()

#arquivo = open('clientes.txt','a')
#arquivo.write(f'{dados[0]},{dados[1]},{dados[2]} \n')
#arquivo.close()






