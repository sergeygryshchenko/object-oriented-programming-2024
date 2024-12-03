from communicator import TCommunicator  
from common import Messages, Modes
from rational import TRational
from complex import TComplex
from square_matrix import TSquareMatrix

class TApplication:
    def __init__(self):
        self.communicator = TCommunicator("localhost", 10001, "localhost", 10000) 
        self.matrix = TSquareMatrix()
        self.work = True
        while self.work: 
            msg=self.communicator.receive()
            print(msg)
            self.answer(msg)
            if not self.work:
                break 
        
   
    def to_communicator(self, msg):
        self.communicator.send(msg)

    def from_communicator(self):
        return self.communicator.receive()

    def answer(self,msg):
        split_msg = msg.split()
        mode = split_msg[0]
        msg = split_msg[1]
        if mode == str(Modes.F_MODE.value) :
            if self.matrix.num_type != float:
                self.matrix = TSquareMatrix(num_type= float)
            if msg == str(Messages.INPUT_MATRIX.value) :
                msg = "Enter dimension:"
                self.to_communicator(msg)
                dimension=self.from_communicator()
                self.matrix.parseMatrix(self.from_communicator())
            if msg == str(Messages.FIND_DETERMINANT.value):
                msg = str(self.matrix.matrixDeterminant(self.matrix.matrix))
                self.to_communicator(msg)
                print('deter')
            if msg == str(Messages.TRANSPOSE_MATRIX.value) :
                transposed=self.matrix.transposeMatrix()
                msg = "\n".join(" ".join(map(str, row)) for row in transposed)
                self.to_communicator(msg)
            if msg == str(Messages.FIND_RANK_OF_MATRIX.value):
                msg = str(self.matrix.computeRank(self.matrix.matrix))
                self.to_communicator(msg)
                print('rank')
            if msg == str(Messages.PRINT_CURRENT_MATRIX.value):
                msg = "\n".join(" ".join(map(str, row)) for row in self.matrix.matrix)
                self.to_communicator(msg)
            if msg == str(Messages.EXIT.value):
                self.to_communicator(msg)
                print("Сервер закончил работу")
                self.work = False

        if mode == str(Modes.C_MODE.value) :
            if self.matrix.num_type != TComplex:
                self.matrix = TSquareMatrix(num_type= TComplex)
            if msg == str(Messages.INPUT_MATRIX.value) :
                msg = "Enter dimension:"
                self.to_communicator(msg)
                dimension=self.from_communicator()
                self.matrix.parseMatrix(self.from_communicator())
            if msg == str(Messages.FIND_DETERMINANT.value):
                msg = str(self.matrix.matrixDeterminant(self.matrix.matrix))
                self.to_communicator(msg)
                print('deter')
            if msg == str(Messages.TRANSPOSE_MATRIX.value) :
                transposed=self.matrix.transposeMatrix()
                msg = "\n".join(" ".join(map(str, row)) for row in transposed)
                self.to_communicator(msg)
            if msg == str(Messages.FIND_RANK_OF_MATRIX.value):
                msg = str(self.matrix.computeRank(self.matrix.matrix))
                self.to_communicator(msg)
                print('rank')
            if msg == str(Messages.PRINT_CURRENT_MATRIX.value):
                msg = "\n".join(" ".join(map(str, row)) for row in self.matrix.matrix)
                self.to_communicator(msg)
            if msg == str(Messages.EXIT.value):
                self.to_communicator(msg)
                print("Сервер закончил работу")
                self.work = False

        if mode == str(Modes.R_MODE.value) :
            if self.matrix.num_type != TRational:
                self.matrix = TSquareMatrix(num_type= TRational)
            if msg == str(Messages.INPUT_MATRIX.value) :
                msg = "Enter dimension:"
                self.to_communicator(msg)
                dimension=self.from_communicator()
                self.matrix.parseMatrix(self.from_communicator())
            if msg == str(Messages.FIND_DETERMINANT.value):
                msg = str(self.matrix.matrixDeterminant(self.matrix.matrix))
                self.to_communicator(msg)
                print('deter')
            if msg == str(Messages.TRANSPOSE_MATRIX.value) :
                transposed=self.matrix.transposeMatrix()
                msg = "\n".join(" ".join(map(str, row)) for row in transposed)
                self.to_communicator(msg)
            if msg == str(Messages.FIND_RANK_OF_MATRIX.value):
                msg = str(self.matrix.computeRank(self.matrix.matrix))
                self.to_communicator(msg)
                print('rank')
            if msg == str(Messages.PRINT_CURRENT_MATRIX.value):
                msg = "\n".join(" ".join(map(str, row)) for row in self.matrix.matrix)
                self.to_communicator(msg)
            if msg == str(Messages.EXIT.value):
                self.to_communicator(msg)
                print("Сервер закончил работу")
                self.work = False


    