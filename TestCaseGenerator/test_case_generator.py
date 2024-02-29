import sys
import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import random

ASSEMBLED_FILE_KEYWORD = 'res'
TEST_CASE_GEN_PSEUDO_EXTENSION = '_tcg'
PY_FILE_EXTENSION = '.py'

VARIANTS_COMBINATION_DIR_KEYWORD = 'var'

TEST_CASE_INPUT_KEYWORD = 'entrada'
TEST_CASE_OUTPUT_KEYWORD = 'salida'
TXT_FILE_EXTENSION = '.txt'

MAIN_FILE_TCG_KEYWORD = 'main_tcg.py'

YES_OPTION = 'S'
NO_OPTION = 'N'

VISIBLE_TEST_CASES_FILE_KEYWORD = 'visibilidad.txt'

def choose_python_exercise_test_case_generator_files_dir_location(): # ESTO FUNCIONA
    # Este procedimiento debería funcionar bien en Windows 10/11.
    # Preguntar por la ruta del directorio que contiene los archivos ensamblados (.py) por cada combinación de variantes, 
    #   los cuales conforman, cada uno, una propuesta de solución al ejercicio de programación en Python con la combinación
    #   de variante aplicada.
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.iconify()
    print('En la ventana que aparecerá en pantalla, seleccione el directorio que contiene los archivos .py ' +
          'generadores de entradas y salidas para casos de prueba, una por cada combinación de variantes ' + 
          '(Estos deben llamarse: res1_tcg.py, res2_tcg.py, ..., resN_tcg.py, ' +
          'donde N es el número de combinaciones de variantes del ejercicio de programación)')
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
    
def choose_test_cases_files_dir_location(): # ESTO FUNCIONA
    # Este procedimiento debería funcionar bien en Windows 10/11.
    # Preguntar por la ruta del directorio que contiene los archivos ensamblados (.py) por cada combinación de variantes, 
    #   los cuales conforman, cada uno, una propuesta de solución al ejercicio de programación en Python con la combinación
    #   de variante aplicada.
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.iconify()
    print('En la ventana que aparecerá en pantalla, seleccione el directorio en el que quiere albergar los casos ' +
          'de prueba que se generarán para todas las combinaciones de variantes.')
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

def get_test_case_generator_files_from_directory(assembled_files_main_dir): # ESTO FUNCIONA
    # Encontrar los archivos en el directorio que cumplan la siguiente característica:
    # 1) Ser nombrados así: res<número de combinación de variantes>_tcg.py

    files = []
    # Haciendo un recorrido top-down desde la raíz:
    root_path = True    
    for dir_path, dir_names, file_names in os.walk(assembled_files_main_dir):
        # https://docs.python.org/3/library/os.html#os.walk
        # dirpath is a string, the path to the directory.
        # dirnames is a list of the names of the subdirectories in dirpath (including symlinks to directories, 
        #   and excluding '.' and '..').
        # filenames is a list of the names of the non-directory files in dirpath. 
        #   Note that the names in the lists contain no path components.
        # Para tomar sólo los resultados del directorio raíz, y no de los subdirectorios:
        if (root_path == True):
            for file_name_found in file_names:
                file_name = str(file_name_found)
                # print(file_name[0:3:1])
                # print(file_name[3:len(file_name)-7:1])
                # print(file_name[len(file_name)-7:len(file_name)-3:1])
                # print(file_name[len(file_name)-3:len(file_name)+1:1])
                # print('-- EOF DATA --')
                if ((file_name[0:3:1] == ASSEMBLED_FILE_KEYWORD
                and file_name[3:len(file_name)-7:1].isnumeric()
                and file_name[len(file_name)-7:len(file_name)-3:1] == TEST_CASE_GEN_PSEUDO_EXTENSION 
                and file_name[len(file_name)-3:len(file_name)+1:1] == PY_FILE_EXTENSION)
                or (file_name == MAIN_FILE_TCG_KEYWORD)):
                    files.append(os.path.join(dir_path, file_name))
            root_path = False
        else:
            return files
    return files

