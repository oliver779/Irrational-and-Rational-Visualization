import variables as v

"""This is the Turtle_Drawing Class, which will need an input in the form
of words or a number and will be able to plot it using the python turtle
library.
It allows for the visualization of irrational and rational numbers as well as 
words and sentences. It imports variables and a json file to do so.
"""

class Turtle_Drawing:
    def __init__(self, basse, itt, num = None, phra = None, x = None, y = None):
        self.base = basse
        self.itterations = itt
        self.length = 10
        self.number = num
        self.phrase = phra
        self.x = x
        self.y = y
        self.full_circle = 360
        self.list_of_values = []
        self.distance = 5
        self.m_data = v.json.load(open(v.os.path.join(v.os.path.dirname(v.os.path.abspath(__file__)), 'turtle.json')))
        self.letter_array = []
        self.letter_to_number_array = []
        self.final_letter_array = []
        self.value_of_angle = self.full_circle/self.base
        self.zero_angle = self.value_of_angle * 0
        self.one_angle = self.value_of_angle * 1
        self.two_angle = self.value_of_angle * 2 
        self.three_angle = self.value_of_angle * 3
        self.four_angle = self.value_of_angle * 4
        self.five_angle = self.value_of_angle * 5
        self.six_angle = self.value_of_angle * 6
        self.seven_angle = self.value_of_angle * 7
        self.eight_angle = self.value_of_angle * 8
        self.nine_angle = self.value_of_angle * 9
     
    def zero(self):
        if self.zero_angle > 360:
            while self.zero_angle >= 360:
                self.zero_angle = self.zero_angle - 360
        v.t.hideturtle()
        v.t.speed(0)
        v.skk.right(self.zero_angle)
        v.skk.forward(self.distance)
    
    def one(self):
        if self.one_angle > 360:
            while self.one_angle >= 360:
                self.one_angle = self.one_angle - 360
        v.t.hideturtle()
        v.t.speed(0)
        v.skk.right(self.one_angle)
        v.skk.forward(self.distance)
    
    def two(self):
        if self.two_angle > 360:
            while self.two_angle >= 360:
                self.two_angle = self.two_angle - 360
        v.t.hideturtle()
        v.t.speed(0)
        v.skk.right(self.two_angle)
        v.skk.forward(self.distance)
    
    def three(self):
        if self.three_angle > 360:
            while self.three_angle >= 360:
                self.three_angle = self.three_angle - 360
        v.t.hideturtle()
        v.t.speed(0)
        v.skk.right(self.three_angle)
        v.skk.forward(self.distance)
    
    def four(self):
        if self.four_angle > 360:
            while self.four_angle >= 360:
                self.four_angle = self.four_angle - 360
        v.t.hideturtle()
        v.t.speed(0)
        v.skk.right(self.four_angle)
        v.skk.forward(self.distance)
    
    def five(self):
        if self.five_angle > 360:
            while self.five_angle >= 360:
                self.five_angle = self.five_angle - 360
        v.t.hideturtle()
        v.t.speed(0)
        v.skk.right(self.five_angle)
        v.skk.forward(self.distance)
    
    def six(self):
        if self.six_angle > 360:
            while self.six_angle >= 360:
                self.six_angle = self.six_angle - 360
        v.t.hideturtle()
        v.t.speed(0)
        v.skk.right(self.six_angle)
        v.skk.forward(self.distance)
    
    def seven(self):
        if self.seven_angle > 360:
            while self.seven_angle >= 360:
                self.seven_angle = self.seven_angle - 360
        v.t.hideturtle()
        v.t.speed(0)
        v.skk.right(self.seven_angle)
        v.skk.forward(self.distance)
    
    def eight(self):
        if self.eight_angle > 360:
            while self.eight_angle >= 360:
                self.eight_angle = self.eight_angle - 360
        v.t.hideturtle()
        v.t.speed(0)
        v.skk.right(self.eight_angle)
        v.skk.forward(self.distance)
    
    def nine(self):
        if self.nine_angle > 360:
            while self.nine_angle >= 360:
                self.nine_angle = self.nine_angle - 360
        v.t.hideturtle()
        v.t.speed(0)
        v.skk.right(self.nine_angle)
        v.skk.forward(self.distance)
        
    def get_number(self):
        if self.number == None:
            v.getcontext().prec = self.itterations       
            v1 = v.Decimal(self.x)
            v2 = v.Decimal(self.y)
            self.number = v1/v2
            
    def split_number(self):
        number_as_string = str(self.number)
        for character in number_as_string:
            if not character.isdigit():
                continue  
            self.list_of_values.append(int(character))
        return self.list_of_values

    def Turtle_function(self):
        for element in self.list_of_values:
            if element == 0:
                Turtle_Drawing.zero(self)
            if element == 1:
                Turtle_Drawing.one(self)
            if element == 2:
                Turtle_Drawing.two(self)
            if element == 3:
                Turtle_Drawing.three(self)
            if element == 4:
                Turtle_Drawing.four(self) 
            if element == 5:
                Turtle_Drawing.five(self)
            if element == 6:
                Turtle_Drawing.six(self)
            if element == 7:
                Turtle_Drawing.seven(self)
            if element == 8:
                Turtle_Drawing.eight(self)
            if element == 9:
                Turtle_Drawing.nine(self)
        v.t.done()
        
    def Turtle_letter(self):
        for i in self.phrase:
            self.letter_array.append(i)
        for i in self.letter_array:
            self.letter_to_number_array.append(self.m_data[i])
        for i in self.letter_to_number_array:
            for element in i:
                self.final_letter_array.append(int(element))
        for element in self.final_letter_array:
            if element == 0:
                Turtle_Drawing.zero(self)
            if element == 1:
                Turtle_Drawing.one(self)
            if element == 2:
                Turtle_Drawing.two(self)
            if element == 3:
                Turtle_Drawing.three(self)
            if element == 4:
                Turtle_Drawing.four(self) 
            if element == 5:
                Turtle_Drawing.five(self)
            if element == 6:
                Turtle_Drawing.six(self)
            if element == 7:
                Turtle_Drawing.seven(self)
            if element == 8:
                Turtle_Drawing.eight(self)
            if element == 9:
                Turtle_Drawing.nine(self)
        v.t.done()
        
obj= Turtle_Drawing(10, 500, x = 1, y = 9997)
obj.get_number()
obj.split_number()
obj.Turtle_function()
# obj.Turtle_letter()
        
        
        
        
        
        
        
        
        
        
        
        
        
