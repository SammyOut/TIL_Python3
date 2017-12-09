# 파이썬에서 변수의 기본 자료형은 int, float, stirng 밖에 없다.
# int형의 변수는 정수를 담을 수 있고, 값의 크기에 따라 자동으로 메모리가 할당되므로 담을 수 있는 값의 범위 제한은 없다.
# float형의 변수는 실수(소수)를 담을 수 있다.
# string형의 변수는 문자열을 담을 수 있다. string형도 값의 크기에 따라 자동으로 메모리가 할당되므로 담을 수 있는 길이의 제한은 없다.

# 변수를 선언할 때 자료형을 명시하지 않아도, 변수를 선언한다고 명시하지 않아도 변수를 선언할 수 있다.
# 파이썬에서 변수를 선언하면 값의 리터럴에 따라 자동으로 타입 캐스팅이 된다.
# (변수 명) = (변수의 값)과 같이 하면 변수가 선언된다.
a = 10
b = 10.5
c = "Hello World!"

print("Variable a Type: {0}, Value: {1}".format(type(a), a))
print("Variable b Type: {0}, Value: {1}".format(type(b), b))
print("Variable c Type: {0}, Value: {1}".format(type(c), c))

# 파이썬의 변수는 모두 참조 타입이다. 그래서 변수의 값을 변경하면 변수 안의 값이 변하는게 아니라 변수가 가리키는 것이 바뀐다.
# 파이썬의 id()함수를 사용하면 변수의 주소를 알 수 있다.
a = 3600
print("Variable a Id: {0}, Value: {1}".format(id(a), a))
a = 3601
print("Variable a Id: {0}, Value: {1}".format(id(a), a))

# 값이 같은 두 변수 두 쌍을 선언해보자
a = 10
b = 10
c = 2017
d = 2017

# 그리고 한 쌍 씩 id()함수를 사용하여 주소를 비교해보자
print("Variable a Id: {0}, Value: {1}, Variable b Id: {2}, Value: {3}, id(a) == id(b): {4}".format(id(a), a, id(b), b, id(a) == id(b)))
print("Variable c Id: {0}, Value: {1}, Variable d Id: {2}, Value: {3}, id(c) == id(d): {4}".format(id(c), c, id(d), d, id(c) == id(d)))

# 무엇인가 이상하다. 왜 a와 b의 주솟값은 같은데 c와 d의 주솟값은 다른걸까?
# 그 이유는 파이썬은 자주 쓰이는 수라고 추측되는 -5 ~ 256의 값을 사용되는 사용이 되지 않든 미리 메모리에 선언을 해두기 때문이다.
