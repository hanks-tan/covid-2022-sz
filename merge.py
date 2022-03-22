import os, os.path
import sys

def mergeFiles(fileList):
  outf = './output/allData.csv'
  outfile = open(outf, 'w', encoding='utf-8')
  ishead = True
  for fs in fileList:
    f = open(fs, 'r', encoding='utf-8')
    lines = f.readlines()
    if (ishead):
      outfile.writelines(lines)
      ishead = False
    else:
      outfile.writelines(lines[1:])
  outfile.close()

def main():
  scan = './output/'

  allDataFile = os.path.join(scan, 'allData.csv')
  if (os.path.exists(allDataFile)):
    os.remove(allDataFile)
  
  files = []
  for f in os.listdir(scan):
    if (f.endswith('.csv')):
      files.append(os.path.join(scan, f))
  mergeFiles(files)

if __name__ == '__main__':
  main()