import qrcode

file_path = 'QRcode\\qrList.txt'

f = open(file_path, 'r', encoding='UTF-8')
lines = f.readlines()

for line in lines :
    line = line.strip()
    print(line)

f.close()