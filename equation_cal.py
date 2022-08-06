from numpy import sqrt, gcd
from decimal import Decimal

class quadratic_with_one_unknown():
    '''
    calculate using formula (-b±√b^2-4ac)/2a
    '''
    def simplify_sqrt(self, num):
        self.n = 1000
        while self.n != 0:
            b = num / self.n / self.n
            list_1 = []
            list_1.append(b)
            for i in list_1:
                self.list_2 = '{:g}'.format(i)
            if Decimal(self.list_2) == Decimal(self.list_2).to_integral():
                if int(self.list_2) == 1:
                    print(self.n)
                    del list_1[0]
                    self.n = 0
                else:
                    if self.n == 1:
                        return "√" + self.list_2
                    else:
                        return str(self.n) + "√" + self.list_2
            else:
                self.n -= 1
                del list_1[0]
    def basic_processing(self, equation):
        polynomial = equation.split("=")[0]
        all_terms = polynomial.split("+")
        term_1 = all_terms[0]
        term_2 = all_terms[1]
        term_3 = all_terms[2]
        try:
            self.a = int(term_1.split("x^2")[0])
        except ValueError:
            self.a = 1
        try:
            self.b = int(term_2.split("x")[0])
        except ValueError:
            self.b = 1
        try:
            self.c = int(term_3)
        except ValueError:
            self.c = 1
        common_division_1 = gcd(self.a, self.b)
        common_division_2 = gcd(self.b, self.c)
        common_division_all = gcd(common_division_1, common_division_2)
        self.a = round(self.a / common_division_all)
        self.b = round(self.b / common_division_all)
        self.c = round(self.c / common_division_all)
        self.delta = self.b ** 2 - 4 * self.a * self.c
    def exact_result(self, equation):
        '''
        input string like ax^2+bx+c=0, terms arrange in descending order according to times, 
        and then export exact result (output is a string)
        '''
        self.basic_processing(equation)
        if self.delta < 0:
            simplify_res = self.simplify_sqrt(-self.delta)
            if gcd(self.n, self.b) % 2 == 0:
                self.b = round(self.b / 2)
                self.n = self.n / 2
                if self.n == 1:
                    self.n = ""
                else:
                    self.n = round(self.n)
                simplify_res = str(self.n) + "√" + self.list_2
                if self.a == 1:
                    return str(-self.b) + "±" + simplify_res + "i"
                else:
                    return "(" + str(-self.b) + "±" + simplify_res + "i)/" + str(self.a)
            else:
                return "(" + str(-self.b) + "±" + simplify_res + "i)/" + str(2 * self.a)
        elif self.delta == 0:
            return str(-self.b / 2 / self.a)
        else:
            simplify_res = self.simplify_sqrt(self.delta)
            if gcd(self.n, self.b) % 2 == 0:
                self.b = round(self.b / 2)
                self.n = self.n / 2
                if self.n == 1:
                    self.n = ""
                else:
                    self.n = round(self.n)
                simplify_res = str(self.n) + "√" + self.list_2
                if self.a == 1:
                    return str(-self.b) + "±" + simplify_res
                else:
                    return "(" + str(-self.b) + "±" + simplify_res + ")/" + str(self.a)
            else:
                return "(" + str(-self.b) + "±" + simplify_res + ")/" + str(2 * self.a)
myCal = quadratic_with_one_unknown()
print (myCal.exact_result("x^2+4x+1=0"))