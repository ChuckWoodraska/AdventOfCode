import os

for i in range(1, 26):
    path = os.path.dirname(__file__)
    dir_path = os.path.join(path, f'day{i}')
    os.mkdir(dir_path)
    open(os.path.join(dir_path, f'day{i}.py'), 'w')
    open(os.path.join(dir_path, 'test_input.txt'), 'w')
    open(os.path.join(dir_path, 'input.txt'), 'w')
