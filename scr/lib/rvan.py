def x(mat: list[list[float | int]]) -> list[float]:#Проверка на рванную функцию
    rvan = [len(x) for x in mat]
    if len(set(rvan)) != 1:
        return 'ValueError' 