from matrix import Matrix

class Application:
    @staticmethod
    def mainMenu():
        matrix_obj = Matrix()
        matrix = []

        while True:
            print("\n\nMenu:")
            print("1. Input matrix")
            print("2. Compute determinant")
            print("3. Transpose matrix")
            print("4. Rank of matrix")
            print("5. Print current matrix")
            print("6. Exit")

            choice = input("Select the menu item: ")

            if choice == "1":
                matrix = matrix_obj.inputMatrix()

            elif choice == "2":
                matrix_to_use = matrix if matrix else matrix_obj.matrix
                print('\nDeterminant: ', matrix_obj.matrixDeterminant(matrix_to_use))

            elif choice == "3":
                print('\nTranspose matrix:')
                transposed = matrix_obj.transposeMatrix()

            elif choice == "4":
                matrix_to_use = matrix if matrix else matrix_obj.matrix
                print('\nRank: ', matrix_obj.computeRank(matrix_to_use))

            elif choice == "5":
                if matrix:
                    matrix_obj.printMatrix(matrix)
                else:
                    matrix_obj.printMatrix(matrix_obj.matrix)
    
            elif choice == "6":
                print("\nProgram is finished")
                #exit(code = 200)


