import time
import random


menulist = ['바람은', '빗물은']


print("그대여 아무 걱정하지 말아요.")
print("우리 함께 노래 합시다.")
print("밤은 다시 길고 깊어졌네 나는 점점 멀어 잠 못들게 돼 너도 느겼으면 좋겠는데")
print("나를 지나가며 웃은 거라지만 너의 하얀 옷은 너의 윙크가 묻어 닦아 ")
print("달콤한 색감이 물들어 조금씩 정신을 차렸을땐 알아 볼 수 도 없지 ")
for i in range(4, 0, -1):  
    print(f'{i}..')
    time.sleep(1)
# print("4..")
# time.sleep(1)
# print("3..")
# time.sleep(1) 
# print("2..")
# time.sleep(1)
# print("1..")
print("가득찬 마음이 여물다 못해 터지고 있어 내일은 말을 걸어 봐야지")
print("글로 적어내긴 어려운 내 기분을 너도 느꼈으면 좋겠는데")
print("??? 맞고 빛물의 젖어 흐려지겠지만 너는 항상 빛을 번쩍이겠지만")
menu = random.choice(menulist)
print(f'{menu}입니다')
