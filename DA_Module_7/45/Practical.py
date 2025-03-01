"""
45) Write a Python program to unzip a list of tuples into individual lists.
"""


def unzip_tuples(tuple_list):
    unzipped = zip(*tuple_list)
    return [list(t) for t in unzipped]

tuple_list = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

unzipped_lists = unzip_tuples(tuple_list)

for index, lst in enumerate(unzipped_lists, start=1):
    print(f"List {index}: {lst}")


