

class Main():
    def __init__(self, minValue, maxValue):
        self.minValue = minValue
        self.maxValue = maxValue

    def IterateValue(self,to_iterate):
        test = str(to_iterate)
        isPassed = 0
        for element in range(1, len(test)):
            if test[element] == test[element-1]:
                isPassed = 1
            else:
                pass
            if test[element-1] > test[element]:
                isPassed = 0
                break

        return isPassed

    def CheckNumbers(self):
        results = 0
        for i in range(self.minValue, self.maxValue):
            results += self.IterateValue(i)
        return results

    def GetResult(self):
        return self.CheckNumbers()

range_min = 265275
range_max = 781584
task1 = Main(range_min,range_max)
result = task1.GetResult()
print(result)