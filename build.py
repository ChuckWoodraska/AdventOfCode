import os

for i in range(26):
    path = os.path.dirname(__file__)
    dir_path = os.path.join(path, 'day{}'.format(i))
    os.mkdir(dir_path)
    open(os.path.join(dir_path, 'day{}.py'.format(i)), 'w')
    open(os.path.join(dir_path, 'test_input.txt'), 'w')
    open(os.path.join(dir_path, 'input.txt'), 'w')
