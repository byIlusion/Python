from random import randint

class Matrix:
    def __init__(self, matrix=[]):
        self.matrix = matrix

    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, matrix):
        self.__matrix = matrix

    def rand_matrix(self, x=2, y=2, start=0, stop=100):
        self.matrix = [[randint(start, stop) for m in range(y)] for n in range(x)]

    def __str__(self):
        matrix_str = "" if len(self.__matrix) else "Matrix is empty!"
        for i, n in enumerate(self.__matrix):
            for m in n:
                matrix_str += f"{m:>8}"
            matrix_str += "\n" if i < len(self.__matrix) - 1 else ""
        return matrix_str

    def __add__(self, other):
        try:
            if self.size_eq(other):
                return Matrix([[m + other.matrix[i][j] for j, m in enumerate(n)] for i, n in enumerate(self.__matrix)])
            else:
                raise Exception
        except:
            print("Ошибка! Сложение не имеет смысла, т.к. матрицы разного размера")

    def size_eq(self, other):
        if len(self.__matrix) != len(other.matrix):
            return False
        for i, n in enumerate(self.__matrix):
            if len(n) != len(other.matrix[i]):
                return False
        return True


m_1 = Matrix()
print(f"Матрица 1 в виде массива: {m_1.matrix}")
print(f"Матрица 1 (пустая):\n{m_1}")
m_1.rand_matrix(3, 3, stop=1000)
print(f"Матрица 1 в виде массива: {m_1.matrix}")
print(f"Матрица 1 (размер 3*3):\n{m_1}")
m_1.rand_matrix(2, 4, stop=10)
print(f"Матрица 1 (размер 2*4):\n{m_1}")

m_2 = Matrix([[31, 22], [37, 43], [51, 86]])
print(f"Матрица 2 в виде массива: {m_2.matrix}")
print(f"Матрица 2:\n{m_2}")

m_3 = Matrix()
m_3.rand_matrix(3, 2, -50, 50)
print(f"Матрица 3:\n{m_3}")

m_4 = m_2 + m_3
print(f"Матрица 4 (сумма матриц 2 и 3):\n{m_4}")
