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

def binary_search(zoznam, cislo):
    zoradene_cisla = sorted(set(zoznam))
    low=0
    high=len(zoradene_cisla)-1
    while low<=high:
        mid=(low+high)//2
        if zoradene_cisla[mid]==cislo:
            return mid
        elif zoradene_cisla[mid]<cislo:
            low=mid+1
        else:
            high=mid-1
    return None


def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    ciselne_hladanie=linear_search(sequential_data, 3)
    print(ciselne_hladanie)
    binarni_hledani=binary_search(sequential_data, 9)
    print(binarni_hledani)
    pass


if __name__ == '__main__':
    main()