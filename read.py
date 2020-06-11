
data = []
count = 0
with open ("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # %是用來求餘數，等於1000筆才印一次 
			print (len(data))

print ("檔案讀取完畢，總共有", len(data), '筆資料') # 算出資料共幾筆


sun_len = 0
for d in data:
	sun_len += len(d)
print ('平均長度是', sun_len / len(data))  