def get_test_cases_from_user(exercise_dir, files):
    # Revisar si todos los archivos generadores de casos de prueba son de CB o de VE 
    # (NOTA: No debería ocurrir que existan archivos generadores de casos de prueba a partir de CB y VE al mismo tiempo)
    base_code_tcg_exists = False
    for f in files:
        if (f == exercise_dir + '\\' + MAIN_FILE_TCG_KEYWORD):
            base_code_tcg_exists = True
            break
    
    num_test_cases = None
    while (num_test_cases == None):
        try:
            if (base_code_tcg_exists):
                user_option = input('¿Cuántos casos de prueba quiere crear con el archivo generador de caso ' +
                    'de prueba creado a partir del código base del ejercicio (CB)? ' + 
                    '\n>> ')
            else:
                user_option = input('¿Cuántos casos de prueba quiere crear con cada uno de los archivos generadores de caso ' +
                    'de prueba creados a partir de todas las variantes de ejercicio (VE) producidas con todas las combinaciones ' +
                    'de variantes? ' + 
                    '\n>> ')
            num = int(user_option)
            if num < 1:
                print('Se debe poder crear, por lo menos, un caso de prueba. Por favor, ingrese otro valor.')
            else:
                return num
        except ValueError:
            print('No se ingresó un número de casos de prueba. Por favor, ingrese otro valor.')

def get_starting_test_case_number_from_user():
    starting_tc_number = None
    while (starting_tc_number == None):
        try:            
            user_option = input('¿A partir de qué número quiere comenzar a generar los archivos de casos de prueba?' +
                 '\nUsualmente, este valor debería ser 1. El número ingresado debe ser un número mayor que 0.' +
                 '\nSi no ingresa ningún valor y presiona ENTER, o si no ingresa un número, se sobreentenderá que ' +
                 'el primer número de caso de prueba a crear es el 1.' + 
                 '\n>> ')
            starting_tc_number = int(user_option)
            if starting_tc_number < 1:
                print('El número a partir del cual se comienza a generar archivos de casos de prueba debe ser un número ' 
                      + 'mayor que 0. Por favor, ingrese otro valor.')
            else:
                return starting_tc_number
        except ValueError:
            return 1

def get_generate_tc_visibility_files_permission_from_user():
    # Revisar si todos los archivos generadores de casos de prueba son de CB o de VE 
    # (NOTA: No debería ocurrir que existan archivos generadores de casos de prueba a partir de CB y VE al mismo tiempo)
    base_code_tcg_exists = False
    for f in files:
        if (f == exercise_dir + '\\' + MAIN_FILE_TCG_KEYWORD):
            base_code_tcg_exists = True
            break
    
    user_option = None
    while (user_option != YES_OPTION and user_option != NO_OPTION):        
        if (base_code_tcg_exists):
            # Pregunte al usuario si por cada CB o VE, se debería insertar el número del primer caso de prueba 
            # generado como caso de prueba visible, de manera automática.
            user_option = input('¿Desea agregar automáticamente el primer caso de prueba generado con el archivo generador ' + 
                'de casos de prueba del código base del ejercicio (CB) como un caso de prueba visible en el archivo de ' +
                'casos de prueba visibles para este ejercicio' + 
                '\n(Si el archivo no existe, se creará, y si ya existe, se ' +
                'agregará 1 línea más a este archivo, o se sobrescribirá, dependiendo de lo que responda después)' 
                '\nEscriba S y presione ENTER para responder sí a esta pregunta.' + 
                '\nEscriba N y presione ENTER para responder no a esta pregunta.' + 
                '\n>> ')
        else:
            user_option = input('¿Desea agregar automáticamente el primer caso de prueba generado con los archivos generadores ' + 
                'de casos de prueba de variantes de este ejercicio (VE) como un caso de prueba visible en los archivos de ' +
                'casos de prueba visibles para las variantes de este ejercicio (VE)' +
                '\n(Si el archivo no existe, se creará, y si ya existe, se ' +
                'agregará 1 línea más a este archivo, o se sobrescribirá, dependiendo de lo que responda después)' 
                '\nEscriba S y presione ENTER para responder sí a esta pregunta.' + 
                '\nEscriba N y presione ENTER para responder no a esta pregunta.' + 
                '\n>> ')
        if user_option != YES_OPTION and user_option != NO_OPTION:
            print('Por favor escriba S o N para responder la siguiente pregunta:')
        else:
            if (user_option == YES_OPTION):
                print('Ha decidido añadir los primeros casos de prueba generados como casos visibles.')
                return True
            else:
                print('Ha decidido NO añadir los primeros casos de prueba generados como casos visibles.')
                return False

