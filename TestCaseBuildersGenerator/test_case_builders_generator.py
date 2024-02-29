import sys
import tkinter as tk
from tkinter import filedialog
import os
import re

ASSEMBLED_FILE_KEYWORD = 'res'
PY_FILE_EXTENSION = '.py'

TEST_CASE_GEN_PSEUDO_EXTENSION = '_tcg'

NEWLINE_TOKEN = '\n'

SINGLE_LINE_COMMENT_TOKEN = '#' # Un comentario también representa un fin de una línea lógica en Python.

EQUAL_SIGN = '='
INPUT_DATA_GENERATOR_MODULE_TOKEN = 'idg'
OPENING_PARENTHESIS_TOKEN = '('
CLOSING_PARENTHESIS_TOKEN = ')'

POINT_TOKEN = '.'

MAIN_FILE_KEYWORD = 'main.py'

def choose_python_exercise_assembled_variant_combination_files_dir_location(): # ESTO FUNCIONA
    # Este procedimiento debería funcionar bien en Windows 10/11.
    # Preguntar por la ruta del directorio que contiene los archivos ensamblados (.py) por cada combinación de variantes, 
    #   los cuales conforman, cada uno, una propuesta de solución al ejercicio de programación en Python con la combinación
    #   de variante aplicada.
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.iconify()
    print('En la ventana que aparecerá en pantalla, seleccione el directorio que contiene los archivos ' +
          'ensamblados (.py) por cada combinación de variantes (Estos deben llamarse: res1.py, res2.py, ..., resN.py, ' +
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

def get_assembled_variant_combination_files_from_directory(assembled_files_main_dir): # ESTO FUNCIONA
    # Encontrar los archivos en el directorio que cumplan la siguiente característica:
    # 1) Ser nombrados así: res<número de combinación de variantes>.py

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
                # print(file_name[3 : len(file_name)-3 : 1])
                # print(file_name[len(file_name)-3 : len(file_name)+1 : 1])
                # print('-- EOF DATA --')
                if (file_name[0:3:1] == ASSEMBLED_FILE_KEYWORD and file_name[3:len(file_name)-3:1].isnumeric() 
                and file_name[len(file_name)-3:len(file_name)+1:1] == PY_FILE_EXTENSION):
                    files.append(os.path.join(dir_path, file_name))
            root_path = False
        else:
            return files
    return files

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

def textline_has_newline_ending(textline):
    textline_str = str(textline)
    if textline_str.endswith(NEWLINE_TOKEN):
        return True
    else:
        return False
    
def get_gen_function_variable_and_indent_from_line(line):
    # NOTA: NO SE VALIDARÁ LA SINTAXIS COMPLETA DE LAS FUNCIONES GENERADORAS, SINO SÓLO UNA PARTE DE ELLA EN EL PROTOTIPO.
    #   ESTO DEBERÍA CORREGIRSE EN FUTURAS VERSIONES DE ESTE PROGRAMA:
    # Funciones generadoras válidas
    '''
    var = idg.<nombre_funcion>(<parametros>)
    '''
    variable = None
    # https://stackoverflow.com/questions/2268532/grab-a-lines-whitespace-indention-with-python
    indent = re.match(r"\s*", str(line)).group()
    ln = str(line).strip() # Remueve los espacios en blanco al inicio y al final de la línea.
    if ln.find(SINGLE_LINE_COMMENT_TOKEN) != -1: # Se encontró un comentario #
        single_line_comment_index = ln.find(SINGLE_LINE_COMMENT_TOKEN)
        if (single_line_comment_index > 0):
            ln = ln[0:single_line_comment_index:1] # [índice inicial inclusivo, índice final exclusivo, paso]
        else:
            return None, None

    # No se encontró un signo igual => No es una función generadora válida.
    if ln.find(EQUAL_SIGN) == -1: 
        return None, None
    # No se encontró la palabra clave idg => No es una función generadora válida.
    if ln.find(INPUT_DATA_GENERATOR_MODULE_TOKEN) == -1:
        return None, None
    # No se encontró al menos un paréntesis que abre => No es una función generadora válida.
    if ln.find(OPENING_PARENTHESIS_TOKEN) == -1: 
        return None, None
    # No se encontró al menos un paréntesis que cierra => No es una función generadora válida.
    if ln.find(CLOSING_PARENTHESIS_TOKEN) == -1: 
        return None, None
    # Se debería revisar también si el último caracter de la línea es un paréntesis que cierra.
    if ln[len(ln)-1:len(ln):1] != CLOSING_PARENTHESIS_TOKEN: 
        return None, None

    # Número de paréntesis que abren y cierran:
    # Deben ser 1 que abre y 1 que cierra (Por lo menos)
    # El número de paréntesis que abren debe ser igual al número de paréntesis que cierran
    opening_parentheses = 1
    closing_parentheses = 1
    opening_parenthesis_index = ln.find(OPENING_PARENTHESIS_TOKEN)
    begin_index = opening_parenthesis_index + 1
    while begin_index < len(ln) and ln[begin_index:len(ln):1].find(OPENING_PARENTHESIS_TOKEN) != -1:
        opening_parentheses += 1
        begin_index += ln[begin_index:len(ln):1].find(OPENING_PARENTHESIS_TOKEN) + 1

    closing_parenthesis_index = ln.find(CLOSING_PARENTHESIS_TOKEN)
    begin_index = closing_parenthesis_index + 1
    while begin_index < len(ln) and ln[begin_index:len(ln):1].find(CLOSING_PARENTHESIS_TOKEN) != -1:
        closing_parentheses += 1
        begin_index += ln[begin_index:len(ln):1].find(CLOSING_PARENTHESIS_TOKEN) + 1            
    
    if not (opening_parentheses == closing_parentheses and (opening_parentheses >= 1)):
        return None, None

    # Si hay al menos 1 paréntesis que abre y 1 que cierra, asuma que se puede encontrar una función generadora.    
    if opening_parentheses >= 1:
        # Validar el orden de los tokens
        # i.e.: Identificador(variable), signo igual, palabra clave idg, nombre de función, paréntesis que abre, 
        #   parámetros, y paréntesis que cierra.
        # Entre estos tokens pueden haber 0 o 1 espacios en blanco
        equal_sign_index = ln.find(EQUAL_SIGN)
        idg_keyword_index = ln.find(INPUT_DATA_GENERATOR_MODULE_TOKEN)
        opening_parenthesis_index = ln.find(OPENING_PARENTHESIS_TOKEN)
        closing_parenthesis_index = ln.find(CLOSING_PARENTHESIS_TOKEN)
        if not (equal_sign_index < idg_keyword_index < opening_parenthesis_index < closing_parenthesis_index):
            return None, None

        substring_by_equal_sign = ln.split(EQUAL_SIGN)
        variable = substring_by_equal_sign[0].strip()
        remainder = substring_by_equal_sign[1].strip()
        if not variable.isidentifier(): # No se encontró una variable inicial, puesto que el identificador no es válido 
        # => No es una instrucción válida.
            return None, None

        substring_by_opening_parenthesis = remainder.split(OPENING_PARENTHESIS_TOKEN)
        idg_keyword_and_function_name_part = substring_by_opening_parenthesis[0].strip()
        substring_by_point = idg_keyword_and_function_name_part.split(POINT_TOKEN)
        idg_keyword = substring_by_point[0].strip()
        function_name = substring_by_point[1].strip()
        # Esto no es de interés ahora:             
        # parameters_and_closing_parenthesis_part = substring_by_opening_parenthesis[1].strip()

        if idg_keyword == INPUT_DATA_GENERATOR_MODULE_TOKEN \
        and (function_name == 'fixed_str_data_gen'
        or function_name == 'fixed_int_data_gen'
        or function_name == 'fixed_float_data_gen'
        or function_name == 'fixed_true_data_gen'
        or function_name == 'fixed_false_data_gen'
        or function_name == 'random_str_data_from_list_gen'
        or function_name == 'random_int_data_from_list_gen'
        or function_name == 'random_float_data_from_list_gen'
        or function_name == 'random_int_from_closed_interval_data_gen'
        or function_name == 'random_int_from_range_data_gen'
        or function_name == 'random_float_from_closed_interval_data_gen'
        or function_name == 'random_float_from_closed_interval_with_fixed_precision_data_gen'
        or function_name == 'random_strict_bool_data_gen'
        or function_name == 'fixed_sequential_str_data_from_list_gen'
        or function_name == 'fixed_sequential_int_data_from_list_gen'
        or function_name == 'fixed_sequential_float_data_from_list_gen'
        or function_name == 'fixed_sequential_strict_bool_data_from_list_gen') :
            return variable, indent
    else:
        return None, None
    return variable, indent

# PROGRAMA PRINCIPAL:

# MODIFICACIÓN 23/03/2023
# Modifique este programa para poder soportar ESV (Puesto que en este momento sólo funciona con variantes).
# Es decir, se debe permitir que este programa añada código a los códigos base de un ejercicio 
#   para poder generar automáticamente los archivos de entrada de casos de prueba junto con los archivos de salida 
#   que normalmente se obtienen cuando se ejecutan estos códigos.

# Paso 1: Elegir el directorio en donde están los archivos del ejercicio de programación
# NOTA: Sólo se considerarán los archivos que terminen en res<número de variante>.py.
# Además, estos archivos res<número de variante>.py deben estar ensamblados para que este programa funcione bien.
exercise_dir = choose_python_exercise_assembled_variant_combination_files_dir_location()

# Paso 2: Buscar cada archivo res<número de variante>.py en el directorio principal.
files = get_assembled_variant_combination_files_from_directory(exercise_dir)
# print(files)

# Por cada archivo de variante de ejercicio (VE):
if (len(files) > 0): # El ejercicio tiene VE.
    file_index = 0
    for file in files:
        # Paso 3: Obtenga el nombre del archivo generador de casos de prueba para la combinación de variante asociada
        #   al archivo en revisión.
        # ERROR:
        # tc_gen_file_name = file.split('\\')[1].split('.')[0] + TEST_CASE_GEN_PSEUDO_EXTENSION + PY_FILE_EXTENSION
        tc_gen_file_name = file.split('\\')[0] + '\\' + file.split('\\')[1].split('.')[0] \
            + TEST_CASE_GEN_PSEUDO_EXTENSION + PY_FILE_EXTENSION
        # print(tc_gen_file_name)

        # Paso 4: Cree (o sobreescriba) y abra un archivo nuevo en ese mismo directorio para escritura, 
        #   que se llame res<número de variante>_tc_gen.py
        # Abrir un archivo en modo 'w' significa que el archivo se creará si no existe, y se abrirá sólo para SOBREESCRIBIRLO.
        # Usar codificación UTF-8 para textos es MUY importante para reconocer correctamente caracteres como las tildes y la ñ.
        with open(tc_gen_file_name, mode='w', encoding='utf-8') as new_file:
            # Paso 5: Escriba en el archivo nuevo el código inicial que debe tener el programa para poder generar archivos 
            #   de entrada en un paso posterior, en otro programa.
            # Esto es:
            #   La inicialización de la lista de datos de entrada como una lista vacía.
            #   La lectura de un argumento adicional de línea de comandos, correspondiente a la ruta y nombre del archivo de 
            #       entrada (.txt)
            #   que se generará al ejecutar el programa res<número de variante>_tc_gen.py en un paso posterior, en otro programa.
            new_file.write('# Configuración inicial para generar archivos de entrada de este programa - NO MODIFICAR\n')
            new_file.write('import sys\n')
            new_file.write('input_data_list = []\n')
            new_file.write('input_data_file_route = None\n')
            new_file.write('if (len(sys.argv) == 2):\n')
            new_file.write('\tinput_data_file_route = sys.argv[1]\n')        
            new_file.write('# Fin de configuración inicial para generar archivos de entrada de este programa - NO MODIFICAR\n')

            # Paso 6: Abra el archivo res<número de variante>.py en modo de lectura, y lea cada línea de este
            # Abrir un archivo en modo 'r' significa que el archivo se abrirá sólo para leerlo.
            with open(file, mode='r', encoding='utf-8') as original_file:                
                append_newline_before_textline = False                
                line = 0
                # El operador := es de asignación para una variable, pero permite hacer operaciones con 
                #   el valor de variable en una misma línea. (MUY CONVENIENTE EN ESTE CASO).
                # Por cada línea:
                while ((file_line_string := original_file.readline()) != ''):                
                    line += 1
                    # En un archivo .py, se espera que se cumpla que:
                    # file_line_string = '\n' cuando la línea de código .py está vacía.
                    # file_line_string = '' cuando la última línea de código .py está vacía, 
                    #   y cuando se alcanza el EOF: End of File (Fin del archivo .py).

                    # Para evitar escribir un caracter '\n' innecesario al final, si la última detección de una instrucción de 
                    #   lectura de Python se hizo en una línea diferente a la última, haga lo siguiente:
                    # Asuma que ninguna línea leída debe tener un caracter '\n' al final:
                    #   Mire si el último caracter de una línea es '\n' o '' (No hay un '\n')
                    #   Si es '\n', entonces escriba el resto de la línea, y almacene este caracter para ser agregado si se encuentra
                    #       otra instrucción de lectura de datos después. Si no se encuentra otra instrucción después, 
                    #       el caracter '\n' no se usa, y de esta forma, se desecha eficazmente.
                    #   Si no hay un '\n' al final, simplemente escriba toda la línea.

                    line_to_write = ''
                    if (append_newline_before_textline):
                        line_to_write += '\n'
                        append_newline_before_textline = False

                    # Escriba, en el archivo resultante, la línea de contenido correspondiente
                    if (textline_has_newline_ending(file_line_string)):
                        # Paso 7: Revise si en la línea hay una variable que obtiene un valor a partir de una función generadora.
                        # Si no lo hay, copie la línea de res<número de variante>.py en res<número de variante>_tc_gen.py, tal cual.
                        # Si lo hay, además de copiar lo anterior, agregue en otra línea una instrucción para introducir el valor 
                        #   de la variable en la lista de datos de entrada.                    
                        variable, indent = get_gen_function_variable_and_indent_from_line(file_line_string)
                        # print(variable)
                        # print(indent)
                        # Si la línea no contiene una función generadora que asigna un valor a una variable:
                        if variable == None: 
                            # Escriba la línea del contenido del archivo original, tal cual:
                            line_to_write += file_line_string[0:len(file_line_string)-1:1]
                            new_file.write(line_to_write) # Escribe toda la línea, excepto el último caracter.
                            append_newline_before_textline = True
                        else: # Si la línea contiene una función generadora que asigna un valor a una variable:
                            # Copie la línea tal cual, conservando la identación, pero agregue una línea adicional que 
                            #   contenga una instrucción para introducir el valor de la variable en la lista de datos de entrada.
                            new_file.write('\n' + file_line_string) # Se deja el '\n' al final porque se escribirá otra línea adicional aquí
                            # Esta línea no tiene '\n' porque esta es la última línea a escribir en esta iteración:
                            if indent == None:
                                new_file.write('input_data_list.append(' + str(variable) + ')')
                            else:
                                new_file.write(indent + 'input_data_list.append(' + str(variable) + ')')
                            append_newline_before_textline = True
                    else:
                        # Paso 7: Revise si en la línea hay una variable que obtiene un valor a partir de una función generadora.
                        # Si no lo hay, copie la línea de res<número de variante>.py en res<número de variante>_tc_gen.py, tal cual.
                        # Si lo hay, además de copiar lo anterior, agregue en otra línea una instrucción para introducir el valor 
                        #   de la variable en la lista de datos de entrada.
                        variable, indent = get_gen_function_variable_and_indent_from_line(file_line_string)
                        # Si la línea no contiene una función generadora que asigna un valor a una variable:
                        if variable == None:
                            # Escriba la línea del contenido del archivo original, tal cual:
                            line_to_write += file_line_string
                            new_file.write(line_to_write)
                        else: # Si la línea contiene una función generadora que asigna un valor a una variable:
                            # Copie la línea tal cual, conservando la identación, pero agregue una línea adicional que 
                            #   contenga una instrucción para introducir el valor de la variable en la lista de datos de entrada.                 
                            new_file.write(indent + file_line_string) # Se deja el '\n' porque se escribirá otra línea adicional aquí
                            if indent == None:
                                new_file.write('input_data_list.append(' + variable + ')\n')
                            else:
                                new_file.write(indent + 'input_data_list.append(' + variable + ')\n')
                        pass
                    pass
                pass

            # Paso 8: Al terminar de revisar el archivo res<número de variante>.py:
            # Agregue en res<número de variante>_tc_gen.py el código final que debe tener el programa para poder generar archivos de
            #   entrada en un paso posterior, en otro programa.
            # Esto es:
            #   La creación y apertura de un nuevo archivo cuyo nombre fue dado por el argumento de línea de comandos mencionada
            #       anteriormente, en modo de escritura,
            #   Y la posterior escritura de cada dato de entrada guardado en la lista de datos de entrada, en una línea distinta.
            #   (Vea el programa input_data_set_gen_file.py para más información de cómo se puede hacer esto.)
            new_file.write('\n')
            new_file.write('# Configuración final para generar archivos de entrada de este programa - NO MODIFICAR\n')
            new_file.write("if (input_data_file_route != None and input_data_file_route.endswith('.txt')):\n")
            new_file.write('\twith open(input_data_file_route, mode=\'w\', encoding=\'utf-8\') as input_file:\n')
            new_file.write('\t\tcounter = len(input_data_list) # Variable auxiliar para no dejar líneas en blanco en el archivo .txt\n')
            new_file.write('\t\tfor input_data in input_data_list:\n')
            new_file.write('\t\t\tif (counter != 1):\n')
            new_file.write('\t\t\t\tinput_file.write(str(input_data) + \'\\n\')\n')
            new_file.write('\t\t\telse:\n')
            new_file.write('\t\t\t\tinput_file.write(str(input_data))\n')
            new_file.write('\t\t\tcounter -= 1\n')
            new_file.write('# Fin de configuración final para generar archivos de entrada de este programa - NO MODIFICAR\n')

        file_index += 1

else: # El ejercicio sólo tiene CB
    # Paso 3: Busque el archivo de CB (main.py) en el directorio del ejercicio.
    base_code_file_list = get_main_file_from_directory(exercise_dir)
    base_code_file = None
    if len(base_code_file_list) == 0:
        print('No existen códigos de variantes de ejercicio (VE) ni un código base (CB) en el directorio del ejercicio. ' + 
              'Cerrando la aplicación...')
        sys.exit()
    else:
        base_code_file = base_code_file_list[0]

    # Paso 4: Obtenga el nombre del archivo generador de casos de prueba para el código base.
    # ERROR:
    # tc_gen_file_name = file.split('\\')[1].split('.')[0] + TEST_CASE_GEN_PSEUDO_EXTENSION + PY_FILE_EXTENSION
    tcg_file_name = base_code_file.split('\\')[0] + '\\' + base_code_file.split('\\')[1].split('.')[0] \
        + TEST_CASE_GEN_PSEUDO_EXTENSION + PY_FILE_EXTENSION
    # print(tc_gen_file_name)

    # Paso 5: Cree (o sobreescriba) y abra un archivo nuevo en ese mismo directorio para escritura, 
    #   que se llame main_tcg.py
    # Abrir un archivo en modo 'w' significa que el archivo se creará si no existe, y se abrirá sólo para SOBREESCRIBIRLO.
    # Usar codificación UTF-8 para textos es MUY importante para reconocer correctamente caracteres como las tildes y la ñ.
    with open(tcg_file_name, mode='w', encoding='utf-8') as new_file:
        # Paso 6: Escriba en el archivo nuevo el código inicial que debe tener el programa para poder generar archivos 
        #   de entrada en un paso posterior, en otro programa.
        # Esto es:
        #   La inicialización de la lista de datos de entrada como una lista vacía.
        #   La lectura de un argumento adicional de línea de comandos, correspondiente a la ruta y nombre del archivo de 
        #       entrada (.txt)
        #   que se generará al ejecutar el programa res<número de variante>_tc_gen.py en un paso posterior, en otro programa.
        new_file.write('# Configuración inicial para generar archivos de entrada de este programa - NO MODIFICAR\n')
        new_file.write('import sys\n')
        new_file.write('input_data_list = []\n')
        new_file.write('input_data_file_route = None\n')
        new_file.write('if (len(sys.argv) == 2):\n')
        new_file.write('\tinput_data_file_route = sys.argv[1]\n')        
        new_file.write('# Fin de configuración inicial para generar archivos de entrada de este programa - NO MODIFICAR\n')

        # Paso 7: Abra el archivo main.py en modo de lectura, y lea cada línea de este
        # Abrir un archivo en modo 'r' significa que el archivo se abrirá sólo para leerlo.
        with open(base_code_file, mode='r', encoding='utf-8') as original_file:                
            append_newline_before_textline = False                
            line = 0
            # El operador := es de asignación para una variable, pero permite hacer operaciones con 
            #   el valor de variable en una misma línea. (MUY CONVENIENTE EN ESTE CASO).
            # Por cada línea:
            while ((file_line_string := original_file.readline()) != ''):                
                line += 1
                # En un archivo .py, se espera que se cumpla que:
                # file_line_string = '\n' cuando la línea de código .py está vacía.
                # file_line_string = '' cuando la última línea de código .py está vacía, 
                #   y cuando se alcanza el EOF: End of File (Fin del archivo .py).

                # Para evitar escribir un caracter '\n' innecesario al final, si la última detección de una instrucción de 
                #   lectura de Python se hizo en una línea diferente a la última, haga lo siguiente:
                # Asuma que ninguna línea leída debe tener un caracter '\n' al final:
                #   Mire si el último caracter de una línea es '\n' o '' (No hay un '\n')
                #   Si es '\n', entonces escriba el resto de la línea, y almacene este caracter para ser agregado si se encuentra
                #       otra instrucción de lectura de datos después. Si no se encuentra otra instrucción después, 
                #       el caracter '\n' no se usa, y de esta forma, se desecha eficazmente.
                #   Si no hay un '\n' al final, simplemente escriba toda la línea.

                line_to_write = ''
                if (append_newline_before_textline):
                    line_to_write += '\n'
                    append_newline_before_textline = False

                # Escriba, en el archivo resultante, la línea de contenido correspondiente
                if (textline_has_newline_ending(file_line_string)):
                    # Paso 8a: Revise si en la línea hay una variable que obtiene un valor a partir de una función generadora.
                    # Si no lo hay, copie la línea de main.py en main_tcg.py, tal cual.
                    # Si lo hay, además de copiar lo anterior, agregue en otra línea una instrucción para introducir el valor 
                    #   de la variable en la lista de datos de entrada.                    
                    variable, indent = get_gen_function_variable_and_indent_from_line(file_line_string)
                    # print(variable)
                    # print(indent)
                    # Si la línea no contiene una función generadora que asigna un valor a una variable:
                    if variable == None: 
                        # Escriba la línea del contenido del archivo original, tal cual:
                        line_to_write += file_line_string[0:len(file_line_string)-1:1]
                        new_file.write(line_to_write) # Escribe toda la línea, excepto el último caracter.
                        append_newline_before_textline = True
                    else: # Si la línea contiene una función generadora que asigna un valor a una variable:
                        # Copie la línea tal cual, conservando la identación, pero agregue una línea adicional que 
                        #   contenga una instrucción para introducir el valor de la variable en la lista de datos de entrada.
                        new_file.write('\n' + file_line_string) # Se deja el '\n' al final porque se escribirá otra línea adicional aquí
                        # Esta línea no tiene '\n' porque esta es la última línea a escribir en esta iteración:
                        if indent == None:
                            new_file.write('input_data_list.append(' + str(variable) + ')')
                        else:
                            new_file.write(indent + 'input_data_list.append(' + str(variable) + ')')
                        append_newline_before_textline = True
                else:
                    # Paso 8b: Revise si en la línea hay una variable que obtiene un valor a partir de una función generadora.
                    # Si no lo hay, copie la línea de main.py en main_tcg.py, tal cual.
                    # Si lo hay, además de copiar lo anterior, agregue en otra línea una instrucción para introducir el valor 
                    #   de la variable en la lista de datos de entrada.
                    variable, indent = get_gen_function_variable_and_indent_from_line(file_line_string)
                    # Si la línea no contiene una función generadora que asigna un valor a una variable:
                    if variable == None:
                        # Escriba la línea del contenido del archivo original, tal cual:
                        line_to_write += file_line_string
                        new_file.write(line_to_write)
                    else: # Si la línea contiene una función generadora que asigna un valor a una variable:
                        # Copie la línea tal cual, conservando la identación, pero agregue una línea adicional que 
                        #   contenga una instrucción para introducir el valor de la variable en la lista de datos de entrada.                 
                        new_file.write(indent + file_line_string) # Se deja el '\n' porque se escribirá otra línea adicional aquí
                        if indent == None:
                            new_file.write('input_data_list.append(' + variable + ')\n')
                        else:
                            new_file.write(indent + 'input_data_list.append(' + variable + ')\n')
                    pass
                pass
            pass

        # Paso 9: Al terminar de revisar el archivo main.py:
        # Agregue en main_tcg.py el código final que debe tener el programa para poder generar archivos de
        #   entrada en un paso posterior, en otro programa.
        # Esto es:
        #   La creación y apertura de un nuevo archivo cuyo nombre fue dado por el argumento de línea de comandos mencionada
        #       anteriormente, en modo de escritura,
        #   Y la posterior escritura de cada dato de entrada guardado en la lista de datos de entrada, en una línea distinta.
        #   (Vea el programa input_data_set_gen_file.py para más información de cómo se puede hacer esto.)
        new_file.write('\n')
        new_file.write('# Configuración final para generar archivos de entrada de este programa - NO MODIFICAR\n')
        new_file.write("if (input_data_file_route != None and input_data_file_route.endswith('.txt')):\n")
        new_file.write('\twith open(input_data_file_route, mode=\'w\', encoding=\'utf-8\') as input_file:\n')
        new_file.write('\t\tcounter = len(input_data_list) # Variable auxiliar para no dejar líneas en blanco en el archivo .txt\n')
        new_file.write('\t\tfor input_data in input_data_list:\n')
        new_file.write('\t\t\tif (counter != 1):\n')
        new_file.write('\t\t\t\tinput_file.write(str(input_data) + \'\\n\')\n')
        new_file.write('\t\t\telse:\n')
        new_file.write('\t\t\t\tinput_file.write(str(input_data))\n')
        new_file.write('\t\t\tcounter -= 1\n')
        new_file.write('# Fin de configuración final para generar archivos de entrada de este programa - NO MODIFICAR\n')