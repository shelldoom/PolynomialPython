import operator
import itertools as it

class Polynomial:
    def __init__(self, coeff = [], var = "x"):
        self.coeff = coeff
        self.degree = None
        self.var = var
        if(len(coeff) > 0):
            self.degree = len(coeff)-1
    
    def __eq__(self, p2):
        assert isinstance(p2, Polynomial)
        return self.coeff == p2.coeff

    def __len__(self):
        '''
        Returns the maximum degree of the equation
        '''
        return self.degree

    def __str__(self):
        degree_counter = self.degree
        expression = []
        for current_coeff in self.coeff:
            if current_coeff == 0:
                degree_counter -= 1
                continue
            if degree_counter == 0:
                current_coeff = f"{current_coeff}"
            if current_coeff in {-1, 1}:
                current_coeff = "" if current_coeff == 1 else "-"

            if degree_counter > 1:  # ax^2
                expression.append(f"{current_coeff}{self.var}^{degree_counter}")
            elif degree_counter == 1: # bx
                expression.append(f"{current_coeff}{self.var}")
            else: # constant
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
            r *= r
        return r
    
    def value(self, x):
        '''
        Get the value of the polynomial at 'x'
        '''
        r = 0
        for i in range(self.degree, -1, -1):
            r += (x**i)*self.coeff[self.degree - i]
        
        return r


if __name__ == "__main__":
    # p1 = Polynomial([1, 2, 0, 3, 4])
    # p2 = Polynomial([1, 2, 4, 5, 6])
    # print(p1)
    # print(p2)
    # print(p1+p2)
    # print(p1-p2)
    # print(Polynomial([]))
    # print(Polynomial([0, 0, 1]))
    # print(Polynomial([0, 1, 0]))
    # print(Polynomial([0, 0, 10]))
    # print(Polynomial([1, 1]) * Polynomial([1, 1]))
    # print(Polynomial([1, 1]) ** 2)
    # print(Polynomial([1, 2, 1]).value(x = 4))   # x^2 + 2x + 1 == (x + 1)^2
    print(str(Polynomial([1, 2, 4], var="n")))