num = 0
callA = 0
callB = 0
count = 0
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

    for num in range(callA):
        print("playerA: {}".format(num+1+count))
    count = count + callA
    
    if(count>30):
        break;

    num = 0
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

    for num in range(callB):
        print("playerB: {}".format(num+1+count))
    count = count + callB

    if(count>30):
        
        break;


    
