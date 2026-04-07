import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    with open(file_name, 'r') as file:
        data = json.load(file)
    if field not in data:
        return None
    return data[field]


def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    pass

if __name__ == '__main__':
    main()