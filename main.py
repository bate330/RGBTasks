

class Main():
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def IterateValue(self,to_iterate):
        test = str(to_iterate)
        is_passed = 0
        for element in range(1, len(test)):
            if test[element] == test[element-1]:
                is_passed = 1
            else:
                pass
            if test[element-1] > test[element]:
                is_passed = 0
                break

        return is_passed

    def CheckNumbers(self):
        results = 0
        for i in range(self.min_value, self.max_value):
            results += self.IterateValue(i)
        return results

    def GetResult(self):
        return self.CheckNumbers()

range_min = 265275
range_max = 781584
task1 = Main(range_min,range_max)
result = task1.GetResult()
print(result)