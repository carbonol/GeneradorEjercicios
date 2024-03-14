# GeneradorEjercicios
Este es un repositorio que alberga la implementación de un sistema de generación automática de ejercicios de programación que implican el uso del lenguaje Python (3.11.1). El código escrito aquí fue producto de un trabajo de tesis de maestría realizado por el autor de este mismo repositorio, y es un trabajo en progreso.

## Editores y Lenguajes Usados

Todos los módulos fueron originalmente implementados con Python 3.11.1, en el editor de Visual Studio Code en Windows 10.

## Componentes y Módulos

La implementación del sistema de generación automática de ejercicios de programación en Python mostrado en este repositorio consta de 6 módulos principales.

1. **PythonInputInstrToFunctConverter**: Convierte las instrucciones de lectura del código base y de los códigos de variantes en funciones generadoras dadas por el usuario. Esto corresponde al paso 1 de la fase de ensamblaje del sistema de generación de ejercicios.
2. **CodeAssembler**: Ensamblador de variantes de código en el código base. Esto corresponde al paso 2 de la fase de ensamblaje del sistema de generación de ejercicios.
3. **DDFilesGenerator**: Permite generar archivos de niveles de dificultad base y de variantes, y los enunciados de variantes (considerados en esta implementación como descriptores). Este módulo podría considerarse una extensión de la fase de diseño del sistema de generación de ejercicios, aunque en esta implementación se diseñó que este módulo fuese usado después de haber generado el código de los ejercicios resultantes, porque en ese momento ya se sabe cuántos ejercicios resultantes se generaron, y eso permite saber cuántas veces hay que preguntar al usuario por niveles de dificultad y por enunciados de variantes. Al mismo tiempo, este módulo también permite generar los archivos de nivel de dificultad resultantes: esto corresponde al paso 3 de la fase de ensamblaje del sistema de generación de ejercicios. En cuanto al paso 4 de esta fase, que es el ensamblaje de enunciados, esta implementación realiza el primer paso interno de unificación de enunciados de variantes por cada ejercicio resultante, según las variantes utilizadas para generar esos ejercicios, pero no realiza el segundo paso interno, que es el ensamblaje de enunciados unificados de variantes en el enunciado base para generar los enunciados de cada ejercicio resultante. En cambio, esto se había dejado en manos del sistema de práctica de la programación, el cual está albergado en otro repositorio. Por supuesto, este es un aspecto por mejorar.
4. **TestCaseBuildersGenerator**: Añade código a los códigos de ejercicios resultantes para habilitar el uso de las funciones generadoras al ejecutar estos códigos, y al mismo tiempo, automatizar la creación de datos de entrada para casos de prueba de estos ejercicios. Esto corresponde al paso 5 de la fase de ensamblaje del sistema.
5. **TestCaseGenerator**: Permite la ejecución de códigos de ejercicios resultantes para crear sus casos de prueba de forma automática, dependiendo del número de casos de prueba que indique el usuario. Además, puede crear un archivo de visibilidad de casos de prueba para cada ejercicio resultante, según el criterio del usuario. Esto corresponde a la fase de creación de casos de prueba del sistema de generación automática de ejercicios.
6. **ExerciseFilesGenerator**: Aunque su nombre pareciere indicar que genera nuevos archivos de niveles de dificultad y de enunciados de variantes (considerados en esta implementación como descriptores), en realidad sólo hace una copia de estos archivos generados anteriormente, reubicándolos en los directorios de cada ejercicio resultante.

## PythonInputInstrToFunctConverter
Este componente consta de 4 módulos:

1. **python_input_instr_to_funct_converter.py**: Módulo principal del componente PythonInputInstrToFunctConverter. 
2. **python_input_instr_identifier.py**: Contiene utilidades que sirven principalmente para poder identificar ínstrucciones de lectura en líneas de código escritas en Python.
3. **PythonFileInputInstruction.py**: Clase que representa una instrucción de lectura encontrada en un archivo de código fuente de Python (.py)
4. **input_data_generators.py**: Módulo de funciones generadoras que pueden utilizar los usuarios (profesores) para reemplazar instrucciones de lectura. En particular, el uso de funciones generadoras complejas, que combina el uso de funciones generadoras que generan valores fijos, aleatorios o basados en un patrón para mejorar la automatización de la creación de casos de prueba, es una idea en progreso.

## CodeAssembler
Este componente consta de 2 módulos:

1. **assembler.py**: Módulo principal del componente CodeAssembler.
2. **print_combinations_list.py**: Módulo que permite hallar las combinaciones posibles que se pueden crear con un número finito de elementos repetibles en un vector o lista. Este módulo se usa principalmente en la combinación de variantes de código en el código base.

## Los demás componentes
En cuanto a los 4 componentes restantes, cada uno consta de 1 solo módulo:

1. **DDFilesGenerator**: **dd_files_generator.py**
2. **TestCaseBuildersGenerator**: **test_case_builders_generator.py**
3. **TestCaseGenerator**: **test_case_generator.py**
4. **ExerciseFilesGenerator**: **exercise_files_generator.py**

## Cómo usar estos módulos

Estos módulos se pueden ejecutar con un intérprete de Python. En general, para usar o probar la implementación en Python del sistema de generación automática de ejercicios, se deben ejecutar los módulos principales de cada componente, en el orden dado en la sección de **Componentes y Módulos**.

En la ejecución de los módulos, se debe tener en cuenta que emplea una estructura de archivos inicial para comenzar a trabajar con el primer módulo, además de que en ciertos casos se debe revisar y hacer modificaciones al código fuente para cambiar las rutas de algunos directorios, e incluso, es posible que se deba cambiar algunas palabras clave en el código, como por ejemplo, el nombre del intérprete de Python dado en Windows (en el cmd; e.g. python), en caso de que este llegase a ser diferente en algunos equipos. Este asunto de parametrización puede ser un aspecto por mejorar de la implementación. En todo caso, se dejan varios archivos de texto, entre otros, en el repositorio, que pueden servir como guía para saber cómo se deben usar estos módulos, y qué se puede esperar de ellos cuando se ejecutan. Además, en el repositorio se dejan algunos ejemplos de datos base de ejercicios de programación que pueden servir para probar el sistema incluido en este repositorio. También es pertinente mencionar que esta implementación aún no se ha probado en Linux, y es posible que deban realizarse modificaciones al código si se quiere hacer la prueba con otro sistema operativo.

### Documentación

Los archivos **tests.txt** y **tests_results.txt**, especialmente en las secciones de *Preparación para la prueba* en el primer archivo, y *4.1) ¿Qué datos necesita el sistema para ser usado?* en el segundo, pueden ser utilizados como guía para saber cómo usar o probar la implementación. Por otro lado, en **tests_results.txt** se puede visualizar un ejemplo de mensajes de ejecución al utilizar cada módulo.

### Ejemplos de diseño de ejercicios

Para probar ejercicios, se pueden utilizar los documentos PDF, y los archivos **exercise1_design.txt** y **exercise5_design.txt** para tener una mejor idea de cómo diseñar ejercicios antes de usar el sistema.

Además, los directorios **test_files** contiene las estructuras de archivos iniciales necesarias para generar ejercicios resultantes a partir de variantes en el sistema. Los directorios exercise1 y exercise5 continen información completa, pero aún falta añadir la información relevante para los demás. El directorio **generated_files** contiene ejemplos de estructuras de directorio generadas con los ejercicios resultantes para los casos de exercise1 y exercise5 (cuando estos fueron utilizados como problemas raíz o base).

## Licencia

MIT.

## Autor

Leandro Alejandro Niebles Carbonó (GitHub: carbonol).