def get_visible_test_case_count_from_user(test_cases):
    # Revisar si todos los archivos generadores de casos de prueba son de CB o de VE 
    # (NOTA: No debería ocurrir que existan archivos generadores de casos de prueba a partir de CB y VE al mismo tiempo)
    base_code_tcg_exists = False
    for f in files:
        if (f == exercise_dir + '\\' + MAIN_FILE_TCG_KEYWORD):
            base_code_tcg_exists = True
            break
    
    num_visible_test_cases = None
    while (num_visible_test_cases == None):
        try:
            if (base_code_tcg_exists):
                user_option = input('¿Cuántos casos de prueba visibles quiere crear con el archivo generador de casos ' +
                    'de prueba creado a partir del código base del ejercicio (CB)?' + 
                    '\nPuesto que ya ha seleccionado que quiere generar 1 caso de prueba visible, entonces el número ' + 
                    'mínimo de casos de prueba visibles a generar es 1.' + 
                    '\nAdemás, tenga en cuenta que los números de casos de prueba visibles a incluir en los archivos de ' +
                    'casos de prueba visibles son aleatorios, excepto por el primer caso de prueba generado a partir del ' + 
                    'archivo generador de casos de prueba del código base del ejercicio (CB):' + 
                    '\nFinalmente, como ya existen ' + str(test_cases) + ' nuevos casos de prueba a crear, la cantidad de casos de ' + 
                    'prueba visibles no puede exceder esta cantidad.'
                    '\n>> ')
            else:
                user_option = input('¿Cuántos casos de prueba visibles quiere crear con cada uno de los archivos generadores de caso ' +
                    'de prueba creados a partir de todas las variantes de ejercicio (VE) producidas con todas las combinaciones ' +
                    'de variantes?' + 
                    '\nPuesto que ya ha seleccionado que quiere generar 1 caso de prueba visible, entonces el número ' + 
                    'mínimo de casos de prueba visibles a generar es 1.' + 
                    '\nAdemás, tenga en cuenta que los números de casos de prueba visibles a incluir en los archivos de ' +
                    'casos de prueba visibles son aleatorios, excepto por el primer caso de prueba generado a partir de ' + 
                    'cada archivo generador de casos de prueba de cada variante de ejercicio (VE):' + 
                    '\nFinalmente, como ya existen ' + str(test_cases) + ' nuevos casos de prueba a crear, la cantidad de casos de ' + 
                    'prueba visibles no puede exceder esta cantidad.'
                    '\n>> ')
            num = int(user_option)
            if num < 1:
                print('Se debe poder crear, por lo menos, un caso de prueba visible. Por favor, ingrese otro valor.')
            if num > test_cases:
                print('No es posible crear esa cantidad de casos de prueba visibles, ya que ese número excede a la cantidad ' +
                'de casos de prueba a generar. Por favor, ingrese otro valor.')
            else:
                return num
        except ValueError:
            print('No se ingresó un número de casos de prueba visibles. Por favor, ingrese otro valor.')

def get_override_tc_visibility_file_content_permission_from_user():
    # Revisar si todos los archivos generadores de casos de prueba son de CB o de VE 
    # (NOTA: No debería ocurrir que existan archivos generadores de casos de prueba a partir de CB y VE al mismo tiempo)
    base_code_tcg_exists = False
    for f in files:
        if (f == exercise_dir + '\\' + MAIN_FILE_TCG_KEYWORD):
            base_code_tcg_exists = True
            break
    
    user_option = None
    while (user_option != YES_OPTION and user_option != NO_OPTION):        
        if (base_code_tcg_exists):
            # Pregunte al usuario si se debería sobrescribir o no los archivos de casos de prueba visibles.
            user_option = input('¿Desea sobrescribir los archivos de casos de prueba visibles para el código base del ' + 
                'ejercicio (CB)?'
                '\nEscriba S y presione ENTER para responder sí a esta pregunta.' + 
                '\nEscriba N y presione ENTER para responder no a esta pregunta.' + 
                '\n>> ')
        else:
            user_option = input('¿Desea sobrescribir los archivos de casos de prueba visibles para las ' + 
                'variantes de este ejercicio (VE)?'
                '\nEscriba S y presione ENTER para responder sí a esta pregunta.' + 
                '\nEscriba N y presione ENTER para responder no a esta pregunta.' + 
                '\n>> ')
        if user_option != YES_OPTION and user_option != NO_OPTION:
            print('Por favor escriba S o N para responder la siguiente pregunta:')
        else:
            if (user_option == YES_OPTION):
                print('Ha decidido sobrescribir los archivos de casos de prueba visibles.')
                return True
            else:
                print('Ha decidido NO sobrescribir los archivos de casos de prueba visibles.')
                return False

