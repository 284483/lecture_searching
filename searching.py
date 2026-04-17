import json
import time
def read_data(file_name, pole):
    with open(file_name, 'r') as subor:
        data = json.load(subor)
    if pole not in data:
        return None
    return data[pole]

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
    start=time.perf_counter()

    while low<=high:
        mid=(low+high)//2
        if zoradene_cisla[mid]==cislo:
            return mid
        elif zoradene_cisla[mid]<cislo:
            low=mid+1
        else:
            high=mid-1
    end=time.perf_counter()
    duration=end-start
    return  (f"Měření trvalo {duration:.8f} s, a cislo sa nenaslo")

def pattern_search(sekvencia, kodon):
    pozicie=set()
    dlzka_sekvencie=len(sekvencia)
    dlzka_kodonu=len(kodon)
    for i in range(dlzka_sekvencie - dlzka_kodonu + 1):
        pravdivost=True
        for j in range(dlzka_kodonu):
            if sekvencia[i + j] != kodon[j]:
                pravdivost=False
                break
        if pravdivost:
            pozicie.add(i)
    return pozicie

def main():
    data_nezoradene_cisla = read_data("sequential.json", "unordered_numbers")
    dna_sekvencie = read_data("sequential.json", "dna_sequence")
    print(data_nezoradene_cisla)
    ciselne_hladanie = linear_search(data_nezoradene_cisla, 3)
    print(ciselne_hladanie)
    binarni_hledani = binary_search(data_nezoradene_cisla, 9)
    print(binarni_hledani)
    pass

    # json_subor="sequential.json"
    # with open(json_subor, "r") as subor:
    #     dna_data=json.load(subor)
    vyhledavani_kodonu=pattern_search(dna_sekvencie, "ATA")
    print(vyhledavani_kodonu)

if __name__ == '__main__':
    main()