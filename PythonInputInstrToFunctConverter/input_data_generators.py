from typing import Any
import types
import random

# Estas constantes no se están utilizando ahora:
# LOWERCASE = 1
# UPPERCASE = 2
# CAPITALIZE = 3
# ANYCASE = 4
                
class FixedSequenceBasedInputDataGenerator:
    # Constructor con parámetros opcionales
    def __init__(self, possible_input_values_list: list=None, input_values_list_type: type=str, next_index: int=0):
        # Validar los tipos de los argumentos pasados a este constructor:
        # Por defecto, el argumento possible_input_values_list no tiene valor (es igual a None), 
        #   pero si el valor del argumento es None, entonces esta clase devolverá una excepción de tipo Exception.
        if possible_input_values_list == None:
            raise Exception('Se debe especificar un valor para el parámetro possible_input_values_list de tipo ' + list.__name__)
        if type(possible_input_values_list) != list:
            raise TypeError('El argumento possible_input_values_list debe ser un valor de tipo ' + list.__name__)
        if len(possible_input_values_list) == 0:
            raise Exception('La lista dada como argumento possible_input_values_list debe tener al menos un elemento')

        # Por defecto, el argumento input_values_list_type tiene valor str (el tipo de cadena de caracteres),
        #   y este puede ser de tipo str, int, float y bool (los cuales son valores de tipo type).
        #   Si este argumento no cumple con esta condición, entonces esta clase devolverá una excepción de tipo Exception.
        if type(input_values_list_type) != type:
            raise TypeError('El argumento input_values_list_type debe ser un valor de tipo ' + type.__name__ + 
                            ' que puede ser: str, int, float o bool')
        if input_values_list_type.__name__ != 'str' and input_values_list_type.__name__ != 'int' \
        and input_values_list_type.__name__ != 'float' and input_values_list_type.__name__ != 'bool':
            raise TypeError('El argumento input_values_list_type debe ser un valor de tipo ' + type.__name__ + 
                            ' que puede ser: str, int, float o bool')

        # Validar que todos los elementos de la lista sean del tipo definido por el usuario
        for value in possible_input_values_list:
            if type(value) != input_values_list_type:
                raise TypeError('Todos los elementos de la lista possible_input_values_list deben ser de tipo ' 
                + input_values_list_type.__name__)

        # Validar que el argumento next_index sea de tipo int
        if type(next_index) != int:
            raise TypeError('El argumento next_index debe ser un valor de tipo ' + int.__name__)

        # El número de elementos de la lista debería ser, usualmente, el número de ejecuciones de una misma instrucción
        #   de lectura dentro de la ejecución de un mismo programa.
        # No obstante, la elección de elementos de la lista se puede repetir desde el principio, en caso de que se sigan
        #   solicitando valores de lista cuando todos los elementos de la lista se han elegido.
        # Es responsabilidad del usuario suministrar correctamente este número de elementos.

        # Use el underscore dos veces antes de un identificador, para definir un atributo privado en Python.
        self.__possible_input_values_list = possible_input_values_list        
        self.__max_index = len(self.__possible_input_values_list) - 1

        # El valor next_index debe estar entre 0 y el último índice de la lista dada por el usuario.
        # Si este argumento no cumple con esta condición, entonces esta clase devolverá una excepción de tipo Exception.
        if next_index < 0 or next_index > self.__max_index:
            raise ValueError('El argumento next_index debe ser un valor entre 0 y ' + str(self.__max_index) 
            + ', puesto que la lista possible_input_values_list tiene ' + str(self.__max_index + 1) + ' elementos.')
        self.__next_index = next_index

        # Por defecto, el argumento input_values_list_type es str
        self.__input_values_list_type = input_values_list_type

    # Getters
    def get_possible_input_values_list(self):
        return self.__possible_input_values_list
    
    def get_input_values_list_type(self):
        return self.__input_values_list_type

    def get_max_index(self):
        return self.__max_index
    
    def get_next_index(self):
        return self.__next_index

    # Setters
    def set_next_index(self, next_index):
        self.__next_index = next_index

    # Obtenga el próximo valor a retornar de la lista, dentro de la secuencia
    def get_next_value_and_index(self):
        value = self.get_possible_input_values_list()[self.get_next_index()]
        self.set_next_index(self.get_next_index() + 1)
        if self.get_next_index() > self.get_max_index(): # Si ya no hay más elementos de la lista por recorrer  
            self.set_next_index(0) # Reinicie el recorrido, para volver a tomar el primer elemento de la lista
            # en la siguiente iteración.
        index = self.get_next_index()
        return value, index
    
