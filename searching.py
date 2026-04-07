import os
import json
# get current working directory path
cwd_path = os.getcwd()
x_cisla=[4,3,2,5,1,8,7,45,12,14,25,4,5,7,8,2,1,6,5,9,4,8,5,3,6,2,1,5,4,7,8,2,1,5,6,4,8,9,2,3,5,1,4,7,8,5,6,4,2]

def read_data(file_name, field):
    with open(file_name, 'r') as file:
        data = json.load(file)
    if field not in data:
        return None
    return data[field]

def linear_search(sequence, number):
    positions=[]
    count_number=sequence.count(number)
    for i in range(len(sequence)):
        if sequence[i]==number:
            positions.append(i)

    return {"positions": positions, "count": count_number}


def main():

    # sequential_data = read_data("sequential.json", "unordered_numbers")
    # print(sequential_data)
    ciselne_hladanie=linear_search(x_cisla, 4)
    print(ciselne_hladanie)
    pass


if __name__ == '__main__':
    main()