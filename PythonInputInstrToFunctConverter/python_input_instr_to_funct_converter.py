import shutil
import python_input_instr_identifier as pyininid

## Opciones para controlar el flujo del programa
# Cerrar el programa (str, int, float, bool)
EXIT_PROGRAM_OPTION = 'E'
# Visualizar de nuevo los datos de la siguiente instrucción a procesar (str, int, float, bool)
REVIEW_INSTRUCTION_DATA = 'R'
# Regresar al menú anterior - En cuanto esto sea posible (str, int, float, bool)
BACK_OPTION = 'B'
## Opciones que conllevan a la obtención de una función generadora: USAR
# Función generadora de un valor fijo (str, int, float)
FIXED_OPTION = '1'
# Función generadora de un valor aleatorio mediante lista (str, int, float)
RANDOM_BY_LIST_OPTION = '2'
# Función generadora de un valor aleatorio mediante intervalo cerrado (int, float)
RANDOM_BY_CLOSED_INTERVAL_OPTION = '3'
# Función generadora de un valor aleatorio mediante rango (int)
RANDOM_BY_RANGE_OPTION = '4'
# Función generadora de un valor aleatorio mediante intervalo cerrado con precisión fija (float)
RANDOM_BY_CLOSED_INTERVAL_AND_PRECISION_OPTION = '4'
# Función generadora de un valor fijo diferente a partir de una secuencia de valores a retornar en formato de 
#   lista (int, float)
NUMBER_FIXED_SEQUENCE_OPTION = '5'
# Función generadora compleja (int, float)
NUMBER_COMPLEX_OPTION = '6'

## Sólo para instrucciones de lectura que obtienen valores booleanos:
# Función generadora de un valor fijo: Falso (bool)
FIXED_FALSE_OPTION = '1'
# Función generadora de un valor fijo: Verdadero (bool)
FIXED_TRUE_OPTION = '2'
# Función generadora de un valor aleatorio de tipo booleano (bool)
RANDOM_STRICT_BOOL_OPTION = '3'
# Función generadora de un valor fijo diferente a partir de una secuencia de valores a retornar en formato de 
#   lista (bool)
BOOL_FIXED_SEQUENCE_OPTION = '4'
# Función generadora compleja (bool)
BOOL_COMPLEX_OPTION = '5'

## Sólo para instrucciones de lectura que obtienen valores de tipo str:
# Función generadora de un valor fijo diferente a partir de una secuencia de valores a retornar en formato de 
#   lista (str)
STR_FIXED_SEQUENCE_OPTION = '3'
# Función generadora compleja (bool)
STR_COMPLEX_OPTION = '4'

## Tipos de reemplazo
FIXED_GEN_FUN = '1'
RANDOM_BY_LIST_GEN_FUN = '2'
RANDOM_BY_CLOSED_INTERVAL_GEN_FUN = '3'

FIXED_FALSE_GEN_FUN = '4'
FIXED_TRUE_GEN_FUN = '5'
RANDOM_STRICT_BOOL_GEN_FUN = '6'

RANDOM_INT_BY_RANGE_GEN_FUN = '7'

RANDOM_FLOAT_BY_CLOSED_INTERVAL_AND_PRECISION_GEN_FUN = '8'

FIXED_SEQUENCE_GEN_FUN = '9'
COMPLEX_GEN_FUN = '10'

# Opciones específicas para el menú de confirmación de funciones generadoras por cada archivo:
ACCEPT_OPTION = 'A'
REJECT_OPTION = 'R'
REVIEW_GEN_FUN_CONFIG = 'V'

#### Estas rutas deberían poder ser configuradas por el usuario
# Directorio de archivos cuyas instrucciones de lectura son reemplazadas
# CONVERTED_FILES_DIR = 'C:\\Users\\leand\\Desktop\\Experimentos en Python\\Uso del generador automático de ejercicios\\PythonInputInstrToFunctConverter\\converted_files'
CONVERTED_FILES_DIR = 'C:\\Users\\leand\\Documents\\Python3Projects\\GeneradorEjercicios\\PythonInputInstrToFunctConverter\\converted_files'
# Módulo de funciones generadoras de datos
# INPUT_DATA_GENERATORS_MODULE_FILE = 'C:/Users/leand/Desktop/Experimentos en Python/Uso del generador automático de ejercicios/PythonInputInstrToFunctConverter/input_data_generators.py'
INPUT_DATA_GENERATORS_MODULE_FILE = 'C:/Users/leand/Documents/Python3Projects/GeneradorEjercicios/PythonInputInstrToFunctConverter/input_data_generators.py'

# GENERADORES DE MENÚS PARA ELEGIR FUNCIONES GENERADORAS
########################################################

# FUNCIONES GENERADORAS: VALORES FIJOS (ESTA LISTA NO ESTÁ ACTUALIZADA)
# ------------------------------------
# fixed_str_data_gen(value: str)
# fixed_int_data_gen(value: int)
# fixed_float_data_gen(value: float)
# fixed_true_data_gen()
# fixed_false_data_gen()

# FUNCIONES GENERADORAS: VALORES ALEATORIOS (ESTA LISTA NO ESTÁ ACTUALIZADA)
# -----------------------------------------
# random_str_data_from_list_gen(possible_input_values_list: list)
# random_int_data_from_list_gen(possible_input_values_list: list)
# random_float_data_from_list_gen(possible_input_values_list: list)
# random_strict_bool_data_from_list_gen(possible_input_values_list: list)

# random_alphanumeric_str_of_fixed_length_data_gen(length: int, case_option: int, include_spanish_characters: bool)
# random_alphanumeric_str_of_random_length_data_gen(min_length: int, max_length: int, case_option: int, 
#     include_spanish_characters: bool)
# random_alphabetic_str_of_fixed_length_data_gen(length: int, case_option: int, include_spanish_characters: bool)
# random_alphabetic_str_of_random_length_data_gen(min_length: int, max_length: int, 
#     case_option: int, include_spanish_characters: bool)
# random_numeric_str_of_fixed_length_data_gen(length: int)
# random_numeric_str_of_random_length_data_gen(min_length: int, max_length: int)

# random_int_from_closed_interval_data_gen(min_value: int, max_value: int)
# random_int_from_closed_intervals_data_gen(interval_tuples_list: list)
# random_int_from_range_data_gen(data_range: range)
# random_int_from_ranges_data_gen(data_ranges_list: list)

# random_float_from_closed_interval_data_gen(min_value: float, max_value: float)
# random_float_from_closed_interval_with_fixed_precision_data_gen(min_value: float, max_value: float, precision: int)
# random_float_from_closed_interval_with_random_precision_data_gen(min_value: float, max_value: float, 
#     min_precision: int, max_precision: int)
# random_float_from_closed_intervals_data_gen(interval_tuples_list: list)
# random_float_from_closed_intervals_with_fixed_precision_data_gen(interval_tuples_list: list, precision: int)
# random_float_from_closed_intervals_with_random_precision_data_gen(interval_tuples_list: list, 
#     min_precision: int, max_precision: int)

# random_strict_bool_data_gen()

# ESTO YA NO ES NECESARIO: DEJAR ESTA FUNCIÓN COMENTADA:
# def get_test_cases_from_user(): # ESTO FUNCIONA
#     num_test_cases = None
#     while (num_test_cases == None):
#         try:
#             user_option = input('¿Cuántos casos de prueba quiere crear? (Para salir de este programa, escriba "' + EXIT_PROGRAM_OPTION + '"): ')
#             if user_option == EXIT_PROGRAM_OPTION:
#                 pyininid.sys.exit()
#             num = int(user_option)
#             if num < 1:
#                 print('Se debe ingresar, por lo menos, un caso de prueba. Por favor, ingrese otro valor.')
#             else:
#                 return num
#         except ValueError:
#             print('No se ingresó un número de casos de prueba. '
#             + 'Por favor, ingrese otro valor.')

def show_instruction_data_message(python_input_instruction): # ESTO FUNCIONA
    print('----------------')
    print('Archivo', current_short_file_name)
    print(python_input_instruction.get_input_line(), ':', python_input_instruction.get_string_representation())
    print('----------------')
    print('Esta es la instrucción de lectura que está en la línea ', python_input_instruction.get_input_line(), ' del archivo ',
    current_short_file_name, ', mediante la cual se obtiene un valor de tipo ', python_input_instruction.get_input_type(), ', y es asignada a la variable ',
    python_input_instruction.get_variable_name(), '. ¿Con qué función generadora quiere reemplazar esta instrucción de lectura? ', sep='')
    print('----------------------------------------------------------------------------------------------------------------')

