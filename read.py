
data = []
count = 0
with open ("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # %是用來求餘數，等於1000筆才印一次 
			print (len(data))
print (data [0]) #印出第一筆資料
print (len(data)) # 算出資料共幾筆
