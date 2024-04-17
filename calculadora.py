import math

class Calculadora:
    def __init__(self):
        pass
    
    def soma(self, n1:int, n2:int):
        return n1 + n2
    
    def sub(self, n1:int, n2:int):
        return n1 - n2
    
    def mult(self, n1:int, n2:int):
        return n1 * n2
    
    def divi(self, n1:int, n2:int):
        if n2 == 0 or n1 == 0:
            return "Erro: divisão por zero."
        return n1 / n2
    
    def porcent(self, valor:int, percentual:int):
        return (valor * percentual) / 100
    
    def raiz_quadrada(self, n1:int):
        return math.sqrt(n1)
    
    def potenciacao(self, base:int, expoente:int):
        return base ** expoente
    
    def confirmar_str(self,a:str):
        return a
    
    def confirmar_none(self, b:None):
        return b