def get_replacement_type_from_user(python_input_instruction): # ESTO FUNCIONA
    show_instruction_data_message(python_input_instruction)

    value_type = python_input_instruction.get_input_type()
    valid_option_list = [EXIT_PROGRAM_OPTION, REVIEW_INSTRUCTION_DATA]
    if value_type == pyininid.TYPE_BOOL_KEYWORD:
        valid_option_list = [EXIT_PROGRAM_OPTION, REVIEW_INSTRUCTION_DATA, FIXED_FALSE_OPTION, FIXED_TRUE_OPTION, 
                             RANDOM_STRICT_BOOL_OPTION, BOOL_FIXED_SEQUENCE_OPTION]
        # valid_option_list = [EXIT_PROGRAM_OPTION, REVIEW_INSTRUCTION_DATA, FIXED_FALSE_OPTION, FIXED_TRUE_OPTION, 
        #                      RANDOM_STRICT_BOOL_OPTION, BOOL_FIXED_SEQUENCE_OPTION, BOOL_COMPLEX_OPTION]
    elif value_type == pyininid.TYPE_STR_KEYWORD:
        valid_option_list = [EXIT_PROGRAM_OPTION, REVIEW_INSTRUCTION_DATA, FIXED_OPTION, RANDOM_BY_LIST_OPTION,
                             STR_FIXED_SEQUENCE_OPTION]
        # valid_option_list = [EXIT_PROGRAM_OPTION, REVIEW_INSTRUCTION_DATA, FIXED_OPTION, RANDOM_BY_LIST_OPTION,
        #                      STR_FIXED_SEQUENCE_OPTION, STR_COMPLEX_OPTION]
    elif value_type == pyininid.TYPE_INT_KEYWORD:
        valid_option_list = [EXIT_PROGRAM_OPTION, REVIEW_INSTRUCTION_DATA, FIXED_OPTION, RANDOM_BY_LIST_OPTION, 
                             RANDOM_BY_CLOSED_INTERVAL_OPTION, RANDOM_BY_RANGE_OPTION, NUMBER_FIXED_SEQUENCE_OPTION]
        # valid_option_list = [EXIT_PROGRAM_OPTION, REVIEW_INSTRUCTION_DATA, FIXED_OPTION, RANDOM_BY_LIST_OPTION, 
        #                      RANDOM_BY_CLOSED_INTERVAL_OPTION, RANDOM_BY_RANGE_OPTION, NUMBER_FIXED_SEQUENCE_OPTION,
        #                      NUMBER_COMPLEX_OPTION]
    elif value_type == pyininid.TYPE_FLOAT_KEYWORD:
        valid_option_list = [EXIT_PROGRAM_OPTION, REVIEW_INSTRUCTION_DATA, FIXED_OPTION, RANDOM_BY_LIST_OPTION, 
                            RANDOM_BY_CLOSED_INTERVAL_OPTION, RANDOM_BY_CLOSED_INTERVAL_AND_PRECISION_OPTION,
                            NUMBER_FIXED_SEQUENCE_OPTION]
        # valid_option_list = [EXIT_PROGRAM_OPTION, REVIEW_INSTRUCTION_DATA, FIXED_OPTION, RANDOM_BY_LIST_OPTION, 
        #                     RANDOM_BY_CLOSED_INTERVAL_OPTION, RANDOM_BY_CLOSED_INTERVAL_AND_PRECISION_OPTION,
        #                     NUMBER_FIXED_SEQUENCE_OPTION, NUMBER_COMPLEX_OPTION]

    user_option = None
    while (user_option not in valid_option_list or user_option == REVIEW_INSTRUCTION_DATA):
        if value_type == pyininid.TYPE_BOOL_KEYWORD:
            print('1) Con una que genera un valor False para cualquier ejecución de la instrucción de lectura.')
            print('2) Con una que genera un valor True para cualquier ejecución de la instrucción de lectura.')
            print('3) Con una que genera un valor aleatorio (True o False) para cualquier ejecución de la instrucción de lectura.')
            print('4) Con una que genera un valor fijo (True o False) a partir de una secuencia de valores dada en una lista '
                  + 'que se sigue considerando en múltiples ejecuciones de la instrucción de lectura en un mismo programa.')
            # print('5) Con una función generadora compleja que usa otras funciones generadoras simples para generar un valor '
            #       + '(True o False) a partir del orden de ejecución de estas funciones, y el número de veces que se ejecutan '
            #       + 'estas.')
            print('E) Salir de este programa')
            print('R) Volver a ver la información de la instrucción a procesar')
            # print('Escriba el número o letra mayúscula de la opción y presione ENTER >> ')
            print('Escriba el número o letra mayúscula de la opción y presione ENTER')
            # user_option = input('Escriba el número o letra mayúscula de la opción y presione ENTER >> ')
            user_option = input('>> ')
            if user_option not in valid_option_list:
                print('No se ingresó una opción válida. Por favor, ingrese otro valor.')
            elif user_option == REVIEW_INSTRUCTION_DATA:
                show_instruction_data_message(python_input_instruction)

        elif value_type == pyininid.TYPE_STR_KEYWORD:
            print('1) Con una que genera un valor fijo de tipo str para cualquier ejecución de la instrucción de lectura.')
            print('2) Con una que genera un valor aleatorio de tipo str, elegido de una lista, para cualquier ejecución', 
                  'de la instrucción de lectura.')
            print('3) Con una que genera un valor fijo de tipo str a partir de una secuencia de valores dada en una lista '
                  + 'que se sigue considerando en múltiples ejecuciones de la instrucción de lectura en un mismo programa.')
            # print('4) Con una función generadora compleja que usa otras funciones generadoras simples para generar un valor '
            #       + 'de tipo str a partir del orden de ejecución de estas funciones, y el número de veces que se ejecutan '
            #       + 'estas.')
            print('E) Salir de este programa')
            print('R) Volver a ver la información de la instrucción a procesar')
            # print('Escriba el número o letra mayúscula de la opción y presione ENTER >> ')
            print('Escriba el número o letra mayúscula de la opción y presione ENTER')
            # user_option = input('Escriba el número o letra mayúscula de la opción y presione ENTER >> ')
            user_option = input('>> ')
            if user_option not in valid_option_list:
                print('No se ingresó una opción válida. Por favor, ingrese otro valor.')
            elif user_option == REVIEW_INSTRUCTION_DATA:
                show_instruction_data_message(python_input_instruction)

        elif value_type == pyininid.TYPE_INT_KEYWORD:
            print('1) Con una que genera un valor fijo de tipo int para cualquier ejecución de la instrucción de lectura.')
            print('2) Con una que genera un valor aleatorio de tipo int, elegido de una lista, para cualquier ejecución', 
                  'de la instrucción de lectura.')
            print('3) Con una que genera un valor aleatorio de tipo int, elegido de un intervalo cerrado, para cualquier ejecución', 
                  'de la instrucción de lectura.')
            print('4) Con una que genera un valor aleatorio de tipo int, elegido de un rango con paso, para cualquier ejecución', 
                  'de la instrucción de lectura.')
            print('5) Con una que genera un valor fijo de tipo int a partir de una secuencia de valores dada en una lista '
                  + 'que se sigue considerando en múltiples ejecuciones de la instrucción de lectura en un mismo programa.')
            # print('6) Con una función generadora compleja que usa otras funciones generadoras simples para generar un valor '
            #       + 'de tipo int a partir del orden de ejecución de estas funciones, y el número de veces que se ejecutan '
            #       + 'estas.')
            print('E) Salir de este programa')
            print('R) Volver a ver la información de la instrucción a procesar')
            # print('Escriba el número o letra mayúscula de la opción y presione ENTER >> ')
            print('Escriba el número o letra mayúscula de la opción y presione ENTER')
            # user_option = input('Escriba el número o letra mayúscula de la opción y presione ENTER >> ')
            user_option = input('>> ')
            if user_option not in valid_option_list:
                print('No se ingresó una opción válida. Por favor, ingrese otro valor.')
            elif user_option == REVIEW_INSTRUCTION_DATA:
                show_instruction_data_message(python_input_instruction)

        elif value_type == pyininid.TYPE_FLOAT_KEYWORD:
            print('1) Con una que genera un valor fijo de tipo float para cualquier ejecución de la instrucción de lectura.')
            print('2) Con una que genera un valor aleatorio de tipo float, elegido de una lista, para cualquier ejecución', 
                  'de la instrucción de lectura.')
            print('3) Con una que genera un valor aleatorio de tipo float, elegido de un intervalo cerrado, para cualquier ejecución', 
                  'de la instrucción de lectura.')
            print('4) Con una que genera un valor aleatorio de tipo float que tiene una precisión fija,',
                  'elegido de un intervalo cerrado, para cualquier ejecución de la instrucción de lectura.')
            print('5) Con una que genera un valor fijo de tipo float a partir de una secuencia de valores dada en una lista '
                  + 'que se sigue considerando en múltiples ejecuciones de la instrucción de lectura en un mismo programa.')
            # print('6) Con una función generadora compleja que usa otras funciones generadoras simples para generar un valor '
            #       + 'de tipo float a partir del orden de ejecución de estas funciones, y el número de veces que se ejecutan '
            #       + 'estas.')
            print('E) Salir de este programa')
            print('R) Volver a ver la información de la instrucción a procesar')
            # print('Escriba el número o letra mayúscula de la opción y presione ENTER >> ')
            print('Escriba el número o letra mayúscula de la opción y presione ENTER')
            # user_option = input('Escriba el número o letra mayúscula de la opción y presione ENTER >> ')
            user_option = input('>> ')
            if user_option not in valid_option_list:
                print('No se ingresó una opción válida. Por favor, ingrese otro valor.')
            elif user_option == REVIEW_INSTRUCTION_DATA:
                show_instruction_data_message(python_input_instruction)
        
    if user_option == EXIT_PROGRAM_OPTION:
        pyininid.sys.exit()
    else:
        if value_type == pyininid.TYPE_BOOL_KEYWORD:
            if user_option == FIXED_FALSE_OPTION:
                return FIXED_FALSE_GEN_FUN
            elif user_option == FIXED_TRUE_OPTION:
                return FIXED_TRUE_GEN_FUN
            elif user_option == RANDOM_STRICT_BOOL_OPTION:
                return RANDOM_STRICT_BOOL_GEN_FUN
            elif user_option == BOOL_FIXED_SEQUENCE_OPTION:
                return FIXED_SEQUENCE_GEN_FUN
            # elif user_option == BOOL_COMPLEX_OPTION:
            #     return COMPLEX_GEN_FUN
            
        if value_type == pyininid.TYPE_INT_KEYWORD:
            if user_option == RANDOM_BY_RANGE_OPTION:
                return RANDOM_INT_BY_RANGE_GEN_FUN
            elif user_option == NUMBER_FIXED_SEQUENCE_OPTION:
                return FIXED_SEQUENCE_GEN_FUN
            # elif user_option == NUMBER_COMPLEX_OPTION:
            #     return COMPLEX_GEN_FUN
            
        if value_type == pyininid.TYPE_FLOAT_KEYWORD:
            if user_option == RANDOM_BY_CLOSED_INTERVAL_AND_PRECISION_OPTION:
                return RANDOM_FLOAT_BY_CLOSED_INTERVAL_AND_PRECISION_GEN_FUN
            elif user_option == NUMBER_FIXED_SEQUENCE_OPTION:
                return FIXED_SEQUENCE_GEN_FUN
            # elif user_option == NUMBER_COMPLEX_OPTION:
            #     return COMPLEX_GEN_FUN
            
        if value_type == pyininid.TYPE_STR_KEYWORD:
            if user_option == STR_FIXED_SEQUENCE_OPTION:
                return FIXED_SEQUENCE_GEN_FUN
            # elif user_option == STR_COMPLEX_OPTION:
            #     return COMPLEX_GEN_FUN

        # Casos restantes
        if user_option == FIXED_OPTION:
            return FIXED_GEN_FUN
        elif user_option == RANDOM_BY_LIST_OPTION:
            return RANDOM_BY_LIST_GEN_FUN
        elif user_option == RANDOM_BY_CLOSED_INTERVAL_OPTION:
            return RANDOM_BY_CLOSED_INTERVAL_GEN_FUN

