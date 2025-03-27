class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
    
    def calcular_salario(self):
        return self.salario_base


class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus
    
    def calcular_salario(self):
        return self.salario_base + self.bonus


class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, comissao):
        super().__init__(nome, salario_base)
        self.comissao = comissao
    
    def calcular_salario(self):
        return self.salario_base + self.comissao


funcionario = Funcionario("Ana", 3000)
gerente = Gerente("Gabriel", 5000, 2000)
vendedor = Vendedor("Antony", 2500, 800)

print(f"Salário do Funcionário: {funcionario.calcular_salario()}")
print(f"Salário do Gerente: {gerente.calcular_salario()}")
print(f"Salário do Vendedor: {vendedor.calcular_salario()}")
