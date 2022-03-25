import sys
import dataHelper
import merge


def main():
  f = open('./record.csv')
  c = sys.argv[1:]
  
  record=[]
  if (c == 'all'):
    record = f.readlines()
  else:
    record = f.readlines()[-1:]

  print(record)
  for k in record:
    dataHelper.export(k.split(',')[1])
  
  merge.main()

if __name__ == '__main__':
    main()
    