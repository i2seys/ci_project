import pytest
from matrix_inverse import matrix_inverse

def test_inverse_2x2():
    """Обратная матрица 2x2"""
    A = [[4, 7], [2, 6]]
    A_inv = matrix_inverse(A)
    # Проверка через умножение: A * A_inv = I
    assert abs(A_inv[0][0] - 0.6) < 1e-9
    assert abs(A_inv[0][1] - (-0.7)) < 1e-9

def test_inverse_3x3():
    """Обратная матрица 3x3"""
    A = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
    A_inv = matrix_inverse(A)
    # Проверяем что A * A_inv ≈ I
    result = [[sum(A[i][k] * A_inv[k][j] for k in range(3)) 
               for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            expected = 1.0 if i == j else 0.0
            assert abs(result[i][j] - expected) < 1e-9 # Погрешность float на всякий

def test_singular_matrix():
    """Вырожденная матрица (определитель = 0)"""
    A = [[1, 2], [2, 4]]  # Вторая строка = 2 * первую
    with pytest.raises(ValueError, match="Некорректная матрица"):
        matrix_inverse(A)

def test_identity_matrix():
    """Единичная матрица обратна самой себе"""
    I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    I_inv = matrix_inverse(I)
    assert I_inv == I

def test_non_square_matrix():
    """Неквадратная матрица"""
    A = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError, match="Матрица должна быть квадратной"):
        matrix_inverse(A)