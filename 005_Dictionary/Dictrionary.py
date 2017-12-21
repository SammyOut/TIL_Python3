# Dictionary는 사전 자료형이다. (JAVA의 map 자료형과 비슷하다.)
dictA = {"치킨": "치킨 먹고싶다", "피자": "피자도 좋아", "족발": "족발 안먹은지 오래됐네"}
# 사전은 키: 값 으로 매칭이 되어있다. 키를 넣어주면 값을 반환해준다.
print("dictA['치킨']: {0}".format(dictA["치킨"]))
print("dictA['피자']: {0}\n".format(dictA["피자"]))

# dictionary에 키와 값을 추가할 수 도 있다.
dictA["추가"] = "추가한 내용!"
print("dictA['추가']: {0}\n".format(dictA["추가"]))

# keys() 메소드를 사용해 dictionary에 있는 키 들을 리스트로 담을 수 있다.
print("dictA.keys(): {0}\n".format(dictA.keys()))

# values() 메소드를 사용해 dictionary에 있는 값 들을 리스트로 담을 수 있다.
print("dictA.values(): {0}\n".format(dictA.values()))
