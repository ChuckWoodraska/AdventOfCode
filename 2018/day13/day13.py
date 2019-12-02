import pandas as pd
from operator import itemgetter

grid_list = []
cart_list = []
carts_to_remove = []


def find_overwritten_char(c):
    if c == '>' or c == '<':
        return '-'
    elif c == 'v' or c == '^':
        return '|'

def remove_crashed_carts():
    cart_pos = []
    for index, cart in enumerate(cart_list):
        if cart['overwritten_char'] in ['>', 'v', '<', '^'] and index not in carts_to_remove:
            carts_to_remove.append(index)
            cart_pos.append(cart['current_pos'])
            cart['crashed'] = True
    for index, cart in enumerate(cart_list):
        if cart['overwritten_char'] not in ['>', 'v', '<', '^'] and cart['current_pos'] in cart_pos and index not in carts_to_remove:
            carts_to_remove.append(index)
            grid_list[cart['current_pos'][1]][cart['current_pos'][0]] = cart['overwritten_char']
            cart['crashed'] = True
    # print(cart_list)

def remove_crashed_carts2():
    cart_pos = []
    for index, cart in enumerate(cart_list):
        if cart['overwritten_char'] in ['>', 'v', '<', '^'] and not cart['crashed']:
            cart_pos.append(cart['current_pos'])
            cart['crashed'] = True
    for index, cart in enumerate(cart_list):
        if cart['overwritten_char'] not in ['>', 'v', '<', '^'] and cart['current_pos'] in cart_pos and not cart['crashed']:
            grid_list[cart['current_pos'][1]][cart['current_pos'][0]] = cart['overwritten_char']
            cart['crashed'] = True


