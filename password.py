import random
length = int(input("enter length of the password "))
word = "abcdedghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=`~_+[]{};:?><,./"
password = "".join(random.sample(word, length))
print(password)
