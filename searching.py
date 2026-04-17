import json


def pattern_search(sekvencia, kodon):
    pozicie=set()
    dlzka_sekvencie=len(sekvencia)
    dlzka_kodonu=len(kodon)
    for i in range(dlzka_sekvencie - dlzka_kodonu + 1):
        if sekvencia[i : i + dlzka_kodonu]==kodon:
            pozicie.add(i)
    return pozicie

def main():
    json_subor="sequential.json"
    with open(json_subor, "r") as subor:
        dna_data=json.load(subor)
    vyhledavani_kodonu=pattern_search(dna_data["dna_sequence"], "ATA")
    print(vyhledavani_kodonu)
    pass

if __name__ == '__main__':
    main()