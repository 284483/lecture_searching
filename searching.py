import json
import time
import matplotlib.pyplot as plt

def read_data(file_name, pole):
    try:
        with open(file_name, 'r') as subor:
            data = json.load(subor)
        if pole not in data:
            return None
        return data[pole]
    except FileNotFoundError:
        print(f"Tento subor {file_name} zial neexisutuje")
        return None

def linear_search(sekvencia, cislo):
    pozicie=[]
    pocet_cisel=sekvencia.count(cislo)
    for i in range(len(sekvencia)):
        if sekvencia[i]==cislo:
            pozicie.append(i)
    return {"pozícia": pozicie, "počet nájdení": pocet_cisel}

def binary_search(zoznam, cislo):
    spodok=0
    vrch=len(zoznam)-1
    start=time.perf_counter()

    while spodok<=vrch:
        stred=(spodok+vrch)//2
        if zoznam[stred]==cislo:
            return stred
        elif zoznam[stred]<cislo:
            spodok=stred+1
        else:
            vrch=stred-1
    end=time.perf_counter()
    duration=end-start
    return None

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

def porovnanie_rychlosti():
    cisla = [100, 500, 1000, 5000, 10000]
    linear_casy = []
    binary_casy = []

    for n in cisla:
        test_data = list(range(n))
        hladane = n - 1

        # Meriam linear
        t1 = time.perf_counter()
        linear_search(test_data, hladane)
        linear_casy.append(time.perf_counter() - t1)

        # Meriam binary
        t2 = time.perf_counter()
        binary_search(test_data, hladane)
        binary_casy.append(time.perf_counter() - t2)

    # Kreslenie grafu
    plt.plot(cisla, linear_casy, label="Linear")
    plt.plot(cisla, binary_casy, label="Binary")
    plt.xlabel("Pocet prvkov")
    plt.ylabel("Cas v sekundach")
    plt.title("Linearne vs Binárne hladanie")
    plt.legend()
    plt.show()

def main():
    data_nezoradene_cisla = read_data("sequential.json", "unordered_numbers")
    data_zoradene_cisla=read_data("sequential.json", "ordered_numbers")
    dna_sekvencie = read_data("sequential.json", "dna_sequence")

    print("Výsledok lineárneho hľadania je:", linear_search(data_nezoradene_cisla, 3))
    print("Index z binárneho hľadania:", binary_search(data_zoradene_cisla, 9))
    print("Pozície DNA vzoru sú:", pattern_search(dna_sekvencie, "ATA"))



    ciselne_hladanie = linear_search(data_nezoradene_cisla, 3)
    print(ciselne_hladanie)

    binarni_hledani = binary_search(data_zoradene_cisla, 9)
    print(binarni_hledani)

    # json_subor="sequential.json"
    # with open(json_subor, "r") as subor:
    #     dna_data=json.load(subor)
    vyhledavani_kodonu=pattern_search(dna_sekvencie, "ATA")
    print(vyhledavani_kodonu)

    porovnanie_rychlosti()
    print("\nVýsledky potvrdili, že lineárne hľadanie je O(n) a binárne O(log n).")

if __name__ == '__main__':
    main()