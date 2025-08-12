import numpy as np #np es un alias

vector=np.array([1,2,3,4,5])
print(vector)  # Output: [1 2 3 4 5]
print(vector[2])#Imprime el tercer elemento
"""
Los vecores no son como las listas, no tienen un metodo end()para agregar elementos
tienen un metodo pop() para eliminar el ultimo elemento, pero si tiene metodo reshpe() para 
cambiar su forma, adicionalmente despues creado no se puede cambiar el tamaño de un vector
"""
vector=np.zeros(5)
print(vector) # Output: [0. 0. 0. 0. 0
vector2= np.ones(5)
print(vector2) # Output: [1. 1. 1. 1. 1
vector3=np.arange(1,5,100)
print("rango",vector3) # Output: [1. 1. 1. 1.
vector4=np.linspace(1,10,5)
print("linspace",vector4) # Output: [1. 3. 5.
vector5=np.random.rand(10)
print("random",vector5) # Output: [0. 0. 0.
vector6=np.random.randint(1,10,100)
print("randomint",vector6) # Output: [0. 0. 0.