def get_fixed_value_generator_function_from_user(value_type): # ESTO FUNCIONA 
    # print()
    if value_type == pyininid.TYPE_STR_KEYWORD: # ESTO FUNCIONA
        print('Generar un valor fijo de tipo ' + pyininid.TYPE_STR_KEYWORD + ':')
        user_option = input('Por favor escriba la cadena de caracteres que reemplazará a la instrucción de lectura:\n>> ')
        return 'idg.fixed_str_data_gen(\'' + user_option + '\')'
    elif value_type == pyininid.TYPE_INT_KEYWORD: # ESTO FUNCIONA
        print('Generar un valor fijo de tipo ' + pyininid.TYPE_INT_KEYWORD + ':')
        user_option = None
        while (user_option == None):
            try:
                user_option = int(input('Por favor escriba el número entero que reemplazará a la instrucción de lectura:\n>> '))
                return 'idg.fixed_int_data_gen(' + str(user_option) + ')'
            except ValueError:
                print('No se ingresó un número entero. Por favor, inténtelo otra vez.')
    elif value_type == pyininid.TYPE_FLOAT_KEYWORD: # ESTO FUNCIONA
        print('Generar un valor fijo de tipo ' + pyininid.TYPE_FLOAT_KEYWORD + ':')
        user_option = None
        while (user_option == None):
            try:
                user_option = float(input('Por favor escriba el número real (punto flotante) que reemplazará a la instrucción de lectura:\n>> '))
                return 'idg.fixed_float_data_gen(' + str(user_option) + ')'
            except ValueError:
                print('No se ingresó un número real (punto flotante). Por favor, inténtelo otra vez.')
    
def get_random_value_by_list_generator_function_from_user(value_type): # ESTO FUNCIONA
    if value_type == pyininid.TYPE_STR_KEYWORD: # ESTO FUNCIONA
        user_option = None
        while (user_option == None):
            print('Generar un valor aleatorio a partir de una lista de tipo ' + pyininid.TYPE_STR_KEYWORD + ':')
            user_option = input('Por favor escriba la lista de cadena de caracteres que reemplazará a la instrucción de lectura.' +
                    '\nPara ello debe usar la siguiente sintaxis: <valor1>,<valor2>,...,<valorN>' +
                    '\nTenga en cuenta que los valores de la lista están separados por comas, ' +
                    'y los espacios en blanco se considerarán como parte de cada cadena de caracteres o elementos de la lista.' +
                    '\nNOTA: Si no se ingresa nada, se sobreentenderá que la lista tiene un elemento: una cadena vacía ([\'\'])' +
                    '\n>> ')
            user_made_list = user_option.split(',')
            return 'idg.random_str_data_from_list_gen(' + str(user_made_list) + ')'

    elif value_type == pyininid.TYPE_INT_KEYWORD: # ESTO FUNCIONA
        user_option = None
        while (user_option == None):
            print('Generar un valor aleatorio a partir de una lista de tipo ' + pyininid.TYPE_INT_KEYWORD + ':')
            try:
                user_option = input('Por favor escriba la lista de números enteros que reemplazará a la instrucción de lectura.' +
                    '\nPara ello debe usar la siguiente sintaxis: <valor1>,<valor2>,...,<valorN>' +
                    '\nTenga en cuenta que los valores de la lista están separados por comas, ' +
                    'y los espacios en blanco al principio y al final de cada elemento de la lista serán eliminados.' +
                    '\n>> ')
                user_made_list = user_option.split(',')
                user_made_int_list = list(map(int, list(map(str.strip, user_made_list))))
                return 'idg.random_int_data_from_list_gen(' + str(user_made_int_list) + ')'
            except ValueError:
                user_option = None
                print('Todos los elementos de la lista ingresada deben ser de tipo ' + int.__name__ + '. Por favor, inténtelo de nuevo.')
    elif value_type == pyininid.TYPE_FLOAT_KEYWORD: # ESTO FUNCIONA        
        user_option = None
        while (user_option == None):
            print('Generar un valor aleatorio a partir de una lista de tipo ' + pyininid.TYPE_FLOAT_KEYWORD + ':')
            try:
                user_option = input('Por favor escriba la lista de números reales (valores punto flotante) que reemplazará ' + 
                    'a la instrucción de lectura.' +
                    '\nPara ello debe usar la siguiente sintaxis: <valor1>,<valor2>,...,<valorN>' +
                    '\nTenga en cuenta que los valores de la lista están separados por comas, ' +
                    'el punto decimal se establece con un punto, ' +
                    'y los espacios en blanco al principio y al final de cada elemento de la lista serán eliminados.' +
                    '\n>> ')
                user_made_list = user_option.split(',')
                user_made_float_list = list(map(float, list(map(str.strip, user_made_list))))
                return 'idg.random_float_data_from_list_gen(' + str(user_made_float_list) + ')'
            except ValueError:
                user_option = None
                print('Todos los elementos de la lista ingresada deben ser de tipo ' + float.__name__ + '. Por favor, inténtelo de nuevo.')

