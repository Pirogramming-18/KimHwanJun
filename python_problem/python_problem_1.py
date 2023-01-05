num = 0
def brGame():
    call = 0
    while(True):
        try:
            call = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
            if ( not 0<call<4 ):
                raise Exception("")
        except ValueError:
            print("정수를 입력하세요")
        except Exception:
            print("1,2,3 중 하나를 입력하세요")
        else:
            break;
    return call

while(True):

    add1 = brGame()
    for i in range(add1):
        print("playerA: {}".format(i+1+num))

    num = num + add1
    if(num>30):
        print("playerA win!") 
        break;

    add2 = brGame()
    for i in range(add2):
        print("playerB: {}".format(i+1+num))

    num = num + add2
    if(num>30):
        print("playerB win!") 
        break;



    
