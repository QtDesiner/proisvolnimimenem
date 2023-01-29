import os


def human_read_format(size):
    sizes = ['Б', 'КБ', 'МБ', 'ГБ']
    index = 0
    for i in range(len(sizes)):
        if size / (1024 ** i) < 1:
            break
        index = i
    return f'{round(size / (1024 ** index))}{sizes[index]}'


def get_files_sizes():
    b = []
    for i in os.listdir():
        if os.path.isfile(i):
            b += (i, os.path.getsize(i))
    return b

for i in get_files_sizes():
    