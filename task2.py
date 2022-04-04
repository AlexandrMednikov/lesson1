"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

time = int(input("Введите количество секунд:"))
fakeminutes = time//60
sec = time % 60
hours = fakeminutes//60

if hours>24:
    print("Введеное вами число насчитывает более 24 часов, попробуйте еще раз")
else:
 if hours==False:
    minutes = fakeminutes
 else:
    minutes = hours%60
 if hours < 10:
    hours = "0"+str(hours)
 if minutes < 10:
    minutes = "0"+str(minutes)
 if sec < 10:
    sec = "0"+str(sec)
 print(f"{hours}:{minutes}:{sec}")
