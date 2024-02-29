import sys
import os

import tkinter as tk
from tkinter import filedialog

from print_combinations_list import gen_variant_combinations_list as gvcl

SUB_KEYWORD = 's'
VARIANT_KEYWORD = 'v'
PY_FILE_EXTENSION = '.py'

PYCASS_KEYWORD = '#pycass'
SUBROUTINE_KEYWORD = 's'

MAIN_FILE_KEYWORD = 'main.py'
RESULT_DIR_KEYWORD = 'res'

def choose_main_dir_location():
    # Este procedimiento debería funcionar bien en Windows 10/11.
    # Preguntar por la ruta del directorio en donde se albergarán los archivos y directorios del ejercicio con sus variantes.
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.iconify()
    print('En la ventana que aparecerá en pantalla, seleccione el directorio en donde se albergarán los archivos y directorios del ejercicio con sus variantes.')
    # Obtiene el directorio seleccionado y referenciado con la ruta absoluta (Desde el disco C:/)
    main_dir = filedialog.askdirectory(title='Seleccione un directorio', parent=root)
    root.destroy()    

    # Si no se selecciona ningún directorio, dé un mensaje al usuario y detenga esta aplicación:
    if (main_dir.strip() == ''):
        print('No se ha seleccionado ningún directorio. Cerrando la aplicación...')
        sys.exit()
    else:
        print('El directorio principal seleccionado para el ejercicio es:', main_dir)
        return main_dir

def find_dirs_in_dir(search_path):
    # https://docs.python.org/3/library/os.html#os.walk
    dirs = []
    # Haciendo un recorrido top-down desde la raíz:
    for dir_path, dir_names, file_names in os.walk(search_path):
        # dirpath is a string, the path to the directory.
        # dirnames is a list of the names of the subdirectories in dirpath (including symlinks to directories, and excluding '.' and '..').
        # filenames is a list of the names of the non-directory files in dirpath. Note that the names in the lists contain no path components.

        for dir_name_found in dir_names:
            dir_name = str(dir_name_found)
            dirs.append(dir_name)
    return dirs

def find_files_in_dir(search_path):
    # https://docs.python.org/3/library/os.html#os.walk
    files = []
    # Haciendo un recorrido top-down desde la raíz:
    for dir_path, dir_names, file_names in os.walk(search_path):
        # dirpath is a string, the path to the directory.
        # dirnames is a list of the names of the subdirectories in dirpath (including symlinks to directories, and excluding '.' and '..').
        # filenames is a list of the names of the non-directory files in dirpath. Note that the names in the lists contain no path components.

        for file_name_found in file_names:
            file_name = str(file_name_found)
            files.append(file_name)
    return files

def find_main_file_in_subroutine_dir(search_path):
    # https://docs.python.org/3/library/os.html#os.walk
    files = []
    # Haciendo un recorrido top-down desde la raíz:
    root_path = True
    for dir_path, dir_names, file_names in os.walk(search_path):
        # dirpath is a string, the path to the directory.
        # dirnames is a list of the names of the subdirectories in dirpath (including symlinks to directories, and excluding '.' and '..').
        # filenames is a list of the names of the non-directory files in dirpath. Note that the names in the lists contain no path components.
        # Para tomar sólo los resultados del directorio raíz, y no de los subdirectorios:
        if (root_path == True):
            for file_name_found in file_names:
                file_name = str(file_name_found)
                if (file_name == MAIN_FILE_KEYWORD):
                    files.append(os.path.join(dir_path, file_name))
            root_path = False
        else:
            return files
    return files

def find_subroutine_dirs_in_dir(search_path):
    # https://docs.python.org/3/library/os.html#os.walk
    dirs = []
    # Haciendo un recorrido top-down desde la raíz:
    for dir_path, dir_names, file_names in os.walk(search_path):
        # dirpath is a string, the path to the directory.
        # dirnames is a list of the names of the subdirectories in dirpath (including symlinks to directories, and excluding '.' and '..').
        # filenames is a list of the names of the non-directory files in dirpath. Note that the names in the lists contain no path components.

        for dir_name_found in dir_names:
            dir_name = str(dir_name_found)
            if (dir_name[0:1:1] == SUB_KEYWORD and dir_name[::-1][0:1:1].isnumeric()):
                dirs.append(dir_name)
    return dirs

