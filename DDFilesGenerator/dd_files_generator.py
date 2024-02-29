import sys
import tkinter as tk
from tkinter import filedialog
import os

# Esto no funciona:
# from print_combinations_list import gen_variant_combinations_list as gvcl
# Usar esto en su lugar:
from pydoc import importfile
# Módulo de funciones generadoras de datos
# GEN_VARIANT_COMBINATIONS_LIST_MODULE_FILE = 'C:/Users/leand/Desktop/Experimentos en Python/Uso del generador automático de ejercicios/CodeAssembler/print_combinations_list.py'
GEN_VARIANT_COMBINATIONS_LIST_MODULE_FILE = 'C:/Users/leand/Documents/Python3Projects/GeneradorEjercicios/CodeAssembler/print_combinations_list.py'
gvcl = importfile(GEN_VARIANT_COMBINATIONS_LIST_MODULE_FILE)

MAIN_FILE_KEYWORD = 'main.py'
SUB_CODE_DIR_KEYWORD = 's'
SUB_CODE_VARIANT_FILE_KEYWORD = 'v'
PYTHON_FILE_EXTENSION = '.py'
EXERCISE_VARIANT_FILE_KEYWORD = 'res'
DIFFICULTY_TXT_FILE_NAME = 'dificultad.txt'
DIFFICULTY_KEYWORD = 'dificultad'
TEXT_FILE_EXTENSION = '.txt'
DESCRIPTORS_KEYWORD = 'descriptores'

# Para permitir al usuario definir niveles de dificultad y descriptores por código base (CB) y/o variante de subcódigo (VS), 
#   y no por variante de ejercicio (VE), crear un programa en Python que es semejante en propósito al programa ensamblador 
#   de código, así:

# Dado un directorio de ejercicio con un código base y variantes de subcódigo sin ensamblar:
# Pregunte al usuario por:
# a) El nivel de dificultad del código base del ejercicio: DCB
# b) El nivel de dificultad de cada una de las variantes de subcódigo del ejercicio: DVS
# c) El número de descriptores a usar por cada VS
# d) Cada uno de los descriptores a usar por cada VS
# En donde:
# a) Los niveles de dificultad tanto para el código base como para las variantes de subcódigo, y el número de descriptores, pueden ser mayor o igual que 0.
# b) Un descriptor puede ser, incluso, una línea vacía.

# Nota: Se modifica la implementación del establecimiento de niveles de dificultad, permitiendo al usuario ingresar niveles 
#   de dificultad iguales a 0, porque:
# Si un código base o una variante de ejercicio tiene contenido una línea vacía, pues se puede argumentar que no existe 
#   dificultad alguna para implementar la parte relacionada con ese código base o variante de ejercicio.

# Calcule:
# a) El nivel de dificultad de una variante de ejercicio: DVE (Sólo si el ejercicio tiene variantes)
# b) El nivel de dificultad de un ejercicio: DE
# c) Los descriptores de una variante de ejercicio: DVE (Sólo si el ejercicio tiene variantes)

# Considerando las siguientes fórmulas:
# Si el ejercicio tiene variantes:
# DE = PROMEDIO(DVE)
# DVE = SUMA(DVS) + DCB
# Si el ejercicio NO tiene variantes:
# DE = DCB
# Donde:
# DE = El nivel de dificultad de un ejercicio
# DVE = El nivel de dificultad de una variante de ejercicio
# DVS = El nivel de dificultad de una variante de subcódigo
# DCB = El nivel de dificultad del código base

# Genere:
# a) Los archivos de nivel de dificultad de las variantes de ejercicio: DVE, en el directorio raíz dado por el usuario (Sólo si el ejercicio tiene variantes)
# Llamados dificultadN.txt, donde N es el número de la VE.
# b) El archivo de nivel de dificultad de ejercicio: DE, en el directorio raíz dado por el usuario.
# Llamado dificultad.txt
# c) Los archivos de descriptores de las variantes de ejercicio, en el directorio raíz dado por el usuario (Sólo si el ejercicio tiene variantes)
# Llamados descriptoresN.txt, donde N es el número de la VE.

