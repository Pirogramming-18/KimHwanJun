num = 0

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
