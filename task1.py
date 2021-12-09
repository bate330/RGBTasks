

class Main():
    def __init__(self, minValue, maxValue):
        self.minValue = minValue
        self.maxValue = maxValue

    def __IterateValue(self, iterateValue): #iterate number from arg
        iterateStr = str(iterateValue)
        isPassed = 0
        for element in range(1, len(iterateStr)):   #iterate all digit from iterate value
            if iterateStr[element] == iterateStr[element-1]:    #check if is it pair
                isPassed = 1
            else:
                pass
            if iterateStr[element-1] > iterateStr[element]: #check if raise
                isPassed = 0
                break
        return isPassed

    def __CheckNumbers(self):   #check numbers from range and put into iterate
        results = 0
        for i in range(self.minValue, self.maxValue):
            results += self.__IterateValue(i)
        return results

    def GetResult(self):    #get final result
        return self.__CheckNumbers()    #get number of correct solutions only

minValue = 265275
maxValue = 781584
task1 = Main(minValue, maxValue)
result = task1.GetResult()
print(result)