class ComplexInputDataGenerator:
    # El propósito principal de la clase ComplexInputDataGenerator es dar la posibilidad al usuario de crear funciones
    #   generadoras de datos que puedan reemplazar operaciones de lectura de datos para casos más complejos, como por ejemplo,
    #   las operaciones de lectura que son determinantes en la lógica posterior de un programa y que están incluidos dentro de
    #   ciclos repetitivos, incluso, anidados. En casos como este, se pueden generan múltiples datos de entrada diferentes, pese 
    #   a que se utiliza una misma instrucción de lectura para ello, y aunque existe la clase FixedSequenceBasedInputDataGenerator
    #   para ello, esta no cuenta con mecanismos para generar una cantidad aleatoria de datos de entrada, como sí lo hace la clase
    #   ComplexInputDataGenerator, el cual permite utilizar funciones generadoras simples fijas y aleatorias, incluyendo las que
    #   son posibilitadas mediante el uso de la clase FixedSequenceBasedInputDataGenerator, controlando las veces en que se ejecutan
    #   estas funciones, en orden, y repitiendo su uso desde el principio. En este sentido, es como una secuencia de funciones
    #   generadoras que se ejecutan las veces que lo defina el usuario, antes de seguir con la siguiente función generadora en la
    #   lista. De esta forma, se enriquece aún más la automatización del reemplazo de operaciones de lectura con funciones
    #   generadoras que emulan ese ingreso de datos, y con esto, la creación de diferentes casos de prueba para un mismo ejercicio 
    #   de programación - con o sin variantes, y su aplicación en una diversidad de ejercicios de programación en los cuales
    #   se evalúa el resultado de un programa construido por un usuario frente al resultado esperado, para realizar una evaluación
    #   automática.

    # Constructor con parámetros opcionales
    def __init__(self, input_values_list_type: type=str, next_index: int=0, functions: tuple=None):
        # Por defecto, el argumento input_values_list_type tiene valor str (el tipo de cadena de caracteres),
        #   y este puede ser de tipo str, int, float y bool (los cuales son valores de tipo type).
        #   Si este argumento no cumple con esta condición, entonces esta clase devolverá una excepción de tipo Exception.
        if type(input_values_list_type) != type:
            raise TypeError('El argumento input_values_list_type debe ser un valor de tipo ' + type.__name__ + 
                            ' que puede ser: str, int, float o bool')
        if input_values_list_type.__name__ != 'str' and input_values_list_type.__name__ != 'int' \
        and input_values_list_type.__name__ != 'float' and input_values_list_type.__name__ != 'bool':
            raise TypeError('El argumento input_values_list_type debe ser un valor de tipo ' + type.__name__ + 
                            ' que puede ser: str, int, float o bool')
        
        # Validar que el argumento next_index sea de tipo int
        if type(next_index) != int:
            raise TypeError('El argumento next_index debe ser un valor de tipo ' + int.__name__)
        
        # Validar las funciones generadoras simples ingresadas a la clase
        # 1) El argumento functions debe ser una tupla
        if type(functions) != tuple:
            raise TypeError('El argumento functions debe ser una tupla; es decir, un valor de tipo ' + tuple.__name__)
        
        # 2) Debe haber al menos un elemento en la tupla functions, el cual representa una función
        if len(functions) < 1:
            raise ValueError('El argumento functions debe tener al menos un elemento')
        
        for funct in functions:
            # 3) Los elementos que tenga la tupla functions deben ser tuplas; cada tupla representa una función
            if type(funct) != tuple:
                raise TypeError('Todos los elementos del argumento functions (el cual es una tupla) deben ser de tipo ' 
                    + tuple.__name__)
            # 4) Los elementos que tenga la tupla functions deben ser tuplas de dos o tres elementos:
            #   El primer elemento de la tupla de dos o tres elementos es la función
            #       Este elemento debe ser de tipo function,
            #           y dependiendo del tipo dado por parámetros a esta clase, debe ser una de las posibles funciones
            #           para el tipo dado.
            #   El segundo elemento puede ser:
            #       Una tupla de al menos un elemento que representan los parámetros de la función
            #           (En este caso, la tupla debe contener tres elementos; no dos.)
            #       Un número entero mayor que 0 que represente las veces que se ejecutará la función
            #           (En este caso, la tupla debe contener dos elementos; no tres.)
            #   El tercer elemento, si lo hay, debe ser el número entero mayor que 0 que represente 
            #       las veces que se ejecutará la función
            elif len(funct) != 2 and len(funct) != 3:
                raise ValueError('Todos los elementos del argumento functions (el cual es una tupla) ' + 
                                    'deben ser tuplas de 2 o 3 elementos.')
            elif type(funct[0]) != types.FunctionType:
                # print(type(funct[0]))
                raise TypeError('El primer elemento de cualquier tupla que sea un elemento del argumento functions ' +
                                    '(el cual es una tupla) debe ser una función; es decir, el nombre de una función, ' + 
                                    'sin paréntesis; o dicho de otro modo, un valor de tipo ' + types.FunctionType.__name__)
            elif input_values_list_type == str:
                if funct[0] != fixed_str_data_gen and funct[0] != random_str_data_from_list_gen \
                and funct[0] != fixed_sequential_str_data_from_list_gen:
                    raise ValueError('Considerando que el valor a reemplazar debe ser de tipo str, ' + 
                                        'el primer elemento de cualquier tupla que sea un elemento del argumento functions' +                                          
                                        '(el cual es una tupla) debe tener como valor uno de los siguientes nombres de función: ' +
                                        'fixed_str_data_gen, random_str_data_from_list_gen, o ' + 
                                        'fixed_sequential_str_data_from_list_gen.')
            elif input_values_list_type == int:
                if funct[0] != fixed_int_data_gen and funct[0] != random_int_data_from_list_gen \
                and funct[0] != random_int_from_closed_interval_data_gen \
                and funct[0] != random_int_from_range_data_gen \
                and funct[0] != fixed_sequential_int_data_from_list_gen:
                    raise ValueError('Considerando que el valor a reemplazar debe ser de tipo int, ' + 
                                        'el primer elemento de cualquier tupla que sea un elemento del argumento functions' +                                          
                                        '(el cual es una tupla) debe tener como valor uno de los siguientes nombres de función: ' +
                                        'fixed_int_data_gen, random_int_data_from_list_gen, ' + 
                                        'random_int_from_closed_interval_data_gen, random_int_from_range_data_gen, o ' + 
                                        'fixed_sequential_int_data_from_list_gen.')
            elif input_values_list_type == float:
                if funct[0] != fixed_float_data_gen and funct[0] != random_float_data_from_list_gen \
                and funct[0] != random_float_from_closed_interval_data_gen \
                and funct[0] != random_float_from_closed_interval_with_fixed_precision_data_gen \
                and funct[0] != fixed_sequential_float_data_from_list_gen:
                    raise ValueError('Considerando que el valor a reemplazar debe ser de tipo float, ' + 
                                        'el primer elemento de cualquier tupla que sea un elemento del argumento functions' +                                          
                                        '(el cual es una tupla) debe tener como valor uno de los siguientes nombres de función: ' +
                                        'fixed_float_data_gen, random_float_data_from_list_gen, ' + 
                                        'random_float_from_closed_interval_data_gen, ' + 
                                        'random_float_from_closed_interval_with_fixed_precision_data_gen, o ' + 
                                        'fixed_sequential_float_data_from_list_gen.')
            elif input_values_list_type == bool:
                if funct[0] != fixed_true_data_gen and funct[0] != fixed_false_data_gen \
                and funct[0] != random_strict_bool_data_gen \
                and funct[0] != fixed_sequential_strict_bool_data_from_list_gen:
                    raise ValueError('Considerando que el valor a reemplazar debe ser de tipo bool, ' + 
                                        'el primer elemento de cualquier tupla que sea un elemento del argumento functions' +                                          
                                        '(el cual es una tupla) debe tener como valor uno de los siguientes nombres de función: ' +
                                        'fixed_true_data_gen, fixed_false_data_gen, ' + 
                                        'random_strict_bool_data_gen, o' + 
                                        'fixed_sequential_strict_bool_data_from_list_gen')
            
            if len(funct) == 2:
                if type(funct[1]) != int:
                    raise TypeError('El segundo elemento de cualquier tupla de dos elementos que sea un elemento del ' + 
                                    'argumento functions (el cual es una tupla) debe ser un valor de tipo ' + int.__name__)
                elif funct[1] < 1:
                    raise ValueError('El segundo elemento de cualquier tupla de dos elementos que sea un elemento del ' + 
                                    'argumento functions (el cual es una tupla) debe ser un número mayor que 0, puesto que este ' +
                                    'elemento representa el número de veces que se va a ejecutar la función generadora ' +
                                    '(que en este caso no requiere parámetros)')
            elif len(funct) == 3:
                # if type(funct[1]) != tuple:
                #   No exigir esto al usuario, porque si el número de parámetros para una función generadora simple es 1,
                #       entonces este elemento no será una tupla, sino que será del tipo del parámetro, que puede ser,
                #       incluso, por ejemplo, una lista (que es un iterable).
                #     raise TypeError('El segundo elemento de cualquier tupla de tres elementos que sea un elemento del ' + 
                #                     'argumento functions (el cual es una tupla) debe ser un valor de tipo ' + tuple.__name__)
                # elif len(funct[1]) < 1:
                #     raise ValueError('El segundo elemento de cualquier tupla de tres elementos que sea un elemento del ' + 
                #                     'argumento functions (el cual es una tupla) debe ser una tupla con al menos un elemento, ' + 
                #                     'dado que en este caso se sobreentiende que la función a ejecutar usa al menos 1 argumento.')
                if type(funct[1]) == tuple and len(funct[1]) < 1:
                    raise ValueError('El segundo elemento de cualquier tupla de tres elementos que sea un elemento del ' + 
                                    'argumento functions (el cual es una tupla) debe tener al menos un elemento, si es ' + 
                                    ' una tupla, dado que si los parámetros se especifican en tuplas, se sobreentiende ' +
                                    'que la función a ejecutar usa al menos 1 argumento.')
                elif type(funct[2]) != int:
                    raise TypeError('El tercer elemento de cualquier tupla de tres elementos que sea un elemento del ' + 
                                    'argumento functions (el cual es una tupla) debe ser un valor de tipo ' + int.__name__)
                elif funct[2] < 1:
                    raise ValueError('El tercer elemento de cualquier tupla de tres elementos que sea un elemento del ' + 
                                    'argumento functions (el cual es una tupla) debe ser un número mayor que 0, puesto que este ' +
                                    'elemento representa el número de veces que se va a ejecutar la función generadora ' +
                                    '(que en este caso requiere al menos 1 parámetro')
            else: # Error inesperado
                raise Exception('Por alguna razón, la cantidad de elementos de una tupla en el argumento functions ' + 
                                '(el cual es una tupla), es diferente de 2 o 3, lo cual es inesperado, dada la lógica ' + 
                                'del programa. Claramente, hubo un error del sistema que no debió haber sucedido nunca.')

        # En este punto, se han terminado de hacer las validaciones de argumentos para esta clase.
        # Use el underscore dos veces antes de un identificador, para definir un atributo privado en Python.

        # Las funciones generadoras simples que harán parte de la función generadora compleja
        self.__functions = functions

        # El número máximo de ejecuciones, antes del reinicio de esta secuencia de funciones generadoras simples,
        #   está determinado por la sumatoria del número de veces que el usuario definió que se ejecutaba cada una de las
        #   funciones generadoras simples.
        # Además, el número máximo de ejecuciones por función generadora simple se puede calcular de la siguiente manera:
        sgf_max_indexes = []
        sgf_sequence_exec_times = 0
        for funct in self.__functions:
            sgf_sequence_exec_times += funct[len(funct) - 1]
            sgf_max_indexes.append(sgf_sequence_exec_times - 1) # Porque los índices empiezan desde 0, no desde 1
        self.__max_index = sgf_sequence_exec_times - 1 # Porque los índices empiezan desde 0, no desde 1
        self.__sgf_max_indexes = sgf_max_indexes

        # El valor next_index debe estar entre 0 y el último índice de la lista dada por el usuario.
        # Si este argumento no cumple con esta condición, entonces esta clase devolverá una excepción de tipo Exception.
        if next_index < 0 or next_index > self.__max_index:
            raise ValueError('El argumento next_index debe ser un valor entre 0 y ' + str(self.__max_index) 
            + ', puesto que el número de veces que se ejecutan en total las funciones generadoras simples, según la definición ' +
             'del usuario, así lo establece. En este caso, ese número es de ' + str(self.__max_index + 1) + '.')
        self.__next_index = next_index

        # Por defecto, el argumento input_values_list_type es str
        self.__input_values_list_type = input_values_list_type

    # Getters
    def get_functions(self):
        return self.__functions
    
    def get_input_values_list_type(self):
        return self.__input_values_list_type

    def get_max_index(self):
        return self.__max_index
    
    def get_sgf_max_indexes(self):
        return self.__sgf_max_indexes
    
    def get_next_index(self):
        return self.__next_index

    # Setters
    def set_next_index(self, next_index):
        self.__next_index = next_index

    # Obtenga el próximo valor a retornar de la lista, dentro de la secuencia
    def get_next_value_and_index(self):
        value = None
        function_count = 0
        for sgf_max_index in self.get_sgf_max_indexes():
            if self.get_next_index() <= sgf_max_index:
                funct = self.get_functions()[function_count]
                if len(funct) == 3:
                    # Los parámetros de funciones deberían ser contenidos en una tupla para que puedan
                    #   funcionar correctamente como parámetros de una función a ejecutar.
                    # Recuerde que las funciones en Python son objetos.
                    # Así también, los parámetros de funciones pueden ser representados en tuplas, por ejemplo,
                    #   y una instancia de la clase tuple es un objeto en Python.
                    params = None
                    if type(funct[1]) != tuple:
                        params = (funct[1],)
                    else:
                        params = funct[1]
                    value = funct[0](*params)
                    break
                elif len(funct) == 2:
                    value = funct[0]()
                    break
            function_count += 1
        self.set_next_index(self.get_next_index() + 1)
        # Si ya no hay más funciones generadoras simples en la secuencia por recorrer:
        if self.get_next_index() > self.get_max_index(): 
            self.set_next_index(0) # Reinicie el recorrido, para volver a tomar la primera función generadora simple
            #  de la secuencia en la siguiente iteración.
        index = self.get_next_index()
        return value, index

