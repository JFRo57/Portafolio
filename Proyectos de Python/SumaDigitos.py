#Definimos la clase Potencia, el cual es la calculadora de la potencia
class Potencia:
    def __init__(self, base, exp): # Se define el constructor
        self.base = base #Base de la potencia
        self.exp = exp   #El exponente al que será elevada

#Calculamos la potencia en de la base con el exponente
    def calcular_potencia(self):
        return self.base ** self.exp

class SumaCuadrados(Potencia): # Esta Clase sumará los cuadrados de los dígitos
    def __init__(self, numeros2):
        self.numeros2 = numeros2 #Se define el contructor de la clase

    def calcular_cuadrados(self):
        suma = 0
        for num in str(self.numeros2): #Se leen los numeros y se tranforman en digitos individuales
            potencia = Potencia(int(num), 2) #Se elevan esos dígitos al cuadrado
            suma += potencia.calcular_potencia() # Se calcula la suma de los cuadrados de esos números
        return suma 

class SumaCubos(Potencia): # Esta Clase sumará los cubos de los dígitos
    def __init__(self, numeros3):#Se define el contructor de la clase

        self.numeros3 = numeros3

    def calcular_cubos(self):
        suma = 0
        for num in str(self.numeros3): #Se leen los numeros y se tranforman en digitos individuales
            potencia = Potencia(int(num), 3)#Se elevan esos dígitos al cubo
            suma += potencia.calcular_potencia() # Se calcula la suma de los cubos de esos números
        return suma

numeros = 111 #Ejemplo puede ser cambiado por cualquier número, sin embargo para fines prácticos lo dejamos en este


suma_cuadrados = SumaCuadrados(numeros) #Usamos los métodos 
resultado_cuadrados = suma_cuadrados.calcular_cuadrados()
print("Cuadrados Resultado:", resultado_cuadrados)# Imprimimos el resultado

suma_cubos = SumaCubos(numeros)
resultado_cubos = suma_cubos.calcular_cubos()
print("Cubos Resultado:", resultado_cubos)# Imprimimos el resultado 

resultado_final = resultado_cuadrados + resultado_cubos
print("Resultado Final:", resultado_final)#Imprimios el resultado final 
