def matrix_inverse(matrix):
    n = len(matrix)
    
    if any(len(row) != n for row in matrix):
        raise ValueError("Матрица должна быть квадратной")
    
    # Расширенная матрица [A | I]
    augmented = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] 
                 for i, row in enumerate(matrix)]

    for col in range(n):
        # Поиск ведущего элемента
        max_row = max(range(col, n), key=lambda r: abs(augmented[r][col]))
        if abs(augmented[max_row][col]) < 1e-10: # доп. проверка из-за погрешности
            raise ValueError("Некорректная матрица")
        
        # Обмен строк
        augmented[col], augmented[max_row] = augmented[max_row], augmented[col]
        
        # Нормализация
        pivot = augmented[col][col]
        augmented[col] = [x / pivot for x in augmented[col]]
        
        # Обнуление столбца
        for row in range(n):
            if row != col:
                factor = augmented[row][col]
                augmented[row] = [augmented[row][i] - factor * augmented[col][i] 
                                  for i in range(2 * n)]

    return [row[n:] for row in augmented]