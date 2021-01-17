class Observable:

    def __init__(self):
        self._observers = []


    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)    

            return True
        return False

    
    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)    

            return True
        return False


    def notify(self, msg):
        for observer in self._observers:
            observer.update(f"{msg}")
                


class Observer:
    
    def __init__(self, nome):
        self._nome = nome


    def update(self, msg):
        print(f"{msg}")


cliente1 = Observer()
cliente2 = Observer()
cliente3 = Observer()

produto = Observable()

produto.subscribe(cliente1)
produto.subscribe(cliente2)
produto.subscribe(cliente3)

produto.notify("Hello, World!!")
