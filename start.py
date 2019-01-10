
"""
Alex's Input and Output library
"""

"""
Output will be controlled/ set up by a plain txt file that you can configure, the layoiut in the txt file will be how it 
appears in the console!
"""


class Output:
    def __init__(self, template_file):
        self._templateFile = template_file
        with open(self._templateFile, 'r') as templateFileOpen:
            self._template = templateFileOpen.read()

    def __str__(self):
        return "Template File Name : {}".format(self._templateFile)

    @staticmethod
    def info():
        return """ Just type away in a normal txt file it will hold the same shape and structure as it, if you want to 
        add variables to the template just us {} and when giving the variable that will be placed in those spots be sure
        to have them in a list in order of what goes where."""

    def output(self, items_list):
        temp_var = self._template
        print(temp_var.format(*items_list))


if __name__ == '__main__':
    test1 = Output('testTemplate.txt')
    print(test1)
    test1.output([1, 2, 3, 4])
    test1.output(['pog', 'absolute', 'champ', 'mydoode'])

    test2 = Output('testTemplate2.txt')
    test2.output(['1.5million euro', 'Veteran in Quake maybe', 'none'])

    test2.output(['wow would you look at that', 'PRO minecraft', 'mincraft takes skill'])