def find_subroutine_dir_routes_in_dir(search_path):
    # https://docs.python.org/3/library/os.html#os.walk
    dir_routes = []
    # Haciendo un recorrido top-down desde la raíz:
    for dir_path, dir_names, file_names in os.walk(search_path):
        # dirpath is a string, the path to the directory.
        # dirnames is a list of the names of the subdirectories in dirpath (including symlinks to directories, and excluding '.' and '..').
        # filenames is a list of the names of the non-directory files in dirpath. Note that the names in the lists contain no path components.

        for dir_name_found in dir_names:
            dir_name = str(dir_name_found)
            if (dir_name[0:1:1] == SUB_KEYWORD and dir_name[1:len(dir_name):1].isnumeric()):
                dir_routes.append(os.path.join(dir_path, dir_name))
    return dir_routes

def find_variant_files_in_subroutine_dir(search_path):
    # ADVERTENCIA: LOS ARCHIVOS DE VARIANTES A ENCONTRAR SON ARCHIVOS DE EXTENSIÓN .PY

    # https://docs.python.org/3/library/os.html#os.walk
    files = []
    # Haciendo un recorrido top-down desde la raíz:
    root_path = True
    for dir_path, dir_names, file_names in os.walk(search_path):
        # dirpath is a string, the path to the directory.
        # dirnames is a list of the names of the subdirectories in dirpath (including symlinks to directories, and excluding '.' and '..').
        # filenames is a list of the names of the non-directory files in dirpath. Note that the names in the lists contain no path components.
        # Para tomar sólo los resultados del directorio raíz, y no de los subdirectorios:
        if (root_path == True):
            for file_name_found in file_names:
                file_name = str(file_name_found)
                if (file_name[0:1:1] == VARIANT_KEYWORD and file_name[1:len(file_name)-3:1].isnumeric() and file_name[len(file_name)-3:len(file_name)+1:1] == PY_FILE_EXTENSION):
                    files.append(os.path.join(dir_path, file_name))
            root_path = False
        else:
            return files
    return files

def get_subroutine_dir_routes_list(main_dir):
    # Las subrutinas son directorios cuyo nombre es: s<numero>, donde <numero> es el número asociado a una subrutina del ejercicio.
    # Se debe obtener la lista de las subrutinas que hay en, y dentro del directorio principal del ejercicio.
    return find_subroutine_dir_routes_in_dir(main_dir)

def get_subroutine_variant_counts(subroutine_dir_routes_list):
    # Cada subrutina puede tener un número variable de variantes.
    # Se debe encontrar el directorio de cada subrutina, y para cada uno de esos directorios, encontrar el número de archivos en 
    #   esos directorios cuyo nombre es: v<numero>, donde <numero> es el número asociado a una variante de la subrutina.
    # Se debe obtener una lista de cantidades de variantes que hay por subrutina.

    variant_counts_list = []

    # El número de subrutinas se puede obtener fácilmente mediante el número de elementos de subroutine_list
    subroutine_count = len(subroutine_dir_routes_list)

    for s in range(1, subroutine_count + 1, 1):
        # Revisar la subrutina s
        # Encontrar la ruta de la subrutina s
        subroutine_dir_path = subroutine_dir_routes_list[s - 1]

        # Encontrar los archivos de variantes disponibles para la subrutina
        subroutine_variant_files = find_variant_files_in_subroutine_dir(subroutine_dir_path)

        # Colocar el número de variantes para la subrutina s aquí:
        variant_counts_list.append(len(subroutine_variant_files))

    return variant_counts_list

def get_possible_variant_combinations_list(subroutine_variant_counts):
    variant_combinations = gvcl(subroutine_variant_counts)
    return variant_combinations

