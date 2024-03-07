# Matrix

Evaluate matrix expressions in Python.

# Run the program

- Windows
```bash
python matrix.py
```

- Mac/Linux
```bash
python3 matrix.py
```

# Commands and Usage

## Create matrix:
    CREATE MATRIX
    *Enter name*: {name_of_matrix}
    *Enter order*: mxn
    *Enter row 1*: [a(1,1) a(1, 2) ... a(1, n)]
    .
    .
    *Enter row m* 

## Display matrix:
    DISPLAY MATRIX {name_of_matrix}
        
## Index matrix:
    INDEX MATRIX {name_of_matrix} x(int) y(int)

## Evaluate matrix expressions:
    EVAL {expression}

## Add matrices:
    EVAL C=A+B+..

## Subtract matrices:
    EVAL C=A-B-..

## Multiply matrices:
    EVAL C=AxBx..

## Transpose of matrix:
    TRANSPOSE MATRIX B=A
> here, B becomes the transpose matrix of A

# Logic
- What is the logic for matrix addition?
> For two matrices `A = [aᵢⱼ]ₘₓₙ` and `B = [bᵢⱼ]ₘₓₙ`, `A + B = [aᵢⱼ + bᵢⱼ]ₘₓₙ`
> Order of both matrices should be the same

- What is the logic for matrix subtraction?
> For two matrices `A = [aᵢⱼ]ₘₓₙ` and `B = [bᵢⱼ]ₘₓₙ`, `A - B = [aᵢⱼ - bᵢⱼ]ₘₓₙ`
> Order of both matrices should be the same

- What is the logic for matrix multiplication?
> For two matrices `A = [aᵢⱼ]ₘₓₙ` and `B = [bⱼₖ]ₙₓₚ`, `A x B = C`
> Here, `C = [cᵢₖ]ₘₓₚ` where `cᵢₖ ` is sum of product of iᵗʰ row of A and kᵗʰ column of B
> Number of columns of A should be the same as number of rows of B [n = n]

> [!NOTE]
> You can contribute to this repository by [creating a pull request](https://github.com/UnrealFar/Matrix/pulls)
