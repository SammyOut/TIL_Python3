# for문은 코드를 반복 실행하는 반복문이다.

# for문의 구조는 for (변수) in (iterable object)이다.
# iterable object는 리스트, 튜플, 문자열 등등 이라고 간단하게 생각하자 (정확한 설명은 아니다.)
# 보통은 range()함수를 사용하여 for문을 사용한다.
for i in range(1, 10):
    print("i: {0}".format(i))
print()

# range(a, b)을 했을 때 i 에 a부터 b-1 값이 하나씩 대입되어 실행되는 것을 알 수 있다.
# 이를 응용하여 구구단 프로그램을 만들어보자
for i in range(1, 10):
    for j in range(1, 10):
        print("{0} * {1} = {2}".format(i, j, i * j))
print()
# 이 같이 for문 안에 for문이 있는 것을 이중 for문 이라고 한다.

# for문의 iterable object에 string을 넣을 수 도 있다고 했다.
stringA = "Hello World!"
for i in stringA:
    print("i: {0}".format(i))
print()

# 파이썬에는 for문을 사용하는 list comprehension 이라는 매우 강력한 친구가 있다.
# list comprehension 은 리스트 안에 for문과 if문을 넣어 리스트를 간편하게 생성해주는 친구이다.
# 예시로 1부터 20까지의 정수 중 짝수인 정수만 들어있는 리스트를 만들어보자
listA = [i for i in range(1, 21) if i % 2 == 0]
print("listA: {0}".format(listA))
