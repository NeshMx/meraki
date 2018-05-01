import random


class Matrix(object):
    '''
    Class that defines the matrix structure and some methods to interact with them.
    '''

    def __init__(self, size, input_matrix=[]):
        self.size = size
        if input_matrix == []:
            self.generate_matrix()
        else:
            self.matrix = input_matrix

    def __str__(self):
        matrix_string = ''
        for row in self.matrix:
            for element in row:
                matrix_string += str(element) + ' | '
            matrix_string = matrix_string[:-3] + \
                '\n' + ('- - ' * self.size)[:-2] + '\n'
        return ('- - ' * self.size)[:-2] + '\n' + matrix_string

    def generate_matrix(self):
        self.matrix = [[random.randint(0, 4) for j in range(
            self.size)] for i in range(self.size)]

    def create_matrix_manually(self):
        pass

    def min_algorithm(self, numbers):
        min_num = None
        min_counter = 0
        for key, value in numbers.items():
            if min_num == None:
                min_num = key
                min_counter = value
            elif value > min_counter:
                min_num = key
                min_counter = value
            elif value == min_counter and key < min_num:
                min_num = key
                min_counter = value
        return min_num

    def max_algorithm(self, numbers):
        max_num = None
        max_counter = 0
        for key, value in numbers.items():
            if max_num == None:
                max_num = key
                max_counter = value
            elif value > max_counter:
                max_num = key
                max_counter = value
            elif value == max_counter and key > max_num:
                max_num = key
                max_counter = value
        return max_num

    def travel_neighbors(self, x, y):
        numbers = {}
        for i in range(3):
            for j in range(3):
                x_pos = x + i - 1
                y_pos = y + j - 1
                if x_pos >= 0 and y_pos >= 0 and x_pos < self.size and y_pos < self.size:
                    tmp_num = self.matrix[x_pos][y_pos]
                    if not tmp_num in numbers:
                        numbers.update({tmp_num: 1})
                    else:
                        numbers[tmp_num] += 1
        return numbers

    def travel_matrix(self):
        '''
        Method for visiting each matrix cell and apply the needed algorithms.
        '''
        min_algorithm_matrix = []
        max_algorithm_matrix = []
        for x in range(self.size):
            tmp_min_row = []
            tmp_max_row = []
            for y in range(self.size):
                numbers = self.travel_neighbors(x, y)
                tmp_min_row.append(self.min_algorithm(numbers))
                tmp_max_row.append(self.max_algorithm(numbers))
            min_algorithm_matrix.append(tmp_min_row)
            max_algorithm_matrix.append(tmp_max_row)
        min_matrix = Matrix(size=len(min_algorithm_matrix[0]), input_matrix=min_algorithm_matrix)
        max_matrix = Matrix(size=len(max_algorithm_matrix[0]), input_matrix=max_algorithm_matrix)
        print('Algoritmo con valores mínimos: \n')
        print(min_matrix)
        print('Algoritmo con valores máximos: \n')
        print(max_matrix)


if __name__ == '__main__':
    matrix_size = int(input('Ingrese el tamaño de la matriz: '))
    matrix = Matrix(matrix_size)
    print(matrix)
    matrix.travel_matrix()