# a) Generadores de 1 valor fijo para todos los casos de prueba.
def fixed_str_data_gen(value: str):
    if (type(value) == str):
        return value
    else:
        raise TypeError('No se suministró un valor de tipo ' + str.__name__)

def fixed_int_data_gen(value: int):
    if (type(value) == int):
        return value
    else:
        raise TypeError('No se suministró un valor de tipo ' + int.__name__)

def fixed_float_data_gen(value: float):
    if (type(value) == float):
        return value
    else:
        raise TypeError('No se suministró un valor de tipo ' + float.__name__)

# def fixed_nonstrict_bool_data_gen(value: Any):
#     return bool(value) # Admite cualquier valor, pero este es convertido a un valor de tipo bool, dependiendo de su valor.

def fixed_true_data_gen():
    return True

def fixed_false_data_gen():
    return False

# def fixed_any_type_data_gen(value: Any):
#     return value

# b) Generadores de 1 valor aleatorio, seleccionado de una forma repetible a partir de una lista dada por el usuario. 
#   Siempre retornará un valor aleatorio, independientemente de si se termina repitiendo una selección o no.
def random_str_data_from_list_gen(possible_input_values_list: list):
    # Validar los tipos de los argumentos pasados a este constructor
    if possible_input_values_list == None:
        raise Exception('Se debe especificar un valor para el parámetro possible_input_values_list de tipo ' + list.__name__)
    if type(possible_input_values_list) != list:
        raise TypeError('El argumento possible_input_values_list debe ser un valor de tipo ' + list.__name__)
    if len(possible_input_values_list) == 0:
        raise Exception('La lista dada como argumento possible_input_values_list debe tener al menos un elemento')

    # Validar que todos los elementos de la lista sean del tipo str
    for value in possible_input_values_list:
        if type(value) != str:
            raise TypeError('Todos los elementos de la lista possible_input_values_list deben ser de tipo ' + str.__name__)

    return random.choice(possible_input_values_list)

def random_int_data_from_list_gen(possible_input_values_list: list):
    # Validar los tipos de los argumentos pasados a este constructor
    if possible_input_values_list == None:
        raise Exception('Se debe especificar un valor para el parámetro possible_input_values_list de tipo ' + list.__name__)
    if type(possible_input_values_list) != list:
        raise TypeError('El argumento possible_input_values_list debe ser un valor de tipo ' + list.__name__)
    if len(possible_input_values_list) == 0:
        raise Exception('La lista dada como argumento possible_input_values_list debe tener al menos un elemento')

    # Validar que todos los elementos de la lista sean del tipo int
    for value in possible_input_values_list:
        if type(value) != int:
            raise TypeError('Todos los elementos de la lista possible_input_values_list deben ser de tipo ' + int.__name__)

    return random.choice(possible_input_values_list)

def random_float_data_from_list_gen(possible_input_values_list: list):
    # Validar los tipos de los argumentos pasados a este constructor
    if possible_input_values_list == None:
        raise Exception('Se debe especificar un valor para el parámetro possible_input_values_list de tipo ' + list.__name__)
    if type(possible_input_values_list) != list:
        raise TypeError('El argumento possible_input_values_list debe ser un valor de tipo ' + list.__name__)
    if len(possible_input_values_list) == 0:
        raise Exception('La lista dada como argumento possible_input_values_list debe tener al menos un elemento')

    # Validar que todos los elementos de la lista sean del tipo float
    for value in possible_input_values_list:
        if type(value) != float:
            raise TypeError('Todos los elementos de la lista possible_input_values_list deben ser de tipo ' + float.__name__)

    return random.choice(possible_input_values_list)

# def random_nonstrict_bool_data_from_list_gen(possible_input_values_list: list):
#     # Validar los tipos de los argumentos pasados a este constructor
#     if possible_input_values_list == None:
#         raise Exception('Se debe especificar un valor para el parámetro possible_input_values_list de tipo ' + list.__name__)
#     if type(possible_input_values_list) != list:
#         raise TypeError('El argumento possible_input_values_list debe ser un valor de tipo ' + list.__name__)
#     if len(possible_input_values_list) == 0:
#         raise Exception('La lista dada como argumento possible_input_values_list debe tener al menos un elemento')

#     # Convertir todos los valores dados a valores de tipo bool
#     boolean_input_values_list = list(map(bool, possible_input_values_list))
#     return random.choice(boolean_input_values_list)

