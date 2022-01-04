import os
import time

print("Installing modules....")
time.sleep(2)
os.system("pip install requests")
print("\n<~~~~~~~~~~~~~~~~~~~~> Module requests installed\n")
os.system("pip install colorama")
print("\n<~~~~~~~~~~~~~~~~~~~~> Module colorama installed\n")
time.sleep(1)
os.remove("setup.py")
print("All modules installed")