def get_random_value_by_closed_interval_generator_function_from_user(value_type): # ESTO FUNCIONA
    if value_type == pyininid.TYPE_INT_KEYWORD: # ESTO FUNCIONA 
        user_option = None
        while (user_option == None):
            print('Generar un valor aleatorio a partir de un intervalo cerrado de valores de tipo ' + pyininid.TYPE_INT_KEYWORD + ':')
            try:
                user_option = input('Por favor escriba el intervalo cerrado de posibles números enteros que ' + 
                        'reemplazará a la instrucción de lectura.' +
                        '\nPara ello debe usar la siguiente sintaxis:' + 
                        '\n<valorMenor> <valorMayor>' +
                        '\nTenga en cuenta que estos valores pueden estar separados por uno o más espacios en blanco, ' +
                        'y los espacios en blanco al principio y al final de estos valores serán eliminados.' +
                        '\n>> ')
                user_given_parameters = user_option.strip().split()
                if len(user_given_parameters) != 2:
                    user_option = None
                    print('Se deben ingresar exactamente dos números enteros como parámetros. Por favor, inténtelo de nuevo.')
                else:
                    user_given_int_parameters = list(map(int, user_given_parameters))
                    if user_given_int_parameters[0] > user_given_int_parameters[1]:
                        user_option = None
                        print('El primer número entero ingresado debe ser menor o igual al segundo número ingresado. ' + 
                              'Por favor, inténtelo de nuevo.')
                    else:
                        return 'idg.random_int_from_closed_interval_data_gen(' \
                            + str(user_given_int_parameters[0]) + ', ' + str(user_given_int_parameters[1]) + ')'
            except ValueError:
                user_option = None
                print('Todos los parámetros ingresados deben ser de tipo ' + int.__name__ + '. Por favor, inténtelo de nuevo.')
    elif value_type == pyininid.TYPE_FLOAT_KEYWORD: # ESTO FUNCIONA
        user_option = None
        while (user_option == None):
            print('Generar un valor aleatorio a partir de un intervalo cerrado de valores de tipo ' + pyininid.TYPE_FLOAT_KEYWORD + ':')
            try:
                user_option = input('Por favor escriba el intervalo cerrado de posibles números reales (valores punto flotante) que ' + 
                        'reemplazará a la instrucción de lectura.' +
                        '\nPara ello debe usar la siguiente sintaxis:' + 
                        '\n<valorMenor> <valorMayor>' +
                        '\nTenga en cuenta que estos valores pueden estar separados por uno o más espacios en blanco, ' +
                        'y los espacios en blanco al principio y al final de estos valores serán eliminados.' +
                        '\n>> ')
                user_given_parameters = user_option.strip().split()
                if len(user_given_parameters) != 2:
                    user_option = None
                    print('Se deben ingresar exactamente dos números reales (valores punto flotante) como parámetros. ' + 
                          'Por favor, inténtelo de nuevo.')
                else:
                    user_given_float_parameters = list(map(float, user_given_parameters))
                    if user_given_float_parameters[0] > user_given_float_parameters[1]:
                        user_option = None
                        print('El primer número real ingresado debe ser menor o igual al segundo número ingresado. ' + 
                              'Por favor, inténtelo de nuevo.')
                    else:
                        return 'idg.random_float_from_closed_interval_data_gen(' \
                            + str(user_given_float_parameters[0]) + ', ' + str(user_given_float_parameters[1]) + ')'
            except ValueError:
                user_option = None
                print('Todos los parámetros ingresados deben ser de tipo ' + float.__name__ + '. Por favor, inténtelo de nuevo.')

def get_random_value_by_closed_interval_and_precision_generator_function_from_user(): # ESTO FUNCIONA
    user_option = None
    while (user_option == None):
        print('Generar un valor punto flotante aleatorio con una precisión fijada por el usuario, a partir de un intervalo cerrado' + 
              ' de valores de tipo ' + pyininid.TYPE_FLOAT_KEYWORD + ':')
        try:
            user_option = input('Por favor escriba el intervalo cerrado de posibles números reales (valores punto flotante) que ' + 
                    'reemplazará a la instrucción de lectura, seguido de la precisión a utilizar.' +
                    '\nPara ello debe usar la siguiente sintaxis:' + 
                    '\n<valorMenor (float)> <valorMayor (float)> <precisión (int)>' +
                    '\nTenga en cuenta que estos valores pueden estar separados por uno o más espacios en blanco, ' +
                    'y los espacios en blanco al principio y al final de estos valores serán eliminados.' +
                    '\n>> ')
            user_given_parameters = user_option.strip().split()
            if len(user_given_parameters) != 3:
                user_option = None
                print('Se deben ingresar exactamente tres números como parámetros: ' + 
                    'Los primeros dos parámetros deben ser de tipo ' + float.__name__ + ', mientras que el tercer parámetro ' + 
                    'debe ser de tipo ' + int.__name__ + '. Por favor, inténtelo de nuevo.')
            else:                
                user_given_float_parameters = list(map(float, user_given_parameters[0:2:1]))
                user_given_int_parameters = list(map(int, user_given_parameters[2:3:1]))
                if user_given_float_parameters[0] > user_given_float_parameters[1]:
                    user_option = None
                    print('El primer número real ingresado debe ser menor o igual al segundo número ingresado. ' + 
                            'Por favor, inténtelo de nuevo.')
                else:
                    return 'idg.random_float_from_closed_interval_with_fixed_precision_data_gen(' \
                        + str(user_given_float_parameters[0]) + ', ' + str(user_given_float_parameters[1]) \
                        + ', ' + str(user_given_int_parameters[0]) +')'
        except ValueError:
            user_option = None
            print('Los primeros dos parámetros deben ser de tipo ' + float.__name__ + ', mientras que el tercer parámetro ' + 
                  'debe ser de tipo ' + int.__name__ + '. Por favor, inténtelo de nuevo.')

def get_random_value_by_range_generator_function_from_user(value_type): # ESTO FUNCIONA
    if value_type == pyininid.TYPE_INT_KEYWORD: # ESTO FUNCIONA
        user_option = None
        while (user_option == None):
            print('Generar un valor aleatorio a partir de un rango de valores con paso, de tipo ' + pyininid.TYPE_INT_KEYWORD + ':')
            try:
                user_option = input('Por favor escriba el rango con paso de los posibles números enteros a escoger aleatoriamente que ' + 
                        'reemplazará a la instrucción de lectura.' +
                        '\nPara ello debe usar la siguiente sintaxis, considerando un recorrido de números posibles:' + 
                        '\n<valorInicioRecorrido (Inclusivo)> <valorFinRecorrido (Exclusivo)> <pasoDeRecorrido>' +
                        '\nTenga en cuenta que estos valores pueden estar separados por uno o más espacios en blanco, ' +
                        'y los espacios en blanco al principio y al final de estos valores serán eliminados.' +
                        '\nAdemás, considere que los valores solicitados funcionan de forma semejante a los parámetros de ' + 
                        'la función range(start, stop, step) de Python. Esto significa que el número de <valorFinRecorrido (Exclusivo)> ' +
                        'nunca será generado.' +
                        '\n>> ')
                user_given_parameters = user_option.strip().split()
                # print(user_given_parameters)
                if len(user_given_parameters) != 3:
                    user_option = None
                    print('Se deben ingresar exactamente tres números enteros como parámetros. Por favor, inténtelo de nuevo.')
                else:
                    user_given_int_parameters = list(map(int, user_given_parameters))
                    r = range(user_given_int_parameters[0], user_given_int_parameters[1], user_given_int_parameters[2])
                    l = list(r)
                    if len(l) < 1:
                        user_option = None
                        print('Con el rango ingresado se debe poder seleccionar, al menos, 1 número entero. ' + 
                              'Por favor, inténtelo de nuevo.')
                    else:
                        return 'idg.random_int_from_range_data_gen(range(' \
                            + str(user_given_int_parameters[0]) + ', ' + str(user_given_int_parameters[1]) + ', ' \
                            + str(user_given_int_parameters[2]) + '))'
            except ValueError:
                user_option = None
                print('Todos los parámetros ingresados deben ser de tipo ' + int.__name__ + '. Por favor, inténtelo de nuevo.')

def get_short_instruction_data(python_input_instruction):
    return str(python_input_instruction.get_input_line()) + ' : ' + python_input_instruction.get_string_representation()

def get_short_modified_instruction_data(python_input_instruction, gen_function):
    return str(python_input_instruction.get_variable_name()) + ' = ' + gen_function

# ESTA FUNCIÓN SIGUE SIENDO NECESARIA, PERO SU NOMBRE SERÁ CAMBIADO PORQUE YA NO SE CREARÁN CASOS DE PRUEBA
#   EN ESTE PROGRAMA:
# def show_test_case_chosen_generator_functions_for_file_data_message(gen_functions_list, 
#     python_input_instructions_list, current_short_file_name):
def show_chosen_generator_functions_for_file_data_message(gen_functions_list, 
    python_input_instructions_list, current_short_file_name):

    print()
    print('-- RESUMEN DE FUNCIONES GENERADORAS EN EL ARCHIVO --')
    print('Para reemplazar las instrucciones de lectura del archivo ', current_short_file_name, ', se han elegido ', 
          'las siguientes funciones generadoras:', sep='')
    print('----------------')
    print('Archivo', current_short_file_name)
    index = 0
    for python_input_instruction in python_input_instructions_list:
        print(get_short_instruction_data(python_input_instruction), '>>', 
              get_short_modified_instruction_data(python_input_instruction, gen_functions_list[index]))
        index += 1
    print('----------------')

