import sys
import tkinter as tk
from tkinter import filedialog
import os

from PythonFileInputInstruction import PythonFileInputInstruction as PyFileInputInstr

# from PythonInputInstructionSearch import PythonInputInstructionSearch as PyInputInstrSearch

SUB_KEYWORD = 's'
VARIANT_KEYWORD = 'v'
PY_FILE_EXTENSION = '.py'
MAIN_FILE_KEYWORD = 'main.py'

INPUT_IDENTIFIER_RESULTS_FILE = 'input_identifier_results.txt'

WHITESPACE_TOKENS = [' ', '\t', '\f'] # Caracteres que separan tokens en una línea lógica en Python.
# Sin embargo, no está permitido el uso de estos caracteres al principio de una línea (Excepto si se colocan como cadenas de caracteres)
# https://docs.python.org/3/reference/lexical_analysis.html
# Except at the beginning of a logical line or in string literals, the whitespace characters space, tab and formfeed can be used 
#   interchangeably to separate tokens. 
# Whitespace is needed between two tokens only if their concatenation could otherwise be interpreted as a different token 
#   (e.g., ab is one token, but a b is two tokens).

NEWLINE_TOKEN = '\n' # Cada vez que se lee una línea de un archivo de Python (.py) con la función open() y el método readline(),
#   la cadena de caracteres leída siempre termina en '\n', a menos que sea la última línea o se haya llegado a un EOF 
#   (Que corresponde a una lectura de cadena vacía: '')

SEMICOLON_TOKEN = ';' # Permite que haya más de una instrucción en una línea lógica en Python.
# Normalmente, en Python, sólo puede haber una instrucción por línea lógica.
# Por otro lado, el punto y coma no puede cerrar una línea lógica en Python.
EXPLICIT_PHYSICAL_LINE_JOIN_TOKEN = '\\' # Este es un token que junta dos o más líneas físicas en una línea lógica de Python, 
#   haciendo que una línea lógica en Python se extienda a más de 1 línea física 
#   - Una línea física se termina con un salto de línea, dependiendo del sistema operativo usado para hacer el script de Python:
# https://stackoverflow.com/questions/6907245/what-type-of-line-breaks-does-a-python-script-normally-have
#   This has nothing to do with Python but with the underlying OS. 
#   If you save a text file on Windows, you get CRLF linebreaks, 
#   if you save it on Mac/Unix systems, you get LF linebreaks 
#   (and on stone-age Macs, CR linebreaks).
# https://docs.python.org/3/reference/lexical_analysis.html
#   A physical line is a sequence of characters terminated by an end-of-line sequence. 
#   In source files and strings, any of the standard platform line termination sequences can be used 
#   - the Unix form using ASCII LF (linefeed), the Windows form using the ASCII sequence CR LF (return followed by linefeed), 
#   or the old Macintosh form using the ASCII CR (return) character. 
#   All of these forms can be used equally, regardless of platform. 
#   The end of input also serves as an implicit terminator for the final physical line.
# Básicamente, permite la definición de un llamado a función o expresión de Python en varias líneas.
# Para más información, vea la documentación del análisis léxico en Python: 
# https://docs.python.org/3/reference/lexical_analysis.html

# Los comentarios son ignorados por el intérprete Python.
SINGLE_LINE_COMMENT_TOKEN = '#' # Un comentario también representa un fin de una línea lógica en Python.
MULTI_LINE_COMMENT_TOKENS = ['"""',"'''"] # Es posible añadir una instrucción después del cierre de un comentario multilínea si se usa un punto y
#   coma después de este comentario.

STRING_LITERAL_DEFINITION_CHARACTERS = ['"',"'"] # Estos caracteres abren y cierran una cadena de caracteres.
# Lo que haga parte de una cadena de caracteres no puede ser considerado como un llamado a una función (e.g., la función input())

OPENING_PARENTHESIS_TOKEN = '('
CLOSING_PARENTHESIS_TOKEN = ')'

EQUAL_SIGN = '='
TYPE_STR_KEYWORD = 'str'
TYPE_INT_KEYWORD = 'int'
TYPE_FLOAT_KEYWORD = 'float'
TYPE_BOOL_KEYWORD = 'bool'

INPUT_KEYWORD = 'input'

PY_FILE_EXTENSION = '.py'

# 1) Lectura de archivo y validación de la presencia de subcadenas de caracteres 'input' en el archivo, mediante 
#   la comparación entre las cadenas de caracteres presentes en cada línea del archivo y el valor 'input' - un literal de cadena de caracteres.

