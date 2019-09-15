def vacances (deb_ami_1, fin_ami_1, deb_ami_2, fin_ami_2):
    """Cette fonction a pour but en fonction des dates de vacances de deux amis de
    renseigner sur le fait qu'ils puissent ou non se voir durant leurs vacances
    paramètres : 
        deb_ami_1 : jour de début des vacances du 1er ami
        fin_ami_1 : jour de fin des vacances du 1er ami
        deb_ami_2 : jour de début des vacances du 2eme ami
        fin_ami_2 : jour de fin des vacances du 2eme ami"""
    if deb_ami_1 < fin_ami_2 and deb_ami_1 > deb_ami_2 :
        return True
    if fin_ami_1 < fin_ami_2 and fin_ami_1 > deb_ami_2 :
        return True
    return False

assert vacances(3,8,6,16)==True, "Les deux auraient amis doivent pouvoir se rencontrer dans cet intervalle de date"
assert vacances(19,27,11,20)==True, "Les deux auraient amis doivent pouvoir se rencontrer dans cet intervalle de date"
assert vacances(12,20,1,10)==False, "Les deux auraient amis ne doivent pas pouvoir se rencontrer dans cet intervalle de date"
assert vacances(5,11,12,20)==False, "Les deux auraient amis ne doivent pas pouvoir se rencontrer dans cet intervalle de date"

print(vacances(3,8,6,16), "\n")
print(vacances(12,20,1,10), "\n")
print(vacances(5,11,12,20), "\n")
print(vacances(19,27,11,20))