data=[]
with open('C:/Users/ASUS/Desktop/reviews.txt','r')as f:
    for line in f:
        data.append(line)
print('總共',len(data),'筆資料')
print(data[0])