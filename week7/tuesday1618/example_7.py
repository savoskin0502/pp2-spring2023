import os

print(os.getcwd())
os.chdir('./tests')  # relative path
# os.chdir('/Users/roman/Desktop/lectures/pp2/pp2-spring2023/week7/tuesday1618/tests')  # absolute path
print(os.getcwd())
print(
    os.listdir(os.getcwd())
)