############################################################
# FUNCIONES
############################################################
def choose_python_exercise_dir_location(): # ESTO FUNCIONA
    # Este procedimiento debería funcionar bien en Windows 10/11.
    # Preguntar por la ruta del directorio del ejercicio de programación con sus variantes.
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.iconify()
    print('En la ventana que aparecerá en pantalla, seleccione el directorio del directorio del ejercicio ' +
          'de programación con sus variantes.')
    # Obtiene la ruta absoluta del directorio seleccionado (Desde el disco C:/):
    file = filedialog.askdirectory(title='Seleccione un directorio', parent=root)
    root.destroy()

    # Si no se selecciona ningún directorio, dé un mensaje al usuario y detenga esta aplicación:
    if (file.strip() == ''):
        print('No se ha seleccionado ningún directorio. Cerrando la aplicación...')
        sys.exit()
    else:
        print('El directorio seleccionado es:', file)
        return file
    
def get_main_file_from_directory(exercise_main_dir): # ESTO FUNCIONA
    # https://docs.python.org/3/library/os.html#os.walk
    files = []
    # Haciendo un recorrido top-down desde la raíz:
    root_path = True
    for dir_path, dir_names, file_names in os.walk(exercise_main_dir):
        # dirpath is a string, the path to the directory.
        # dirnames is a list of the names of the subdirectories in dirpath (including symlinks to directories, and excluding '.' and '..').
        # filenames is a list of the names of the non-directory files in dirpath. Note that the names in the lists contain no path components.
        # Para tomar sólo los resultados del directorio raíz, y no de los subdirectorios:
        if (root_path == True):
            for file_name_found in file_names:
                file_name = str(file_name_found)
                # print(file_name)
                if (file_name == MAIN_FILE_KEYWORD):
                    files.append(os.path.join(dir_path, file_name))
            root_path = False
        else:
            return files
    return files

def get_sub_code_dirs_from_directory(exercise_main_dir): # ESTO FUNCIONA
    # https://docs.python.org/3/library/os.html#os.walk
    dirs = []
    # Haciendo un recorrido top-down desde la raíz:
    for dir_path, dir_names, file_names in os.walk(exercise_main_dir):
        # dirpath is a string, the path to the directory.
        # dirnames is a list of the names of the subdirectories in dirpath (including symlinks to directories, and excluding '.' and '..').
        # filenames is a list of the names of the non-directory files in dirpath. 
        #   Note that the names in the lists contain no path components.
        for dir_name_found in dir_names:
            dir_name = str(dir_name_found)
            # print(dir_name[0:1:1])
            # print(dir_name[1 : len(dir_name) : 1])
            if (dir_name[0:1:1] == SUB_CODE_DIR_KEYWORD and dir_name[1:len(dir_name):1].isnumeric()):
                dirs.append(os.path.join(dir_path, dir_name))
    return dirs

def get_sub_code_variant_files_from_sub_code_directory(sub_code_dir): # ESTO FUNCIONA
    # https://docs.python.org/3/library/os.html#os.walk
    files = []
    # Haciendo un recorrido top-down desde la raíz:
    root_path = True
    for dir_path, dir_names, file_names in os.walk(sub_code_dir):
        # dirpath is a string, the path to the directory.
        # dirnames is a list of the names of the subdirectories in dirpath (including symlinks to directories, and excluding '.' and '..').
        # filenames is a list of the names of the non-directory files in dirpath. Note that the names in the lists contain no path components.
        # Para tomar sólo los resultados del directorio raíz, y no de los subdirectorios:
        if (root_path == True):
            for file_name_found in file_names:
                file_name = str(file_name_found)
                if (file_name[0:1:1] == SUB_CODE_VARIANT_FILE_KEYWORD and file_name[1:len(file_name)-3:1].isnumeric() 
                    and file_name[len(file_name)-3:len(file_name)+1:1] == PYTHON_FILE_EXTENSION):
                    files.append(os.path.join(dir_path, file_name))
            root_path = False
        else:
            return files
    return files

