def numar_divizori(n) -> int:
    """
    Determina numarul de divizori ai lui n.
    :param n: element din lista
    :return: o valoare de tip int
    """
    contor = 2
    for i in range(2, n // 2):
        if n % i == 0:
            contor += 1
    return contor


def test_numar_divizori():
    assert is_prime(6) == 4
    assert is_prime(12) == 6
    assert is_prime(31) == 2
    assert is_prime(48) == 10
    assert is_prime(13) == 2


def get_longest_same_div_count(lista: list[int]) -> list[int]:
    """
    Determina cea mai lunga secventa de valori din parametrul lista cu acelasi numar de divizori.
    :param lista: lista in care au fost introduse elementele
    :return: paramentrul return_lista in care a fost salvata cea mai lunga secventa care indeplineste proprietatea
    """
    result_list = []
    parametru = 0
    cea_mai_lunga = 0
    inceput = -1
    cml_inceput = 0
    elementul_trecut = lista[0]
    for i in range(1, len(lista)):
        elementul_actual = lista[i]
        if numar_divizori(elementul_trecut) == numar_divizori(elementul_actual):
            parametru += 1
            if inceput == -1:
                inceput = i - 1
            if parametru > cea_mai_lunga:
                cea_mai_lunga = parametru
        elif numar_divizori(elementul_actual) != numar_divizori(elementul_trecut):
            cml_inceput = inceput
            parametru = 0
        elementul_trecut = elementul_actual
    cea_mai_lunga += 1
    for i in range(cml_inceput, cml_inceput + cea_mai_lunga):
        result_list.append(lista[i])
    return result_list


def is_prime(n) -> bool:
    """
    Determina primalitatea unui numar.
    :param n: elementul din lista care vrem sa fie verificat
    :return: o valoare de adevar in functie de caz
    """
    if n < 2:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(12) == False
    assert is_prime(31) == True
    assert is_prime(48) == False
    assert is_prime(13) == True


def get_longest_all_primes(lista: list[int]) -> list[int]:
    """
    Determina cea mai lunga secventa de numere prime din lista.
    :param lista: lista in care se afla valorile
    :return: cea mai lunga secventa de numere prime din parametrul lista, salvate in parametrul result_list
    """
    result_list = []
    parametru = 0
    cea_mai_lunga = 0
    inceput = -1
    cml_inceput = 0
    for i in range(0, len(lista)):
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
    for i in range(cml_inceput, cea_mai_lunga + cml_inceput):
        result_list.append(lista[i])
    return result_list


def citire_lista() -> list[int]:
    """
    Citeste elementele listei.
    :return: parametrul result_list in care au fost introduse elementele.
    """
    dimensiune = int(input("Dimensiune lista: "))
    result_list = []
    while dimensiune:
        element = int(input("Adauga elementul: "))
        result_list.append(element)
        dimensiune -= 1
    return result_list


def main():
    stop = True
    while stop:
        optiune = input("Determinare cea mai lunga secventa cu proprietatea: ")
        if optiune == '2':
            lista = citire_lista()
            lista = get_longest_all_primes(lista)
            test_is_prime()
            print(lista)
        elif optiune == '12':
            lista = citire_lista()
            lista = get_longest_same_div_count(lista)
            test_is_prime()
            print(lista)
        elif optiune == 'x':
            stop = False


main()
