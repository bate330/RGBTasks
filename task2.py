

class Main():
    def __init__(self, filename, params, paramsWithCondition):
        self.filename = filename
        self.params = params
        self.paramsWithCondition = paramsWithCondition

    def __OpenFile(self, filename):
        file = open(filename,"r")
        return file.readlines()

    def __Refactor(self):
        content = self.__OpenFile(self.filename)
        content.append('\n')
        refactoredContent = []
        oneDoc = ''
        for i in content:
            if i == '\n':
                refactoredContent.append(oneDoc)
                oneDoc = ''
                continue
            else:
                i = i.replace('\n', ' ')
                oneDoc += i
        return self.__GetDictionary(refactoredContent)

    def __ConvertToDict(self, lst):
        res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
        return res_dct

    def __GetDictionary(self, content):
        attribs = []
        for i in content:
            attribs.append(i.split())
        changedattribs = []
        dictionary = []
        for attrib in attribs:
            changedattribs.clear()
            for param in attrib:
                changedattribs.append(param.split(':')[0])
                changedattribs.append(param.split(':')[1])
            dictionary.append(self.__ConvertToDict(changedattribs))
        return dictionary

    def __GetCorrectDocs(self, dictionary):
        correctDocs = 0
        for doc in dictionary:
           if set(doc) == set(self.params) or set(doc) == set(self.paramsWithCondition):
               correctDocs += 1
        return correctDocs

    def GetResult(self):
        content = self.__Refactor()
        correctDocs = self.__GetCorrectDocs(content)
        return correctDocs


path = '.\\Docs\\InputFile.txt'
params = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt']
paramsWithCondition = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
task2 = Main(path, params, paramsWithCondition)
result = task2.GetResult()
print(result)
