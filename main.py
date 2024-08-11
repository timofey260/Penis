from Drizzle.Data.LingoList import LingoList, LingoNumber

algo = LingoList([LingoNumber(0), LingoNumber(1), LingoNumber(-2)])
algo.sort()
for i in algo:
    print(i)