import PySimpleGUI as sg

def menu_principal():
    
    layout = [
        [sg.Text('Escolha um opção:')],
        [sg.Button('Clientes')],
        [sg.Button('Contas')],
    ]
    return sg.Window('Menu Principal', layout=layout, finalize=True)

def menu_cliente():

    layout = [
        [sg.Text('Escolha um opção:')],
        [sg.Button('Cadastrar Cliente')],
        [sg.Button('Localizar Cliente')],
        [sg.Button('Excluir Cliente')],
        [sg.Button('Voltar ao menu Principal')],
    ]
    return sg.Window('Menu Cliente', layout=layout, finalize=True)

def cadastrar_cliente():
    layout = [
        [sg.Text('Cadastro de Clientes')],
        [sg.Text('CPF', size=(8,0)),sg.Input(size=(30,0),key='cpf')],
        [sg.Text('Nome', size=(8,0)),sg.Input(size=(30,0), key='nome')],
        [sg.Text('Telefone', size=(8,0)),sg.Input(size=(30,0), key='telefone')],
        [sg.Button('Cadastrar')]
    ]
    return sg.Window('Cadastro de Clientes', layout=layout, finalize=True)

janela_principal, janela_clientes = menu_principal(), None
        
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

    if window == janela_principal and event == 'Menu Cliente':
        janela_clientes = menu_cliente()
        janela_principal.hide()