def get_exercise_variant_files_from_directory(exercise_main_dir): # ESTO FUNCIONA
    # https://docs.python.org/3/library/os.html#os.walk
    files = []
    # Haciendo un recorrido top-down desde la raíz:
    root_path = True
    for dir_path, dir_names, file_names in os.walk(exercise_main_dir):
        # dirpath is a string, the path to the directory.
        # dirnames is a list of the names of the subdirectories in dirpath (including symlinks to directories, and excluding '.' and '..').
        # filenames is a list of the names of the non-directory files in dirpath. Note that the names in the lists contain no path components.
        # Para tomar sólo los resultados del directorio raíz, y no de los subdirectorios:
        if (root_path == True):
            for file_name_found in file_names:
                file_name = str(file_name_found)
                if (file_name[0:3:1] == EXERCISE_VARIANT_FILE_KEYWORD and file_name[3:len(file_name)-3:1].isnumeric() 
                    and file_name[len(file_name)-3:len(file_name)+1:1] == PYTHON_FILE_EXTENSION):
                    files.append(os.path.join(dir_path, file_name))
            root_path = False
        else:
            return files
    return files

def get_short_file_names(file_list): # ESTO FUNCIONA
    short_file_name_list = []
    for file in file_list:
        # print(file)
        short_file_name_parts = file.split('\\')
        if len(short_file_name_parts) == 2: # Es un archivo de código base
            # print('Este es un archivo de código base (CB)')
            short_file_name_list.append(short_file_name_parts[1])
        elif len(short_file_name_parts) == 3: # Es un archivo de variante de subcódigo
            # print('Este es un archivo de variante de subcódigo (VS)')
            short_file_name_list.append(short_file_name_parts[1] + '\\' + short_file_name_parts[2])
    return short_file_name_list

def get_sub_code_variant_counts(sub_code_dirs_list): # ESTO FUNCIONA
    # Cada subcódigo puede tener un número variable de variantes.
    # Se debe encontrar el directorio de cada subcódigo, y para cada uno de esos directorios, 
    #   encontrar el número de archivos en esos directorios cuyo nombre es: 
    #   v<numero>.py, donde <numero> es el número asociado a una variante de subcódigo.
    # El objetivo de esta función es obtener una lista de cantidades de variantes que hay por subcódigo.
    # (Cada índice de esta lista corresponde a una subrutina sM, donde M = 1, 2, ..., número de subcódigos del ejercicio)
    sub_code_variant_counts_list = []

    # El número de subcódigos se puede obtener fácilmente mediante el número de elementos de sub_code_dirs_list
    sub_code_count = len(sub_code_dirs_list)

    for s in range(1, sub_code_count + 1, 1):
        # Revisar el subcódigo s
        # Encontrar el subcódigo s (identificado con la ruta de directorio en el que está)
        sub_code_dir = sub_code_dirs_list[s - 1]

        # Encontrar los archivos de variantes disponibles para la subrutina
        sub_code_variant_files = get_sub_code_variant_files_from_sub_code_directory(sub_code_dir)

        # Colocar el número de variantes para la subrutina s aquí:
        sub_code_variant_counts_list.append(len(sub_code_variant_files))

    return sub_code_variant_counts_list

