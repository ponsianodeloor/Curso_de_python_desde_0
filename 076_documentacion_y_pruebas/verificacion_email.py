def compruebaEmail(mailUsusario):
    """
    La funcion comprueba email evalua un email recibido en busca de la @
    si tiene una @ es correcto, si tiene mas de un @ es incorrecto
    si la @ esta al final es incorrecto
    >>>compruebaEmail('ponsianodeloor@gmail.com')
    True
    >>>compruebaEmail('ponsianodeloor.gmail.com@')
    False
    >>>compruebaEmail('ponsianodeloor.gmail.com')
    False
    >>>compruebaEmail('ponsianodeloor@gmail.com@')
    False
    """
    arroba = mailUsusario.count('@')
    if arroba != 1 or mailUsusario.rfind('@') == len(mailUsusario)-1 or mailUsusario.find('@'):
        return False
    else:
        return True



import doctest
doctest.testmod()
