print('키와 몸무게를 미국 표준 단위로 변환해 드립니다.')
cm = int(input('손님의 키를 센티미터 단위로 입력하세요. '))
print('키는', cm, '센티미터 입니다.')
kg = int(input('손님의 몸무게를 킬로그램 단위로 입력하세요. '))
print('몸무게는', kg, '킬로그램 입니다.')

cm2foot = int(cm*0.032808399)
inch = round((cm*0.032808399-int(cm*0.032808399))*12)
kg2pound = round(kg*2.2046226218)

print('손님의 키와 몸무게는 다음과 같습니다.')
print(cm2foot,'피트', inch, '인치')
print(kg2pound, '파운드')
print('저희 서비스를 이용해주셔서 감사드립니다.')