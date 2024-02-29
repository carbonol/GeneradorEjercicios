import sys
import tkinter as tk
from tkinter import filedialog
import os
import shutil

VARIANTS_COMBINATION_DIR_KEYWORD = 'var'
MAIN_FILE_KEYWORD = 'main.py'
MAIN_DIR_KEYWORD = 'main'
DIFFICULTY_TXT_FILE_NAME = 'dificultad.txt'
DESCRIPTORS_TXT_FILE_NAME = 'descriptores.txt'

DIFFICULTY_TXT_FILE_KEYWORD = 'dificultad'
DESCRIPTORS_TXT_FILE_KEYWORD = 'descriptores'
TEXT_FILE_EXTENSION = '.txt'

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
    
def get_variant_dirs_from_directory(exercise_main_dir):
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
            if (dir_name[0:3:1] == VARIANTS_COMBINATION_DIR_KEYWORD and dir_name[3:len(dir_name):1].isnumeric()):
                dirs.append(os.path.join(dir_path, dir_name))
    return dirs

def get_main_file_from_directory(exercise_main_dir):
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

def get_difficulty_rating_from_user(short_dir_name): # ESTO FUNCIONA
    difficulty = None
    while (difficulty == None):
        try:
            if short_dir_name == MAIN_DIR_KEYWORD:
                # No hay variantes
                user_option = input('Por favor ingrese el nivel de dificultad estimado para el ejercicio (Mayor que 0): ')
            else:
                # Hay variantes
                user_option = input('Por favor ingrese el nivel de dificultad estimado para la variante ' + 
                                    short_dir_name + ' (Mayor que 0): ')
            num = int(user_option)
            if num < 1:
                print('El nivel de dificultad debe ser por lo menos 1. Por favor, ingrese otro valor.')
            else:
                return num
        except ValueError:
            print('No se ingresó un número. Por favor, ingrese un valor mayor que 1 para establecer la dificultad del ' + 
                  'ejercicio o variante.')

def generate_exercise_difficulty_file(dir, difficulty):
    with open(dir + '\\' + DIFFICULTY_TXT_FILE_NAME, mode="w", encoding='utf-8') as difficulty_file:
        difficulty_file.write(str(difficulty))
    print('Archivo de dificultad generado: ' + dir + '\\' + DIFFICULTY_TXT_FILE_NAME)

# PROGRAMA PRINCIPAL:

# MODIFICACIÓN 24/03/2023
# Modifique este programa para que:
# a) NO pregunte ya al usuario por niveles de dificultad, ya que eso se debe hacer antes del ensamblaje, y no después.
# b) Traslade los archivos de:
# Dificultad de cada variante de ejercicio (VE): dificultadN.txt
# Descriptores de cada variante de ejercicio (VE): descriptoresN.txt
# A los directorios que correspondan para ello, a fin de que puedan ser usados en el programa de evaluación automática.

# Paso 1: Elegir la ubicación del directorio del ejercicio de programación con sus variantes.
# NOTA: La estructura del directorio elegido debe tener una estructura semejante a la siguiente, donde ejercicioM es el
#   nombre del ejercicio que estará en el nivel M del flujo de ejercicios mostrado al estudiante, y varN es el directorio
#   de la combinación de variantes N para el ejercicio de programación.
# <ejercicio1>
#   <var1>
#       (...)
#   <var2>
#       (...)
#   (...)
#       (...)
#   <varN>
#       (...)
exercise_dir = choose_python_exercise_dir_location()

# Paso 2: Buscar cada directorio de variante en el directorio del ejercicio.
dirs = get_variant_dirs_from_directory(exercise_dir)
# print(dirs)

short_dir_names = []

# MODIFICACIÓN 24/03/2023
# Ya no se necesita revisar si existe el archivo main.py en el directorio del ejercicio, porque esta aplicación
#   sólo sirve para ejericicios con VE.
# Paso 3: Revisar si hay al menos un directorio de variante de ejercicio (VE) en el directorio del ejercicio.
if len(dirs) == 0:
    print('No existen directorios de variantes de ejercicio (VE). Cerrando la aplicación...')
    sys.exit()
# Si hay al menos un directorio de VE, entonces obtenga los nombres cortos de los directorios
else:
    for dir in dirs:
        split_dir_name_parts = dir.split('\\')
        short_dir_name = ''
        for name_part_index in range(1, len(split_dir_name_parts), 1):
            short_dir_name += split_dir_name_parts[name_part_index]
        short_dir_names.append(short_dir_name)
# print(short_dir_names)

# MODIFICACIÓN 24/03/2023
# a) NO pregunte ya al usuario por niveles de dificultad, ya que eso se debe hacer antes del ensamblaje, y no después.
# b) Traslade los archivos de:
# Dificultad de cada variante de ejercicio (VE): dificultadN.txt
# Descriptores de cada variante de ejercicio (VE): descriptoresN.txt
# A los directorios que correspondan para ello, a fin de que puedan ser usados en el programa de evaluación automática.

dir_index = 0
for dir in dirs:
    # print(dir)
    # Paso 4: Por cada directorio de VE, obtenga el número de la variante del ejercicio (VE):
    exercise_variant_number = short_dir_names[dir_index][3: len(short_dir_names[dir_index]) + 1: 1]
    # print(short_dir_names[dir_index][3: len(short_dir_names[dir_index]) + 1: 1])

    # Paso 5: Obtenga las rutas de los archivos de dificultadN.txt y descriptoresN.txt a copiar
    original_ev_difficulty_level_file = exercise_dir + '\\' + DIFFICULTY_TXT_FILE_KEYWORD + \
        exercise_variant_number + TEXT_FILE_EXTENSION
    original_ev_descriptors_file = exercise_dir + '\\' + DESCRIPTORS_TXT_FILE_KEYWORD + \
        exercise_variant_number + TEXT_FILE_EXTENSION
    
    # Paso 6: Obtenga las rutas de los nuevos archivos de dificultadN.txt y descriptoresN.txt, dependiendo del número de VE.
    new_ev_difficulty_level_file = dir + '\\' + DIFFICULTY_TXT_FILE_NAME
    new_ev_descriptors_file = dir + '\\' + DESCRIPTORS_TXT_FILE_NAME
    
    # Paso 6: Por cada directorio de VE, copie los archivos de dificultadN.txt y descriptoresN.txt en el directorio dir
    created_ev_difficulty_level_file = shutil.copyfile(original_ev_difficulty_level_file, new_ev_difficulty_level_file)
    print('Se ha generado el archivo:',created_ev_difficulty_level_file)
    created_ev_descriptors_file = shutil.copyfile(original_ev_descriptors_file, new_ev_descriptors_file)
    print('Se ha generado el archivo:',created_ev_descriptors_file)
    
    dir_index += 1