
class NQueensProblem:

    #инициалиазация класса количеством ферзей
    def __init__(self, numOfQueens):
        self.numOfQueens = numOfQueens
    #получение числа ферзей
    def __len__(self):
        return self.numOfQueens
    #счетчик числа отклонений
    def getViolationsCount(self, positions):

        if len(positions) != self.numOfQueens:
            raise ValueError("size of positions list should be equal to ", self.numOfQueens)

        violations = 0

        # проход по каждой паре ферзей для поиска нахождения на одной диагонали:
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):

               
                column1 = i
                row1 = positions[i]

               
                column2 = j
                row2 = positions[j]

                if abs(column1 - column2) == abs(row1 - row2):
                    violations += 1

        return violations

   
def main():
    nQueens = NQueensProblem(8)

    solution = [1, 2, 7, 5, 0, 3, 4, 6]

    print("Number of violations = ", nQueens.getViolationsCount(solution))

    plot = nQueens.plotBoard(solution)
    plot.show()


if __name__ == "__main__":
    main()

