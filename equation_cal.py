from numpy import sqrt, gcd
from decimal import Decimal

class quadratic_with_one_unknown():
    '''
    calculate using formula (-b±√b^2-4ac)/2a
    '''
    def simplify_sqrt(self, num):
        '''
        simplify the num in sqrt
        '''
        self.integral = 1000
        while self.integral != 0:
            b = num / self.integral / self.integral
            list_1 = []
            list_1.append(b)
            for i in list_1:
                self.root = '{:g}'.format(i)
            if Decimal(self.root) == Decimal(self.root).to_integral():
                if int(self.root) == 1:
                    print(self.integral)
                    del list_1[0]
                    self.integral = 0
                else:
                    if self.integral == 1:
                        return "√" + self.root
                    else:
                        return str(self.integral) + "√" + self.root
            else:
                self.integral -= 1
                del list_1[0]
    def basic_processing(self, equation):
        '''
        analyze the equation, get its information and then simplify it
        '''
        # get the "a", "b", "c" in the formula
        polynomial = equation.split("=")[0]
        all_terms = polynomial.split("+")
        term_1 = all_terms[0]
        term_2 = all_terms[1]
        term_3 = all_terms[2]
        # if there isn't any coefficient written, then set it to 1
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
        # get the greatest common divisor of a, b, c
        common_division_1 = gcd(self.a, self.b)
        common_division_2 = gcd(self.b, self.c)
        common_division_all = gcd(common_division_1, common_division_2)
        # simplify a, b, c by dividing them with their greatest common divisor
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
        # no real root
        if self.delta < 0:
            simplify_res = self.simplify_sqrt(-self.delta)
            # if 2 is b's and integral's common divisor, then simplify the number by dividing all of them with 2
            if gcd(self.integral, self.b) % 2 == 0:
                self.b = round(self.b / 2)
                self.integral = self.integral / 2
                # if integral is 1, then don't show it
                if self.integral == 1:
                    self.integral = ""
                else:
                    self.integral = round(self.integral)
                simplify_res = str(self.integral) + "√" + self.root
                # if the denominator is 1, then avoid showing the fraction line
                if self.a == 1:
                    return str(-self.b) + "±" + simplify_res + "i"
                else:
                    return "(" + str(-self.b) + "±" + simplify_res + "i)/" + str(self.a)
            else:
                return "(" + str(-self.b) + "±" + simplify_res + "i)/" + str(2 * self.a)
        # one real root
        elif self.delta == 0:
            return str(-self.b / 2 / self.a)
        # two real root
        else:
            simplify_res = self.simplify_sqrt(self.delta)
            # if 2 is b's and integral's common divisor, then simplify the number by dividing all of them with 2
            if gcd(self.integral, self.b) % 2 == 0:
                self.b = round(self.b / 2)
                self.integral = self.integral / 2
                # if integral is 1, then don't show it
                if self.integral == 1:
                    self.integral = ""
                else:
                    self.integral = round(self.integral)
                simplify_res = str(self.integral) + "√" + self.root
                # if the denominator is 1, then avoid showing the fraction line
                if self.a == 1:
                    return str(-self.b) + "±" + simplify_res
                else:
                    return "(" + str(-self.b) + "±" + simplify_res + ")/" + str(self.a)
            else:
                return "(" + str(-self.b) + "±" + simplify_res + ")/" + str(2 * self.a)
    def fuzzy_result(self, equation):
        '''
        input string like ax^2+bx+c=0, terms arrange in descending order according to times, 
        and then export fuzzy result (output is a string)
        '''
        self.basic_processing(equation)
        # no real root
        if self.delta < 0:
            return str(-self.b / 2 / self.a) + "±" + str(round(sqrt(-self.delta) / 2 / self.a, 3)) + "i"
        # one real root
        elif self.delta == 0:
            return str(-self.b / 2 / self.a)
        # two real root
        else:
            base_num = -self.b / 2 / self.a
            delta_num = sqrt(self.delta) / 2 / self.a
            return str(round(base_num + delta_num, 3)) + " or " + str(round(base_num - delta_num, 3))
myCal = quadratic_with_one_unknown()
equation = input("input an equation")
print (myCal.exact_result(equation))