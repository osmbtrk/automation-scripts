import time
import os
x= input("shutdown after:")
y=int(x)
z=y*60
print(type(z))
print(z)
time.sleep(z)
os.system("shutdown /s /t 1")