# Configuración inicial para generar archivos de entrada de este programa - NO MODIFICAR
import sys
input_data_list = []
input_data_file_route = None
if (len(sys.argv) == 2):
	input_data_file_route = sys.argv[1]
# Fin de configuración inicial para generar archivos de entrada de este programa - NO MODIFICAR
# Importación del módulo de funciones generadoras - NO MODIFICAR
from pydoc import importfile
idg = importfile('C:/Users/leand/Documents/Python3Projects/GeneradorEjercicios/PythonInputInstrToFunctConverter/input_data_generators.py')
sequential_idg_list = []
for i in range(1): sequential_idg_list.append([0])
# Fin de la importación del módulo de funciones generadoras - NO MODIFICAR
num = 1
acum = 0
while (num != 0):
    # num = idg.fixed_sequential_int_data_from_list_gen([-1, -2, -7, 4, 2, -5, 0], sequential_idg_list[0])
    # num = idg.fixed_sequential_int_data_from_list_gen([2, 3, 5, 0], sequential_idg_list[0])
    # num = idg.fixed_sequential_int_data_from_list_gen([-4, -7, -6, 0], sequential_idg_list[0])
    # num = idg.fixed_sequential_int_data_from_list_gen([2, 4, 6, -3, -1, 2, 0], sequential_idg_list[0])
    num = idg.fixed_sequential_int_data_from_list_gen([0], sequential_idg_list[0])
    input_data_list.append(num)
    if (num != 0):
        if (num > 0):
            acum += 1
print(acum)
# Configuración final para generar archivos de entrada de este programa - NO MODIFICAR
if (input_data_file_route != None and input_data_file_route.endswith('.txt')):
	with open(input_data_file_route, mode='w', encoding='utf-8') as input_file:
		counter = len(input_data_list) # Variable auxiliar para no dejar líneas en blanco en el archivo .txt
		for input_data in input_data_list:
			if (counter != 1):
				input_file.write(str(input_data) + '\n')
			else:
				input_file.write(str(input_data))
			counter -= 1
# Fin de configuración final para generar archivos de entrada de este programa - NO MODIFICAR