def get_generator_function_choosing_confirmation_from_user(gen_functions_list, 
    python_input_instructions_list, current_short_file_name):

    # ESTA FUNCIÓN SIGUE SIENDO NECESARIA, PERO SU NOMBRE SERÁ CAMBIADO PORQUE YA NO SE CREARÁN CASOS DE PRUEBA
    #   EN ESTE PROGRAMA:
    # show_test_case_chosen_generator_functions_for_file_data_message(gen_functions_list, 
    #         python_input_instructions_list, current_short_file_name)
    show_chosen_generator_functions_for_file_data_message(gen_functions_list, 
    python_input_instructions_list, current_short_file_name)

    valid_options_list = [ACCEPT_OPTION, REJECT_OPTION, EXIT_PROGRAM_OPTION, REVIEW_GEN_FUN_CONFIG]

    user_option = None
    while (user_option not in valid_options_list or user_option == REVIEW_GEN_FUN_CONFIG):
        print('Con base en lo anterior, ¿acepta o rechaza la configuración anterior de funciones generadoras para reemplazar', 
            'las instrucciones de lectura del archivo?')
        print('(Después de este paso, NO se podrán realizar cambios a esta configuración durante la ejecución de este programa.)')
        print('A) ACEPTAR')
        print('R) RECHAZAR')
        print('E) Salir de este programa')
        print('V) Volver a ver la información de la configuración de funciones generadoras para el archivo')
        # print('Escriba el número o letra mayúscula de la opción y presione ENTER >> ')
        print('Escriba el número o letra mayúscula de la opción y presione ENTER')
        # user_option = input('Escriba el número o letra mayúscula de la opción y presione ENTER >> ')
        user_option = input('>> ')
        if user_option not in valid_options_list:
            print('No se ingresó una opción válida. Por favor, ingrese otro valor.')
        elif user_option == REVIEW_GEN_FUN_CONFIG:
            # ESTA FUNCIÓN SIGUE SIENDO NECESARIA, PERO SU NOMBRE SERÁ CAMBIADO PORQUE YA NO SE CREARÁN CASOS DE PRUEBA
            #   EN ESTE PROGRAMA:
            # show_test_case_chosen_generator_functions_for_file_data_message(gen_functions_list, 
            # python_input_instructions_list, current_short_file_name)
            show_chosen_generator_functions_for_file_data_message(gen_functions_list, 
            python_input_instructions_list, current_short_file_name)
        
    if user_option == EXIT_PROGRAM_OPTION:
        pyininid.sys.exit()
    else:
        if user_option == ACCEPT_OPTION:
            return True
        elif user_option == REJECT_OPTION:
            return False

# ESTO YA NO ES NECESARIO: DEJAR ESTA FUNCIÓN COMENTADA:
# def get_test_cases_to_build_with_generator_function_set_from_user(gen_functions_list, 
#     python_input_instructions_list, current_short_file_name, remaining_test_cases, next_test_case, num_test_cases):

#     user_option = None
#     while True:
#         print()
#         print('Por favor indique cuántos casos de prueba quiere generar con las funciones generadoras de datos',
#               'que fueron definidas anteriormente (Mínimo: 1, Máximo:', str(remaining_test_cases) + ')')
#         print('Recuerde que el próximo caso de prueba a procesar para el archivo', current_short_file_name, 
#               'es el número', next_test_case, 'de los', num_test_cases, 'casos de prueba definidos para tal efecto.')
#         print('E) Salir de este programa')
#         print('V) Volver a ver la información de la configuración de funciones generadoras para el archivo')
#         print('Escriba el número o letra mayúscula de la opción y presione ENTER')
#         try:
#             user_option = input('>> ')
#             user_option = int(user_option)
#             if user_option < 1:
#                 print('El número de casos de prueba seleccionado es menor al mínimo. Este debe ser al menos 1. Por favor, corrija esto.')
#             elif user_option > remaining_test_cases:
#                 print('El número de casos de prueba seleccionado sobrepasa a los restantes por procesar en el archivo,',
#                       'según fue definido anteriormente. Este debe ser a lo sumo', str(remaining_test_cases) + 
#                       '. Por favor, corrija esto.')
#             else:
#                 return user_option
#         except ValueError:
#             if user_option == EXIT_PROGRAM_OPTION:
#                 pyininid.sys.exit()
#             elif user_option == REVIEW_GEN_FUN_CONFIG:
#                 show_chosen_generator_functions_for_file_data_message(gen_functions_list, 
#                 python_input_instructions_list, current_short_file_name)
#                 show_test_case_chosen_generator_functions_for_file_data_message(gen_functions_list, 
#                 python_input_instructions_list, current_short_file_name)
#             else:
#                 print('No se ingresó una opción válida ni un número entero. Por favor, inténtelo otra vez.')

def get_fixed_value_by_sequence_in_list_generator_function_from_user(value_type, python_instruction_number):
    if value_type == pyininid.TYPE_BOOL_KEYWORD:
        user_option = None
        while (user_option == None):
            print('Generar un valor fijo a partir de una secuencia de valores en una lista de tipo ' 
                  + pyininid.TYPE_BOOL_KEYWORD + ', que continúa a través de múltiples ejecuciones de la misma '
                  + 'instrucción de lectura del programa:')
            try:
                user_option = input('Por favor ingrese la lista de valores booleanos (True o False) que conformarán una ' +
                    'secuencia de valores que se generarán por cada llamado a la función generadora que se creará a continuación, ' +
                    'la cual reemplazará a la instrucción de lectura.' +
                    '\nPara ello debe usar la siguiente sintaxis: <valor1>,<valor2>,...,<valorN>' +
                    '\nTenga en cuenta que los valores de la lista están separados por comas, ' +
                    'y los espacios en blanco al principio y al final de cada elemento de la lista serán eliminados.' +
                    '\nAdemás, considere que la secuencia de valores ingresada se repite una vez la función generadora ' +
                    'a crear haya dado todos los valores de entrada de datos de la lista, desde el primero hasta el último.' +
                    '\n>> ')
                user_made_list = user_option.split(',')
                user_made_bool_list = list(map(bool, list(map(str.strip, user_made_list))))
                return 'idg.fixed_sequential_strict_bool_data_from_list_gen(' + str(user_made_bool_list) + \
                ', sequential_idg_list[' + str(python_instruction_number) + '])'
            except ValueError:
                user_option = None
                print('Todos los elementos de la lista ingresada deben ser de tipo ' + bool.__name__ + 
                    '. Por favor, inténtelo de nuevo.')
            
    elif value_type == pyininid.TYPE_STR_KEYWORD:
        user_option = None
        while (user_option == None):
            print('Generar un valor fijo a partir de una secuencia de valores en una lista de tipo ' 
                  + pyininid.TYPE_STR_KEYWORD + ', que continúa a través de múltiples ejecuciones de la misma '
                  + 'instrucción de lectura del programa:')
            user_option = input('Por favor ingrese la lista de cadenas de caracteres que conformarán una ' +
                'secuencia de valores que se generarán por cada llamado a la función generadora que se creará a continuación, ' +
                'la cual reemplazará a la instrucción de lectura.' +
                '\nPara ello debe usar la siguiente sintaxis: <valor1>,<valor2>,...,<valorN>' +
                '\nTenga en cuenta que los valores de la lista están separados por comas, ' +
                'y los espacios en blanco se considerarán como parte de cada cadena de caracteres o elemento de la lista.' +
                '\nNOTA: Si no se ingresa nada, se sobreentenderá que la lista tiene un elemento: una cadena vacía ([\'\'])' +
                '\nAdemás, considere que la secuencia de valores ingresada se repite una vez la función generadora ' +
                'a crear haya dado todos los valores de entrada de datos de la lista, desde el primero hasta el último.' +
                '\n>> ')            
            user_made_list = user_option.split(',')
            return 'idg.fixed_sequential_str_data_from_list_gen(' + str(user_made_list) + \
            ', sequential_idg_list[' + str(python_instruction_number) + '])'

    elif value_type == pyininid.TYPE_INT_KEYWORD:
        user_option = None
        while (user_option == None):
            print('Generar un valor fijo a partir de una secuencia de valores en una lista de tipo ' 
                  + pyininid.TYPE_INT_KEYWORD + ', que continúa a través de múltiples ejecuciones de la misma '
                  + 'instrucción de lectura del programa:')
            try:
                user_option = input('Por favor ingrese la lista de números enteros que conformarán una ' +
                'secuencia de valores que se generarán por cada llamado a la función generadora que se creará a continuación, ' +
                'la cual reemplazará a la instrucción de lectura.' +
                '\nPara ello debe usar la siguiente sintaxis: <valor1>,<valor2>,...,<valorN>' +
                '\nTenga en cuenta que los valores de la lista están separados por comas, ' +
                'y los espacios en blanco al principio y al final de cada elemento de la lista serán eliminados.' +
                '\nAdemás, considere que la secuencia de valores ingresada se repite una vez la función generadora ' +
                'a crear haya dado todos los valores de entrada de datos de la lista, desde el primero hasta el último.' +
                '\n>> ')
                user_made_list = user_option.split(',')
                user_made_int_list = list(map(int, list(map(str.strip, user_made_list))))                
                return 'idg.fixed_sequential_int_data_from_list_gen(' + str(user_made_int_list) + \
                ', sequential_idg_list[' + str(python_instruction_number) + '])'
            except ValueError:
                user_option = None
                print('Todos los elementos de la lista ingresada deben ser de tipo ' + int.__name__ + 
                      '. Por favor, inténtelo de nuevo.')
                
    elif value_type == pyininid.TYPE_FLOAT_KEYWORD:      
        user_option = None
        while (user_option == None):
            print('Generar un valor fijo a partir de una secuencia de valores en una lista de tipo ' 
                  + pyininid.TYPE_FLOAT_KEYWORD + ', que continúa a través de múltiples ejecuciones de la misma '
                  + 'instrucción de lectura del programa:')
            try:
                user_option = input('Por favor ingrese la lista de números reales (valores punto flotante) que conformarán una ' +
                'secuencia de valores que se generarán por cada llamado a la función generadora que se creará a continuación, ' +
                'la cual reemplazará a la instrucción de lectura.' +
                '\nPara ello debe usar la siguiente sintaxis: <valor1>,<valor2>,...,<valorN>' +
                '\nTenga en cuenta que los valores de la lista están separados por comas, ' +
                'el punto decimal se establece con un punto, ' +
                'y los espacios en blanco al principio y al final de cada elemento de la lista serán eliminados.' +
                '\nAdemás, considere que la secuencia de valores ingresada se repite una vez la función generadora ' +
                'a crear haya dado todos los valores de entrada de datos de la lista, desde el primero hasta el último.' +
                '\n>> ')
                user_made_list = user_option.split(',')
                user_made_float_list = list(map(float, list(map(str.strip, user_made_list))))
                return 'idg.fixed_sequential_float_data_from_list_gen(' + str(user_made_float_list) + \
                ', sequential_idg_list[' + str(python_instruction_number) + '])'
            except ValueError:
                user_option = None
                print('Todos los elementos de la lista ingresada deben ser de tipo ' + float.__name__ + 
                      '. Por favor, inténtelo de nuevo.')

