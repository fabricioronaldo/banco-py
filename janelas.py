import PySimpleGUI as sg

def menu_principal():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Escolha um opção:', font=('Helvetica', 20),pad=(0,20))],
        [sg.Button('Clientes', size=(50,0))],
        [sg.Button('Contas', size=(50,0))]
    ]
    return sg.Window('Menu Principal', layout=layout, finalize=True)

def menu_cliente():

    layout = [
        [sg.Text('Escolha um opção:')],
        [sg.Button('Cadastrar Cliente', size=(50,0))],
        [sg.Button('Localizar Cliente', size=(50,0))],
        [sg.Button('Excluir Cliente', size=(50,0))],
        [sg.Button('Voltar', size=(50,0))]
    ]
    return sg.Window('Menu Cliente', layout=layout, finalize=True)

def cadastrar_cliente():

    layout = [
        [sg.Text('Cadastro de Clientes')],
        [sg.Text('CPF', size=(8,0)),sg.Input(size=(30,0),key='cpf')],
        [sg.Text('Nome', size=(8,0)),sg.Input(size=(30,0), key='nome')],
        [sg.Text('Telefone', size=(8,0)),sg.Input(size=(30,0), key='telefone')],
        [sg.Button('Cadastrar'), sg.Button('Voltar')]
    ]
    return sg.Window('Cadastro de Clientes', layout=layout, finalize=True)

janela_principal, janela_clientes, j_cad_clientes = menu_principal(), None, None
        
     #Extrair dados da tela
     #self.button, self.values = janela.Read()

#def Iniciar(self):
        
    #cpf = self.values['cpf']
    #nome = self.values['nome']
    #telefone =self.values['telefone']
    
        #print(self.values)
    #return cpf, nome, telefone


while True:
    window, event, values = sg.read_all_windows()

    # Quando a janela for fechada
    if window == janela_principal and event == sg.WIN_CLOSED:
        break

    # Quando queremos ir para próxima janela

    if window == janela_principal and event == 'Clientes':
        janela_clientes = menu_cliente()
        janela_principal.hide()

    if window == janela_clientes and event == 'Cadastrar Cliente':
        janela_cad_clientes = cadastrar_cliente()
        janela_clientes.hide()
    elif window == janela_clientes and event == 'Voltar':
        janela_clientes.hide()
        janela_principal.un_hide()
