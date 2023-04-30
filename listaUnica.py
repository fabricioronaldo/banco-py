class ListaUnica:
    def __init__(self, elem_class):
        self.lista = []
        self.elem_class = elem_class
    
    def __len__(self):
        return len(self.lista)
    
    def __iter__(self):
        return iter(self.lista)
    
    def __getitem__(self,p):
        return self.lista[p]
    
    def indiceValido(self, i):
        return i >= 0 and i < len(self.lista)
    
    def adiciona(self, elemento):
       if self.pesquisa(elemento) == -1:
           self.lista.append(elemento)

    def remover(self, elemento):
        self.lista.remove(elemento)

    def verifica_tipo(self, elemento):
        if type(elemento) != self.elem_class:
            raise TypeError("Tipo inválido") 
        
    def pesquisa(self, elemento):
        self.verifica_tipo(elemento)
        try:
            return self.lista.index(elemento)
        except ValueError:
            return -1
