import csv
import datetime

def strip(s):
  return s[1:len(s)-1]

def remove_comma(s):
  return ''.join(s.split(','))

def num_month(s):
  if s == 'Jan': 
    return 1
  elif s == 'Feb':
    return 2
  elif s == 'Mar':
    return 3
  elif s == 'Apr':
    return 4
  elif s == 'May':
    return 5
  elif s == 'Jun':
    return 6
  elif s == 'Jul':
    return 7
  elif s == 'Aug':
    return 8
  elif s == 'Sep':
    return 9
  elif s == 'Oct':
    return 10
  elif s == 'Nov':
    return 11
  else:
    return 12  

def parse_date(s):
  date = s.split(' ')
  return [num_month(date[0]), int(date[1]), int(date[2])]

stock = []
price_num = []
num_stock = 7

for i in range(num_stock):
    stock.append([])

with open('data/data_new.csv', 'rU') as f:
  reader = csv.reader(f)
 
  i = j = 0
  title_old = ''
  for line in reader:
    num_price = len(line[1])
    price = map(remove_comma, map(strip, line[1][2:num_price-2].split(', u')))

    date = line[0][2:].split(', u')
    del(date[len(date)-1])
    date = map(strip, date)
    date = map(remove_comma, date)
    date = map(parse_date, date)

    weekDay = [str(datetime.date(x[2], x[0], x[1]).weekday()) for x in date] 

    title = line[2][:len(line[2])-1]

    if j == 0:
      title_old = title

    if title != title_old:
      title_old = title
      i += 1
    
    if i == 3:
      stock[num_stock-1] += weekDay
    #stock[i] += map(lambda (x,y): x + ',' + y, zip(price, weekDay))
    stock[i] += price
    j += 1
    
  print len(stock[3])
  print len(stock[num_stock-1])

  for i in range(num_stock):
    price_num.append(len(stock[i]))

  min_num = min(price_num)

  stock_trim = []
  stock_trim.append(stock[3][:min_num])

  for i in range(num_stock):
    if i != 3:
      stock_trim.append(stock[i][:min_num])

  stock_table = zip(*stock_trim)

  f = open("price_data.txt", 'r+')

  for i in range(min_num):
    f.write('| '.join(stock_table[i]) + '\n')

  f.close()