def file_has_python_code_assembler_keyword(file):
    if (file == ''):
        return False

    # Usar codificación UTF-8 para textos es MUY importante para reconocer correctamente caracteres como las tildes y la ñ.
    with open(file, mode='r', encoding='utf-8') as file_to_check:
        while ((file_to_check_line := file_to_check.readline()) != ''):
            if (textline_has_python_code_assembler_keyword(file_to_check_line)):
                return True
    return False

def textline_has_python_code_assembler_keyword(text):
    # https://stackoverflow.com/questions/10974932/split-string-based-on-a-regular-expression
    # There is no need for regex, str.split without any delimiter specified will split this by whitespace for you. 
    #   This would be the best way in this case.
    pycass_components = str(text).strip().split()
    if len(pycass_components) >= 2:
        pycass_subroutine_number = pycass_components[1][1::]
    
    # https://developer.rhino3d.com/guides/rhinopython/python-statements/
    # You cannot split a statement into multiple lines in Python by pressing Enter. 
    #   Instead, use the backslash (\) to indicate that a statement is continued on the next line.
    # https://www.w3schools.com/python/ref_string_isnumeric.asp
    # The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
        return pycass_components[0] == PYCASS_KEYWORD and \
            pycass_components[1].startswith(SUBROUTINE_KEYWORD) and \
            str(pycass_subroutine_number).isnumeric() == True
    else:
        return False # No hay suficientes tokens (palabras) en la línea para representar una línea de ensamblado de código.

def get_code_file_to_assemble(read_line, variant_combination, main_dir):
    pycass_components = str(read_line).strip().split()
    pycass_subroutine_number = pycass_components[1][1::]
    # Dependiendo del número de la subrutina, buscar la variante a aplicar para la subrutina a partir de 
    #   la combinación de variantes seleccionada anteriormente.
    pycass_variant_number = variant_combination[int(pycass_subroutine_number) - 1]
    # Ahora se debe buscar el archivo que corresponde a la variante de la subrutina.
    subroutine_dir_routes = find_subroutine_dir_routes_in_dir(main_dir)
    subroutine_dir_route = ''
    for sr in subroutine_dir_routes:
        if sr.split('\\')[-1] == SUB_KEYWORD + pycass_subroutine_number:
            subroutine_dir_route = sr
            break
    variant_file_routes = find_variant_files_in_subroutine_dir(subroutine_dir_route)
    for vr in variant_file_routes:
        if vr.split('\\')[-1] == VARIANT_KEYWORD + str(pycass_variant_number) + PY_FILE_EXTENSION:
            return vr

