import sys
import os
from collections import deque

def timestamp_to_seconds(timestamp):
    """Converte HH:MM:SS para segundos desde meia-noite."""
    try:
        h, m, s = map(int, timestamp.split(':'))
        return h*3600 + m*60 + s
    except ValueError:
        return None
def seconds_to_timestamp(seconds):
    """Converte segundos desde meia-noite para HH:MM:SS."""
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"
def process_log(file_path, window_size):
    """Processa o log e encontra a janela com mais erros."""
    error_queue = deque()
    max_errors = 0
    window_start_time = None
    window_end_time = None

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if ',' not in line:
                continue
            timestamp_str, message = line.split(',', 1)
            timestamp_sec = timestamp_to_seconds(timestamp_str.strip())
            if timestamp_sec is None:
                continue
            if 'ERROR' in message:
                error_queue.append(timestamp_sec)
                while error_queue and error_queue[0] < timestamp_sec-window_size:
                    error_queue.popleft()
                if len(error_queue) > max_errors:
                    max_errors = len(error_queue)
                    window_start_time = error_queue[0]
                    window_end_time = timestamp_sec

    if max_errors == 0:
        print("Nenhum erro encontrado no arquivo de log.")
    else:
        print(f"Janela mais movimentada encontrada: {seconds_to_timestamp(window_start_time)} - {seconds_to_timestamp(window_end_time)}, com {max_errors} erros.")

def main():
    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} <caminho_para_arquivo_log> <tamanho_da_janela_em_segundos>")
        sys.exit(1)
    file_path = sys.argv[1]
    try:
        window_size = int(sys.argv[2])
        if window_size <= 0:
            raise ValueError
    except ValueError:
        print("O tamanho da janela deve ser um número inteiro positivo.")
        sys.exit(1)

    if not os.path.isfile(file_path):
        print(f"Arquivo '{file_path}' não encontrado.")
        sys.exit(1)

    process_log(file_path, window_size)

if __name__ == "__main__":
    main()