# def random_any_type_data_from_list_gen(possible_input_values_list: list):
#     # Validar los tipos de los argumentos pasados a este constructor
#     if possible_input_values_list == None:
#         raise Exception('Se debe especificar un valor para el parámetro possible_input_values_list de tipo ' + list.__name__)
#     if type(possible_input_values_list) != list:
#         raise TypeError('El argumento possible_input_values_list debe ser un valor de tipo ' + list.__name__)
#     if len(possible_input_values_list) == 0:
#         raise Exception('La lista dada como argumento possible_input_values_list debe tener al menos un elemento')

#     return random.choice(possible_input_values_list)

# c) Generadores de 1 valor aleatorio, seleccionado de una forma repetible mediante parámetros diferentes a una lista.
#   Siempre retornará un valor aleatorio, independientemente de si se repita una selección o no.
# def random_alphanumeric_str_of_fixed_length_data_gen(length: int, case_option: int, include_spanish_characters: bool):
#     if type(length) != int:
#         raise TypeError('El argumento length debe ser un valor de tipo ' + int.__name__)
#     if length <= 0:
#         raise ValueError('El argumento length debe ser un número entero mayor que 0')

#     if type(case_option) != int:
#         raise TypeError('El argumento case_option debe ser un valor de tipo ' + int.__name__)
#     if case_option != LOWERCASE and case_option != UPPERCASE and case_option != CAPITALIZE and case_option != ANYCASE:
#         raise ValueError('El argumento case_option debe ser uno de los siguientes números enteros: 1, 2, 3 o 4')

#     if type(include_spanish_characters) != bool:
#         raise TypeError('El argumento include_spanish_characters debe ser un valor de tipo ' + bool.__name__)

#     possible_lowercase_alphabetic_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
#         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     possible_uppercase_alphabetic_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
#         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     possible_lowercase_spanish_alphabetic_characters = ['á', 'é', 'í', 'ó', 'ñ', 'ú', 'ü']
#     possible_uppercase_spanish_alphabetic_characters = ['Á', 'É', 'Í', 'Ó', 'Ñ', 'Ú', 'Ü']
#     possible_numeric_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     possible_characters = possible_numeric_characters.copy()
#     if case_option == LOWERCASE:
#         possible_characters.extend(possible_lowercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_lowercase_spanish_alphabetic_characters)
#     elif case_option == UPPERCASE:
#         possible_characters.extend(possible_uppercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_uppercase_spanish_alphabetic_characters)
#     elif case_option == CAPITALIZE:
#         possible_characters.extend(possible_uppercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_uppercase_spanish_alphabetic_characters)
#     elif case_option == ANYCASE:
#         possible_characters.extend(possible_lowercase_alphabetic_characters)
#         possible_characters.extend(possible_uppercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_lowercase_spanish_alphabetic_characters)
#             possible_characters.extend(possible_uppercase_spanish_alphabetic_characters)

#     if case_option != CAPITALIZE:
#         chosen_characters = random.choices(possible_characters, k = length)
#         # https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
#         return ''.join(chosen_characters[0: length: 1])
#     else:
#         # case_option == CAPITALIZE:
#         chosen_character = random.choices(possible_characters, k = 1)
#         possible_characters = []
#         possible_characters.extend(possible_lowercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_lowercase_spanish_alphabetic_characters)
#         if length > 1:
#             chosen_characters = random.choices(possible_characters, k = length - 1)
#             # https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
#             return ''.join(chosen_character[0: 1: 1]) + ''.join(chosen_characters[0: length-1: 1])
#         elif length == 1:
#             return ''.join(chosen_character[0: 1: 1])

# def random_alphanumeric_str_of_random_length_data_gen(min_length: int, max_length: int, 
#     case_option: int, include_spanish_characters: bool):
    
#     if type(min_length) != int:
#         raise TypeError('El argumento min_length debe ser un valor de tipo ' + int.__name__)
#     if min_length < 0:
#         raise ValueError('El argumento min_length debe ser un número entero mayor o igual que 0')

#     if type(max_length) != int:
#         raise TypeError('El argumento max_length debe ser un valor de tipo ' + int.__name__)

#     if min_length > max_length:
#         raise ValueError('El argumento min_length debe ser menor o igual que max_length')

#     if type(case_option) != int:
#         raise TypeError('El argumento case_option debe ser un valor de tipo ' + int.__name__)
#     if case_option != LOWERCASE and case_option != UPPERCASE and case_option != CAPITALIZE and case_option != ANYCASE:
#         raise ValueError('El argumento case_option debe ser uno de los siguientes números enteros: 1, 2, 3 o 4')

#     if type(include_spanish_characters) != bool:
#         raise TypeError('El argumento include_spanish_characters debe ser un valor de tipo ' + bool.__name__)

#     possible_lowercase_alphabetic_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
#         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     possible_uppercase_alphabetic_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
#         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     possible_lowercase_spanish_alphabetic_characters = ['á', 'é', 'í', 'ó', 'ñ', 'ú', 'ü']
#     possible_uppercase_spanish_alphabetic_characters = ['Á', 'É', 'Í', 'Ó', 'Ñ', 'Ú', 'Ü']
#     possible_numeric_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     possible_characters = possible_numeric_characters.copy()
#     if case_option == LOWERCASE:
#         possible_characters.extend(possible_lowercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_lowercase_spanish_alphabetic_characters)
#     elif case_option == UPPERCASE:
#         possible_characters.extend(possible_uppercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_uppercase_spanish_alphabetic_characters)
#     elif case_option == CAPITALIZE:
#         possible_characters.extend(possible_uppercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_uppercase_spanish_alphabetic_characters)
#     elif case_option == ANYCASE:
#         possible_characters.extend(possible_lowercase_alphabetic_characters)
#         possible_characters.extend(possible_uppercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_lowercase_spanish_alphabetic_characters)
#             possible_characters.extend(possible_uppercase_spanish_alphabetic_characters)

#     length = random.randint(min_length, max_length)

#     if length == 0:
#         return ''
    
#     if case_option != CAPITALIZE:
#         chosen_characters = random.choices(possible_characters, k = length)
#         return ''.join(chosen_characters[0: length: 1])
#     else:
#         # case_option == CAPITALIZE:
#         chosen_character = random.choices(possible_characters, k = 1)
#         possible_characters = []
#         possible_characters.extend(possible_lowercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_lowercase_spanish_alphabetic_characters)
#         if length > 1:
#             chosen_characters = random.choices(possible_characters, k = length - 1)
#             return ''.join(chosen_character[0: 1: 1]) + ''.join(chosen_characters[0: length-1: 1])
#         elif length == 1:
#             return ''.join(chosen_character[0: 1: 1])

# def random_alphabetic_str_of_fixed_length_data_gen(length: int, case_option: int, include_spanish_characters: bool):
#     if type(length) != int:
#         raise TypeError('El argumento length debe ser un valor de tipo ' + int.__name__)
#     if length <= 0:
#         raise ValueError('El argumento length debe ser un número entero mayor que 0')

#     if type(case_option) != int:
#         raise TypeError('El argumento case_option debe ser un valor de tipo ' + int.__name__)
#     if case_option != LOWERCASE and case_option != UPPERCASE and case_option != CAPITALIZE and case_option != ANYCASE:
#         raise ValueError('El argumento case_option debe ser uno de los siguientes números enteros: 1, 2, 3 o 4')

#     if type(include_spanish_characters) != bool:
#         raise TypeError('El argumento include_spanish_characters debe ser un valor de tipo ' + bool.__name__)

#     possible_lowercase_alphabetic_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
#         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     possible_uppercase_alphabetic_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
#         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     possible_lowercase_spanish_alphabetic_characters = ['á', 'é', 'í', 'ó', 'ñ', 'ú', 'ü']
#     possible_uppercase_spanish_alphabetic_characters = ['Á', 'É', 'Í', 'Ó', 'Ñ', 'Ú', 'Ü']
#     possible_characters = []
#     if case_option == LOWERCASE:
#         possible_characters.extend(possible_lowercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_lowercase_spanish_alphabetic_characters)
#     elif case_option == UPPERCASE:
#         possible_characters.extend(possible_uppercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_uppercase_spanish_alphabetic_characters)
#     elif case_option == CAPITALIZE:
#         possible_characters.extend(possible_uppercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_uppercase_spanish_alphabetic_characters)
#     elif case_option == ANYCASE:
#         possible_characters.extend(possible_lowercase_alphabetic_characters)
#         possible_characters.extend(possible_uppercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_lowercase_spanish_alphabetic_characters)
#             possible_characters.extend(possible_uppercase_spanish_alphabetic_characters)

