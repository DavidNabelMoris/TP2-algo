
def creer_liste():
    return None


def vide(lst):
    return lst is None


def premier(lst):
    return lst[0]

def reste(lst):
    return lst[1]


def prefixer(elem, lst):
    return (elem, lst)


def suffixer(elem, lst):
    if vide(lst):
        return prefixer(elem, creer_liste())
    return prefixer(premier(lst), suffixer(elem, reste(lst)))

if __name__ == "__main__":
    lst = creer_liste()
    lst = prefixer(1, lst)
    lst = prefixer(2, lst)
    print(lst)