def choose_python_file_location():
    # Este procedimiento debería funcionar bien en Windows 10/11.
    # Preguntar por la ruta del archivo .py en donde se buscarán las instrucciones de lectura para un programa en Python.
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.iconify()
    print('En la ventana que aparecerá en pantalla, seleccione el archivo .py en donde se buscarán instrucciones de lectura escritos en Python.')
    # Obtiene la ruta absoluta del archivo seleccionado (Desde el disco C:/):
    file = filedialog.askopenfilename(title='Seleccione un archivo .py', \
        filetypes=[('Archivos de programas de Python (.py)', '*.py')], parent=root)
    root.destroy()

    # Si no se selecciona ningún archivo, dé un mensaje al usuario y detenga esta aplicación:
    if (file.strip() == ''):
        print('No se ha seleccionado ningún archivo. Cerrando la aplicación...')
        sys.exit()
    else:
        print('El archivo seleccionado para buscar en él instrucciones de lectura de Python es:', file)
        return file

def choose_python_exercise_variants_dir_location():
    # Este procedimiento debería funcionar bien en Windows 10/11.
    # Preguntar por la ruta del directorio que contiene el archivo Python (.py) del código principal y los subdirectorios (s1, s2, etc.)
    #   que contienen archivos Python (.py) por variante, los cuales conforman una propuesta de solución a un ejercicio de programación 
    #   en Python, para todas las variantes propuestas.
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.iconify()
    print('En la ventana que aparecerá en pantalla, seleccione el directorio que contiene el archivo Python del código principal ' 
    + '(main.py) y los subdirectorios (s1, s2, etc.) que contienen, cada uno, archivos Python por variante (v1.py, v2.py, etc.) '
    + 'que conforman una propuesta de solución a un ejercicio de programación en Python con variantes.')
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

def read_and_print_contents_of_python_file(file):
    file_route = str(file)
    if (file_route.endswith(PY_FILE_EXTENSION)):
        # Abrir un archivo en modo 'r' significa que el archivo se abrirá sólo para leerlo.
        # Usar codificación UTF-8 para textos es MUY importante para reconocer correctamente caracteres como las tildes y la ñ.
        with open(file, mode='r', encoding='utf-8') as file_to_read:
            # file_line_string = '\n' cuando la línea de código .py está vacía.
            # file_line_string = '' cuando se alcanza el EOF: End of File (Fin del archivo).
            while ((file_line_string := file_to_read.readline()) != ''):
                print(file_line_string, end='')

def read_and_print_contents_of_python_file(file):
    file_route = str(file)
    if (file_route.endswith(PY_FILE_EXTENSION)):
        # Abrir un archivo en modo 'r' significa que el archivo se abrirá sólo para leerlo.
        # Usar codificación UTF-8 para textos es MUY importante para reconocer correctamente caracteres como las tildes y la ñ.
        with open(file, mode='r', encoding='utf-8') as file_to_read:
            # file_line_string = '\n' cuando la línea de código .py está vacía.
            # file_line_string = '' cuando se alcanza el EOF: End of File (Fin del archivo).
            while ((file_line_string := file_to_read.readline()) != ''):
                print(file_line_string, end='')

def read_and_print_lines_of_python_file_where_input_keyword_is_present(file):
    file_route = str(file)
    if (file_route.endswith(PY_FILE_EXTENSION)):
        # Abrir un archivo en modo 'r' significa que el archivo se abrirá sólo para leerlo.
        # Usar codificación UTF-8 para textos es MUY importante para reconocer correctamente caracteres como las tildes y la ñ.
        with open(file, mode='r', encoding='utf-8') as file_to_read:
            # file_line_string = '\n' cuando la línea de código .py está vacía.
            # file_line_string = '' cuando se alcanza el EOF: End of File (Fin del archivo).
            while ((file_line_string := file_to_read.readline()) != ''):
                if (file_line_string.find(INPUT_KEYWORD) != -1):
                    print(file_line_string, end='')

def textline_has_python_input_keyword(textline):
    textline_str = str(textline)
    if textline_str.find(INPUT_KEYWORD) != -1:
        return True
    else:
        return False

def count_python_input_keywords_in_textline(textline):
    input_keyword_count = 0
    start_index = 0
    end_index = len(textline)
    textline_str = str(textline)
    while (start_index < end_index):
        if (keyword_index := textline_str.find(INPUT_KEYWORD, start_index)) != -1:
            input_keyword_count += 1
            start_index = keyword_index + len(INPUT_KEYWORD)
        else:
            start_index = end_index
    return input_keyword_count