def get_file_difficulty_level_from_user(exercise_dir_short_file_name): # ESTO FUNCIONA
    difficulty_level = None
    while (difficulty_level == None):
        try:            
            if (exercise_dir_short_file_name == MAIN_FILE_KEYWORD): # Es un código base
                print('---------------------------------------------------------------')
                print('Establecimiento del nivel de dificultad del código base ' + exercise_dir_short_file_name + ':')
                print('---------------------------------------------------------------')
                user_option = input('Por favor ingrese el nivel de dificultad estimado para el código base (CB) ' + 
                    'del ejercicio (NOTA: El nivel de dificultad debe ser mayor o igual que 0; tenga en cuenta que si el ' +
                    'ejercicio no tiene variantes de subcódigo (VS), el nivel de dificultad del ejercicio será igual ' + 
                    'al nivel de dificultad del CB): ')
            else: # Es un código de variante
                print('---------------------------------------------------------------')
                print('Establecimiento del nivel de dificultad de la variante de subcódigo ' + exercise_dir_short_file_name + ':')  
                print('---------------------------------------------------------------')
                user_option = input('Por favor ingrese el nivel de dificultad estimado para esta variante de subcódigo (VS) ' + 
                    'del ejercicio (NOTA: El nivel de dificultad debe ser mayor o igual que 0; como este ejercicio tiene ' +
                    '1 o más VS, entonces se producirán 1 o más variantes de ejercicio (VE). El nivel de dificultad de las ' +
                    'variantes de ejercicio está dada por la suma de los niveles de dificultad del CB y de las VS, mientras ' +
                    'que el nivel de dificultad del ejercicio será igual al promedio de los niveles de dificultad de las VS): ')
            num = int(user_option)
            if num < 0:
                print('El nivel de dificultad asociado al código debe ser mayor igual que 0. Por favor, ingrese otro valor.')
            else:
                return num
        except ValueError:
            print('No se ingresó un número. Por favor, ingrese un valor mayor o igual a 0 para establecer ' + 
                  'la dificultad del código base (CB) o variante de subcódigo (VS).')

def get_file_descriptors_count_from_user(exercise_dir_short_file_name): # ESTO FUNCIONA
    file_descriptors_count = None
    while (file_descriptors_count == None):
        if (exercise_dir_short_file_name != MAIN_FILE_KEYWORD): # Es un código de variante
            try:
                print('---------------------------------------------------------------')
                print('Definición de los descriptores de la variante de subcódigo ' 
                        + exercise_dir_short_file_name + ' - FASE 1:')  
                print('---------------------------------------------------------------')
                user_option = input('Por favor ingrese el número de descriptores a ingresar para esta variante de ' + 
                    'subcódigo (VS) del ejercicio, los cuales podrán ser tenidos en cuenta para definir la descripción de ' + 
                    'variantes generadas con esta VS (NOTA: El número de descriptores debe ser mayor o igual que 1): ')            
                num = int(user_option)
                if num < 1:
                    print('El número de descriptores a ingresar debe ser mayor o igual que 1. Por favor, ingrese otro valor.')
                else:
                    return num
            except ValueError:
                print('No se ingresó un número. Por favor, ingrese un valor mayor o igual a 1 para establecer ' + 
                  'el número de descriptores a ingresar para esta variante de subcódigo (VS).')
        else: # Esto no debería ocurrir nunca:                
            return None        

def get_file_descriptors_from_user(file_descriptors_count, exercise_dir_short_file_name): # ESTO FUNCIONA
    file_descriptors = []

    if (exercise_dir_short_file_name == MAIN_FILE_KEYWORD): # Es un código base (No es necesario pedir descriptores aquí.)
        # Esto no debería ocurrir nunca:
        return None
    
    for descriptor_number in range(1, file_descriptors_count + 1, 1):
        print('---------------------------------------------------------------')    
        print('Definición de los descriptores de la variante de subcódigo ' + exercise_dir_short_file_name + ' - FASE 2:')  
        print('---------------------------------------------------------------')
        print('---- ' + exercise_dir_short_file_name + ': Descriptor # ' + str(descriptor_number) + ' ----')
        print('---------------------------------------------------------------')
        descriptor = input('Por favor ingrese el descriptor (texto) número ' + str(descriptor_number) + 
            ' a ingresar para esta variante de subcódigo (VS) del ejercicio, el cual podrá ser considerado en ' +
            'la definición de la descripción de variantes generadas con esta VS' + 
            '\n(NOTA: Si no escribe nada, y presiona ENTER, se sobreentiende que uno de los descriptores es una cadena vacía):\n')            
        file_descriptors.append(descriptor)
    
    return file_descriptors

