class Animal:
    def emitir_som(self):
         raise NotImplementedError('Subclasse devem implementar este método')

class Cachorro(Animal):
    def emitir_som(self):
        print("Au, Au")

class Gato(Animal):
    def emitir_som(self):
        print("Miau")

class Pato(Animal):
    def emitir_som(self):
        print("Quack")

animal1 = Cachorro()
animal2 = Gato()
animal3 = Pato()

animal1.emitir_som()
animal2.emitir_som()
animal3.emitir_som()