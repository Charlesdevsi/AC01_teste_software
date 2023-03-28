from conversor import converte

def test_deve_entender_simbolo_I():
    assert converte('I')==1

def test_deve_entender_simbolo_V():
    assert converte('V')==5

def test_deve_entender_simbolo_X():
    assert converte('X')==10

def test_deve_entender_simbolo_VII():
    assert converte('VII')==7

def test_deve_entender_simbolo_XIII():
    assert converte('XIII')==8   

def test_deve_entender_simbolo_IX():
    assert converte('IX')==9

def test_deve_entender_simbolo_X():
    assert converte('X')==10

def test_deve_entender_simbolo_XV():
    assert converte('XV')==15  

def test_deve_entender_simbolo_XX():
    assert converte('XX')==20 

def test_deve_entender_simbolo_XXV():
    assert converte('XXV')==25

def test_deve_entender_simbolo_XXX():
    assert converte('XXX')==30

def test_deve_entender_simbolo_XXXV():
    assert converte('XXXV')==35

def test_deve_entender_simbolo_L():
    assert converte('L')==50

def test_deve_entender_simbolo_C():
    assert converte('C')==100 

def test_deve_entender_simbolo_D():
    assert converte('D')==500   

def test_deve_entender_simbolo_M():
    assert converte('M')==1000

def subtracao(test_deve_entender_simbolo_L , test_deve_entender_simbolo_C):
    return 'C','L'

try:
    resultado  = subtracao(test_deve_entender_simbolo_L,test_deve_entender_simbolo_C)
    assert resultado == 50
    print("numero romano correto")
except AssertionError:
    print("resultado errado")    

def soma(test_deve_entender_simbolo_X, test_deve_entender_X, test_deve_entender_v):
    return 'X','X','V'

try:
    resultado = soma(test_deve_entender_simbolo_X, test_deve_entender_simbolo_X, test_deve_entender_simbolo_V)
    assert resultado == 20
    print('numero romano errado')

except AssertionError:
    print('numero romano correto  25')   

def soma(X, V):
    return X + V

try:
    resultado = soma(9.5, 10.5)
    assert resultado == 15
    print('numero romano inexistente')

except AssertionError:
    print('Tente novamente') 


def sub(X,L):
    return (X - L) * -1

try:
    resultado = sub(10,50)
    assert resultado == 40
    print('numero romano correto')
except AssertionError:
    print('Tente novamente')    
        