from tkinter import *
import random
menulist = ['바람은', '빗물은']



#  예제 1) tkinter 파이썬 GUI 레이블(label)
# tkinter를 사용하여 텍스트를 나타내보자

# 1. 루트화면 (root window) 생성
tk = Tk() 
# 2. 텍스트 표시
label = Label(tk,text='그라데이션') 
# 3. 레이블 배치 실행
label.pack()
def event():
    menu = random.choice(menulist)
    button['text'] = f'{menu}추천!'

button = Button(tk,text='추천메뉴.',command=event)
# button2 = Button(tk,text='버튼2 입니다.')
button.pack(side=LEFT,padx=10,pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
# button2.pack(side=LEFT, padx=10, pady= 10)
# tk.mainloop()
# 4. 메인루프 실행
tk.mainloop()