# def get_value_by_complex_function_from_user(value_type, python_instruction_number):
#     pass


# PARA DIRECTORIOS DE VARIANTES DE EJERCICIOS: EN IMPLEMENTACIÓN
################################################################
# ESTO FUNCIONA:
################
python_exercise_variant_files_dir = pyininid.choose_python_exercise_variants_dir_location() # ESTO FUNCIONA
files = pyininid.get_python_files_from_directory(python_exercise_variant_files_dir)
python_input_instructions_per_file = pyininid.get_python_instructions_from_files(files)

# Validar que exista al menos un archivo que tenga una instrucción de lectura de Python
# (Considere, para los siguientes pasos, sólo los archivos que tengan, al menos, una instrucción de lectura de datos)
# CASO PARTICULAR:
# Si no existe un solo archivo que tenga una instrucción de lectura, entonces no tiene sentido hacer cambios en el código.
# (En ese caso, sólo se debería ensamblar el código base con el de sus variantes, y ejecutar cada programa ensamblado 
# una sola vez, para crear 1 solo caso de prueba por ensamblado que no tenga datos de entrada en su archivo .txt 
# de entrada pero que tenga la salida esperada del programa en su archivo .txt de salida.)
discarded_files = []
file_indexes_without_python_input_instructions = []
file_index = 0

# Cuente las instrucciones de lectura que existen en todos los archivos detectados
python_input_instructions_count = 0

for python_input_instruction_list in python_input_instructions_per_file:
    if (len(python_input_instruction_list) == 0):
        file_indexes_without_python_input_instructions.append(file_index)
    else:
        python_input_instructions_count += len(python_input_instruction_list)
    file_index += 1

# Indique que el número máximo de funciones generadoras de valores diferentes por una secuencia de valores dada por lista
#   y el número máximo de funciones generadoras complejas es igual al número de instrucciones detectados en todos los
#   archivos.
max_sequential_idg_count = python_input_instructions_count
# max_complex_idg_count = python_input_instructions_count

if len(file_indexes_without_python_input_instructions) == len(python_input_instructions_per_file):
    # No existe, al menos, un archivo que contenga una instrucción de lectura de Python
    print('No existe, al menos, un archivo que contenga una instrucción de lectura de Python. Saliendo de la aplicación...')
    pyininid.sys.exit()
# Conservar sólo los archivos y listados de instrucciones relevantes para el resto del proceso
for index_with_index_to_remove in range(len(file_indexes_without_python_input_instructions) - 1, -1, -1):
    discarded_files.append(files[file_indexes_without_python_input_instructions[index_with_index_to_remove]])
    files.remove(files[file_indexes_without_python_input_instructions[index_with_index_to_remove]])
    python_input_instructions_per_file.remove(python_input_instructions_per_file
        [file_indexes_without_python_input_instructions[index_with_index_to_remove]])

short_file_names = []
for file in files:
    split_file_name_parts = file.split('\\')
    short_file_name = ''
    for name_part_index in range(1, len(split_file_name_parts), 1):
        short_file_name += '\\' + split_file_name_parts[name_part_index]
    short_file_names.append(short_file_name)

# YA NO SE CONSIDERARÁ LA CREACIÓN DE CASOS DE PRUEBA EN ESTE PROGRAMA: DEJAR COMENTADA LA SIGUIENTE LÍNEA:
# num_test_cases = get_test_cases_from_user()
################

# Esta variable controla si se debe inicializar el directorio principal de los resultados de este programa 
#   con sus subdirectorios, cuando se comienza a hacer la conversión de instrucciones de lectura a funciones generadoras
#   para un archivo.
is_new_result = True

file_index = 0

first_instruction_index = 0

