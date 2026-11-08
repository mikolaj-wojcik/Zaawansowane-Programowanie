from time import sleep, time


while(True):
    file = open("work.txt", "a")
    file.writelines('pending\n')
    file.close()
    sleep(2)