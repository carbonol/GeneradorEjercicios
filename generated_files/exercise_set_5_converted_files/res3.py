# Importación del módulo de funciones generadoras - NO MODIFICAR
from pydoc import importfile
idg = importfile('C:/Users/leand/Documents/Python3Projects/GeneradorEjercicios/PythonInputInstrToFunctConverter/input_data_generators.py')
sequential_idg_list = []
for i in range(1): sequential_idg_list.append([0])
# Fin de la importación del módulo de funciones generadoras - NO MODIFICAR
num = 1
acum = 0
while (num != 0):
    num = idg.fixed_sequential_int_data_from_list_gen([-1, -2, -7, 4, 2, -5, 0], sequential_idg_list[0])
    if (num != 0):
        if (num > 0):
            acum += 1
print(acum)