#     if case_option != CAPITALIZE:
#         chosen_characters = random.choices(possible_characters, k = length)
#         return ''.join(chosen_characters[0: length: 1])
#     else:
#         # case_option == CAPITALIZE:
#         chosen_character = random.choices(possible_characters, k = 1)
#         possible_characters = []
#         possible_characters.extend(possible_lowercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_lowercase_spanish_alphabetic_characters)
#         if length > 1:
#             chosen_characters = random.choices(possible_characters, k = length - 1)
#             return ''.join(chosen_character[0: 1: 1]) + ''.join(chosen_characters[0: length-1: 1])
#         elif length == 1:
#             return ''.join(chosen_character[0: 1: 1])

# def random_alphabetic_str_of_random_length_data_gen(min_length: int, max_length: int, 
#     case_option: int, include_spanish_characters: bool):
    
#     if type(min_length) != int:
#         raise TypeError('El argumento min_length debe ser un valor de tipo ' + int.__name__)
#     if min_length < 0:
#         raise ValueError('El argumento min_length debe ser un número entero mayor o igual que 0')

#     if type(max_length) != int:
#         raise TypeError('El argumento max_length debe ser un valor de tipo ' + int.__name__)

#     if min_length > max_length:
#         raise ValueError('El argumento min_length debe ser menor o igual que max_length')

#     if type(case_option) != int:
#         raise TypeError('El argumento case_option debe ser un valor de tipo ' + int.__name__)
#     if case_option != LOWERCASE and case_option != UPPERCASE and case_option != CAPITALIZE and case_option != ANYCASE:
#         raise ValueError('El argumento case_option debe ser uno de los siguientes números enteros: 1, 2, 3 o 4')

#     if type(include_spanish_characters) != bool:
#         raise TypeError('El argumento include_spanish_characters debe ser un valor de tipo ' + bool.__name__)

#     possible_lowercase_alphabetic_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
#         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     possible_uppercase_alphabetic_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
#         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     possible_lowercase_spanish_alphabetic_characters = ['á', 'é', 'í', 'ó', 'ñ', 'ú', 'ü']
#     possible_uppercase_spanish_alphabetic_characters = ['Á', 'É', 'Í', 'Ó', 'Ñ', 'Ú', 'Ü']
#     possible_characters = []
#     if case_option == LOWERCASE:
#         possible_characters.extend(possible_lowercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_lowercase_spanish_alphabetic_characters)
#     elif case_option == UPPERCASE:
#         possible_characters.extend(possible_uppercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_uppercase_spanish_alphabetic_characters)
#     elif case_option == CAPITALIZE:
#         possible_characters.extend(possible_uppercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_uppercase_spanish_alphabetic_characters)
#     elif case_option == ANYCASE:
#         possible_characters.extend(possible_lowercase_alphabetic_characters)
#         possible_characters.extend(possible_uppercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_lowercase_spanish_alphabetic_characters)
#             possible_characters.extend(possible_uppercase_spanish_alphabetic_characters)

#     length = random.randint(min_length, max_length)

#     if length == 0:
#         return ''
    
#     if case_option != CAPITALIZE:
#         chosen_characters = random.choices(possible_characters, k = length)
#         return ''.join(chosen_characters[0: length: 1])
#     else:
#         # case_option == CAPITALIZE:
#         chosen_character = random.choices(possible_characters, k = 1)
#         possible_characters = []
#         possible_characters.extend(possible_lowercase_alphabetic_characters)
#         if include_spanish_characters == True:
#             possible_characters.extend(possible_lowercase_spanish_alphabetic_characters)
#         if length > 1:
#             chosen_characters = random.choices(possible_characters, k = length - 1)
#             return ''.join(chosen_character[0: 1: 1]) + ''.join(chosen_characters[0: length-1: 1])
#         elif length == 1:
#             return ''.join(chosen_character[0: 1: 1])

# def random_numeric_str_of_fixed_length_data_gen(length: int):
#     if type(length) != int:
#         raise TypeError('El argumento length debe ser un valor de tipo ' + int.__name__)
#     if length <= 0:
#         raise ValueError('El argumento length debe ser un número entero mayor que 0')
    
#     possible_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
#     chosen_characters = random.choices(possible_characters, k = length)
#     return ''.join(chosen_characters[0: length: 1])

# def random_numeric_str_of_random_length_data_gen(min_length: int, max_length: int):
#     if type(min_length) != int:
#         raise TypeError('El argumento min_length debe ser un valor de tipo ' + int.__name__)
#     if min_length < 0:
#         raise ValueError('El argumento min_length debe ser un número entero mayor o igual que 0')

#     if type(max_length) != int:
#         raise TypeError('El argumento max_length debe ser un valor de tipo ' + int.__name__)

#     if min_length > max_length:
#         raise ValueError('El argumento min_length debe ser menor o igual que max_length')

#     possible_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#     length = random.randint(min_length, max_length)
#     if length == 0:
#         return ''

#     chosen_characters = random.choices(possible_characters, k = length)
#     return ''.join(chosen_characters[0: length: 1])
    
def random_int_from_closed_interval_data_gen(min_value: int, max_value: int):
    if type(min_value) != int:
        raise TypeError('El argumento min_value debe ser un valor de tipo ' + int.__name__)
    if type(max_value) != int:
        raise TypeError('El argumento max_value debe ser un valor de tipo ' + int.__name__)
    if min_value > max_value:
        raise ValueError('El argumento min_value debe ser menor o igual que max_value')

    return random.randint(min_value, max_value)

# def random_int_from_closed_intervals_data_gen(interval_tuples_list: list):
#     elements_count = 0
#     if type(interval_tuples_list) != list:
#         raise TypeError('El argumento interval_tuples_list debe ser un valor de tipo ' + list.__name__ + ',' + 
#         ' con elementos de tipo ' + tuple.__name__)
#     if len(interval_tuples_list) < 1:
#         raise ValueError('El argumento interval_tuples_list debe ser un valor de tipo ' + list.__name__ +
#         ' que contenga al menos un elemento de tipo ' + tuple.__name__)
#     # for list_elem in range(0, len(interval_tuples_list), 1):
#     for list_elem in interval_tuples_list:
#         if type(list_elem) != tuple:
#             raise TypeError('Todos los elementos de la lista interval_tuples_list deben ser de tipo ' + tuple.__name__ +
#             ' y deben contener exactamente dos elementos: un valor mínimo y un valor máximo (ambos son números enteros)')
#         if len(list_elem) != 2:
#             raise TypeError('Todos los elementos de la lista interval_tuples_list deben ser de tipo ' + tuple.__name__ +
#             ' y deben contener exactamente dos elementos: un valor mínimo y un valor máximo (ambos son números enteros)')
#         count = 0 # 0: min_value, 1: max_value
#         min_value = 0
#         max_value = 0
#         # for tuple_elem in range(0, len(list_elem), 1):
#         for tuple_elem in list_elem:
#             if type(tuple_elem) != int:
#                 raise TypeError('Todos los elementos de la lista interval_tuples_list deben ser de tipo ' + tuple.__name__ +
#                 ' y deben contener exactamente dos números enteros (tipo ' + int.__name__ + ')')
#             if count == 0:
#                 min_value = tuple_elem
#             if count == 1:
#                 max_value = tuple_elem
#             count += 1
#         if min_value > max_value:
#             raise ValueError('El primer elemento de cualquier tupla (min_value) de la lista interval_tuples_list debe ser ' + 
#             'menor o igual que el segundo elemento de la tupla (max_value).')
#         elements_count += max_value - min_value + 1
#         # e.g. 1: max_value = 1 and min_value = 1 : elements_sum = 1 - 1 + 1 = 1 : [1]
#         # e.g. 1: max_value = 5 and min_value = 2 : elements_sum = 5 - 2 + 1 = 4 : [2, 3, 4, 5]
#         # e.g. 1: max_value = -2 and min_value = -5 : elements_sum = -2 - (-5) + 1 = -2 + 5 + 1 = 4 : [-5, -4, -3, -2]
#         # e.g. 1: max_value = 3 and min_value = -2 : elements_sum = 3 - (-2) + 1 = 3 + 2 + 1 = 6 : [-2, -1, 0, 1, 2, 3]

