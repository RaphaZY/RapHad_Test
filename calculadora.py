import math

class Calculadora:
    def __init__(self):
        pass
    
    def somar(self, n1:int, n2:int):
        return n1 + n2
    
    def subtrair(self, n1:int, n2:int):
        return n1 - n2
    
    def multiplicar(self, n1:int, n2:int):
        return n1 * n2
    
    def dividir(self, n1:int, n2:int):
        if n2 == 0 or n1 == 0:
            raise ZeroDivisionError('Divisão Por Zero')
        return n1 / n2
    
    def porcentagem(self, valor:int, percentual:int):
        return (valor * percentual) / 100
    
    def raiz_quadrada(self, n1:int):
        return math.sqrt(n1)
    
    def potenciacao(self, base:int, expoente:int):
        return base ** expoente
    
    def logaritmo(self, log, base):
        return math.log(log,base)

cal = Calculadora()
print(cal.dividir(2,0))