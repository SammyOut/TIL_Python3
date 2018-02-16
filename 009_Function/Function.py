# 함수를 간단하게 설명하면 x라는 값을 넣으면 y라는 값이 나오는 상자 라고 설명할 수 있다.
# 파이썬에서 함수는 def 로 정의를 할 수 있다.
# 아래와 같이 함수를 정의하고 함수를 호출하면 함수 안에 있는 내용이 실행된다.

def func():
    print('함수 실행')

func()
func()

# 함수명 옆에 괄호에 변수를 넣어서 함수에 전달시켜 사용할 수 있다.

def func(a, b):
    print(a)
    print(b)
    print(a+b)

func(5, 10)
func(10, 15)

# 함수 내에서 return 을 하여서 함수의 실행시킨 결과를 어떠한 곳에 반환시킬 수도 있다.

def func(a, b):
    print(a)
    print(b)
    return a+b

result = func(5, 10)    # result = 15
print(result)

result = func(10, 15)   # result = 25
print(result)
