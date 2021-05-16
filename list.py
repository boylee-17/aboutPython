#리스트 실습
li = [3, 1, "배가", 4 "고파요", 5, 1]

#리스트 인덱싱
print(li[2])

#리스트 슬라이싱
print(li[0:4]) #<-꼭꼭 자르고 싶은 놈 뒷 숫자

#리스트 길이 구해주는 내장함수 : Len(리스트 변수명)
print(len(li))

리스트를 오름차 순으로 정렬해주는 내장함수 : 리스트 변수명.sot() <-리스트에만 쓸 수 있음
li2=[3, 1, 4, 5, 2]
print(li2.sort()) #->이건 안됨
li2.sort()
print(li2)

#참고 sorted ->원본배열 건들지 않고 새로운 걸 만들게 됨
print(sorted(li2))
print(li2)

li3=sorted(li2)
print(li3)

print(li2)
li2.sort()
print(li2)

#sort()로 내림차순 하는 법을 구글링 해서 알아보도록 하자 <-보너스 과제
#여기에 코드를 적어주세요 (print 사용)

#리스트 내의 특정 원소 인덱스를 반환하는 함수 : 리스트변수.index()
print(li.index("배가"))

리스트 내의 특정 원소의 갯수를 세어주는 함수 : 리스트변수.count(요소)
print(li.count(1))