#     chosen_tuple_index = 0
#     if len(interval_tuples_list) >= 2:
#         # chosen_tuple_index = random.randint(0, len(interval_tuples_list) - 1)

#         # Calcular la probabilidad de elegir cada intervalo
#         probability_list = []
        
#         for list_elem in interval_tuples_list:
#             probability_list.append(Fraction(list_elem[1] - list_elem[0] + 1, elements_count))

#         # print(list(range(0, len(interval_tuples_list), 1)))
#         chosen_tuple_index = random.choices(list(range(0, len(interval_tuples_list), 1)), weights=probability_list) # k = 1
#         # print(chosen_tuple_index[0])
    
#     # chosen_tuple_values = interval_tuples_list[chosen_tuple_index]
#     chosen_tuple_values = interval_tuples_list[chosen_tuple_index[0]]
#     return random.randint(chosen_tuple_values[0], chosen_tuple_values[1])

def random_int_from_range_data_gen(data_range: range):
    if (type(data_range) == range):
        # print(data_range.start)
        # print(data_range.stop)
        # print(data_range.step)
        return random.randrange(data_range.start, data_range.stop, data_range.step)
    else:
        raise TypeError('El argumento data_range debe ser un valor de tipo ' + range.__name__)    

# def random_int_from_ranges_data_gen(data_ranges_list: list):
#     elements_count = 0
#     if type(data_ranges_list) != list:
#         raise TypeError('El argumento data_ranges_list debe ser un valor de tipo ' + list.__name__ + ',' + 
#         ' con elementos de tipo ' + range.__name__)
#     if len(data_ranges_list) < 1:
#         raise ValueError('El argumento data_ranges_list debe ser un valor de tipo ' + list.__name__ +
#         ' que contenga al menos un elemento de tipo ' + range.__name__)
#     # for list_elem in range(0, len(data_ranges_list), 1):
#     for list_elem in data_ranges_list:
#         if type(list_elem) != range:
#             raise TypeError('Todos los elementos de la lista interval_tuples_list deben ser de tipo ' + range.__name__)        
#         # print(len(list_elem)) # IMPORTANTE: Este es el número de elementos de este iterable - una tupla.
#         # Esto permite saber cuántas veces se ejecuta un ciclo... Si el paso fuese fijo (no variable).
#         # elements_count += max_value - min_value + 1
#         elements_count += len(list_elem)        

#     chosen_range_index = 0
#     if len(data_ranges_list) >= 2:
#         # chosen_range_index = random.randint(0, len(data_ranges_list) - 1)
#         # Calcular la probabilidad de elegir cada uno de los rangos establecidos
#         probability_list = []
#         for list_elem in data_ranges_list:
#             # probability_list.append(Fraction(list_elem[1] - list_elem[0] + 1, elements_count))
#             probability_list.append(Fraction(len(list_elem), elements_count))
#         chosen_range_index = random.choices(list(range(0, len(data_ranges_list), 1)), weights=probability_list) # k = 1
    
#     # return random.randrange(data_ranges_list[chosen_range_index])
#     chosen_range = data_ranges_list[chosen_range_index[0]]
#     # return random.randrange(chosen_range)
#     return random.randrange(chosen_range.start, chosen_range.stop, chosen_range.step)

def random_float_from_closed_interval_data_gen(min_value: float, max_value: float):
    # Advertencia: El valor max_value puede o no incluirse en el rango de valores a escoger,
    #   dependiendo del redondeo de punto flotante que se hace en la operación min_value + (max_value-min_value) * random(),
    #   según la documentación oficial de Python 3.11 de la librería random.
    #   https://docs.python.org/3/library/random.html
    if type(min_value) != float:
        raise TypeError('El argumento min_value debe ser un valor de tipo ' + float.__name__)
    if type(max_value) != float:
        raise TypeError('El argumento max_value debe ser un valor de tipo ' + float.__name__)
    if min_value > max_value:
        raise ValueError('El argumento min_value debe ser menor o igual que max_value')

    return random.uniform(min_value, max_value)

def random_float_from_closed_interval_with_fixed_precision_data_gen(min_value: float, max_value: float, precision: int):
    # Advertencia: El valor max_value puede o no incluirse en el rango de valores a escoger,
    #   dependiendo del redondeo de punto flotante que se hace en la operación min_value + (max_value-min_value) * random(),
    #   según la documentación oficial de Python 3.11 de la librería random.
    #   https://docs.python.org/3/library/random.html
    if type(min_value) != float:
        raise TypeError('El argumento min_value debe ser un valor de tipo ' + float.__name__)
    if type(max_value) != float:
        raise TypeError('El argumento max_value debe ser un valor de tipo ' + float.__name__)
    if min_value > max_value:
        raise ValueError('El argumento min_value debe ser menor o igual que max_value')

    if type(precision) != int:
        raise TypeError('El argumento precision debe ser un valor de tipo ' + int.__name__)

    # Se esperaría que la precisión sea positivo o 0, aunque se permiten valores negativos en la función round de Python.
    return round(random.uniform(min_value, max_value), precision)

# def random_float_from_closed_interval_with_random_precision_data_gen(min_value: float, max_value: float, 
#     min_precision: int, max_precision: int):
#     # Advertencia: El valor max_value puede o no incluirse en el rango de valores a escoger,
#     #   dependiendo del redondeo de punto flotante que se hace en la operación min_value + (max_value-min_value) * random(),
#     #   según la documentación oficial de Python 3.11 de la librería random.
#     #   https://docs.python.org/3/library/random.html
#     if type(min_value) != float:
#         raise TypeError('El argumento min_value debe ser un valor de tipo ' + float.__name__)
#     if type(max_value) != float:
#         raise TypeError('El argumento max_value debe ser un valor de tipo ' + float.__name__)
#     if min_value > max_value:
#         raise ValueError('El argumento min_value debe ser menor o igual que max_value')

#     # Se esperaría que la precisión sea positivo o 0, aunque se permiten valores negativos en la función round de Python.
#     if type(min_precision) != int:
#         raise TypeError('El argumento min_precision debe ser un valor de tipo ' + int.__name__)
#     if type(max_precision) != int:
#         raise TypeError('El argumento max_precision debe ser un valor de tipo ' + int.__name__)
#     if min_precision > max_precision:
#         raise ValueError('El argumento min_precision debe ser menor o igual que max_precision')

#     precision = random.randint(min_precision, max_precision)    
#     return round(random.uniform(min_value, max_value), precision)

