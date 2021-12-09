

class Main():
    def __init__(self, filename, params, paramsWithCondition):
        self.filename = filename
        self.params = params
        self.paramsWithCondition = paramsWithCondition

    def __OpenFile(self, filename): #read-only file
        file = open(filename,"r")
        return file.readlines()

    def __Refactor(self):   #remove special characters
        content = self.__OpenFile(self.filename)
        content.append('\n')    #eof
        refactoredContent = []
        oneDoc = ''
        for i in content:   #for each line
            if i == '\n':   #if empty line
                refactoredContent.append(oneDoc)
                oneDoc = ''
                continue
            else:
                i = i.replace('\n', ' ')
                oneDoc += i
        return self.__GetDictionary(refactoredContent)

    def __ConvertToDict(self, lst): #convert list to dictionary
        res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
        return res_dct

    def __GetDictionary(self, content): #get keys and values to create ditctionary
        pairsToDict = []
        for i in content:   #get pairs(key:value) from file by space
            pairsToDict.append(i.split())
        allElementsOfDict = []
        dictionary = []
        for attrib in pairsToDict:  #for each doc
            allElementsOfDict.clear()
            for param in attrib:    #for each pair in one doc
                allElementsOfDict.append(param.split(':')[0])   #get key
                allElementsOfDict.append(param.split(':')[1])   #get value
            dictionary.append(self.__ConvertToDict(allElementsOfDict))  #create dictionaries
        return dictionary

    def __GetCorrectDocs(self, dictionary): #get a number with correct documents only
        correctDocs = 0
        for doc in dictionary:  #iterate through all documents in file
           if set(doc) == set(self.params) or set(doc) == set(self.paramsWithCondition):    #if keys correct
               correctDocs += 1
        return correctDocs

    def GetResult(self):    #get final result
        try:
            content = self.__Refactor() #refactor content from file
            correctDocs = self.__GetCorrectDocs(content)    #count correct docs
        except:
            correctDocs = 'No file'
        return correctDocs


path = '.\\Docs\\InputFile.txt'
params = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt']
paramsWithCondition = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
task2 = Main(path, params, paramsWithCondition)
result = task2.GetResult()
print(result)
