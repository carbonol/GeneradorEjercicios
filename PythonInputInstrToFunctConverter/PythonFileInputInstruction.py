class PythonFileInputInstruction:
    
    # def __init__(self, input_type=None, input_line=None, number_in_line=None,\
    #      string_representation=None, variable_name=None, variable_line=None, \
    #         instruction_lines=None): # Constructor (Vacío o no vacío)
    #     # Aquí se definen atributos únicos a cada instancia de clase.
    #     self.input_type = input_type
    #     self.input_line = input_line
    #     self.number_in_line = number_in_line
    #     self.string_representation = string_representation
    #     self.variable_name = variable_name
    #     self.variable_line = variable_line
    #     self.instruction_lines = instruction_lines

    def __init__(self, input_line=None, input_type=None, string_representation=None, variable_name=None): # Constructor (Vacío o no vacío)
        # Aquí se definen atributos únicos a cada instancia de clase.
        self.input_type = input_type
        self.input_line = input_line
        # self.number_in_line = number_in_line
        self.string_representation = string_representation
        self.variable_name = variable_name
        # self.variable_line = variable_line
        # self.instruction_lines = instruction_lines

    # Getters
    def get_input_type(self):
        return self.input_type

    def get_input_line(self):
        return self.input_line

    # def get_number_in_line(self):
    #     return self.number_in_line

    def get_string_representation(self):
        return self.string_representation

    def get_variable_name(self):
        return self.variable_name

    # def get_variable_line(self):
    #     return self.variable_line

    # def get_instruction_lines(self):
    #     return self.instruction_lines

    # Setters
    def set_input_type(self, input_type):
        self.input_type = input_type

    def set_input_line(self, input_line):
        self.input_line = input_line

    # def set_number_in_line(self, number_in_line):
    #     self.number_in_line = number_in_line

    def set_string_representation(self, string_representation):
        self.string_representation = string_representation

    def set_variable_name(self, variable_name):
        self.variable_name = variable_name

    # def set_variable_line(self, variable_line):
    #     self.variable_line = variable_line

    # def set_instruction_lines(self, instruction_lines):
    #     self.instruction_lines = instruction_lines

    # Subrutina para imprimir en pantalla los atributos de una instancia de clase. => Esta subrutina debería usarse para pruebas.
    def print_json_representation(self): # Impresión en pantalla de todos los valores de los atributos de esta clase en formato JSON.
        print('{')
        print('\tinput_type: ',self.input_type,',',sep='')
        print('\tinput_line: ',self.input_line,',',sep='')
        # print('\tnumber_in_line: ',self.number_in_line,',',sep='')
        print('\tstring_representation: ',self.string_representation,',',sep='')
        print('\tvariable_name: ',self.variable_name,sep='')
        # print('\tvariable_line: ',self.variable_line,',',sep='')
        # print('\tinstruction_lines: ',self.instruction_lines,sep='')
        print('}')

# input_instruction = PythonFileInputInstruction()
# input_instruction.print_json_representation()