def get_test_case_dir_and_file_routes(file, test_case_number, test_cases_dir): # ESTO FUNCIONA    
    dir_route, input_route, output_route = None, None, None    
    if (file != exercise_dir + '\\' + MAIN_FILE_TCG_KEYWORD): # No es un archivo generador de casos de prueba de un CB
        variants_combination_result_name = file.split('\\')[1].split(TEST_CASE_GEN_PSEUDO_EXTENSION)[0]
        variants_combination_number = variants_combination_result_name[len(variants_combination_result_name) - 1]
        # print(variants_combination_number)
        variants_combination_dir_name = VARIANTS_COMBINATION_DIR_KEYWORD + variants_combination_number
        dir_route = test_cases_dir + '\\' + variants_combination_dir_name
        input_route = test_cases_dir + '\\' + variants_combination_dir_name + '\\' \
            + TEST_CASE_INPUT_KEYWORD + str(test_case_number) + TXT_FILE_EXTENSION
        output_route = test_cases_dir + '\\' + variants_combination_dir_name + '\\' \
            + TEST_CASE_OUTPUT_KEYWORD + str(test_case_number) + TXT_FILE_EXTENSION
    else: # Es un archivo generador de casos de prueba de un CB
        dir_route = test_cases_dir
        input_route = test_cases_dir + '\\' + TEST_CASE_INPUT_KEYWORD + str(test_case_number) + TXT_FILE_EXTENSION
        output_route = test_cases_dir + '\\' + TEST_CASE_OUTPUT_KEYWORD + str(test_case_number) + TXT_FILE_EXTENSION
    return dir_route, input_route, output_route

def get_visible_tc_file_route(file, test_cases_dir):
    vtc_file_route = None
    if (file != exercise_dir + '\\' + MAIN_FILE_TCG_KEYWORD): # No es un archivo generador de casos de prueba de un CB
        variants_combination_result_name = file.split('\\')[1].split(TEST_CASE_GEN_PSEUDO_EXTENSION)[0]
        variants_combination_number = variants_combination_result_name[len(variants_combination_result_name) - 1]
        variants_combination_dir_name = VARIANTS_COMBINATION_DIR_KEYWORD + variants_combination_number
        vtc_file_route = test_cases_dir + '\\' + variants_combination_dir_name + '\\' + VISIBLE_TEST_CASES_FILE_KEYWORD          
    else: # Es un archivo generador de casos de prueba de un CB
        vtc_file_route = test_cases_dir + '\\' + VISIBLE_TEST_CASES_FILE_KEYWORD
    return vtc_file_route

def get_tc_visibility_file_from_directory(exercise_main_dir): # ESTO FUNCIONA
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
                if (file_name == VISIBLE_TEST_CASES_FILE_KEYWORD):
                    files.append(os.path.join(dir_path, file_name))
            root_path = False
        else:
            return files
    return files

# PROGRAMA PRINCIPAL:

# MODIFICACIÓN 23/03/2023
# Modifique este programa, para que:
# a) Soporte ESVs (Puesto que en este momento sólo funciona con variantes). => TERMINADO
# b) Pregunte al usuario por el número de casos de prueba a partir del cual se deberían comenzar a generar estos 
#   (Para que no sea necesariamente 1, sino un número arbitrario mayor que 1).
# No obstante, el número a partir del cual se deberían comenzar a generar casos de prueba debería seguir siendo 1, 
#   por defecto. => TERMINADO
# c) Por cada CB o VE, se inserte el número del primer caso de prueba generado como caso de prueba visible, 
#   de manera automática, si el usuario así lo decide de antemano:
#   Si no existe el archivo de visibilidad.txt para el CB o VE, este debe crearse, y escribir el contenido 
#       correspondiente allí.
#   Si existe el archivo de visibilidad.txt para el CB o VE, este debe agregarse al contenido existente 
#       (opción por defecto), a menos que el usuario quiera sobrescribirlo.
# d) Y permita al usuario decidir cuántos casos de prueba generados automáticamente deberían ser visibles 
#   (aparte del primero – si decidió antes incluir un primer caso adicional), 
#   y estos serían elegidos aleatoriamente (sin incluir el primero), de entre los números de casos de prueba generados.

