import sys
import requests
from bs4 import BeautifulSoup
import re
import datetime
import merge

# # 文章地址
# person_url = 'https://mp.weixin.qq.com/s/c2AjT8UMAM40SdJVmN4b2g'
# 查询接口
api_url = 'https://restapi.amap.com/v3/place/text?parameters'



# return yyyy-mm-dd
def formatDate(date):
  date = re.findall('\d+', date)
  date = [int(i) for i in date]
  if (len(date) == 2):
    date.insert(0, 2022)
  d = datetime.date(date[0], date[1], date[2])
  return d.isoformat()

def getDayDetail (url):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
  }
  resp = requests.get(url, headers)

  bsobj = BeautifulSoup(resp.content, 'lxml')

  p_list = bsobj.find_all('p')
  persons = [] # 确诊病例列表
  no = ''
  for p in p_list:
    text = p.getText()
    if (text.startswith('病例')):
      no = text
    if (text.startswith('男') or text.startswith('女')):
      text = text.replace(' ', '').replace('，',',').replace('。', '')
      text = no + ',' + text
      persons.append(text)
  
  # 发布时间
  em_list = bsobj.find_all('em')
  datetime = ''
  for em in em_list:
    if (em.get('id') == 'publish_time'):
      datetime = em.getText()
  
  titleNode= bsobj.find_all('h1')[0] 
  date = '' # 标题里的日期是发布日期的前一天
  if (titleNode):
    r = re.findall('\d+月\d+日', titleNode.getText())
    if (len(r) > 0):
      date = r[0]

  return {'persons': persons, 'publist_time': datetime, 'date': date}


def getPosition (keywords):
  params = {
    'key': '3ac289c5cd04b1697e4e89fbc6c7b9b3',
    'keywords': keywords,
    'city': 'shenzhen',
  }
  res = requests.get(api_url, params=params)
  data = res.json()
  if(data['status'] == '1'):
    poi_list = data['pois']
    if (len(poi_list) > 0):
      location = poi_list[0]['location']
      return location
  return ''


def export (person_url):
  info = getDayDetail(person_url)
  persons = info.get('persons')
  date = info.get('date')
  date = formatDate(date)
  if (len(persons) == 0):
    print('没有确诊信息')
    return

  outfile = './output/' + date + '.csv'
  f = open(outfile, 'w', encoding='utf-8')
  head = ['no', 'sex', 'age', 'address', 'x', 'y' 'date']
  f.write(','.join(head) + '\n')

  address_dict = {}
  for p in persons:
    line = p.replace('居住在', '')
    person_info = line.split(',')
    address = person_info[3]
    location = address_dict.get(address)
    if (location == None):
      location = getPosition(address).split(',')
      address_dict[address] = location

    if (len(location) != 2):
      location = ['0', '0']
      print('地址异常', person_info[2])
    info = person_info[:3] + [address, location[0], location[1], date]
    line = ','.join(info) + '\n'
    f.write(line)
  print('导出完成')

if __name__ == '__main__':
  url, isMerge = sys.argv[1:]
  if (url) :
    export(url)
    print(url)
    if (isMerge == 'm'):
      merge.main()


# export(person_url)
