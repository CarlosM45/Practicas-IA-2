def is_safe(board, row, col, N):
    # Verificar lado izquierdo
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Verificar diagonal izquierda-arriba
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Verificar diagonal izquierda-abajo
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


# Función para resolver el problema de las N reinas y devolver todas las soluciones posibles
def solve_n_queens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    result = []

    # Función de retroceso para encontrar todas las soluciones
    def backtrack(board, col):
        if col == N:
            result.append([''.join(row) for row in board])
            return

        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 'Q'
                backtrack(board, col + 1)
                board[i][col] = '.'

    backtrack(board, 0)
    return result


def is_safe_with_forward_checking(domains, row, col):
    # Verificar si la posición actual está en el dominio permitido
    return row in domains[col]


def update_domains(domains, row, col, N):
    # Crear una copia del dominio actual para restaurarlo si es necesario
    new_domains = [set(domain) for domain in domains]

    # Eliminar la fila actual de todas las columnas restantes
    for c in range(col + 1, N):
        if row in new_domains[c]:
            new_domains[c].remove(row)

    # Eliminar las diagonales afectadas
    for c in range(col + 1, N):
        if row + (c - col) < N and row + (c - col) in new_domains[c]:
            new_domains[c].remove(row + (c - col))
        if row - (c - col) >= 0 and row - (c - col) in new_domains[c]:
            new_domains[c].remove(row - (c - col))

    return new_domains


# Función para resolver el problema de las N reinas y devolver todas las soluciones posibles usando forward checking
def solve_n_queens_with_forward_checking(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    result = []

    # Inicializar dominios: todas las filas son válidas para cada columna
    domains = [set(range(N)) for _ in range(N)]

    # Función de retroceso con forward checking
    def backtrack_with_forward_checking(board, col, domains):
        if col == N:
            result.append([''.join(row) for row in board])
            return

        for row in list(domains[col]):  # Iterar sobre las filas válidas en el dominio actual
            if is_safe_with_forward_checking(domains, row, col):
                board[row][col] = 'Q'
                # Actualizar dominios para la siguiente columna
                new_domains = update_domains(domains, row, col, N)

                # Verificar si algún dominio quedó vacío
                if all(new_domains[c] for c in range(col + 1, N)):
                    backtrack_with_forward_checking(board, col + 1, new_domains)

                # Restaurar el tablero
                board[row][col] = '.'

    backtrack_with_forward_checking(board, 0, domains)
    return result


# Ejemplo 1
N1 = 4
result1 = solve_n_queens_with_forward_checking(N1)
print(f"Solution for Example 1 with N = {N1}:")
for solution in result1:
    print(solution)
print()

# Ejemplo 2
N2 = 1
result2 = solve_n_queens_with_forward_checking(N2)
print(f"Solution for Example 2 with N = {N2}:")
for solution in result2:
    print(solution)