def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    rvan = [len(x) for x in mat]
    if len(set(rvan))!=1:
        raise ValueError
    return [list(col) for col in zip(*mat)]
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
print('#'*18)
print('')

def row_sums(mat: list[list[float | int]]) -> list[float]:
    rvan = [len(x) for x in mat]
    if len(set(rvan)) != 1:
        raise ValueError
    res = []
    for i in range(len(mat)):
        summ = 0
        res.append(sum(mat[i]))
    return res
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
print('#'*18,' '*18)
print('')

def col_sums(mat: list[list[float | int]]) -> list[float]:
    rvan = [len(x) for x in mat]
    if len(set(rvan)) != 1:
        raise ValueError
    res = []
    for i in range(len(mat[0])):
        s = 0
        for j in range(len(mat)):
            s+=mat[j][i]
        res.append(s)       
    return res
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
print('#'*18)