# def random_float_from_closed_intervals_data_gen(interval_tuples_list: list):
#     # Advertencia: No todos los elementos en cada uno de los intervalos tienen necesariamente la misma probabilidad de ser escogidos.
#     # Este posible podría, quizás, arreglarse en otro momento, pero no es una prioridad ahora mismo debido a su complejidad.
#     # elements_count = 0 # Contabilizar los elementos que puede generar random.uniform() es muy complejo ahora mismo.
#     # Alternativa: Establecer un peso según la distancia entre los números que definen un intervalo.
#     # Si la distancia entre dos números que definen un intervalo es mayor, se puede afirmar que hay más elementos en 
#     #   ese intervalo que en un intervalo donde la distancia entre esos dos números es menor.
#     # La magnitud de la distancia define, entonces, el peso que debería asignarse a cada intervalo para ser elegido, y mejorar
#     #   la probabilidad de que cada intervalo sea elegido, de manera que esté relacionado con la cantidad de elementos pertenecientes
#     #   a un intervalo.
#     distance_count = 0
#     if type(interval_tuples_list) != list:
#         raise TypeError('El argumento interval_tuples_list debe ser un valor de tipo ' + list.__name__ + ',' + 
#         ' con elementos de tipo ' + tuple.__name__)
#     if len(interval_tuples_list) < 1:
#         raise ValueError('El argumento interval_tuples_list debe ser un valor de tipo ' + list.__name__ +
#         ' que contenga al menos un elemento de tipo ' + tuple.__name__)
#     # for list_elem in range(0, len(interval_tuples_list), 1):
#     for list_elem in interval_tuples_list:
#         if type(list_elem) != tuple:
#             raise TypeError('Todos los elementos de la lista interval_tuples_list deben ser de tipo ' + tuple.__name__ +
#             ' y deben contener exactamente dos elementos: un valor mínimo y un valor máximo (ambos son valores de tipo float)')
#         if len(list_elem) != 2:
#             raise TypeError('Todos los elementos de la lista interval_tuples_list deben ser de tipo ' + tuple.__name__ +
#             ' y deben contener exactamente dos elementos: un valor mínimo y un valor máximo (ambos son valores de tipo float)')
#         count = 0 # 0: min_value, 1: max_value
#         min_value = 0
#         max_value = 0
#         # for tuple_elem in range(0, len(list_elem), 1):
#         for tuple_elem in list_elem:
#             if type(tuple_elem) != float:
#                 raise TypeError('Todos los elementos de la lista interval_tuples_list deben ser de tipo ' + tuple.__name__ +
#                 ' y deben contener exactamente dos números reales (tipo ' + float.__name__ + ')')
#             if count == 0:
#                 min_value = tuple_elem
#             if count == 1:
#                 max_value = tuple_elem
#             count += 1
#         if min_value > max_value:
#             raise ValueError('El primer elemento de cualquier tupla (min_value) de la lista interval_tuples_list debe ser ' + 
#             'menor o igual que el segundo elemento de la tupla (max_value).')
#         distance_count += max_value - min_value + 1

#     chosen_tuple_index = 0
#     if len(interval_tuples_list) >= 2:
#         # chosen_tuple_index = random.randint(0, len(interval_tuples_list) - 1)
#         # Calcular la probabilidad de elegir cada intervalo
#         probability_list = []        
#         for list_elem in interval_tuples_list:
#             probability_list.append(Fraction(float(list_elem[1] - list_elem[0] + 1) / distance_count)) # distance_count es float
#         chosen_tuple_index = random.choices(list(range(0, len(interval_tuples_list), 1)), weights=probability_list) # k = 1
    
#     # chosen_tuple_values = interval_tuples_list[chosen_tuple_index]
#     chosen_tuple_values = interval_tuples_list[chosen_tuple_index[0]]
#     return random.uniform(chosen_tuple_values[0], chosen_tuple_values[1])

# def random_float_from_closed_intervals_with_fixed_precision_data_gen(interval_tuples_list: list, precision: int):
#     # Advertencia: No todos los elementos en cada uno de los intervalos tienen necesariamente la misma probabilidad de ser escogidos.
#     # Este posible podría, quizás, arreglarse en otro momento, pero no es una prioridad ahora mismo debido a su complejidad.
#     # elements_count = 0 # Contabilizar los elementos que puede generar random.uniform() es muy complejo ahora mismo.
#     # Alternativa: Establecer un peso según la distancia entre los números que definen un intervalo.
#     # Si la distancia entre dos números que definen un intervalo es mayor, se puede afirmar que hay más elementos en 
#     #   ese intervalo que en un intervalo donde la distancia entre esos dos números es menor.
#     # La magnitud de la distancia define, entonces, el peso que debería asignarse a cada intervalo para ser elegido, y mejorar
#     #   la probabilidad de que cada intervalo sea elegido, de manera que esté relacionado con la cantidad de elementos pertenecientes
#     #   a un intervalo.
#     distance_count = 0
#     if type(interval_tuples_list) != list:
#         raise TypeError('El argumento interval_tuples_list debe ser un valor de tipo ' + list.__name__ + ',' + 
#         ' con elementos de tipo ' + tuple.__name__)
#     if len(interval_tuples_list) < 1:
#         raise ValueError('El argumento interval_tuples_list debe ser un valor de tipo ' + list.__name__ +
#         ' que contenga al menos un elemento de tipo ' + tuple.__name__)
#     # for list_elem in range(0, len(interval_tuples_list), 1):
#     for list_elem in interval_tuples_list:
#         if type(list_elem) != tuple:
#             raise TypeError('Todos los elementos de la lista interval_tuples_list deben ser de tipo ' + tuple.__name__ +
#             ' y deben contener exactamente dos elementos: un valor mínimo y un valor máximo (ambos son valores de tipo float)')
#         if len(list_elem) != 2:
#             raise TypeError('Todos los elementos de la lista interval_tuples_list deben ser de tipo ' + tuple.__name__ +
#             ' y deben contener exactamente dos elementos: un valor mínimo y un valor máximo (ambos son valores de tipo float)')
#         count = 0 # 0: min_value, 1: max_value
#         min_value = 0
#         max_value = 0
#         # for tuple_elem in range(0, len(list_elem), 1):
#         for tuple_elem in list_elem:
#             if type(tuple_elem) != float:
#                 raise TypeError('Todos los elementos de la lista interval_tuples_list deben ser de tipo ' + tuple.__name__ +
#                 ' y deben contener exactamente dos números reales (tipo ' + float.__name__ + ')')
#             if count == 0:
#                 min_value = tuple_elem
#             if count == 1:
#                 max_value = tuple_elem
#             count += 1
#         if min_value > max_value:
#             raise ValueError('El primer elemento de cualquier tupla (min_value) de la lista interval_tuples_list debe ser ' + 
#             'menor o igual que el segundo elemento de la tupla (max_value).')
#         distance_count += max_value - min_value + 1

#     # Se esperaría que la precisión sea positivo o 0, aunque se permiten valores negativos en la función round de Python.
#     if type(precision) != int:
#         raise TypeError('El argumento precision debe ser un valor de tipo ' + int.__name__)

#     chosen_tuple_index = 0
#     if len(interval_tuples_list) >= 2:
#         # chosen_tuple_index = random.randint(0, len(interval_tuples_list) - 1)
#         # Calcular la probabilidad de elegir cada intervalo
#         probability_list = []        
#         for list_elem in interval_tuples_list:
#             probability_list.append(Fraction(float(list_elem[1] - list_elem[0] + 1) / distance_count)) # distance_count es float
#         chosen_tuple_index = random.choices(list(range(0, len(interval_tuples_list), 1)), weights=probability_list) # k = 1
    
#     # chosen_tuple_values = interval_tuples_list[chosen_tuple_index]
#     chosen_tuple_values = interval_tuples_list[chosen_tuple_index[0]]
#     return round(random.uniform(chosen_tuple_values[0], chosen_tuple_values[1]), precision)

