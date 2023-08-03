class myMatrix:

    def __init__(self, n, m):
        if( n <= 0):
            raise ValueError("Rows should be greater than 0.")
        elif(n > 500000):
            raise ValueError("Rows should be less than or equal to 500,000.")
        elif(m <= 0):
            raise ValueError("Columns should be greater than 0.")
        elif(m > 500000):
            raise ValueError("Columns should be less than or equal to 500,000.")
        else:
            self.matrix = self.constructMatrix(n,m)
    
    def constructMatrix(self, n, m):
        matrix = [[0 for columns in range(m)] for rows in range(n)]

        for rows in range(len(matrix)):
            for columns in range(len(matrix[rows])):
                matrix[rows][columns] = (rows+1)*(columns+1)
        return matrix

    def printMatrix(self, matrix):
        output = []
        for row in matrix:
            output.append(str(row))
        return '\n'.join(output)

    def __len__(self):
        return len(self.matrix)
    
    def __str__(self):
        return self.printMatrix(self.matrix)

    def multiply(self, other):
        second = len(other.matrix[0])
        first = len(self.matrix)
        matrix = [[0 for columns in range(second)] for rows in range(first)]

        for i in range(first):
            for j in range(second):
                matrix[i][j] = 0
                for k in range(len(other)):
                    matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return matrix
        
    def __pow__(self, power: int):
        matrix = [[0 for columns in range(len(self.matrix[0]))] for rows in range(len(self.matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = self.matrix[i][j]
        for i in range(power-1):
            for row in range(len(self.matrix)):
                for col in range(len(self.matrix[0])):
                    self.matrix[row][col] *= matrix[row][col]
        return self.printMatrix(self.matrix)

    def __mul__(self, other):
        if isinstance(other, int):
            return self.scalar(other)
        else:
            if(len(self.matrix[0]) == len(other)):
                return self.printMatrix(self.multiply(other))
            else:
                raise ValueError("Columns of the 1st matrix must equal rows of 2nd matrix.")

    def scalar(self, other):
        for row in range(len(self.matrix)):
                for col in range(len(self.matrix[0])):
                    self.matrix[row][col] *= other
        return self.printMatrix(self.matrix)
    
    def __truediv__(self, divisor: int):
        if(divisor == 0):
            raise ValueError("Cannot divide by zero. Please enter a non-zero number.")
        else:
            for row in range(len(self.matrix)):
                for col in range(len(self.matrix[0])):
                    self.matrix[row][col] /= divisor
            return self.printMatrix(self.matrix)

    def sum(self):
        value = 0

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                value += self.matrix[row][col]
        return value
    
def main():
    #zeroSizeMattrix = myMatrix(0,0)
    #tooLargeMatrix = myMatrix(500001, 500001)
    
    matrixTest = myMatrix(3, 3)
    matrixMult = myMatrix(3,2)
    
    print("Matrix test:")
    print(matrixTest)
    print("")
    
    print('Matrix scalar multiplied:')
    print(matrixTest*2)
    print("")
    
    print("Matrix scalar divided:")
    print(matrixTest/2)
    print("")
    
    print("Matrix sum:")
    print(matrixTest.sum())
    print("")
    
    print("Matrix pow: ")
    print(matrixTest**3)
    print("")
    
    print("Matrix multiplication:")
    matrixOther = myMatrix(2,3)

    matrixMultiplied = matrixOther*matrixMult

    print(matrixMultiplied)
    print("")

    
    """print("Matrix reverse multiplication: ")
    print(2*matrixMultiplied)"""
    
if __name__ == "__main__":
    main()
            
