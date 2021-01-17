class Produto:

    def __init__(self, nome, preco):
        self._clientes = []
        self._nome = nome
        self._preco = preco


    @property
    def nome(self):
        return self._nome
    

    @nome.setter
    def nome(self, nome):
        self.notify(f"Nosso produto mudou de nome\n{self._nome} --> {nome}")
        self._nome = nome


    @property
    def preco(self):
        return self._preco
    

    @preco.setter
    def preco(self, preco):
        self.notify(f"Nosso produto está com um novo preço\n{self._preco:.2f} --> {preco:.2f}")
        self._preco = preco
    

    def subscribe(self, cliente):
        if cliente not in self._clientes:
            self._clientes.append(cliente)    

            return True
        return False

    
    def unsubscribe(self, cliente):
        if cliente in self._clientes:
            self._clientes.remove(cliente)    

            return True
        return False


    def notify(self, msg):
        for cliente in self._clientes:
            cliente.update(msg)
            print()


class Cliente:
    
    def __init__(self, nome):
        self._nome = nome


    @property
    def nome(self):
        return self._nome


    @nome.setter
    def nome(self, nome):
        self.nome = nome


    def update(self, msg):
        print(f"Olá {self._nome}\nTemos uma notificação para você")
        print('-' * 40)
        print(msg)


c1 = Cliente("daniel")
c2 = Cliente("marcos")

p = Produto("Manteiga", 3)
p.subscribe(c1)
p.subscribe(c2)

p.nome = "Margarina"
