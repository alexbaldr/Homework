from contextlib import contextmanager
from datetime import datetime

@contextmanager
def get_time():
    try:
        start_time = datetime.utcnow()
        print(f'Начало работы: {start_time}')
        end_time = datetime.utcnow()
        print(f'Конец работы: {end_time}')
        yield
    finally:
        print(end_time- start_time)

with get_time():
    print('Было затрачено: ' )