for file in files:
    current_short_file_name = short_file_names[file_index]
    # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA: 
    #   DEJAR COMENTADAS LAS SIGUIENTES DOS LÍNEAS:
    # next_test_case = 1
    # remaining_test_cases = num_test_cases

    # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
    #   DEJAR COMENTADAS LAS SIGUIENTES DOS LÍNEAS:
    # test_case_interval_list = []    
    # gen_functions_per_test_case_interval_list = []

    instructions_count_in_file = 0
    
    # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
    # DEJAR COMENTADA LA SIGUIENTE LÍNEA, QUITANDO LA IDENTACIÓN EXTRA DEL CÓDIGO EN ESE CICLO, HASTA SU FIN.
    # while remaining_test_cases > 0:
    gen_function_confirmation = False        
    while gen_function_confirmation == False:
        print()
        print('El siguiente archivo en revisión para cambiar sus instrucciones de lectura por ',
              'funciones generadoras de datos es: ', current_short_file_name, sep='')

        python_input_instructions_list = python_input_instructions_per_file[file_index]

        instructions_count_in_file = len(python_input_instructions_list)

        gen_functions_list = []
        # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
        # DEJAR COMENTADA LA SIGUIENTE LÍNEA:
        # is_random_gen_function_chosen = False

        python_instruction_number = -1 + first_instruction_index
        for python_input_instruction in python_input_instructions_list:
            # Este número se cuenta desde el cero porque se va a usar en un índice de lista:
            python_instruction_number += 1
            
            value_replacement_type = get_replacement_type_from_user(python_input_instruction)

            gen_function_text = None
            value_type = python_input_instruction.get_input_type()

            if value_replacement_type == FIXED_GEN_FUN: # ESTO FUNCIONA
                gen_function_text = get_fixed_value_generator_function_from_user(value_type)
                # NOTA: Esta lógica puede parecer incorrecta, pero es una forma rápida de enmendar un error lógico, así:
                # Independientemente de que las funciones generadoras elegidas para transformar instrucciones de un 
                #   solo archivo generen un valor fijo, debería permitir al usuario crear múltiples casos de prueba, 
                #   porque es posible que en otro archivo se encuentre una instrucción de lectura que quiera ser 
                #   reemplazado por un valor aleatorio.
                # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
                # DEJAR COMENTADA LA SIGUIENTE LÍNEA:
                # is_random_gen_function_chosen = True
            elif value_replacement_type == FIXED_FALSE_GEN_FUN: # ESTO FUNCIONA
                gen_function_text = 'idg.fixed_false_data_gen()'
                # NOTA: Esta lógica puede parecer incorrecta, pero es una forma rápida de enmendar un error lógico, así:
                # Independientemente de que las funciones generadoras elegidas para transformar instrucciones de un 
                #   solo archivo generen un valor fijo, debería permitir al usuario crear múltiples casos de prueba, 
                #   porque es posible que en otro archivo se encuentre una instrucción de lectura que quiera ser 
                #   reemplazado por un valor aleatorio.
                # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
                # DEJAR COMENTADA LA SIGUIENTE LÍNEA:
                # is_random_gen_function_chosen = True
            elif value_replacement_type == FIXED_TRUE_GEN_FUN: # ESTO FUNCIONA
                gen_function_text = 'idg.fixed_true_data_gen()'
                # NOTA: Esta lógica puede parecer incorrecta, pero es una forma rápida de enmendar un error lógico, así:
                # Independientemente de que las funciones generadoras elegidas para transformar instrucciones de un 
                #   solo archivo generen un valor fijo, debería permitir al usuario crear múltiples casos de prueba, 
                #   porque es posible que en otro archivo se encuentre una instrucción de lectura que quiera ser 
                #   reemplazado por un valor aleatorio.
                # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
                # DEJAR COMENTADA LA SIGUIENTE LÍNEA:
                # is_random_gen_function_chosen = True
            elif value_replacement_type == RANDOM_BY_LIST_GEN_FUN: # ESTO FUNCIONA
                gen_function_text = get_random_value_by_list_generator_function_from_user(value_type)
                # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
                # DEJAR COMENTADA LA SIGUIENTE LÍNEA:
                # is_random_gen_function_chosen = True
            elif value_replacement_type == RANDOM_BY_CLOSED_INTERVAL_GEN_FUN: # ESTO FUNCIONA
                gen_function_text = get_random_value_by_closed_interval_generator_function_from_user(value_type)
                # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
                # DEJAR COMENTADA LA SIGUIENTE LÍNEA:
                # is_random_gen_function_chosen = True
            elif value_replacement_type == RANDOM_STRICT_BOOL_GEN_FUN: # ESTO FUNCIONA
                gen_function_text = 'idg.random_strict_bool_data_gen()'
                # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
                # DEJAR COMENTADA LA SIGUIENTE LÍNEA:
                # is_random_gen_function_chosen = True
            elif value_replacement_type == RANDOM_INT_BY_RANGE_GEN_FUN: # ESTO FUNCIONA
                gen_function_text = get_random_value_by_range_generator_function_from_user(value_type)
                # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
                # DEJAR COMENTADA LA SIGUIENTE LÍNEA:
                # is_random_gen_function_chosen = True
            elif value_replacement_type == RANDOM_FLOAT_BY_CLOSED_INTERVAL_AND_PRECISION_GEN_FUN: # ESTO FUNCIONA
                gen_function_text = get_random_value_by_closed_interval_and_precision_generator_function_from_user()
                # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
                # DEJAR COMENTADA LA SIGUIENTE LÍNEA:
                # is_random_gen_function_chosen = True
            elif value_replacement_type == FIXED_SEQUENCE_GEN_FUN:
                gen_function_text = get_fixed_value_by_sequence_in_list_generator_function_from_user(
                    value_type, python_instruction_number)
                # NOTA: Esta lógica puede parecer incorrecta, pero es una forma rápida de enmendar un error lógico, así:
                # Independientemente de que las funciones generadoras elegidas para transformar instrucciones de un 
                #   solo archivo generen un valor fijo, debería permitir al usuario crear múltiples casos de prueba, 
                #   porque es posible que en otro archivo se encuentre una instrucción de lectura que quiera ser 
                #   reemplazado por un valor aleatorio.
                # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
                # DEJAR COMENTADA LA SIGUIENTE LÍNEA:
                # is_random_gen_function_chosen = True
            # elif value_replacement_type == COMPLEX_GEN_FUN:
            #     gen_function_text = get_value_by_complex_function_from_user(value_type, python_instruction_number)
            #     # Esto se debe decidir al obtener la función generadora compleja: 
            #     # is_random_gen_function_chosen = True
            print(gen_function_text)
            gen_functions_list.append(gen_function_text)
        
        gen_function_confirmation = get_generator_function_choosing_confirmation_from_user(gen_functions_list, 
            python_input_instructions_list, current_short_file_name) # True or False

        if gen_function_confirmation == True:
            print('La configuración de funciones generadoras ha sido CONFIRMADA... Continuando el proceso...')
        elif gen_function_confirmation == False:
            print('La configuración de funciones generadoras ha sido RECHAZADA...', 
                    'Reiniciando el listado de funciones generadoras...')

    # gen_function_confirmation es igual a True
    # ESTE BLOQUE YA NO ES NECESARIO: DEJAR ESTO COMENTADO:
    # test_cases_to_generate = None
    # if is_random_gen_function_chosen == False:
    #     test_cases_to_generate = 1
    #     test_case_interval_list.append(next_test_case)
    # else:
    #     test_cases_to_generate = get_test_cases_to_build_with_generator_function_set_from_user(
    #         gen_functions_list, python_input_instructions_list, current_short_file_name, 
    #         remaining_test_cases, next_test_case, num_test_cases)
    #     interval = (next_test_case, next_test_case + test_cases_to_generate - 1)
    #     test_case_interval_list.append(interval)

    # QUITAR ESTA INSTRUCCIÓN: YA EXISTE UN LISTADO EN DONDE ESTÁN LAS FUNCIONES GENERADORAS DEL ARCHIVO,
    #   Y YA NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
    # gen_functions_per_test_case_interval_list.append(gen_functions_list)
                
    # ESTE BLOQUE YA NO ES NECESARIO: DEJAR ESTO COMENTADO:
    # remaining_test_cases -= test_cases_to_generate
    # next_test_case += test_cases_to_generate
    # FIN: while remaining_test_cases > 0:

    # DESESTIMAR LA SIGUIENTE AFIRMACIÓN:
    # Después de definir todos los casos de prueba para el archivo o código...
    first_instruction_index += instructions_count_in_file
    #### Realice el reemplazo de las instrucciones de lectura del archivo o código:

    # Valida si se debe inicializar o no el directorio y los subdirectorios de resultados:
    if is_new_result == True:
        # Si el directorio principal existe:
        if pyininid.os.path.exists(CONVERTED_FILES_DIR):
            # Elimina el directorio principal donde se albergarán los resultados (con sus archivos), y crea uno nuevo en su lugar.
            shutil.rmtree(CONVERTED_FILES_DIR)
            pyininid.os.makedirs(CONVERTED_FILES_DIR)
        else:
            # Crea el directorio principal donde se albergarán los resultados.
            pyininid.os.makedirs(CONVERTED_FILES_DIR)
        is_new_result = False # Con esto se asegura que el directorio principal no se elimine cuando se vaya a generar la conversión
        #   del siguiente archivo
    # Si is_new_result = False, no haga nada...

    # Obtención del nombre del archivo procesado sin la extensión .py, y del subdirectorio de variante de subrutina o subprograma,
    #   si no es un programa principal
    current_file_name = None
    current_subprogram_variant_dir = None
    current_relevant_file_route_parts = current_short_file_name.split('\\')
    if len(current_relevant_file_route_parts) == 2: # Es un archivo principal
        current_file_name = current_relevant_file_route_parts[1].split('.')[0]
    elif len(current_relevant_file_route_parts) == 3: # Es un archivo de variante de subrutina o subprograma
        current_subprogram_variant_dir = current_relevant_file_route_parts[1]
        current_file_name = current_relevant_file_route_parts[2].split('.')[0]
        # Creación de subdirectorio de variante
        if not pyininid.os.path.exists(CONVERTED_FILES_DIR + '\\' + current_subprogram_variant_dir):
            pyininid.os.makedirs(CONVERTED_FILES_DIR + '\\' + current_subprogram_variant_dir)
    else: # Error inesperado del sistema
        print('Hubo un error del sistema que no debió haber sucedido nunca. Saliendo de la aplicación...')
        pyininid.sys.exit()

    # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
    # DEJAR COMENTADA LA SIGUIENTE LÍNEA:
    # tc_interval_index = 0
    # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
    # DEJAR COMENTADA LA SIGUIENTE LÍNEA, QUITANDO LA IDENTACIÓN EXTRA DEL CÓDIGO EN ESE CICLO, HASTA SU FIN.
    # for tc_interval in test_case_interval_list:
    # Proceso para crear el archivo que reemplazará al archivo o código para los números de los casos de prueba definidos 
    #   en el intervalo, y ubicarlo en el directorio principal o en uno de los subdirectorios, según corresponda.
    # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
    # DEJAR EL SIGUIENTE BLOQUE COMENTADO:
    # start = None
    # end = None
    # if type(tc_interval) == int:
    #     start = tc_interval
    # elif type(tc_interval) == tuple:
    #     start = tc_interval[0]
    #     end = tc_interval[1]
    # else:
    #     print('Hubo un error del sistema que no debió haber sucedido nunca. Saliendo de la aplicación...')
    #     pyininid.sys.exit()

    # Crea el archivo que reemplazará al archivo o código para los números de los casos de prueba definidos en el intervalo
    
    # ESTO ES IRRELEVANTE AHORA, YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
    # DEJAR EL SIGUIENTE BLOQUE COMENTADO:
    # if end == None:
    #     file_test_case_conversion_file_name = current_file_name + '_tc_' + str(start) + '.py'
    # else:
    #     file_test_case_conversion_file_name = current_file_name + '_tc_' + str(start) + '_' + str(end) + '.py'

    # MODIFICAR LOS NOMBRES DE ALGUNAS DE ESTAS VARIABLES, PARA REFLEJAR QUE YA NO SE CREARÁN CASOS DE PRUEBA EN ESTE
    #   PROGRAMA:
    # file_test_case_conversion_file = None
    # file_test_case_conversion_file_name = current_file_name + '.py'
    # if current_subprogram_variant_dir == None:
    #     file_test_case_conversion_file = CONVERTED_FILES_DIR + '\\' + file_test_case_conversion_file_name
    # else:
    #     file_test_case_conversion_file = CONVERTED_FILES_DIR + '\\' + current_subprogram_variant_dir \
    #         + '\\' + file_test_case_conversion_file_name
    converted_file_route_name = None
    converted_file_name = current_file_name + '.py'
    if current_subprogram_variant_dir == None:
        converted_file_route_name = CONVERTED_FILES_DIR + '\\' + converted_file_name
    else:
        converted_file_route_name = CONVERTED_FILES_DIR + '\\' + current_subprogram_variant_dir \
            + '\\' + converted_file_name

    # Abrir un archivo en modo 'w' significa que el archivo se creará si no existe, y se abrirá sólo para SOBREESCRIBIRLO.
    # Usar codificación UTF-8 para textos es MUY importante para reconocer correctamente caracteres como las tildes y la ñ.
    # with open(file_test_case_conversion_file, mode='w', encoding='utf-8') as converted_file:
    with open(converted_file_route_name, mode='w', encoding='utf-8') as converted_file:
        # Escribe las instrucciones para importar un módulo, dada la ruta absoluta del módulo, configurada en este programa.
        # NOTA: Estas instrucciones sólo deberían estar en el código principal del ejercicio de programación:
        if current_subprogram_variant_dir == None: # Es el código principal del ejercicio de programación:
            converted_file.write('# Importación del módulo de funciones generadoras - NO MODIFICAR\n')
            converted_file.write('from pydoc import importfile\n')
            converted_file.write('idg = importfile(\'' + INPUT_DATA_GENERATORS_MODULE_FILE + '\')\n')
            # Escriba el código que inicialice el listado de seguimiento de índices para el funcionamiento de las 
            #   funciones generadoras basadas en una secuencia fija de valores a manera de lista, como una lista vacía.
            converted_file.write('sequential_idg_list = []\n')
            # Escriba el código que agregue tantos elementos como número de instrucciones hay en todos los archivos, 
            #   en el listado de seguimiento de índices para el funcionamiento de las funciones generadoras basadas en 
            #   una secuencia fija de valores a manera de lista, en donde cada uno de estos elementos es un número 0.
            converted_file.write('for i in range(' + str(max_sequential_idg_count) + '): sequential_idg_list.append([0])\n')
            converted_file.write('# Fin de la importación del módulo de funciones generadoras - NO MODIFICAR\n')

        lines_to_replace = []
        for python_input_instruction in python_input_instructions_list:
            lines_to_replace.append(python_input_instruction.get_input_line())
        line_to_replace_index = 0
        
        # Abrir un archivo en modo 'r' significa que el archivo se abrirá sólo para leerlo.
        with open(file, mode='r', encoding='utf-8') as original_file:                
            append_newline_before_textline = False                
            line = 0
            # El operador := es de asignación para una variable, pero permite hacer operaciones con 
            #   el valor de variable en una misma línea. (MUY CONVENIENTE EN ESTE CASO).
            while ((file_line_string := original_file.readline()) != ''):
                line += 1

                if line_to_replace_index < len(lines_to_replace):
                    next_line_to_replace = lines_to_replace[line_to_replace_index]
                else:
                    next_line_to_replace = -1 # Esto hace que nunca más se encuentre una línea, porque no se puede dar
                    #   reversa al recorrido de la lectura del archivo.

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
                if (pyininid.textline_has_newline_ending(file_line_string)):
                    if line != next_line_to_replace: # Escriba la línea del contenido del archivo original, tal cual:
                        line_to_write += file_line_string[0:len(file_line_string)-1:1]
                        converted_file.write(line_to_write) # Escribe toda la línea, excepto el último caracter.
                        append_newline_before_textline = True
                    else: # Este es la línea del archivo en donde hay que hacer un reemplazo:
                        instr_data = python_input_instructions_list[line_to_replace_index]
                        # En la línea leída, encuentre la posición donde está la instrucción, y reemplácelo:
                        # MODIFIQUE ESTA INSTRUCCIÓN PARA REFLEJAR QUE YA NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
                        # replaced_line = file_line_string.replace(instr_data.get_string_representation(), 
                        #     get_short_modified_instruction_data(python_input_instructions_list[line_to_replace_index], 
                        #     gen_functions_per_test_case_interval_list[tc_interval_index][line_to_replace_index]), 1)
                        replaced_line = file_line_string.replace(instr_data.get_string_representation(), 
                            get_short_modified_instruction_data(python_input_instructions_list[line_to_replace_index], 
                            gen_functions_list[line_to_replace_index]), 1)
                        line_to_write += replaced_line[0:len(replaced_line)-1:1]
                        # NOTA: NINGUNA instrucción de lectura DEBERÍA TENER un caracter '/n' al final de la línea
                        line_to_replace_index += 1
                        converted_file.write(line_to_write) # Escribe toda la línea, excepto el último caracter.
                        append_newline_before_textline = True
                else:
                    if line != next_line_to_replace: # Escriba la línea del contenido del archivo original, tal cual:
                        line_to_write += file_line_string
                        converted_file.write(line_to_write)
                    else: # Este es la línea del archivo en donde hay que hacer un reemplazo:
                        instr_data = python_input_instructions_list[line_to_replace_index]
                        # En la línea leída, encuentre la posición donde está la instrucción, y reemplácelo:
                        # MODIFIQUE ESTA INSTRUCCIÓN PARA REFLEJAR QUE YA NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:                      
                        # replaced_line = file_line_string.replace(instr_data.get_string_representation(), 
                        #     get_short_modified_instruction_data(python_input_instructions_list[line_to_replace_index], 
                        #     gen_functions_per_test_case_interval_list[tc_interval_index][line_to_replace_index]), 1)
                        replaced_line = file_line_string.replace(instr_data.get_string_representation(), 
                            get_short_modified_instruction_data(python_input_instructions_list[line_to_replace_index], 
                            gen_functions_list[line_to_replace_index]), 1)
                        line_to_write += replaced_line[0:len(replaced_line)-1:1]
                        line_to_replace_index += 1
                        converted_file.write(line_to_write)
    
    # CAMBIE EL NOMBRE A ESTA VARIABLE PARA REFLEJAR QUE YA NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA: 
    # print('Se ha generado el archivo:',file_test_case_conversion_file)
    print('Se ha generado el archivo:',converted_file_route_name)
    # ESTA INSTRUCCIÓN ES IRRELEVANTE YA QUE NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
    # tc_interval_index += 1

    # FIN: for tc_interval in test_case_interval_list:
    file_index += 1
        
