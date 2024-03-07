from __future__ import annotations

from typing import List, Tuple, Dict, Optional

class OrderError(Exception):
    ...

class Matrix:
    MATRICES: Dict[str, Matrix] = {}

    def __init__(self, name: str, order: Tuple[int], rows: List[List[int]]) -> None:
        self.name: str = name
        self.order: Tuple[int] = order
        self.rows: List[List[int]] = rows
        self.columns: List[List[int]] = [[r[i] for r in self.rows] for i in range(self.order[1])]
        if len(self.rows) != self.order[0]:
            raise OrderError("Number of rows should be same as given in order")
        if len(self.columns) != self.order[1]:
            raise OrderError("Number of column should be same as given in order")

    def __str__(self) -> str:
        rows = [list(map(str, row)) for row in self.rows]
        ret = "┏ " + " ".join(rows.pop(0)) + " ┓\n"
        lrow = rows.pop()
        for row in rows:
            ret += "┃ " + " ".join(row) + " ┃\n"
        ret += "┗ " + " ".join(lrow) + " ┛"
        return ret

    def index(self, x: int, y: int):
        return self.rows[x-1][y-1]

    def add(self, name: str, other: Matrix) -> Matrix:
        if self.order != other.order:
            raise OrderError("Order of both matrices should be same!")
        rows = [[self.rows[r][c] + other.rows[r][c] for c in range(self.order[1])] for r in range(self.order[0])]
        return Matrix(name, self.order, rows)

    def subtract(self, name: str, other: Matrix) -> Matrix:
        if self.order != other.order:
            raise OrderError("Order of both matrices should be same!")
        rows = [[self.rows[r][c] - other.rows[r][c] for c in range(self.order[1])] for r in range(self.order[0])]
        return Matrix(name, self.order, rows)

    def multiply(self, name: str, other: Matrix) -> Matrix:
        if self.order[1] != other.order[0]:
            raise OrderError("Number of columns in first matrix should be same as number of rows in second matrix")
        rows = [[sum(self.rows[i][k] * other.rows[k][j] for k in range(self.order[1])) for j in range(other.order[1])] for i in range(self.order[0])]
        return Matrix(name, (self.order[0], other.order[1]), rows)

    def transpose(self, name) -> Matrix:
        return Matrix(name, self.order[::-1], self.columns)

def info():
    print("""
    Create matrix:     CREATE MATRIX
        *Enter name*: {name_of_matrix}
        *Enter order*: mxn
        *Enter row 1*: [a(1,1) a(1, 2) ... a(1, n)]
        .
        .
        *Enter row m* 

    Display matrix:    DISPLAY MATRIX {name_of_matrix}
          
    Index matrix:      INDEX MATRIX {name_of_matrix} x(int) y(int)

    Add matrices:      C=A+B+..

    Subtract matrices: C=A-B-..

    Multiply matrices: C=AxBx..
          
    Transpose matrix:  TRANSPOSE {new_name}={old_name}
    """
    )

def create_matrix():
    name: str = input("Enter name of matrix: ")
    order: Tuple[int] = input("Enter order: ").split("x")
    r, c = int(order[0]), int(order[1])
    rows = []
    for i in range(1, r+1):
        row = [int(e) for e in input(f"Enter row {i}: ").replace("[", "").replace("]", "").split()]

        if len(row) != c:
            print("Row is not equal to the max length given in order")
            return
        rows.append(row)
    matrix = Matrix(name, (r, c), rows)
    Matrix.MATRICES[name] = matrix
    return matrix

while True:
    inp = input("What do you want to do? ").strip()
    if inp.upper() == "INFO":
        info()
        continue

    if inp.upper() == "CREATE MATRIX":
        create_matrix()
        continue

    if inp.upper().startswith("DISPLAY MATRIX"):
        matrix = Matrix.MATRICES.get(inp.split(" ")[-1])
        if not matrix:
            print("Matrix with that name was not found")
        print(matrix)
        continue

    if inp.upper().startswith("INDEX MATRIX"):
        spl = inp.split(" ")
        name, x, y = spl[-3], spl[-2], spl[-1]
        matrix = Matrix.MATRICES.get(name)
        if matrix:
            print(matrix.index(int(x), int(y)))
        else:
            print("Matrix with that name was not found")

    if inp.upper().startswith("EVAL"):
        new, exp = inp.split(" ",1)[1].split("=")
        matrix: Optional[Matrix] = None
        ms = list(exp)
        i = 0
        while i<len(ms):
            m = ms[i]
            if m not in "+-x/":
                matrix = Matrix.MATRICES[m]
            if m == "+":
                i+=1
                nm = Matrix.MATRICES[ms[i]]
                matrix = matrix.add(new, nm)
                Matrix.MATRICES[new] = matrix
            if m == "-":
                i+=1
                nm = Matrix.MATRICES[ms[i]]
                matrix = matrix.subtract(new, nm)
                Matrix.MATRICES[new] = matrix
            if m == "x":
                i+=1
                nm = Matrix.MATRICES[ms[i]]
                matrix = matrix.multiply(new, nm)
                Matrix.MATRICES[new] = matrix
            i+=1
        print(matrix)
        continue

    if inp.upper().startswith("TRANSPOSE"):
        e = inp.split(" ")[-1].split("=")
        new, old = e
        matrix = Matrix.MATRICES.get(old)
        if not matrix:
            print("Matrix with that name was not found")
            continue
        new = matrix.transpose(new)
        Matrix.MATRICES[new.name] = matrix
        print(new)

    if inp.upper() == "SHOW MATRICES":
        for k, v in Matrix.MATRICES.items():
            print(k, "=", v)
        continue

    if inp.upper() == "EXIT":
        print("Goodbye!")
        break