def get_difficulty_levels_and_descriptors_from_user(exercise_dir_files): # ESTO FUNCIONA
    # Paso 7: Pregunte al usuario por:
    # a) El nivel de dificultad del código base del ejercicio: DCB
    # b) El nivel de dificultad de cada una de las variantes de subcódigo del ejercicio: DVS
    # c) El número de descriptores a usar por cada VS
    # d) Cada uno de los descriptores a usar por cada VS
    # En donde:
    # a) Los niveles de dificultad tanto para el código base como para las variantes de subcódigo, y el número de descriptores, 
    #   pueden ser mayor o igual que 0.
    # b) Un descriptor puede ser, incluso, una línea vacía.
    difficulty_levels_list = []
    descriptors_list = []
    # for exercise_dir_file in exercise_dir_files:
    #     exercise_dir_short_file_name = get_short_file_names([exercise_dir_file])[0]
    #     difficulty_level = get_file_difficulty_level_from_user(exercise_dir_short_file_name)
    #     difficulty_levels_list.append(difficulty_level)
    #     file_descriptors_count = get_file_descriptors_count_from_user(exercise_dir_short_file_name)
    #     descriptors_list = get_file_descriptors_from_user(file_descriptors_count, exercise_dir_short_file_name)
    for exercise_dir_file in exercise_dir_files:
        exercise_dir_short_file_name = get_short_file_names([exercise_dir_file])[0]
        difficulty_level = get_file_difficulty_level_from_user(exercise_dir_short_file_name)
        difficulty_levels_list.append(difficulty_level)
    for exercise_dir_file in exercise_dir_files:
        exercise_dir_short_file_name = get_short_file_names([exercise_dir_file])[0]
        file_descriptors_count = get_file_descriptors_count_from_user(exercise_dir_short_file_name)
        descr_list = get_file_descriptors_from_user(file_descriptors_count, exercise_dir_short_file_name)
        descriptors_list.append(descr_list)
    return difficulty_levels_list, descriptors_list

def generate_exercise_difficulty_level_file(exercise_dir, exercise_difficulty_level): # ESTO FUNCIONA
    with open(exercise_dir + '\\' + DIFFICULTY_TXT_FILE_NAME, mode="w", encoding='utf-8') as exercise_difficulty_level_file:
        exercise_difficulty_level_file.write(str(exercise_difficulty_level))
    print('Archivo de dificultad del ejercicio generado: ' + exercise_dir + '\\' + DIFFICULTY_TXT_FILE_NAME)

def generate_exercise_variant_difficulty_level_files(exercise_dir, exercise_variant_number, 
                                                     exercise_variant_difficulty_level): # ESTO FUNCIONA
    with open(exercise_dir + '\\' + DIFFICULTY_KEYWORD + str(exercise_variant_number) + TEXT_FILE_EXTENSION, mode="w", 
              encoding='utf-8') as exercise_variant_difficulty_level_file:
        exercise_variant_difficulty_level_file.write(str(exercise_variant_difficulty_level))
    print('Archivo de dificultad de variante de ejercicio (VE) generado: ' + exercise_dir + '\\' + DIFFICULTY_KEYWORD 
          + str(exercise_variant_number) + TEXT_FILE_EXTENSION)

def generate_exercise_variant_descriptor_files(exercise_dir, exercise_variant_number, exercise_variant_descriptors):
    with open(exercise_dir + '\\' + DESCRIPTORS_KEYWORD + str(exercise_variant_number) + TEXT_FILE_EXTENSION, mode="w", 
              encoding='utf-8') as exercise_variant_descriptors_file: # ESTO FUNCIONA
        evd_count = 0
        for evd in exercise_variant_descriptors:
            evd_count += 1
            if (evd_count < len(exercise_variant_descriptors)):
                exercise_variant_descriptors_file.write(evd + '\n')
            else:
                exercise_variant_descriptors_file.write(evd)
    print('Archivo de descriptores de variante de ejercicio (VE) generado: ' + exercise_dir + '\\' + DESCRIPTORS_KEYWORD 
          + str(exercise_variant_number) + TEXT_FILE_EXTENSION)

