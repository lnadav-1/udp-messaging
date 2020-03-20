import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
com = 'start /B start cmd.exe @cmd /k C:\Python34\python.exe  '
os.system(com)
