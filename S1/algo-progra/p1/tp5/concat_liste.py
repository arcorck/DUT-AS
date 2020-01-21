def concat (l1, l2) :
    if l1 == [] :
        res = l2
    else : 
        if l2 == [] :
            res = l1
        else : 
            if l1==[] and l2==[] :
                res = []
            else :
                res = []
                cpt1 = 0
                cpt2 = 0
                while cpt1 < len(l1) and cpt2 < len(l2) :
                    if l1[cpt1] <= l2[cpt2] :
                        res.append(l1[cpt1])
                        cpt1 += 1
                    else:
                        res.append(l2[cpt2])
                        cpt2 += 1
                if cpt1 < len(l1) :
                    for indice in range (cpt1, len(l1), 1):
                        res.append(l1[indice])
                if cpt2 < len(l2) :
                    for indice in range (cpt2, len(l2), 1):
                        res.append(l2[indice])
    return res

assert concat([1,3,5,9], [2,3,4]) == [1,2,3,3,4,5,9], "Erreur"
assert concat([1,3,5,7,9,11], [2,4,6,8,10]) == [1,2,3,4,5,6,7,8,9,10,11], "Erreur"
assert concat([2,4,6], [1,3,5,7,9]) == [1,2,3,4,5,6,7,9], "Erreur"

print(concat([1,3,5,9], [2,3,4]))
print(concat([1,3,5,7,9,11], [2,4,6,8,10]))
print(concat([2,4,6], [1,3,5,7,9]))