############################################################
# PROGRAMA PRINCIPAL => OK
############################################################
# Dado un directorio de ejercicio con un código base (CB) y variantes de subcódigo (VS) sin ensamblar:
# Paso 1: Pregunte al usuario la ubicación del directorio del ejercicio con un CB y/o VS sin ensamblar. => OK
exercise_dir = choose_python_exercise_dir_location()
# Paso 2: Busque si el directorio del ejercicio tiene un código base llamado main.py. => OK
base_code_file_list = get_main_file_from_directory(exercise_dir)
# Paso 3: Si el directorio del ejercicio NO tiene un código base, cierre esta aplicación.
#   (Porque todo ejercicio debe tener, como mínimo, un código base)
#   Si no, agregue el código base (identificado con una ruta completa de archivo) en una lista de archivos, 
#   y continúe la ejecución de esta aplicación. => OK
exercise_dir_files = []
if len(base_code_file_list) == 0:
    print('No existe un código base en el directorio del ejercicio. Cerrando la aplicación...')
    sys.exit()
else:
    exercise_dir_files.append(base_code_file_list[0])
# print(exercise_dir_files)

# Paso 4: Busque si el directorio del ejercicio tiene subdirectorios de subcódigo llamados sM y archivos dentro de estos,
#   llamados vN.py, donde M es el número del subcódigo, y N es el número de variantes del subcódigo. => OK
sub_code_dirs_list = get_sub_code_dirs_from_directory(exercise_dir)
# print(sub_code_dirs_list)
for sub_code_dir in sub_code_dirs_list:
    sub_code_variant_files_list = get_sub_code_variant_files_from_sub_code_directory(sub_code_dir)
    # Paso 5: Si existen subdirectorios sM y archivos vN.py dentro de los subdirectorios, agregue los archivos de variantes
    #   de subcódigo encontradas (identificadas con una ruta completa de archivo, cada una) en una lista de archivos,
    #   y continúe la ejecución de esta aplicación. => OK
    exercise_dir_files.extend(sub_code_variant_files_list)
# print(exercise_dir_files)

# Paso 6: Obtenga el nombre corto de los archivos que están en la lista de archivos, para facilitar la presentación
#   de estos archivos al usuario, al momento de pedirle después que especifique su nivel de dificultad y sus descriptores.
# El nombre corto de los archivos es, por ejemplo: main.py (para el código base), y sM\vN.py (para una variante de subcódigo). => OK
exercise_dir_short_file_names_list = get_short_file_names(exercise_dir_files)
# print(exercise_dir_short_file_names_list)

# Paso 7: Pregunte al usuario por:
# a) El nivel de dificultad del código base del ejercicio: DCB
# b) El nivel de dificultad de cada una de las variantes de subcódigo del ejercicio: DVS
# c) El número de descriptores a usar por cada VS
# d) Cada uno de los descriptores a usar por cada VS
# En donde:
# a) Los niveles de dificultad tanto para el código base como para las variantes de subcódigo, y el número de descriptores, 
#   pueden ser mayor o igual que 0.
# b) Un descriptor puede ser, incluso, una línea vacía. => OK
# DESCOMENTAR LA SIGUIENTE LÍNEA CUANDO SE TERMINEN DE HACER PRUEBAS:
difficulty_levels_and_descriptors = get_difficulty_levels_and_descriptors_from_user(exercise_dir_files)
# print(difficulty_levels_and_descriptors[0])
# print(difficulty_levels_and_descriptors[1])
# [0, 1, 1, 1, 2]
# [None, ['Suma', 'su suma'], ['Resta', 'su resta'], ['Multiplicación', 'su multiplicación'], 
# ['Potencia', 'el resultado de elevar el primer número con el segundo']]

