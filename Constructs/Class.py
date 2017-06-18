class polygon:
    def __init__(self):
        self.no_sides = int(input("Enter number of sides : "))
        self.len = [0 for i in range(self.no_sides)]

    def input_sides(self):
        for i in range(self.no_sides):
            self.len[i] = int(input("Enter side " + str(i+1) + " : "))

class triangle(polygon):
    def calculate_area(self):
        return(self.len[0] * self.len[1] * self.len[2])

t1  = triangle()
t1.input_sides()
print(t1.calculate_area())
