import random
import string

# набора ASCII в верхнем и нижнем регистрах + строка символов, представляющих цифры + наборы знаков препинания
total = string.ascii_letters + string.digits + string.punctuation

# Установим длину пароля в 16 символов
length = 16

password = "".join(random.sample(total, length))

# Вывод результата в консоль
print(password)