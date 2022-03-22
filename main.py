import dataHelper

record_dict = {
  #时间是公众号文章的发布日期
  '20220321': 'https://mp.weixin.qq.com/s/fZ3fQek0kKfBMXYvyIeg4Q',
  '20220320': 'https://mp.weixin.qq.com/s/c2AjT8UMAM40SdJVmN4b2g',
  '20220319': 'https://mp.weixin.qq.com/s/hXwC8qdDhVvFzBa0RGXIEw',
  '20200318': 'https://mp.weixin.qq.com/s/ClFyVViNs4zbu54xDLJpOw',
  '20220317': 'https://mp.weixin.qq.com/s/ALZ5X6fJB24bYzFP1gYkvQ',
  '20220316': 'https://mp.weixin.qq.com/s/RH_Z1aNdcDZO7oLYOZhmag',
  '20220315': 'https://mp.weixin.qq.com/s/k2XGjr4vbl6GsRxgOufqAA',
  '20220314': 'https://mp.weixin.qq.com/s/T7gvHq14Dy9LdJwrHddmZQ',
  '20220313': 'https://mp.weixin.qq.com/s/MPwM7x2IQtkxSbEjDde_cQ',
  '20220312': 'https://mp.weixin.qq.com/s/7OujSHsbPO_PoZ8DV6CUtA',
  '20220311': 'https://mp.weixin.qq.com/s/GAI4Pgo3pIot-hrCsCyoWQ', 
  '20220310': 'https://mp.weixin.qq.com/s/xRIP8h9dDSf7NgvYoMKlHg',
  '20220309': 'https://mp.weixin.qq.com/s/aFmy1D519tRpOEU3SkLfCQ',
  '20220308': 'https://mp.weixin.qq.com/s/Yj282_z0gBCG1Pt6sBuwYg',
  '20220307': 'https://mp.weixin.qq.com/s/UFkFfUQwgSsAqHOEG1hJyQ',
  '20220306': 'https://mp.weixin.qq.com/s/yr4S-tdno2HH881mkYs6UA'
}


def main():
  for k in record_dict.keys():
    dataHelper.export(record_dict[k])  

if __name__ == '__main__':
    main()
    