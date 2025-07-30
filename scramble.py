def scramble (str1,str2):
    aux = []
    for letter in str1:
        if letter in str2:
            aux.append(letter)    
    cad_aux = ''.join(aux)
    if str2 in cad_aux:
        return True
    else:
        return False

print(scramble('cedewaraaossoqqyt', 'codewars'))