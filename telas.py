import PySimpleGUI as sg

class Telas:
    
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Cadastro de Clientes')],
            [sg.Text('CPF', size=(8,0)),sg.Input(size=(30,0),key='cpf')],
            [sg.Text('Nome', size=(8,0)),sg.Input(size=(30,0), key='nome')],
            [sg.Text('Telefone', size=(8,0)),sg.Input(size=(30,0), key='telefone')],
            [sg.Button('Cadastrar')]
        ]
        
        #Janela
        janela = sg.Window('Cadastro de Clientes').layout(layout)
        
        #Extrair dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        
        cpf = self.values['cpf']
        nome = self.values['nome']
        telefone =self.values['telefone']
    
        #print(self.values)
        return cpf, nome, telefone


