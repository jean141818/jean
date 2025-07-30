def first_non_repeating_letter(s):
    aux = s.lower()
    for letter in s:
        if aux.count(letter.lower()) == 1:
            return letter  
    return ''
    
print(first_non_repeating_letter("stress"))