def textline_has_newline_ending(textline):
    textline_str = str(textline)
    if textline_str.endswith(NEWLINE_TOKEN):
        return True
    else:
        return False

def textline_has_explicit_line_joining_character_ending(textline):
    textline_str = str(textline)
    if textline_str.endswith(EXPLICIT_PHYSICAL_LINE_JOIN_TOKEN):
        return True
    else:
        return False

def is_python_identifier(word):
    t = str(word)
    if (t.isidentifier()):
        return True
    else:
        return False

def print_python_file_lines_with_input_keyword_to_results_file_from(file):
    file_route = str(file)
    if (file_route.endswith(PY_FILE_EXTENSION)):
        # Abrir un archivo en modo 'w' significa que el archivo se abrirá sólo para SOBREESCRIBIRLO.
        # Usar codificación UTF-8 para textos es MUY importante para reconocer correctamente caracteres como las tildes y la ñ.
        with open(INPUT_IDENTIFIER_RESULTS_FILE, mode='w', encoding='utf-8') as file_to_write:
            # Abrir un archivo en modo 'r' significa que el archivo se abrirá sólo para leerlo.
            with open(file, mode='r', encoding='utf-8') as file_to_read:
                # El operador := es de asignación para una variable, pero permite hacer operaciones con el valor de variable en una misma línea. 
                    # (MUY CONVENIENTE EN ESTE CASO).
                append_newline_before_textline = False
                line_number_count = 0
                while ((file_line_string := file_to_read.readline()) != ''):
                    line_number_count += 1
                    if (textline_has_python_input_keyword(file_line_string)):
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

                        # Escriba, en el archivo resultante, en una línea, el número de línea en el que se detectó al menos una
                        #   instrucción de lectura de Python, y cuántas detecciones se hicieron en una misma línea:
                        line_to_write += 'Línea ' + str(line_number_count) + ' | Lecturas: '\
                            + str(count_python_input_keywords_in_textline(file_line_string)) + ' -->\t'
                        # Escriba, en el archivo resultante, el contenido de la línea en el que se detectó al menos una 
                        #   instrucción de lectura de Python:
                        if (textline_has_newline_ending(file_line_string)):
                            line_to_write += file_line_string[0:len(file_line_string)-1:1]
                            file_to_write.write(line_to_write) # Escribe toda la línea, excepto el último caracter.
                            append_newline_before_textline = True
                        else:
                            line_to_write += file_line_string
                            file_to_write.write(line_to_write)

def has_inner_whitespace(text):
    count = 0
    for char in text:
        if (count != 0 and count != len(text) - 1):
            c = str(char)
            if c.isspace():
                return True
        count += 1
    return False

