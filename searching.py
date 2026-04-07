import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        if field not in data:
            return None

        return data[field]

    except:
        return None

def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    pass

if __name__ == '__main__':
    main()