def assemble_code_with_variant_combination(combination_number, variant_combination, main_dir):
    # Aquí se realiza el ensamblado del código en un archivo res<combination_number>.py, teniendo en cuenta las 
    #   variantes asignadas a cada subrutina del ejercicio de programación, donde <combination_number> es el número 
    #   asociado a una de las posibles combinaciones de variantes.

    # Ensamblaje de código: Seguir realizando mientras no se encuentren etiquetas #pycass s<numero> válidas en el 
    #   archivo tomado como principal, donde <numero> es el número asociado a una subrutina del ejercicio de programación.
    # Primero se revisará esto con el archivo principal (main.py), y luego, con cada una de las variantes que se usaron 
    #   con este archivo principal para hacer un ensamblaje.
    
    # Paso 1: Valide que exista un archivo main.py en el directorio principal
    if (len(find_main_file_in_subroutine_dir(main_dir)) < 1):
        print('No se ha encontrado ningún archivo principal (main.py) en el directorio principal del ejercicio. Cerrando la aplicación...')
        sys.exit()

    main_file_route = find_main_file_in_subroutine_dir(main_dir)[0]

    with open(main_dir+'\\res' + str(combination_number) + PY_FILE_EXTENSION, mode='w', encoding='utf-8') as output_file:
        
        # Usar codificación UTF-8 para textos es MUY importante para reconocer correctamente caracteres como las tildes y la ñ.
        with open(main_file_route, mode='r', encoding='utf-8') as main_input_file:
            
            # El operador := sirve como asignación para una variable, y permite hacer operaciones con el valor de variable en una misma línea. 
            #   MUY CONVENIENTE EN ESTE CASO.
            # main_line = '\n' para líneas de código vacías.
            # main_line = '' cuando se alcanza el EOF: End of File (Fin del archivo).
            
            # Por cada línea del código principal que no sea el que se va a cambiar por el código secundario:
            #   Lea la siguiente línea del código principal:
            #       Si no es EOF (El texto tiene al menos un caracter '\n'), escriba la línea del código principal en el código ensamblado.
            #       Si es EOF (El texto tiene necesariamente una cadena vacía ''), escriba la línea del código principal en el código ensamblado.
            # Pero si es la línea del código principal que se debe cambiar por el código secundario:
            #   Si esta no es la última línea, escriba todas las líneas del código secundario en el código ensamblado, pero asegúrese de que la
            #       próxima línea a escribir contenga el caracter '\n' al principio, cuando se lea la próxima línea.
            #   Si es la última línea (La siguiente resulta en un EOF), sólo escriba todas las líneas del código secundario en el código ensamblado.
            #       PERO: No se sabe cuándo es la siguiente línea un EOF... Por lo tanto, asuma que el próximo NO ES UN EOF, y añada el caracter '\n'
            #       para la próxima lectura, en caso que no sea un EOF; pero si lo es, no haga nada.

            # ¿Cómo saber cuándo se debe hacer el ensamblaje de todas las líneas del código secundario?
            #   Ver si la palabra reservada #pycass se encuentra o no, sin importar que hayan espacios en blanco al 
            #   principio o al final, en una línea.

            extra_newline = False
            while ((main_line := main_input_file.readline()) != ''):

                if (extra_newline == True):
                    output_file.write('\n')
                    extra_newline = False

                if (textline_has_python_code_assembler_keyword(main_line)):
                    with open(get_code_file_to_assemble(main_line, variant_combination, main_dir), mode="r", encoding='utf-8') as sub_input_file:
                        sub_lines = sub_input_file.readlines() # No añade el último '\n', porque se alcanza el EOF del archivo secundario.
                        output_file.writelines(sub_lines) # Escriba todas las líneas del código secundario en el código ensamblado.
                        extra_newline = True
                else:
                    output_file.write(main_line) # Escriba la línea leída del código principal en el código ensamblado.

# Subrutina principal: Realiza el ensamblado del programa principal con todos los subprogramas para todas las variantes posibles,
#   colocando el resultado del ensamblaje en archivos res.py, en el directorio res
def assemble_code_variants():
    # Primer paso: El usuario debe elegir la ubicación del directorio principal del código del ejercicio de programación con sus variantes.
    main_dir = choose_main_dir_location()

    # Segundo paso: Saber las rutas de las subrutinas (directorios) definidas para el ejercicio de programación,
    #   tanto en el directorio principal del código del ejercicio de programación 
    #   como en los subdirectorios de las subrutinas asociadas al ejercicio de programación.
    subroutine_dir_routes_list = get_subroutine_dir_routes_list(main_dir)
    
    # Tercer paso: Saber cuántas variantes hay por cada subrutina definida para el ejercicio de programación.
    subroutine_variant_counts = get_subroutine_variant_counts(subroutine_dir_routes_list)

    # Cuarto paso: Saber cuántas combinaciones de variantes hay para el ejercicio de programación.
    possible_variant_combinations_list = get_possible_variant_combinations_list(subroutine_variant_counts)

    # Quinto paso: Ejecutar el ensamblador de código para cada una de las combinaciones de variantes posibles,
    #   considerando las etiquetas de ensamblaje tanto en el programa principal como en las subrutinas.
    combination_number = 0
    for variant_combination in possible_variant_combinations_list:
        print(variant_combination)
        combination_number = combination_number + 1
        
        assemble_code_with_variant_combination(combination_number, variant_combination, main_dir)

    # TODO: Sexto paso: Confirmar al usuario que el procedimiento ha sido terminado.
    pass

# Programa Principal: FUNCIONA: DESCOMENTAR CUANDO SE QUIERA PROBAR
assemble_code_variants()