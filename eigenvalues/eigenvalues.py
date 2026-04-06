import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        matrix = np.asarray(matrix, dtype=np.float64)
    except (ValueError, TypeError):
        # Lỗi nếu matrix là danh sách không đồng nhất (ví dụ: [[1,2], [3]])
        return None
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return None
    return np.linalg.eigvals(matrix)