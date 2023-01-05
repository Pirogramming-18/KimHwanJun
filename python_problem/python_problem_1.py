num = 0
while(True):
    while(True):
        try:
            callA = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
            if ( not 0<callA<4 ):
                raise Exception("")
        except ValueError:
            print("정수를 입력하세요")
        except Exception:
            print("1,2,3 중 하나를 입력하세요")
        else:
            break;

    for i in range(callA):
        print("playerA: {}".format(i+num+1))
    num = num + callA
    if(num>30):
        print("playerB win!") 
        break;

    while(True):
        try:
            callB = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
            if ( not 0<callB<4 ):
                raise Exception("")
        except ValueError:
            print("정수를 입력하세요")
        except Exception:
            print("1,2,3 중 하나를 입력하세요")
        else:
            break;

    for i in range(callB):
        print("playerB: {}".format(i+num+1))
    num = num + callB
    if(num>30):
        print("playerB win!") 
        break;
    



    