def get_input_instruction_from_line(line):
    result = None
    ln = str(line).strip() # Remueve los espacios en blanco al inicio y al final de la línea.
    if ln.find(SINGLE_LINE_COMMENT_TOKEN) != -1: # Se encontró un comentario #
        single_line_comment_index = ln.find(SINGLE_LINE_COMMENT_TOKEN)
        if (single_line_comment_index > 0):
            ln = ln[0:single_line_comment_index:1] # [índice inicial inclusivo, índice final exclusivo, paso]
        else:
            return None

    if ln.find(EQUAL_SIGN) == -1: # No se encontró un signo igual => No es una instrucción válida.
        return None
    if ln.find(INPUT_KEYWORD) == -1: # No se encontró la palabra clave input => No es una instrucción válida.
        return None
    if ln.find(OPENING_PARENTHESIS_TOKEN) == -1: # No se encontró al menos un paréntesis que abre => No es una instrucción válida.
        return None
    if ln.find(CLOSING_PARENTHESIS_TOKEN) == -1: # No se encontró al menos un paréntesis que cierra => No es una instrucción válida.
        return None

    # Número de paréntesis que abren y cierran: Deben ser 1 que abre y 1 que cierra, o 2 que abren y 2 que cierran.
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
    
    if not (opening_parentheses == closing_parentheses and (opening_parentheses == 1 or opening_parentheses == 2)):
        return None

    # Si hay 1 paréntesis que abre y 1 que cierra, asuma que se puede encontrar la forma 1 de una instrucción de lectura
    #   (Esto es, sin un llamado a una función de conversión de tipo - Se espera que esta lectura sea para obtener datos de tipo str)
    # Si hay 2 paréntesis que abren y 2 que cierran, asuma que se puede encontrar la forma 2 de una instrucción de lectura
    #   (Esto es, con un llamado a una función de conversión de tipo - int, float o bool)
    if opening_parentheses == 1:
        # Validar el orden de los tokens de la forma 1:
        # i.e.: Identificador(variable), signo igual, palabra clave input, paréntesis que abre, y paréntesis que cierra.
        # Entre estos tokens pueden haber 0 o 1 espacios en blanco.
        equal_sign_index = ln.find(EQUAL_SIGN)
        input_keyword_index = ln.find(INPUT_KEYWORD)
        opening_parenthesis_index = ln.find(OPENING_PARENTHESIS_TOKEN)
        closing_parenthesis_index = ln.find(CLOSING_PARENTHESIS_TOKEN)
        if not (equal_sign_index < input_keyword_index < opening_parenthesis_index < closing_parenthesis_index):
            return None

        substring_by_equal_sign = ln.split(EQUAL_SIGN)
        variable = substring_by_equal_sign[0].strip()
        remainder = substring_by_equal_sign[1].strip()
        if not variable.isidentifier(): # No se encontró una variable inicial, puesto que el identificador no es válido 
        # => No es una instrucción válida.
            return None

        substring_by_opening_parenthesis = remainder.split(OPENING_PARENTHESIS_TOKEN)
        input_keyword_part = substring_by_opening_parenthesis[0].strip()
        closing_parenthesis_part = substring_by_opening_parenthesis[1].strip()

        if input_keyword_part == INPUT_KEYWORD and closing_parenthesis_part == CLOSING_PARENTHESIS_TOKEN:
            result = PyFileInputInstr(input_type=TYPE_STR_KEYWORD, variable_name=variable, string_representation=ln.strip())

    elif opening_parentheses == 2:
        # Validar el orden de los tokens de la forma 2:
        # i.e.: Identificador(variable); signo igual; palabra clave int, float o bool; paréntesis que abre; palabra clave input;
        #   paréntesis que abre; paréntesis que cierra y paréntesis que cierra.
        # Entre estos tokens pueden haber 0 o 1 espacios en blanco.
        # Por otra parte, sólo puede haber 1 palabra clave de tipo en esta forma 2.
        equal_sign_index = ln.find(EQUAL_SIGN)
        type_int_index = ln.find(TYPE_INT_KEYWORD)
        type_float_index = ln.find(TYPE_FLOAT_KEYWORD)
        type_bool_index = ln.find(TYPE_BOOL_KEYWORD)
        input_keyword_index = ln.find(INPUT_KEYWORD)
        opening_parenthesis_index = ln.find(OPENING_PARENTHESIS_TOKEN)
        second_opening_parenthesis_index = opening_parenthesis_index + \
            ln[opening_parenthesis_index + 1:len(ln):1].find(OPENING_PARENTHESIS_TOKEN) + 1
        closing_parenthesis_index = ln.find(CLOSING_PARENTHESIS_TOKEN)
        second_closing_parenthesis_index = closing_parenthesis_index + \
            ln[closing_parenthesis_index + 1:len(ln):1].find(CLOSING_PARENTHESIS_TOKEN) + 1
        
        if type_int_index == -1:
            second_type_int_index = -1
        elif ln[type_int_index + 1:len(ln):1].find(TYPE_INT_KEYWORD) == -1:
            second_type_int_index = -1
        else:
            second_type_int_index = type_int_index + ln[type_int_index + 1:len(ln):1].find(TYPE_INT_KEYWORD) + 1

        if type_float_index == -1:
            second_type_float_index = -1
        elif ln[type_float_index + 1:len(ln):1].find(TYPE_FLOAT_KEYWORD) == -1:
            second_type_float_index = -1
        else:
            second_type_float_index = type_float_index + ln[type_float_index + 1:len(ln):1].find(TYPE_FLOAT_KEYWORD) + 1

        if type_bool_index == -1:
            second_type_bool_index = -1
        elif ln[type_bool_index + 1:len(ln):1].find(TYPE_BOOL_KEYWORD) == -1:
            second_type_bool_index = -1
        else:
            second_type_bool_index = type_bool_index + ln[type_bool_index + 1:len(ln):1].find(TYPE_BOOL_KEYWORD) + 1

        if second_type_int_index != -1 or second_type_float_index != -1 or second_type_bool_index != -1:
            return None

        data_type = None
        data_type_index = None
        if type_int_index != -1 and type_float_index == -1 and type_bool_index == -1:
            data_type = TYPE_INT_KEYWORD
            data_type_index = type_int_index
        elif type_int_index == -1 and type_float_index != -1 and type_bool_index == -1:
            data_type = TYPE_FLOAT_KEYWORD
            data_type_index = type_float_index
        elif type_int_index == -1 and type_float_index == -1 and type_bool_index != -1:
            data_type = TYPE_BOOL_KEYWORD
            data_type_index = type_bool_index
        else:
            return None

        if not (equal_sign_index < data_type_index < opening_parenthesis_index < input_keyword_index \
            < second_opening_parenthesis_index < closing_parenthesis_index < second_closing_parenthesis_index):
            return None

        substring_by_equal_sign = ln.split(EQUAL_SIGN)
        variable = substring_by_equal_sign[0].strip()
        remainder = substring_by_equal_sign[1].strip()
        if not variable.isidentifier(): # No se encontró una variable inicial, puesto que el identificador no es válido 
        # => No es una instrucción válida.
            return None

        substring_by_opening_parenthesis = remainder.split(OPENING_PARENTHESIS_TOKEN, maxsplit=1)
        type_keyword_part = substring_by_opening_parenthesis[0].strip()
        remainder = substring_by_opening_parenthesis[1].strip()
        if type_keyword_part != TYPE_INT_KEYWORD and type_keyword_part != TYPE_FLOAT_KEYWORD and type_keyword_part != TYPE_BOOL_KEYWORD:
            return None
        
        substring_by_second_opening_parenthesis = remainder.split(OPENING_PARENTHESIS_TOKEN, maxsplit=1)
        input_keyword_part = substring_by_second_opening_parenthesis[0].strip()
        remainder = substring_by_second_opening_parenthesis[1].strip()
        if input_keyword_part != INPUT_KEYWORD:
            return None

        tokens = remainder.split()
        if len(tokens) == 1:
            tokens = tokens[0]
            for t in tokens:
                if t != CLOSING_PARENTHESIS_TOKEN:
                    return None
        else:
            for t in tokens:
                if len(tokens) != 2:
                    return None
                else:
                    for t in tokens:
                        if t != CLOSING_PARENTHESIS_TOKEN:
                            return None

        result = PyFileInputInstr(input_type=data_type, variable_name=variable, string_representation=ln.strip())
        # result.print_json_representation()
    else:
        return None
    return result

