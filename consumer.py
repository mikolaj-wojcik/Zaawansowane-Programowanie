

from time import sleep
import os


while(True):
    sleep(5)
    with open("work.txt",'r') as file_r:
        lines = file_r.readlines()
        for line in lines:   
            if line == 'pending\n':
                index = lines.index(line)
                lines[index] = 'in_progress\n'
                with open("work.txt",'w') as file_w1:
                    file_w1.writelines(lines)
                    file_w1.close()
                    sleep(20)
                    with open("work.txt",'w')as file_w:
                        
                        lines[index] = 'done\n'
                        file_w.writelines(lines)
                        file_w.close()
                        break
            
