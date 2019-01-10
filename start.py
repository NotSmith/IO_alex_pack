import re
"""
Alex's Input and Output library
"""

"""
Output will be controlled/ set up by a plain txt file that you can configure, the layoiut in the txt file will be how it 
appears in the console!
"""
#TODO: start working.
class Output:
    def __init__(self, templateFile, itemsList):
        self._templateFile = templateFile
        self._items = itemsList
        with open(self._templateFile, 'r') as templateFileOpen:
            tempVar = templateFileOpen.read()
            print(tempVar.format(*self._items))

    def __str__(self):
        return "Template File Name : {}".format(self._templateFile)

    def info(self):
        return """To use the Output template all you simply have to do is write what you want your output to look like 
        in a simple .txt file.
        For adding variables in a spesific place type {} this whole thing just utilises .format"""

if __name__ == '__main__':
    test1 = Output('testTemplate.txt', [])
    print(test1)