def get_python_input_instructions_from_file(file):
    input_instructions = []

    file_route = str(file)
    if (file_route.endswith(PY_FILE_EXTENSION)):
        # Abrir un archivo en modo 'r' significa que el archivo se abrirá sólo para leerlo.
        with open(file, mode='r', encoding='utf-8') as file_to_read:
            append_newline_before_textline = False
            line_number_count = 0
            # El operador := es de asignación para una variable, pero permite hacer operaciones con el valor de variable en una misma línea. 
                # (MUY CONVENIENTE EN ESTE CASO).
            while ((file_line_string := file_to_read.readline()) != ''):
                line_number_count += 1

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

                # Escriba, en el archivo resultante, en una línea, el número de línea en el que se detectó al menos una
                #   instrucción de lectura de Python, y cuántas detecciones se hicieron en una misma línea:
                # line_to_write += 'Línea ' + str(line_number_count) + ' | Lecturas: '\
                #     + str(count_python_input_keywords_in_textline(file_line_string)) + ' -->\t'

                # Escriba, en el archivo resultante, el contenido de la línea en el que se detectó al menos una 
                #   instrucción de lectura de Python:
                if (textline_has_newline_ending(file_line_string)):
                    line_to_write += file_line_string[0:len(file_line_string)-1:1]
                    # file_to_write.write(line_to_write) # Escribe toda la línea, excepto el último caracter.
                    append_newline_before_textline = True
                else:
                    line_to_write += file_line_string
                    # file_to_write.write(line_to_write)

                # Ya se tiene procesado el contenido de la línea leída del archivo en line_to_write
                # Analizar el contenido de line_to_write
                input_instruction = get_input_instruction_from_line(line_to_write)
                # print(input_instruction)
                if input_instruction != None:
                    input_instruction.set_input_line(line_number_count)
                    input_instructions.append(input_instruction)

    return input_instructions

# def get_python_input_instructions_from_file(file):
#     input_instructions = []
#     file_route = str(file)
#     if (file_route.endswith(PY_FILE_EXTENSION)):

