import csv

def strip(s):
  return s[1:len(s)-1]

def remove_comma(s):
  return ''.join(s.split(','))

stock = []
price_num = []
num_stock = 6

for i in range(num_stock):
    stock.append([])

with open('data_new.csv', 'rU') as f:
  reader = csv.reader(f)
 
  i = j = 0
  title_old = ''
  for line in reader:
    num_price = len(line[1])
    price = map(remove_comma, map(strip, line[1][2:num_price-2].split(', u')))

    title = line[2][:len(line[2])-1]
    if j == 0:
      title_old = title

    if title == title_old:
      stock[i] += price
    else:
      title_old = title
      i += 1
    j += 1
    
    #date = line[0][2:].split(', u')
    #del(date[len(date)-1])
    #date_new = map(strip, date)

  for i in range(num_stock):
    price_num.append(len(stock[i]))

  min_num = min(price_num)

  stock_trim = []
  stock_trim.append(stock[3][:min_num])
  stock_trim.append(stock[0][:min_num])
  stock_trim.append(stock[1][:min_num])
  stock_trim.append(stock[2][:min_num])
  stock_trim.append(stock[4][:min_num])
  stock_trim.append(stock[5][:min_num])

  #for i in range(num_stock):
  #  stock_trim.append(stock[i][:min_num])

  stock_table = zip(stock_trim[0], stock_trim[1], stock_trim[2], stock_trim[3], 
                    stock_trim[4], stock_trim[5])

  f = open("price_data.txt", 'r+')

  for i in range(min_num):
    f.write('| '.join(stock_table[i]) + '\n')

  f.close()


