import os

print(os.getcwd())  # get current working directory
print(os.listdir('.'))
print(os.listdir(os.getcwd()))
os.chdir('./tests')
print(os.getcwd())
# open('rawdata.txt', mode='r') - raise FileNotFoundError