with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    for j, line in enumerate(data):
        temp_list = []
        for i, c in enumerate(line):
            if c in ['>', 'v', '<', '^']:
                cart_list.append(
                    {'last_dir': 'right', 'current_pos': (i, j), 'overwritten_char': find_overwritten_char(c), 'crashed': False})
            temp_list.append(c)
        grid_list.append(temp_list)
    # PART 1
    # no_crash = True
    # first_crash = None
    # while no_crash:
    #     cart_list.sort(key=lambda x: (x['current_pos'][1], x['current_pos'][0]))
    #     # print(cart_list)
    #     for cart in cart_list:
    #         c = grid_list[cart['current_pos'][1]][cart['current_pos'][0]]
    #         new_c = None
    #         grid_c = None
    #         new_pos = None
    #
    #         # print(c)
    #         if c == '>':
    #
    #             new_c = grid_list[cart['current_pos'][1]][cart['current_pos'][0] + 1]
    #             new_pos = (cart['current_pos'][0] + 1, cart['current_pos'][1])
    #             # print(new_c)
    #             if new_c == '+':
    #                 if cart['last_dir'] == 'right':
    #                     grid_c = '^'
    #                     cart['last_dir'] = 'left'
    #                 elif cart['last_dir'] == 'left':
    #                     grid_c = '>'
    #                     cart['last_dir'] = 'straight'
    #                 elif cart['last_dir'] == 'straight':
    #                     grid_c = 'v'
    #                     cart['last_dir'] = 'right'
    #             elif new_c == '\\':
    #                 grid_c = 'v'
    #             elif new_c == '/':
    #                 grid_c = '^'
    #             elif new_c == '-':
    #                 grid_c = '>'
    #             elif no_crash and new_c in ['>', 'v', '<', '^']:
    #                 first_crash = new_pos
    #                 no_crash = False
    #                 break
    #
    #
    #         elif c == '<':
    #             new_c = grid_list[cart['current_pos'][1]][cart['current_pos'][0] - 1]
    #             new_pos = (cart['current_pos'][0] - 1, cart['current_pos'][1])
    #             # print(new_c)
    #             if new_c == '+':
    #                 if cart['last_dir'] == 'right':
    #                     grid_c = 'v'
    #                     cart['last_dir'] = 'left'
    #                 elif cart['last_dir'] == 'left':
    #                     grid_c = '<'
    #                     cart['last_dir'] = 'straight'
    #                 elif cart['last_dir'] == 'straight':
    #                     grid_c = '^'
    #                     cart['last_dir'] = 'right'
    #             elif new_c == '\\':
    #                 grid_c = '^'
    #             elif new_c == '/':
    #                 grid_c = 'v'
    #             elif new_c == '-':
    #                 grid_c = '<'
    #             elif no_crash and new_c in ['>', 'v', '<', '^']:
    #                 first_crash = new_pos
    #                 no_crash = False
    #                 break
    #         elif c == 'v':
    #             new_c = grid_list[cart['current_pos'][1] + 1][cart['current_pos'][0]]
    #             new_pos = (cart['current_pos'][0], cart['current_pos'][1] + 1)
    #             # print(new_c)
    #             if new_c == '+':
    #                 if cart['last_dir'] == 'right':
    #                     grid_c = '>'
    #                     cart['last_dir'] = 'left'
    #                 elif cart['last_dir'] == 'left':
    #                     grid_c = 'v'
    #                     cart['last_dir'] = 'straight'
    #                 elif cart['last_dir'] == 'straight':
    #                     grid_c = '<'
    #                     cart['last_dir'] = 'right'
    #             elif new_c == '\\':
    #                 grid_c = '>'
    #             elif new_c == '/':
    #                 grid_c = '<'
    #             elif new_c == '|':
    #                 grid_c = 'v'
    #             elif no_crash and new_c in ['>', 'v', '<', '^']:
    #                 first_crash = new_pos
    #                 no_crash = False
    #                 break
    #         elif c == '^':
    #             new_c = grid_list[cart['current_pos'][1] - 1][cart['current_pos'][0]]
    #             new_pos = (cart['current_pos'][0], cart['current_pos'][1] - 1)
    #             # print(new_c)
    #             if new_c == '+':
    #                 if cart['last_dir'] == 'right':
    #                     grid_c = '<'
    #                     cart['last_dir'] = 'left'
    #                 elif cart['last_dir'] == 'left':
    #                     grid_c = '^'
    #                     cart['last_dir'] = 'straight'
    #                 elif cart['last_dir'] == 'straight':
    #                     grid_c = '>'
    #                     cart['last_dir'] = 'right'
    #             elif new_c == '\\':
    #                 grid_c = '<'
    #             elif new_c == '/':
    #                 grid_c = '>'
    #             elif new_c == '|':
    #                 grid_c = '^'
    #             elif no_crash and new_c in ['>', 'v', '<', '^']:
    #                 first_crash = new_pos
    #                 no_crash = False
    #                 break
    #         # print(new_pos)
    #         grid_list[cart['current_pos'][1]][cart['current_pos'][0]] = cart['overwritten_char']
    #         cart['overwritten_char'], cart['current_pos'], grid_list[new_pos[1]][new_pos[0]],  = new_c, new_pos, grid_c
    #     df = pd.DataFrame(grid_list)
    #     # print(df)
    #     # print(cart_list)
    # print(first_crash)

    # PART 2
    while len(cart_list) > 1:
        cart_list.sort(key=lambda x: (x['current_pos'][1], x['current_pos'][0]))
        # print(cart_list)
        crash_pos_list = []
        for index, cart in enumerate(cart_list):
            c = grid_list[cart['current_pos'][1]][cart['current_pos'][0]]
            new_c = None
            grid_c = None
            new_pos = None


            # print(c)
            if cart['crashed']:
                pass
            elif c == '>':

                new_c = grid_list[cart['current_pos'][1]][cart['current_pos'][0] + 1]
                new_pos = (cart['current_pos'][0] + 1, cart['current_pos'][1])
                # print(new_c)
                if new_c == '+':
                    if cart['last_dir'] == 'right':
                        grid_c = '^'
                        cart['last_dir'] = 'left'
                    elif cart['last_dir'] == 'left':
                        grid_c = '>'
                        cart['last_dir'] = 'straight'
                    elif cart['last_dir'] == 'straight':
                        grid_c = 'v'
                        cart['last_dir'] = 'right'
                elif new_c == '\\':
                    grid_c = 'v'
                elif new_c == '/':
                    grid_c = '^'
                elif new_c == '-':
                    grid_c = '>'
                elif new_c in ['>', 'v', '<', '^']:
                    grid_c = new_c
                    crash_pos_list.append(new_pos)
                    grid_list[cart['current_pos'][1]][cart['current_pos'][0]] = cart['overwritten_char']
                    cart['overwritten_char'], cart['current_pos'], grid_list[new_pos[1]][
                        new_pos[0]], = new_c, new_pos, grid_c
            elif c == '<':
                new_c = grid_list[cart['current_pos'][1]][cart['current_pos'][0] - 1]
                new_pos = (cart['current_pos'][0] - 1, cart['current_pos'][1])
                # print(new_c)
                if new_c == '+':
                    if cart['last_dir'] == 'right':
                        grid_c = 'v'
                        cart['last_dir'] = 'left'
                    elif cart['last_dir'] == 'left':
                        grid_c = '<'
                        cart['last_dir'] = 'straight'
                    elif cart['last_dir'] == 'straight':
                        grid_c = '^'
                        cart['last_dir'] = 'right'
                elif new_c == '\\':
                    grid_c = '^'
                elif new_c == '/':
                    grid_c = 'v'
                elif new_c == '-':
                    grid_c = '<'
                elif new_c in ['>', 'v', '<', '^']:
                    grid_c = new_c
                    crash_pos_list.append(new_pos)
                    grid_list[cart['current_pos'][1]][cart['current_pos'][0]] = cart['overwritten_char']
                    cart['overwritten_char'], cart['current_pos'], grid_list[new_pos[1]][
                        new_pos[0]], = new_c, new_pos, grid_c
            elif c == 'v':
                new_c = grid_list[cart['current_pos'][1] + 1][cart['current_pos'][0]]
                new_pos = (cart['current_pos'][0], cart['current_pos'][1] + 1)
                # print(new_c)
                if new_c == '+':
                    if cart['last_dir'] == 'right':
                        grid_c = '>'
                        cart['last_dir'] = 'left'
                    elif cart['last_dir'] == 'left':
                        grid_c = 'v'
                        cart['last_dir'] = 'straight'
                    elif cart['last_dir'] == 'straight':
                        grid_c = '<'
                        cart['last_dir'] = 'right'
                elif new_c == '\\':
                    grid_c = '>'
                elif new_c == '/':
                    grid_c = '<'
                elif new_c == '|':
                    grid_c = 'v'
                elif new_c in ['>', 'v', '<', '^']:

                    grid_c = new_c
                    crash_pos_list.append(new_pos)
                    grid_list[cart['current_pos'][1]][cart['current_pos'][0]] = cart['overwritten_char']
                    cart['overwritten_char'], cart['current_pos'], grid_list[new_pos[1]][
                        new_pos[0]], = new_c, new_pos, grid_c
            elif c == '^':
                new_c = grid_list[cart['current_pos'][1] - 1][cart['current_pos'][0]]
                new_pos = (cart['current_pos'][0], cart['current_pos'][1] - 1)
                # print(new_c)
                if new_c == '+':
                    if cart['last_dir'] == 'right':
                        grid_c = '<'
                        cart['last_dir'] = 'left'
                    elif cart['last_dir'] == 'left':
                        grid_c = '^'
                        cart['last_dir'] = 'straight'
                    elif cart['last_dir'] == 'straight':
                        grid_c = '>'
                        cart['last_dir'] = 'right'
                elif new_c == '\\':
                    grid_c = '<'
                elif new_c == '/':
                    grid_c = '>'
                elif new_c == '|':
                    grid_c = '^'
                elif new_c in ['>', 'v', '<', '^']:
                    grid_c = new_c
                    crash_pos_list.append(new_pos)
                    grid_list[cart['current_pos'][1]][cart['current_pos'][0]] = cart['overwritten_char']
                    cart['overwritten_char'], cart['current_pos'], grid_list[new_pos[1]][
                        new_pos[0]], = new_c, new_pos, grid_c
            # print(new_pos)
            if not cart['crashed'] and cart['current_pos'] not in crash_pos_list:
                grid_list[cart['current_pos'][1]][cart['current_pos'][0]] = cart['overwritten_char']
                cart['overwritten_char'], cart['current_pos'], grid_list[new_pos[1]][new_pos[0]],  = new_c, new_pos, grid_c
        df = pd.DataFrame(grid_list)
        # print(df)
        # print(cart_list)
        # print(carts_to_remove)
        remove_crashed_carts2()
        cart_list = [x for i, x in enumerate(cart_list) if not x['crashed']]
    print(cart_list)
    print([x for i, x in enumerate(cart_list) if not x['crashed']])
