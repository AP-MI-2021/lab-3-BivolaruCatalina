
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n//2):
        if n%i == 0 :
            return False
    return True

def get_longest_all_primes(lista: list[int]):
    result_list=[]
    parametru = 0
    cea_mai_lunga = 0
    inceput = -1
    cml_inceput=0
    for i in range(0,len(lista)-1):
        if is_prime(lista[i]):
            parametru += 1
            if inceput == -1:
                inceput = i
            if parametru > cea_mai_lunga:
                cea_mai_lunga = parametru
                cml_inceput = inceput
        elif cea_mai_lunga:
            cml_inceput = inceput
            inceput = -1
            cea_mai_lunga = parametru
            parametru = 0
    if cea_mai_lunga == len(lista):
        cea_mai_lunga += 1
    elif cea_mai_lunga+cml_inceput == len(lista):
        cea_mai_lunga += 1
    for i in range(cml_inceput,cea_mai_lunga+cml_inceput):
        result_list.append(lista[i])
    return result_list

def citire_lista():
    dimensiune=int(input("Dimensiune lista: "))
    result_list=[]
    while dimensiune:
        element=int(input("Adauga elementul: "))
        result_list.append(element)
        dimensiune -= 1
    return result_list

def main():
    stop = True
    while stop:
        lista=[]
        optiune=input("Introduceti numarul proprietatii: ")
        if optiune == '2':
            lista=citire_lista()
            lista=get_longest_all_primes(lista)
            print(lista)
        elif optiune == '12':
            lista=citire_lista()
        elif optiune == 'x':
            stop=False
main()