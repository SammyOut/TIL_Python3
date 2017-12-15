# 리스트는 배열들의 묶음이라고 할 수 있다.
# 파이썬에서 리스트는 다른 언어의 배열과 비슷하다.
# 리스트는 아래와 같이 선언한다.
listA = []

# 리스트를 선언할 때 값을 넣어줄 수 있다.
# 리스트에는 모든 자료형이 다 들어갈 수 있다.
listA = [1, 2, 3, 4, 5]
print("listA: {0}".format(listA))
print("type(listA): {0}\n".format(type(listA)))

# 리스트에 값을 추가하기 위해서 append() 메소드를 사용한다.
# list.append(value) 처럼 사용하면 된다.
listA.append(6)
listA.append(7)
listA.append(8)
print("After append listA: {0}".format(listA))

# 리스트 끝이 아닌 중간에 값을 추가하고 싶다면 insert() 메소드를 사용하면 된다.
# list.insert(index, value) 처럼 사용하면 된다.
listA.insert(0, 0)
listA.insert(2, 33)
print("After insert listA: {0}\n".format(listA))

# 리스트에서 인덱싱이란 것으로 그 배열 내의 원하는 값을 사용할 수 있다.
# 리스트 인덱싱은 리스트 이름 옆 대괄호에 인덱스를 넣으면 된다. (주의! 인덱스는 0부터 시작한다.)
print("list[2]: {0}, list[4]: {1}".format(listA[2], listA[4]))

# 리스트에서 인덱싱을 통해 특정 요소의 값을 변경할 수 있다.
listA[4] = 0
print("after change list[4]: {0}\n".format(listA[4]))

# 파이썬에서 리스트는 슬라이싱이라는 것을 할 수 있다.
# 리스트 슬라이싱은 그 리스트의 n번째 값 부터 m번째 값까지의 리스트를 만드는 것이다.
# listB = listA[n:m] 처럼 사용하면 listB에는 listA의 n번 인덱스 부터 m-1의 인덱스까지의 값이 들어간 리스트가 들어간다.
listB = listA[0:4]
print("listB(listA[0:4]): {0}\n".format(listB))

# 리스트의 길이를 알기 위해서는 len() 함수를 사용하면 된다.
print("len(listA): {0}".format(len(listA)))
print("len(listB): {0}".format(len(listB)))