# Paso 1: Elegir el directorio en donde están los archivos del ejercicio de programación
# MODIFICACIÓN 23/03/2023: Los archivos que terminen en main_tcg.py también serán considerados.
# NOTA: Sólo se considerarán los archivos que terminen en main_tcg.py o res<número de variante>_tcg.py.
exercise_dir = choose_python_exercise_test_case_generator_files_dir_location()

# MODIFICACIÓN 23/03/2023: Los archivos que terminen en main_tcg.py también serán considerados.
# NOTA: Sólo se considerarán los archivos que terminen en main_tcg.py o res<número de variante>_tcg.py.
# Paso 2: Buscar cada archivo main_tcg.py o res<número de variante>_tcg.py en el directorio principal.
files = get_test_case_generator_files_from_directory(exercise_dir)
# print(files)

# Paso 3: Preguntar al usuario cuántas veces quiere ejecutar estos archivos para obtener varios archivos de entradas y de
#   salida por combinación de variante.
# MODIFICACIÓN 23/03/2023: Se debe cambiar el mensaje en get_test_cases_from_user(), en caso de que el ejercicio sólo
#   tenga un archivo generador de casos de prueba a partir de un CB y no a partir de VE.
test_cases = get_test_cases_from_user(exercise_dir, files)
# print(test_cases)

# MODIFICACIÓN 23/03/2023:
# b) Pregunte al usuario por el número de casos de prueba a partir del cual se deberían comenzar a generar estos 
#   (Para que no sea necesariamente 1, sino un número arbitrario mayor que 1).
# No obstante, el número a partir del cual se deberían comenzar a generar casos de prueba debería seguir siendo 1, 
#   por defecto.
starting_test_case_number = get_starting_test_case_number_from_user()

# MODIFICACIÓN 23/03/2023:
# c) Por cada CB o VE, se inserte el número del primer caso de prueba generado como caso de prueba visible, 
#   de manera automática, si el usuario así lo decide de antemano.
# Aquí se debe pedir al usuario si el archivo de visibilidad de casos de prueba se debe generar o no por cada CB o VE.
should_tc_visibility_files_be_generated = get_generate_tc_visibility_files_permission_from_user()
# MODIFICACIÓN 23/03/2023:
# d) Y permita al usuario decidir cuántos casos de prueba generados automáticamente deberían ser visibles 
#   (aparte del primero – si decidió antes incluir un primer caso adicional)
visible_test_cases = 1
if (should_tc_visibility_files_be_generated):
    visible_test_cases = get_visible_test_case_count_from_user(test_cases)
    # MODIFICACIÓN 23/03/2023:
    # Si existe el archivo de visibilidad.txt para el CB o VE, este debe agregarse al contenido existente 
    # (opción por defecto), a menos que el usuario quiera sobrescribirlo.
    # En otras palabras, permita al usuario decidir si el o los archivos de visibilidad.txt deberían ser sobrescritos o no.
    should_tc_visibility_file_content_be_overriden = get_override_tc_visibility_file_content_permission_from_user()


# MODIFICACIÓN 23/03/2023:
# NO preguntar al usuario en qué directorio quiere guardar los casos de prueba generados.
# En cambio, defina el directorio del ejercicio como el directorio en el que se deben guardar los casos de prueba generados.  
# Paso 4: Confirmar el directorio en el que se guardarán los casos de prueba generados.
test_cases_dir = exercise_dir

