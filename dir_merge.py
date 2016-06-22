import sys
import os
import pprint

'''
usage: Python t.py Directory1 Directory2 NEW_DIRECTORY

i.e.
       python t.py tmp1 tmp2 tmp3
'''

d1=sys.argv[1]
d2=sys.argv[2]
d3=sys.argv[3]

files_in_d1 = os.listdir(d1)
files_in_d2 = os.listdir(d2)

print("Contents of d1 are...")
pprint.pprint(files_in_d1)
print("Contents of d2 are...")
pprint.pprint(files_in_d2)

common_files = list(set(files_in_d1).intersection(files_in_d2))
unique_files=  list(set(files_in_d1)-set(files_in_d2))
print("Common Files are ")
pprint.pprint(common_files)
if len(common_files) > 0:
  try:
    os.mkdir(d3)
  except:
    print("Can not create a directory")

  for f in common_files:
     os.rename(d1+'/'+f,d3+'/'+f)
     print("Moved file "+f)
else:
  print("Nothing Matches in the 2 directories")