# Paso 8: Obtenga los archivos de variantes del ejercicio (VE), y agréguelos a una lista de archivos de VE. => OK
exercise_variant_files_list = get_exercise_variant_files_from_directory(exercise_dir)
# print(exercise_variant_files_list)

# Paso 9: Si hay VE, a partir del nombre de los archivos de VE, obtenga, para cada archivo de VE, una lista que indique 
#   los números de variantes de subcódigo seleccionados. => OK
# exercise_dir
# sub_code_dirs_list
# a) Para esto, hay que primero saber cuántas variantes hay por cada subcódigo definido para el ejercicio de programación.
sub_code_variant_counts = get_sub_code_variant_counts(sub_code_dirs_list)
# print(sub_code_variant_counts)
# b) Luego, se debe saber cuántas combinaciones de variantes hay para el ejercicio de programación.
possible_variant_combinations_list = gvcl.gen_variant_combinations_list(sub_code_variant_counts)
# print(possible_variant_combinations_list)
# Entonces, cada elemento de la lista possible_variant_combinations_list corresponde a una lista que indica los números 
#   de variantes de subcódigo seleccionados, de los cuales, al hacer el ensamblaje de código, da como resultado un
#   código de variante de ejercicio (VE) en el directorio del ejercicio que se llama, en este caso, resN.py, donde
#   N es el número de VE.

# Paso 10: Calcule: => OK
# a) El nivel de dificultad de una variante de ejercicio: DVE (Sólo si el ejercicio tiene variantes) => OK
# b) El nivel de dificultad de un ejercicio: DE => OK
# c) Los descriptores de una variante de ejercicio: DVE (Sólo si el ejercicio tiene variantes) => OK
# Considerando las siguientes fórmulas:
# Si el ejercicio tiene variantes:
# DE = PROMEDIO(DVE)
# DVE = SUMA(DVS) + DCB
# Si el ejercicio NO tiene variantes:
# DE = DCB
# Donde:
# DE = El nivel de dificultad de un ejercicio
# DVE = El nivel de dificultad de una variante de ejercicio
# DVS = El nivel de dificultad de una variante de subcódigo
# DCB = El nivel de dificultad del código base
difficulty_levels = difficulty_levels_and_descriptors[0]
descriptors = difficulty_levels_and_descriptors[1]
exercise_difficulty_level = difficulty_levels[0] # DE = DCB (Este es el DE si el ejercicio no tiene VE)
exercise_variant_difficulty_levels = []
exercise_variant_descriptors = []