# Paso 5: Ejecutar todos los archivos generadores de casos de prueba del código base o de todas las combinaciones de variante,
#   las veces que fueron indicadas por el usuario en el paso 3 
#   (Itere primero por archivo generador, y luego, por número de veces indicados por el usuario)
file_index = 0
for file in files: # Archivos generadores de casos de prueba
    # MODIFICACIÓN 23/03/2023
    # Agregar soporte para referenciar el archivo de visibilidad.txt a crear/actualizar para el CB o VE
    vtc_file = get_visible_tc_file_route(file, test_cases_dir)
    for tc in range(1, test_cases + 1, 1): # Número de casos de prueba a crear por archivo generador de casos de prueba
    # Paso 6: Por cada generador de caso de prueba de cada combinación de variante, obtenga la ruta y el nombre de los archivos 
    #   de entrada y salida a crear.
        # MODIFICACIÓN 23/03/2023:
        # Agregar soporte para obtener la ruta y el nombre de los archivos de entrada y salida a crear, cuando
        #   el ejercicio no tiene VE.
        tc_dir, tc_input_file, tc_output_file = get_test_case_dir_and_file_routes(file, 
                                                starting_test_case_number + tc - 1, test_cases_dir)
        # print(tc_dir)
        # print(tc_input_file)
        # print(tc_output_file)
        # print('-------------')
        
        # Paso 7: En cada ejecución de un generador de caso de prueba, genere los archivos de entrada y salida en el 
        #   directorio correspondiente.

        # Validar si el directorio donde se albergarán los datos de entrada y de salida para los casos de prueba existe o no.
        if not os.path.exists(tc_dir):
            # Si el directorio anterior no existe, crearlo:
            os.makedirs(tc_dir)

        # Creación de archivos de entrada y salida de CP
        with open(tc_output_file, mode="w", encoding='utf-8') as output_file:
            if (subprocess.run(['python', file, tc_input_file], stdout=output_file, encoding='utf-8')):
                print('Se ha generado el archivo',tc_input_file,'en el directorio',tc_dir)
                print('Se ha generado el archivo',tc_output_file,'en el directorio',tc_dir)

    # Después de crear los CP mediante el archivo generador de CPs:
    # Inserción de CP visibles del CB o VE en un nuevo archivo o en un archivo existente de CP visibles de CB o VE

    if (should_tc_visibility_files_be_generated):
        # https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
        write_mode = None
        visibility_file_created = False
        visibility_file_overriden = False

        # Validar si el archivo vtc_file existe en el directorio correspondiente:
        visibility_files_list = get_tc_visibility_file_from_directory(test_cases_dir)
        if (len(visibility_files_list) == 0): # El archivo visibilidad.txt no existe.
            # Si el archivo vtc_file NO existe, este se debe crear en el directorio correspondiente.
            write_mode = 'w'
            visibility_file_created = True
        else: # El archivo visibilidad.txt existe
            # Revise si el archivo visibilidad.txt debe ser sobrescrito o no
            if (should_tc_visibility_file_content_be_overriden == True):
                write_mode = 'w'
                visibility_file_overriden = True
            else:
                write_mode = 'a'

        visible_test_cases_to_add = []
        # Buscar el primer número de caso de prueba generado, y añadirlo a la lista de número de CP visibles a agregar
        visible_test_cases_to_add.append(starting_test_case_number)
        if (visible_test_cases > 1):
            # Se deben elegir números de CP generados aleatoriamente, excepto el primero generado.
            min_value = starting_test_case_number + 1
            max_value = starting_test_case_number + (test_cases - 1)
            value_range_list = list(range(min_value, max_value + 1, 1))
            # Randomly select elements from list without repetition in Python
            # https://www.geeksforgeeks.org/randomly-select-elements-from-list-without-repetition-in-python/
            chosen_tc = random.sample(value_range_list, visible_test_cases - 1)
            visible_test_cases_to_add.extend(chosen_tc)
            # for i in range(1, visible_test_cases + 1, 1):
            #     chosen_tc = random.randint(min_value, max_value)
        
        with open(vtc_file, mode=write_mode, encoding='utf-8') as v_file:
            visible_test_cases_to_add_index = 0
            for vtcta in visible_test_cases_to_add:
                visible_test_cases_to_add_index += 1
                if (visible_test_cases_to_add_index < len(visible_test_cases_to_add)):
                    v_file.write(str(vtcta) + '\n')
                else:
                    v_file.write(str(vtcta))

        if (visibility_file_created):
            print('Se ha creado el archivo',vtc_file)
        elif (visibility_file_overriden):
            print('Se ha sobrescrito el archivo',vtc_file)
        else:
            print('Se han agregado nuevos casos de prueba visibles al archivo',vtc_file)

    file_index += 1



