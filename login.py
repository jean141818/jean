def validar(psw):
    if len(psw) < 12:
        return False

    cont1 = cont2 = cont3 = cont4 = 0
    especiales = "!@#$%^&*()_+-=[]{},.<>/?"
    comunes = ["password", "123456", "admin", "qwerty", "letmein"]

    for c in psw:
        if c.isupper():
            cont1 += 1
        elif c.islower():
            cont2 += 1
        elif c.isdigit():
            cont3 += 1
        elif c in especiales:
            cont4 += 1

    if cont1 < 1 or cont2 < 1 or cont3 < 1 or cont4 < 1:
        return False

    for palabra in comunes:
        if palabra in psw.lower():
            return False

    return True

# Entrada y salida
psw = input("Ingrese una contraseña segura: ")

if not validar(psw):
    print("Contraseña no válida ❌")
else:
    print("Contraseña válida ✅")
