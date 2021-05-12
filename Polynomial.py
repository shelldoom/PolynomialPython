import operator
import itertools as it

class Polynomial:
    def __init__(self, coeff = []):
        self.coeff = coeff
        self.degree = None
        if(len(coeff) > 0):
            self.degree = len(coeff)-1
    
    def __eq__(self, p2):
        assert isinstance(p2, Polynomial)
        return self.coeff == p2.coeff

    def __len__(self):
        '''
        Returns the degree of the equation
        '''
        return len(self.coeff)

    def __str__(self):
        degree_counter = self.degree
        expression = []
        for current_coeff in self.coeff:
            if degree_counter == 0:
                current_coeff = f"{current_coeff}"
            if current_coeff == 0:
                degree_counter -= 1
                continue
            if current_coeff == 1:
                current_coeff = ""
            if degree_counter > 1:
                expression.append(f"{current_coeff}x^{degree_counter}")
            elif degree_counter == 1:
                expression.append(f"{current_coeff}x")
            else:    
                expression.append(f"{current_coeff}")
            degree_counter -= 1

        return " + ".join(expression).replace(" + -", " - ")
    
    def __repr__(self):
        return f"Polynomial({self})"

    def __addSubtract(self, p2, operand):
        operand_lookup = {
            "+": operator.add,
            "-": operator.sub,
        }
        operand = operand_lookup[operand]

        assert isinstance(p2, Polynomial)
        p1_coeff = self.coeff
        p2_coeff = p2.coeff

        return Polynomial([operand(i[0],i[1]) for i in it.zip_longest(p1_coeff, p2_coeff, fillvalue=0)])

    def __sub__(self, p2):
        return self.__addSubtract(p2, "-")
    
    def __add__(self, p2):
        return self.__addSubtract(p2, "+")

    def __mul__(self, p2):
        p1 = self
        p3_len = p1.degree + p2.degree 
        p3_coeff = [0]*(p3_len + 1)

        for i in range(len(p1)):
            for j in range(len(p2)):
                p3_coeff[i+j] += p1.coeff[i] * p2.coeff[j]
        return Polynomial(p3_coeff)
    
    def __pow__(self, x):
        if x == 0:
            return Polynomial([1])
        if x == 1:
            return self
        r = self
        for _ in range(1, x):
            print(r)
            r *= r
            print(r)
        return r

# p1 = Polynomial([1, 2, 0, 3, 4])
# p2 = Polynomial([1, 2, 4, 5, 6])
# print(p1)
# print(p2)
# print(p1+p2)
# print(p1-p2)
# print(Polynomial([]))
# print(Polynomial([0, 0, 1]))
# print(Polynomial([0, 0, 10]))
print(Polynomial([1, 1]) * Polynomial([1, 1]))
print(Polynomial([1, 1]) ** 2)



