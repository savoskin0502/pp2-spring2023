import os


print(os.getcwd())
print(os.listdir('.'))
os.chdir('./tests')
print(os.getcwd())
print(os.listdir('.'))
