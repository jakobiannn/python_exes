matr = [
		 [0, -1, 45, 20, 45],
		 [-1, 0, 40, 35, 15],
		 [45, 40, 0, 35, 10],
		 [20, 35, 35, 0, 70],
		 [45, 15, 10, 70, 0]
	   ]
def search_min(tr, vizited):#1 место для оптимизации
	min=max(max(tr))
	index2 = 0
	for ind in vizited:
		for index, elem in enumerate(tr[ind]):
			if elem>0 and elem<min and index not in vizited:
				min=elem#веса путей
				index2=index# индекс города
	return [min, index2]

def prim(matr):
	toVisit=[i for i in range(1,len(matr))]# города кроме начального(0)
	vizited=[0]
	result=[0]# начнем с минска
	for index in toVisit:
		weight, ind=search_min(matr, vizited)
		result.append(weight)#в результат будут заноситься веса
		vizited.append(ind)# содержит карту пути
	result[len(matr) - 1], result[len(matr) - 2] = result[len(matr) - 2], result[len(matr) - 1]
	return result
print(prim(matr))