#         # DESESTIMAR ESTO.
#         # Este es el plan:
#         # 1) Recorrer caracter por caracter hasta obtener un identificador (nombre de variable válida en Python) o la palabra clave input,
#         #   usada para las instrucciones de lectura.
#         # Sin embargo, sólo se puede leer línea por línea, así que es necesario ir almacenando cadenas de caracteres de varias líneas
#         #   conforme a la necesidad.

#         token_search = None

#         # Abrir un archivo en modo 'r' significa que el archivo se abrirá sólo para leerlo.
#         with open(file, mode='r', encoding='utf-8') as file_to_read:            
#             append_newline_before_textline = False
#             line_number_count = 0
#             # El operador := es de asignación para una variable, pero permite hacer operaciones con el valor de variable en una misma línea. 
#                 # (MUY CONVENIENTE EN ESTE CASO).
#             while ((file_line_string := file_to_read.readline()) != ''):
#                 line_number_count += 1

#                 # En un archivo .py, se espera que se cumpla que:
#                 # file_line_string = '\n' cuando la línea de código .py está vacía.
#                 # file_line_string = '' cuando la última línea de código .py está vacía, 
#                 #   y cuando se alcanza el EOF: End of File (Fin del archivo .py).

#                 # Para evitar escribir un caracter '\n' innecesario al final, si la última detección de una instrucción de 
#                 #   lectura de Python se hizo en una línea diferente a la última, haga lo siguiente:
#                 # Asuma que ninguna línea leída debe tener un caracter '\n' al final:
#                 #   Mire si el último caracter de una línea es '\n' o '' (No hay un '\n')
#                 #   Si es '\n', entonces escriba el resto de la línea, y almacene este caracter para ser agregado si se encuentra
#                 #       otra instrucción de lectura de datos después. Si no se encuentra otra instrucción después, 
#                 #       el caracter '\n' no se usa, y de esta forma, se desecha eficazmente.
#                 #   Si no hay un '\n' al final, simplemente escriba toda la línea.

#                 line_to_write = ''
#                 if (append_newline_before_textline):
#                     line_to_write += '\n'
#                     append_newline_before_textline = False

#                 # DESESTIMAR ESTO:
#                 # Escriba, en el archivo resultante, en una línea, el número de línea en el que se detectó al menos una
#                 #   instrucción de lectura de Python, y cuántas detecciones se hicieron en una misma línea:
#                 # line_to_write += 'Línea ' + str(line_number_count) + ' | Lecturas: '\
#                 #     + str(count_python_input_keywords_in_textline(file_line_string)) + ' -->\t'

#                 # Escriba, en el archivo resultante, el contenido de la línea en el que se detectó al menos una 
#                 #   instrucción de lectura de Python:
#                 if (textline_has_newline_ending(file_line_string)):
#                     line_to_write += file_line_string[0:len(file_line_string)-1:1]
#                     # file_to_write.write(line_to_write) # Escribe toda la línea, excepto el último caracter.
#                     append_newline_before_textline = True
#                 else:
#                     line_to_write += file_line_string
#                     # file_to_write.write(line_to_write)

#                 # Ya se tiene procesado el contenido de la línea leída del archivo en line_to_write

#                 # DESESTIMAR ESTO: Ahora se debe recorrer caracter por caracter, como se describió en el paso 1 del plan:

#                 # Ahora, ya se puede ingresar cada caracter de la línea al buscador para que la identificación de instrucciones de lectura
#                 #   de Python se vaya realizando.
                
#                 # print(line_to_write)

#                 if (token_search == None): # Si no se ha hecho ninguna búsqueda de instrucciones de lectura de Python...
#                     token_search = PyInputInstrSearch() # Comience a hacer una nueva búsqueda...
#                     # print(type(token_search) == PyInputInstrSearch)
                

                    



#                 # for character in line_to_write:
#                 #     if (is_python_whitespace(character)):
#                 #         # Si se encuentra un espacio en blanco, entonces puede que ya exista un token completo, o que aún
#                 #         #   no se haya encontrado ni un caracter diferente a un espacio en blanco.
#                 #         if (token == None): # No se había encontrado ni un solo caracter diferente de espacios hasta ahora.
#                 #             # Note que ningún token en construcción tiene una cadena vacía, sino un valor None (Es semejante a un null en Java;
#                 #             #   significa que carece de valor alguno, semánticamente hablando).
#                 #             # No hay un token completo. No haga nada.
#                 #             pass
#                 #         else: # En este momento, ya se cuenta con un token completo definido por los últimos caracteres diferentes a espacios
#                 #             #   en blanco hallados anteriormente, excepto este espacio en blanco, por supuesto.                                
#                 #             complete_token = token # Token completo
#                 #             # ¿Qué es este token? ¿Un identificador, una palabra clave input, u otra cosa?
#                 #             if (token == INPUT_KEYWORD):
#                 #                 # Es una palabra clave input.
#                 #                 print('Es un input.')
#                 #             elif (is_python_identifier(token)):
#                 #                 # Es un identificador (Es un nombre de variable)
#                 #                 print('Es un identificador.')
#                 #             else:
#                 #                 # No es ni una palabra clave input ni un identificador
#                 #                 print('Ni es un input, ni un identificador.')