if (len(possible_variant_combinations_list)) > 0: # El ejercicio tiene VE.
    # Cada elemento de exercise_variant_files_list representa un archivo de VE.
    exercise_variant_number = 0
    
    # DE = PROMEDIO(DVE) = SUMA(DVE) / CANTIDAD(VE)
    exercise_variant_difficulty_level_sum = 0
    exercise_variant_count = 0

    for exercise_variant_file in exercise_variant_files_list:
        # Obtenga el número de la VE.
        # exercise_variant_file_name_part = exercise_variant_file.split('\\' + EXERCISE_VARIANT_FILE_KEYWORD)
        # exercise_variant_file_name_part = exercise_variant_file_name_part[1].split(PYTHON_FILE_EXTENSION)
        # exercise_variant_number = exercise_variant_file_name_part[0]
        # print(exercise_variant_number)
        exercise_variant_number += 1
        # print(exercise_variant_number)

        # Obtenga las selecciones de VS que corresponden a esta VE.
        # Cada elemento de possible_variant_combinations_list representa una selección de VS.
        # Tanto los elementos de exercise_variant_files_list y possible_variant_combinations_list tienen correspondencia.
        sub_code_selected_variants = possible_variant_combinations_list[exercise_variant_number - 1]
        # print(sub_code_selected_variants)

        # Por cada subcódigo dentro de las selecciones de VS, referencie el número del subcódigo y obtenga el número de VS
        #   elegido para ese subcódigo.
        # Por cada VS elegido, construya el archivo asociado al subcódigo y a la VS elegida, 
        #   y busque el índice donde está ese archivo en el listado de archivos del ejercicio.
        sub_code_count = 0

        # SUMA(DVS)
        sub_code_variant_difficulty_level_sum = 0
        # DESCRIPTORES DE VS
        vs_descriptors = []

        # Iteración de VS:
        for scsv in sub_code_selected_variants:            

            sub_code_count += 1            
            # print('Subcódigo: ' + str(sub_code_count))
            # print('Variante de subcódigo (VS): ' + str(scsv))
            # Construya la ruta de archivo de VS con el número del subcódigo y de variante de subcódigo elegida.
            file = exercise_dir + '\\' + SUB_CODE_DIR_KEYWORD + str(sub_code_count) + '\\' \
                  + SUB_CODE_VARIANT_FILE_KEYWORD + str(scsv) + PYTHON_FILE_EXTENSION
            # print(exercise_dir + '\\' + SUB_CODE_DIR_KEYWORD + str(sub_code_count) + '\\' 
            #       + SUB_CODE_VARIANT_FILE_KEYWORD + str(scsv) + PYTHON_FILE_EXTENSION)
            index = exercise_dir_files.index(file)
            # print(exercise_dir_files.index(file))
            # print('----')

            # Obtenga el nivel de dificultad del VS (DVS) 
            # ESTAS NOTAS YA SON IRRRELEVANTES:     
            ####
            # En el listado de niveles de dificultad, primero se itera por subcódigo, y luego por VS.
            # El primer elemento de este listado es el código base.
            # Del segundo elemento en adelante están los códigos de VS.
            ####     
            # Busque el nivel de dificultad del VS en el listado de niveles de dificultad por archivo.
            sub_code_variant_difficulty_level_sum += difficulty_levels[index]

            # Obtenga los descriptores del VS
            vs_descriptors.extend(descriptors[index])          

        # DVE = SUMA(DVS) + DCB (Aquí falta por determinar el valor de SUMA(DVS))
        exercise_variant_difficulty = sub_code_variant_difficulty_level_sum + difficulty_levels[0]        
        exercise_variant_difficulty_levels.append(exercise_variant_difficulty)    
        # DE = PROMEDIO(DVE) = SUMA(DVE) / CANTIDAD(VE)
        exercise_variant_difficulty_level_sum += exercise_variant_difficulty        
        exercise_variant_count += 1    
        # print(exercise_variant_difficulty)
        # print(exercise_variant_count)
        # print('----')
        exercise_variant_descriptors.append(vs_descriptors)

    # DE = PROMEDIO(DVE)
    exercise_difficulty_level = exercise_variant_difficulty_level_sum / exercise_variant_count

    # print(exercise_variant_difficulty_levels)
    # print(exercise_difficulty_level)
    # print(exercise_variant_descriptors)

# Paso 11: Genere:
# a) Los archivos de nivel de dificultad de las variantes de ejercicio: DVE, en el directorio raíz dado por el usuario (Sólo si el ejercicio tiene variantes)
# Llamados dificultadN.txt, donde N es el número de la VE.
# b) El archivo de nivel de dificultad de ejercicio: DE, en el directorio raíz dado por el usuario.
# Llamado dificultad.txt
# c) Los archivos de descriptores de las variantes de ejercicio, en el directorio raíz dado por el usuario (Sólo si el ejercicio tiene variantes)
# Llamados descriptoresN.txt, donde N es el número de la VE.

generate_exercise_difficulty_level_file(exercise_dir, exercise_difficulty_level)
# Cada elemento de exercise_variant_files_list representa un archivo de VE.
exercise_variant_number = 0
for exercise_variant_file in exercise_variant_files_list:    
    exercise_variant_number += 1
    generate_exercise_variant_difficulty_level_files(exercise_dir, exercise_variant_number, 
        exercise_variant_difficulty_levels[exercise_variant_number - 1])
    generate_exercise_variant_descriptor_files(exercise_dir, exercise_variant_number, 
        exercise_variant_descriptors[exercise_variant_number - 1])
