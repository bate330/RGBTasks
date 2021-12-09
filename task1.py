

class Main():
    def __init__(self, minValue, maxValue):
        self.minValue = minValue
        self.maxValue = maxValue

    def __IterateValue(self, iterateValue):
        iterateStr = str(iterateValue)
        isPassed = 0
        for element in range(1, len(iterateStr)):
            if iterateStr[element] == iterateStr[element-1]:
                isPassed = 1
            else:
                pass
            if iterateStr[element-1] > iterateStr[element]:
                isPassed = 0
                break
        return isPassed

    def __CheckNumbers(self):
        results = 0
        for i in range(self.minValue, self.maxValue):
            results += self.__IterateValue(i)
        return results

    def GetResult(self):
        return self.__CheckNumbers()

minValue = 265275
maxValue = 781584
task1 = Main(minValue, maxValue)
result = task1.GetResult()
print(result)