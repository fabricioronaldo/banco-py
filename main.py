from telas import Telas

tela = Telas()
dados = tela.Iniciar()

arquivo = open('clientes.txt','a')
arquivo.write(f'{dados[0]},{dados[1]},{dados[2]} \n')
arquivo.close()






