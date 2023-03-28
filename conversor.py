def converte(simbolo):
    dicionario={'I':1,'V':5,'VII':7,'VIII':8,'IX':9,'X':10,'XV':15,
                'XX':20,'XXV':25,'XXX':30,'XXXV':35,'L':50,
                'LV':55,'LXV':65,'C':100,'D':500,'M':1000}

    if type (dicionario) == int:
      return dicionario.get(simbolo)