# def random_float_from_closed_intervals_with_random_precision_data_gen(interval_tuples_list: list, 
#     min_precision: int, max_precision: int):
#     # Advertencia: No todos los elementos en cada uno de los intervalos tienen necesariamente la misma probabilidad de ser escogidos.
#     # Este posible podría, quizás, arreglarse en otro momento, pero no es una prioridad ahora mismo debido a su complejidad.
#     # elements_count = 0 # Contabilizar los elementos que puede generar random.uniform() es muy complejo ahora mismo.
#     # Alternativa: Establecer un peso según la distancia entre los números que definen un intervalo.
#     # Si la distancia entre dos números que definen un intervalo es mayor, se puede afirmar que hay más elementos en 
#     #   ese intervalo que en un intervalo donde la distancia entre esos dos números es menor.
#     # La magnitud de la distancia define, entonces, el peso que debería asignarse a cada intervalo para ser elegido, y mejorar
#     #   la probabilidad de que cada intervalo sea elegido, de manera que esté relacionado con la cantidad de elementos pertenecientes
#     #   a un intervalo.
#     distance_count = 0
#     if type(interval_tuples_list) != list:
#         raise TypeError('El argumento interval_tuples_list debe ser un valor de tipo ' + list.__name__ + ',' + 
#         ' con elementos de tipo ' + tuple.__name__)
#     if len(interval_tuples_list) < 1:
#         raise ValueError('El argumento interval_tuples_list debe ser un valor de tipo ' + list.__name__ +
#         ' que contenga al menos un elemento de tipo ' + tuple.__name__)
#     # for list_elem in range(0, len(interval_tuples_list), 1):
#     for list_elem in interval_tuples_list:
#         if type(list_elem) != tuple:
#             raise TypeError('Todos los elementos de la lista interval_tuples_list deben ser de tipo ' + tuple.__name__ +
#             ' y deben contener exactamente dos elementos: un valor mínimo y un valor máximo (ambos son valores de tipo float)')
#         if len(list_elem) != 2:
#             raise TypeError('Todos los elementos de la lista interval_tuples_list deben ser de tipo ' + tuple.__name__ +
#             ' y deben contener exactamente dos elementos: un valor mínimo y un valor máximo (ambos son valores de tipo float)')
#         count = 0 # 0: min_value, 1: max_value
#         min_value = 0
#         max_value = 0
#         # for tuple_elem in range(0, len(list_elem), 1):
#         for tuple_elem in list_elem:
#             if type(tuple_elem) != float:
#                 raise TypeError('Todos los elementos de la lista interval_tuples_list deben ser de tipo ' + tuple.__name__ +
#                 ' y deben contener exactamente dos números reales (tipo ' + float.__name__ + ')')
#             if count == 0:
#                 min_value = tuple_elem
#             if count == 1:
#                 max_value = tuple_elem
#             count += 1
#         if min_value > max_value:
#             raise ValueError('El primer elemento de cualquier tupla (min_value) de la lista interval_tuples_list debe ser ' + 
#             'menor o igual que el segundo elemento de la tupla (max_value).')
#         distance_count += max_value - min_value + 1

#     # Se esperaría que la precisión sea positivo o 0, aunque se permiten valores negativos en la función round de Python.
#     if type(min_precision) != int:
#         raise TypeError('El argumento min_precision debe ser un valor de tipo ' + int.__name__)
#     if type(max_precision) != int:
#         raise TypeError('El argumento max_precision debe ser un valor de tipo ' + int.__name__)
#     if min_precision > max_precision:
#         raise ValueError('El argumento min_precision debe ser menor o igual que max_precision')

#     chosen_tuple_index = 0
#     if len(interval_tuples_list) >= 2:
#         # chosen_tuple_index = random.randint(0, len(interval_tuples_list) - 1)
#         # Calcular la probabilidad de elegir cada intervalo
#         probability_list = []        
#         for list_elem in interval_tuples_list:
#             probability_list.append(Fraction(float(list_elem[1] - list_elem[0] + 1) / distance_count)) # distance_count es float
#         chosen_tuple_index = random.choices(list(range(0, len(interval_tuples_list), 1)), weights=probability_list) # k = 1

#     # chosen_tuple_values = interval_tuples_list[chosen_tuple_index]
#     chosen_tuple_values = interval_tuples_list[chosen_tuple_index[0]]
#     precision = random.randint(min_precision, max_precision)
#     return round(random.uniform(chosen_tuple_values[0], chosen_tuple_values[1]), precision)

def random_strict_bool_data_gen():
    # Sólo hay dos valores tipo bool que se admiten: True o False
    possible_values = [True, False]
    return random.choice(possible_values)

# d) Generadores de 1 valor fijo no aleatorio, seleccionado de una forma repetible de una lista dada por el usuario, 
#   siguiendo un orden de selección desde el elemento del índice 0 hasta el del índice n, para n casos de prueba. 
#   Si la lista se agota, y se vuelve a llamar a esta función desde la misma instancia de clase, entonces se retornará 
#   nuevamente el elemento del índice 0.
def fixed_sequential_str_data_from_list_gen(possible_input_values_list: list, fsidg_index_item: list):
    returned_values = FixedSequenceBasedInputDataGenerator(possible_input_values_list, str, 
                                                           fsidg_index_item[0]).get_next_value_and_index()
    fsidg_index_item.clear()
    fsidg_index_item.append(returned_values[1])
    return returned_values[0]

def fixed_sequential_int_data_from_list_gen(possible_input_values_list: list, fsidg_index_item: list):
    returned_values = FixedSequenceBasedInputDataGenerator(possible_input_values_list, int, 
                                                           fsidg_index_item[0]).get_next_value_and_index()
    fsidg_index_item.clear()
    fsidg_index_item.append(returned_values[1])
    return returned_values[0]

def fixed_sequential_float_data_from_list_gen(possible_input_values_list: list, fsidg_index_item: list):
    returned_values = FixedSequenceBasedInputDataGenerator(possible_input_values_list, float, 
                                                           fsidg_index_item[0]).get_next_value_and_index()
    fsidg_index_item.clear()
    fsidg_index_item.append(returned_values[1])
    return returned_values[0]

def fixed_sequential_strict_bool_data_from_list_gen(possible_input_values_list: list, fsidg_index_item: list):
    returned_values = FixedSequenceBasedInputDataGenerator(possible_input_values_list, bool, 
                                                           fsidg_index_item[0]).get_next_value_and_index()
    fsidg_index_item.clear()
    fsidg_index_item.append(returned_values[1])
    return returned_values[0]

# e) Función generadora compleja que acepta 1 o más funciones generadoras simples (con sus respectivos parámetros),
#   las cuales son usadas 1 o más veces antes de usar la siguiente función generadora simple. Cuando todas las funciones
#   generadoras simples se han ejecutado las veces que fueron especificadas, entonces se volverá a usar la primera función
#   generadora simple, y se usará las mismas veces que fueron establecidas y aplicadas antes.
def complex_str_data_gen(cidg_index_item: list, *functions):
    # Al pasar 1 solo argumento en para el parámetro *functions, no se envía una tupla.
    # En cambio, al pasar 2 o más argumentos, sí se envía una tupla.
    # Una forma de controlar estos casos para estandarizar la forma de presentación de los parámetros de funciones
    #   generadoras es convirtiéndolos a tuplas.
    # sent_functions = functions
    # if type(functions) != tuple:
    #     sent_functions = (functions)
    # returned_values = ComplexInputDataGenerator(str, cidg_index_item[0], sent_functions).get_next_value_and_index()
    returned_values = ComplexInputDataGenerator(str, cidg_index_item[0], functions).get_next_value_and_index()
    cidg_index_item.clear()
    cidg_index_item.append(returned_values[1])
    return returned_values[0]

def complex_int_data_gen(cidg_index_item: list, *functions):
    returned_values = ComplexInputDataGenerator(int, cidg_index_item[0], functions).get_next_value_and_index()
    cidg_index_item.clear()
    cidg_index_item.append(returned_values[1])
    return returned_values[0]

def complex_float_data_gen(cidg_index_item: list, *functions):
    returned_values = ComplexInputDataGenerator(float, cidg_index_item[0], functions).get_next_value_and_index()
    cidg_index_item.clear()
    cidg_index_item.append(returned_values[1])
    return returned_values[0]

def complex_strict_bool_data_gen(cidg_index_item: list, *functions):
    returned_values = ComplexInputDataGenerator(bool, cidg_index_item[0], functions).get_next_value_and_index()
    cidg_index_item.clear()
    cidg_index_item.append(returned_values[1])
    return returned_values[0]