# Copiar y pegar directorios y archivos que no se procesaron porque no tenían instrucciones de lectura, en el directorio
#   de resultados:
# Obtener los archivos que no se procesaron
file_index = 0
for discarded_file in discarded_files:
    # Obtener el nombre corto del archivo no procesado
    split_file_name_parts = discarded_file.split('\\')
    short_file_name = ''
    for name_part_index in range(1, len(split_file_name_parts), 1):
        short_file_name += '\\' + split_file_name_parts[name_part_index]
    # Obtener el nombre del archivo no procesado sin la extensión .py, y el subdirectorio de variante de subrutina o subprograma,
    #   si no es un programa principal
    current_file_name = None
    current_subprogram_variant_dir = None
    current_short_file_name = short_file_name
    current_relevant_file_route_parts = current_short_file_name.split('\\')
    if len(current_relevant_file_route_parts) == 2: # Es un archivo principal
        current_file_name = current_relevant_file_route_parts[1].split('.')[0]
    elif len(current_relevant_file_route_parts) == 3: # Es un archivo de variante de subrutina o subprograma
        current_subprogram_variant_dir = current_relevant_file_route_parts[1]
        current_file_name = current_relevant_file_route_parts[2].split('.')[0]
        # Creación de subdirectorio de variante
        if not pyininid.os.path.exists(CONVERTED_FILES_DIR + '\\' + current_subprogram_variant_dir):
            pyininid.os.makedirs(CONVERTED_FILES_DIR + '\\' + current_subprogram_variant_dir)
    else: # Error inesperado del sistema
        print('Hubo un error del sistema que no debió haber sucedido nunca. Saliendo de la aplicación...')
        pyininid.sys.exit()

    # Crea el archivo que reemplazará al archivo o código para los números de los casos de prueba definidos en el intervalo
    # MODIFICAR ESTAS INSTRUCCIONES, CONSIDERANDO QUE YA NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
    # file_test_case_conversion_file = None
    # file_test_case_conversion_file_name = None
    # if num_test_cases == 1:
    #     file_test_case_conversion_file_name = current_file_name + '_tc_1.py'
    # else:
    #     file_test_case_conversion_file_name = current_file_name + '_tc_1_' + str(num_test_cases) + '.py'

    # if current_subprogram_variant_dir == None:
    #     file_test_case_conversion_file = CONVERTED_FILES_DIR + '\\' + file_test_case_conversion_file_name
    # else:
    #     file_test_case_conversion_file = CONVERTED_FILES_DIR + '\\' + current_subprogram_variant_dir \
    #         + '\\' + file_test_case_conversion_file_name
    converted_file_route_name = None
    converted_file_name = current_file_name + '.py'
    if current_subprogram_variant_dir == None:
        converted_file_route_name = CONVERTED_FILES_DIR + '\\' + converted_file_name
    else:
        converted_file_route_name = CONVERTED_FILES_DIR + '\\' + current_subprogram_variant_dir \
            + '\\' + converted_file_name

    # Copiar archivo no procesado en el directorio correspondiente
    # MODIFICAR ESTAS INSTRUCCIONES, CONSIDERANDO QUE YA NO SE CREARÁN CASOS DE PRUEBA EN ESTE PROGRAMA:
    # copied_file = shutil.copyfile(discarded_file, file_test_case_conversion_file)
    # print('Se ha generado el archivo:',file_test_case_conversion_file)
    copied_file = shutil.copyfile(discarded_file, converted_file_route_name)
    print('Se ha generado el archivo:',converted_file_route_name)

    file_index += 1