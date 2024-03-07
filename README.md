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
- What is a matrix?

> Matrices are an ordered rectangular array of numbers(real or complex) or functions arranged into rows and columns. Example:

```
A = ┏1 2 3┓
    ┃4 5 6┃
    ┗7 8 9┛
```

> The horizontal lines are called rows and the vertical lines are called columns.
> Matrices are always represented usign capital letter.
> Matrices are represented by square or simple brackets.
> A matrix of order `mxn` is represented as `A = [aᵢⱼ]ₘₓₙ`.


- What is the order of matrix?
> It gives use the number of rows and columns of a matrix.
> For a matrix of `m` rows and `n` columns, its order is `mxn` and is read as `m by n`


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

- What is the transpose of a matrix?
> The transpose of a matrix can be obtaiend by interchainging rows and columns of a matrix.
> For a matrix `A = [aᵢⱼ]ₘₓₙ`, its transpose is `A' = [aⱼᵢ]ₙₓₘ`.
> For example,

```
A =  ┏1 2 3┓
     ┃4 5 6┃
     ┗7 8 9┛
```

then,

```
A' = ┏1 4 7┓
     ┃2 5 8┃
     ┗3 6 9┛
```


> [!NOTE]
> You can contribute to this repository by [creating a pull request](https://github.com/UnrealFar/Matrix/pulls)