#                 #             token = None # Asigne None al token para prepararlo para construir otros tokens (si los hay).
#                 #     else:
#                 #         # ¿Es este token un identificador, una palabra clave input, u otra cosa?
#                 #         # Pero no se puede saber el contenido completo de un token hasta procesar todos los caracteres.
#                 #         if (token == None): # No se había encontrado ni un solo caracter diferente de espacios hasta ahora.
#                 #             token = character # Comience a armar un token.
#                 #         else:
#                 #             token += character # Siga armando el token encontrado anteriormente.

                        
                            



#     return input_instructions

def get_main_file_from_python_exercise_variant_files_dir(python_exercise_variant_files_dir):
    # https://docs.python.org/3/library/os.html#os.walk
    files = []
    # Haciendo un recorrido top-down desde la raíz:
    root_path = True
    for dir_path, dir_names, file_names in os.walk(python_exercise_variant_files_dir):
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

def get_subroutine_dirs_list(python_exercise_variant_files_dir):
    # https://docs.python.org/3/library/os.html#os.walk
    dir_routes = []
    # Haciendo un recorrido top-down desde la raíz:
    for dir_path, dir_names, file_names in os.walk(python_exercise_variant_files_dir): # python_exercise_variant_files_dir_path
        # dirpath is a string, the path to the directory.
        # dirnames is a list of the names of the subdirectories in dirpath (including symlinks to directories, and excluding '.' and '..').
        # filenames is a list of the names of the non-directory files in dirpath. 
        #   Note that the names in the lists contain no path components.

        for dir_name_found in dir_names:
            dir_name = str(dir_name_found)
            # print(dir_name[0:1:1])
            # print(dir_name[1 : len(dir_name) : 1])
            if (dir_name[0:1:1] == SUB_KEYWORD and dir_name[1:len(dir_name):1].isnumeric()):
                dir_routes.append(os.path.join(dir_path, dir_name))
    return dir_routes

def get_variant_files_from_subroutine_dir(subroutine_dir):
    # ADVERTENCIA: LOS ARCHIVOS DE VARIANTES A ENCONTRAR SON ARCHIVOS DE EXTENSIÓN .PY
    # https://docs.python.org/3/library/os.html#os.walk
    files = []
    # Haciendo un recorrido top-down desde la raíz:
    root_path = True
    for dir_path, dir_names, file_names in os.walk(subroutine_dir):
        # dirpath is a string, the path to the directory.
        # dirnames is a list of the names of the subdirectories in dirpath (including symlinks to directories, and excluding '.' and '..').
        # filenames is a list of the names of the non-directory files in dirpath. 
        #   Note that the names in the lists contain no path components.
        # Para tomar sólo los resultados del directorio raíz, y no de los subdirectorios:
        if (root_path == True):
            for file_name_found in file_names:
                file_name = str(file_name_found)
                # print(file_name[0:1:1])
                # print(file_name[1 : len(file_name)-3 : 1])
                # print(file_name[len(file_name)-3 : len(file_name)+1 : 1])
                if (file_name[0:1:1] == VARIANT_KEYWORD and file_name[1:len(file_name)-3:1].isnumeric() and file_name[len(file_name)-3:len(file_name)+1:1] == PY_FILE_EXTENSION):
                    files.append(os.path.join(dir_path, file_name))
            root_path = False
        else:
            return files
    return files

