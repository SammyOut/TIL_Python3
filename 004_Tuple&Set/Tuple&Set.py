# 튜플은 선언 후 값을 바꿀 수 없는 리스트라고 보면 된다.
# ()로 선언을 한다.
tupleA = (1, 2, 3, 4, 5)
print("tupleA: {0}".format(tupleA))
print("type(tupleA): {0}".format(type(tupleA)))

# 원소가 하나인 튜플은 (a,)와 같이 선언을 한다.
tupleB = (100,)
print("tupleB: {0}".format(tupleB))
print("type(tupleB): {0}\n".format(type(tupleB)))

# 리스트와 같이 인덱스로 값을 호출하거나 슬라이싱을 할 수 있다.
print("tupleA[1]: {0}".format(tupleA[1]))
print("tupleA[0:3]: {0}\n".format(tupleA[0:3]))

# 하지만 append(), insert() 메소드를 사용하지 못하고 인덱스로 접근하여 값을 바꾸지 못한다.
tupleA.append(10)
tupleA.insert(0, 10)
tupleA[0] = 10

# 튜플을 리스트로 변환할 수 있다.
listA = list(tupleA)
print("listA: {0}".format(listA))
print("type(listA): {0}\n".format(type(listA)))

# 그 역으로 리스트를 튜플로 만들 수 있다.
tupleC = tuple(listA)
print("tupleC: {0}".format(tupleC))
print("type(tupleC): {0}\n".format(type(tupleC)))


# set은 집합 자료형이다.
# {}로 선언을 한다.
# 중복된 원소가 없는 리스트와 비슷하다.
# 5라는 중복된 원소가 있었지만 하나가 사라진 것을 확인할 수 있다.
setA = {1, 2, 3, 4, 5, 5}
print("setA: {0}".format(setA))
print("type(setA): {0}".format(type(setA)))
setB = {3, 4, 5, 6, 7, 8}
print("setB: {0}".format(setB))
print("type(setB): {0}\n".format(type(setB)))

# set에서 값을 추가하려면 append() 나 insert()가 아닌 add() 메소드를 사용해야 한다.
setA.add(0)
print("setA: {0}\n".format(setA))

# 집합 자료형인 만큼 교집합, 합집합, 차집합 등을 구할 수 있다.
# 교집합은 & 또는 intersection() 메소드로 구할 수 있다.
print("setA & setB: {0}".format(setA & setB))
print("setA.intersection(setB): {0}\n".format(setA.intersection(setB)))

# 합집합은 | 또는 union() 메소드로 구할 수 있다.
print("setA | setB: {0}".format(setA | setB))
print("setA.union(setB): {0}\n".format(setA.union(setB)))

# 차집합은 - 또는 difference() 메소드로 구할 수 있다.
print("setA - setB: {0}".format(setA - setB))
print("setA.difference(setB): {0}".format(setA.difference(setB)))
