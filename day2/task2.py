import pandas as pd


def get_input():
    return pd.read_csv('input.txt', sep=' ', header=None, names=['command', 'step'])


if __name__ == '__main__':
    commands = get_input()
    commands.loc[commands['command'] == 'up', 'step'] *= -1
    horizontal = commands.loc[commands['command'] == 'forward', 'step'].sum()

    commands['aim'] = 0
    commands.loc[commands['command'].isin(['up', 'down']), 'aim'] = commands.loc[
        commands['command'].isin(['up', 'down']), 'step']

    commands['aim'] = commands['aim'].cumsum()
    depth = (commands.loc[commands['command'] == 'forward', 'step'] * commands.loc[
        commands['command'] == 'forward', 'aim']).sum()

    print(horizontal*depth)