def get_variant_files_from_subroutine_dirs(subroutine_dirs_list):
    # Cada subrutina puede tener un número variable de variantes.
    # Se debe encontrar el directorio de cada subrutina, y para cada uno de esos directorios, encontrar los archivos en 
    #   esos directorios cuyo nombre sea: v<numero>, donde <numero> es el número asociado a una variante de la subrutina.
    # Se debe obtener una lista de archivos de variantes que hay por subrutina.
    subroutine_variant_files = []

    # El número de subrutinas se puede obtener fácilmente mediante el número de elementos de subroutine_dirs_list
    subroutine_count = len(subroutine_dirs_list)

    for s in range(1, subroutine_count + 1, 1):
        # Revisar la subrutina s
        # Encontrar la ruta de la subrutina s
        subroutine_dir = subroutine_dirs_list[s - 1]
        # print(s)
        # print(subroutine_dir_path)

        # Encontrar los archivos de variantes disponibles para la subrutina
        if len(subroutine_variant_files) == 0:
            subroutine_variant_files = get_variant_files_from_subroutine_dir(subroutine_dir)
        else:
            files = get_variant_files_from_subroutine_dir(subroutine_dir)
            for file in files:
                subroutine_variant_files.append(file)
        # print(subroutine_variant_files)

    return subroutine_variant_files

def get_python_files_from_directory(python_exercise_variant_files_dir):
    # Encontrar los archivos escritos con Python que cumplan las siguientes características:
    # 1) Un solo archivo de Python llamado main.py que se encuentre en el directorio dado.
    # 2) En los subdirectorios con nombre s1, s2, ..., sN (N = número de subrutinas) del directorio dado,
    #   los archivos de Python llamados v1, v2, ..., vN (V = número de variantes por subrutina)
    files_found_list = []
    
    # main_dir = python_exercise_variant_files_dir

    main_file = get_main_file_from_python_exercise_variant_files_dir(python_exercise_variant_files_dir) # ESTO FUNCIONA
    if (len(main_file) == 0):
        return files_found_list
    files_found_list.append(main_file[0])

    subroutine_dirs_list = get_subroutine_dirs_list(python_exercise_variant_files_dir) # ESTO FUNCIONA
    subroutine_variant_files = get_variant_files_from_subroutine_dirs(subroutine_dirs_list) # ESTO FUNCIONA
    if (len(subroutine_variant_files) == 0):
        return files_found_list
    files_found_list.extend(subroutine_variant_files)

    return files_found_list

def get_python_instructions_from_files(files):
    python_input_instructions_per_file_list = []
    for file in files:
        file_python_input_instructions = get_python_input_instructions_from_file(file)
        python_input_instructions_per_file_list.append(file_python_input_instructions)
    return python_input_instructions_per_file_list

# Programa principal
# read_and_print_contents_of_python_file(choose_python_file_location())
# read_and_print_lines_of_python_file_where_input_keyword_is_present(choose_python_file_location())
# print_python_file_lines_with_input_keyword_to_results_file_from(choose_python_file_location())
# print(get_python_input_instructions_from_file(choose_python_file_location()))

# Función para encontrar y almacenar las instrucciones de lectura de un archivo de Python.
# input_instructions = get_python_input_instructions_from_file(choose_python_file_location())
# # print(input_instructions)
# if len(input_instructions) == 0:
#     print('No se encontraron instrucciones de lectura de Python en el archivo.')
# for ii in input_instructions:
#     ii.print_json_representation()

# DESESTIMAR ESTO:
# Plan A: => POSPONER POR AHORA.
# 1) Considerar las líneas lógicas de Python como una sola línea para revisión, juntando las líneas separadas por el caracter \
#   hasta que se detecte un caracter de nueva línea o un EOF ('\n' o '')
# Asimismo, mostrar el inicio y fin de la línea lógica de Python en el archivo de resultado, en vez de sólo la línea en donde aparece
#   el token 'input'. => POSPONER POR AHORA.

# 2) Desestimar instrucciones de lectura que hagan parte de un comentario, o de un literal de String
# Comentario de una sola línea: Los que están después del símbolo #
# Comentario multilínea que comienza y termina con ''' (Esto también es un literal String)
# Comentario multilínea que comienza y termina con """ (Esto también es un literal String)
# Strings que comienzan y terminan con '
# Strings que comienzan y terminan con "  => POSPONER POR AHORA.

# 3) Individualizar instrucciones separadas por un punto y coma en una sola línea:
# No, esto no es necesario.

# Plan B: Simplificar el contenido del archivo a analizar en otro archivo que no contenga elementos irrelevantes, antes de
#   realizar el análisis de cuántas instrucciones de lectura de Python hay en el archivo. => DESESTIMAR POR AHORA.
# El problema de este plan es que después puede ser demasiado complejo encontrar la línea de código de la instrucción.

# Plan C: Hacer pruebas con las variantes usadas en assembler.py => HACER ESTO.