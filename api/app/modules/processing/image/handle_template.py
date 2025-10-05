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

def detect_table_lines(binary_img, scale=15):
    h_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (binary_img.shape[1] // scale, 1))
    v_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, binary_img.shape[0] // scale))

    horizontal = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, h_kernel)
    vertical = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, v_kernel)

    # Combina tudo
    return horizontal, vertical

def extract_line_positions(line_img, axis=0, min_gap=5):
    projection = np.sum(line_img, axis=axis)
    threshold = np.max(projection) * 0.5
    coords = np.where(projection > threshold)[0]

    # Junta linhas próximas
    merged = []
    last = -min_gap*2
    for c in coords:
        if c - last > min_gap:
            merged.append(c)
        last = c
    return merged


def extract_cells_from_lines(image, y_lines, x_lines):
    cells = []
    for i in range(len(y_lines)-1):
        for j in range(len(x_lines)-1):
            y1, y2 = y_lines[i], y_lines[i+1]
            x1, x2 = x_lines[j], x_lines[j+1]
            cell = image[y1:y2, x1:x2]
            cells.append(cell)
    return cells
