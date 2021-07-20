import time
from playsound import playsound
def convert():
    Ans = input("Введи что нибудь для прикола ")
    if Ans == ("tiky"):
        print('AOOAOOOOOOOAOO')
        playsound ('Music.mp3')
    else:
        print("Прикол")
        playsound('fard.mp3')
convert()

while True:
    flag = input('Ещё раз? [Да/Нет] (ПИШИ С БОЛЬШОЙ БУКВЫ СУКА): ')

    if flag == 'Да':
          convert()
    else:
        break

time.sleep(100)