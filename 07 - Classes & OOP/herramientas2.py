class Herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def funcion_primo(self):
        for i in self.lista:
            if (self.__funcion_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo') 

    def convertir(self, origen, final):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__convertir(i, origen, final), 'grados', final)

    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))


    def __funcion_primo(self, num):
        esPrimo = True
        for n in range (2, num):
            if(num % n == 0):
                esPrimo = False
                break
        return esPrimo

    def valor_modal(self, lista, menor = True): # trabaja sola porque ya trabaja con una lista de numeros
    
        lista_unicos = []
        lista_repeticiones = []
        if len(lista) == 0:
            return None
        if (menor):
            lista.sort()
        else:
            lista.sort(reverse=True)
        for elemento in lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo

    def __convertir(self, valor, origen, final):
        valor_final = None
        if(origen == 'celsius'):
            if (final == 'celsius'):
                valor_final = valor
            elif (final == 'farenheit'):
                valor_final = (valor + 9/5) + 32
            elif (final == 'kelvin'):
                valor_final = (valor + 273.15)
            else:
                print("Parametro final incorrecto")
        elif (origen == 'farenheit'):
            if (final == 'celsius'):
                valor_final = 5*(valor - 32)/9
            elif(final == 'farenheit'):
                valor_final = valor
            elif (final == 'kelvin'):
                valor_final = 5*(valor - 32)/9 + 273.15
            else: 
                print("Parametro final incorrecto")
        elif (origen == 'kelvin'):
            if (final == 'celsius'):
                valor_final = valor - 273.15
            elif(final == 'farenheit'):
                valor_final = (((valor - 273.15)*9)/5) + 32
            elif (final == 'kelvin'):
                valor_final = valor
            else: 
                print("Parametro final incorrecto")
        else: print('Parametro de origen incorrecto')
        return valor_final

    def __factorial(self, num):
        if(type(num) != int):
            return "el numero debe ser un entero"
        if (num < 0):
            return "El numero debe ser positivo"
        if (num > 1):
            num = num * self.__factorial(num - 1)
        return num       