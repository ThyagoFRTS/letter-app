from numpy import ndarray, where

def find_table_template(image: ndarray, gray_tolerance: int = 200, margin: int = 1):
    """
    Finds top and bottom, left and right contourns from letter template
    Returns ((y_top, y_bottom), (x_left, x_right)).
    """

    height, width = image.shape[:2]
    y_center, x_center = height // 2, width // 2

    def find_limits(line: ndarray):
        """Encontra limites em uma linha 1D de pixels com base no gray_tolerance."""
        dark_indices = where(line < gray_tolerance)[0]
        if len(dark_indices) == 0:
            return None, None
        start = max(dark_indices[0] - margin, 0)
        end = min(dark_indices[-1] + margin, len(line) - 1)
        return int(start), int(end)

    # Varredura vertical (coluna central)
    vertical_line = image[:, x_center]
    y_top, y_bottom = find_limits(vertical_line)

    # Varredura horizontal (linha central)
    horizontal_line = image[y_center, :]
    x_left, x_right = find_limits(horizontal_line)

    return (y_top, y_bottom), (x_left, x_right)