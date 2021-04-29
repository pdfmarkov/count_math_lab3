import math
import numpy as np
from termcolor import cprint
from tabulate import tabulate
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)


class Input:
    a = 0
    b = 0
    accuracy = 0
    type_of_equation = 0
    type_of_method = 0

    def __init__(self):
        self.choose_equation()
        self.choose_method()
        self.choose_borders()
        self.choose_accuracy()
        self.do_some_math()

    def choose_borders(self):
        while 1:
            try:
                cprint('\n♦ Please, choose borders of your integral (example: -10 10) ♦', 'yellow')
                cprint("\nBorders of integral: ", 'yellow')
                borders = list(input().strip().split(" "))
                if len(borders) == 2 and (float(borders[0].strip()) < float(borders[1].strip())):
                    self.a = float(borders[0].strip())
                    self.b = float(borders[1].strip())
                    break
                else:
                    cprint('◘ I\'ve got some troubles with your input (a must be smaller than b), please, try again! ◘',
                           'red')
                    continue
            except TypeError and ValueError:
                cprint('◘ I\'ve got some troubles with your input, please, try again! ◘', 'red')
                continue

    def choose_equation(self):
        while 1:
            try:
                cprint("\n♦ Please, choose a equation: ♦\n"
                       "\t1. 2x^3 - 9x^2 - 7x + 11\n"
                       "\t2. 3/x + x\n"
                       "\t3. e^3x + 3\n"
                       "\t4. x^2 - 2x\n", 'yellow')
                cprint('Your equation: ', 'yellow')
                answer = int(input().strip())
                if answer == 1:
                    self.type_of_equation = 1
                    break
                elif answer == 2:
                    self.type_of_equation = 2
                    break
                elif answer == 3:
                    self.type_of_equation = 3
                    break
                elif answer == 4:
                    self.type_of_equation = 4
                    break
                else:
                    cprint('◘ I\'ve got some troubles with your input (choose only from 1 to 4), please, try again! ◘',
                           'red')
                    continue
            except TypeError and ValueError:
                cprint('◘ I\'ve got some troubles with your input, please, try again! ◘', 'red')
                continue

    def choose_method(self):
        while 1:
            try:
                cprint("\n♦ Please, choose a method: ♦\n"
                       "\t1. Trapezoid\n"
                       "\t2. Simpsons\n"
                       "\t3. Rectangles\n", 'yellow')
                cprint('Your method: ', 'yellow')
                method = int(input().strip())
                if method == 1:
                    self.type_of_method = 1
                    break
                elif method == 2:
                    self.type_of_method = 2
                    break
                elif method == 3:
                    self.type_of_method = 3
                    break
                else:
                    cprint('◘ I\'ve got some troubles with your input (choose only from 1 to 3), please, try again! ◘',
                           'red')
                    continue
            except TypeError and ValueError:
                cprint('◘ I\'ve got some troubles with your input, please, try again! ◘', 'red')
                continue

    def choose_accuracy(self):
        while 1:
            try:
                cprint('\n♦ Please, choose a accuracy ♦', 'yellow')
                cprint("\nAccuracy: ", 'yellow')
                accuracy = float(input().strip())
                if 0 < accuracy:
                    self.accuracy = accuracy
                    break
                else:
                    cprint(
                        '◘ I\'ve got some troubles with your accuracy (it\'s must be positive), please, try again! ◘',
                        'red')
                    continue
            except TypeError and ValueError:
                cprint('◘ I\'ve got some troubles with your accuracy, please, try again! ◘', 'red')
                continue

    def do_some_math(self):
        Calculator(self.a, self.b, self.accuracy, self.type_of_equation, self.type_of_method)


class Calculator:
    a = 0
    b = 0
    n = 4
    h = 0
    start = 0
    steps = 0
    result = 0
    result0 = 0
    result1 = 0
    result2 = 0
    accuracy = 0
    inaccuracy = 0
    inaccuracy0 = 0
    inaccuracy1 = 0
    inaccuracy2 = 0
    previous_count = 0
    type_of_equation = 0
    type_of_method = 0
    type_of_table = 0
    table = []
    xy = []
    average_xy = []
    average_x = 0
    sum = 0

    def __init__(self, a, b, accuracy, type_of_equation, type_of_method):
        self.a = a
        self.b = b
        self.start = a
        self.accuracy = accuracy
        self.type_of_equation = type_of_equation
        self.type_of_method = type_of_method
        self.type_of_table = type_of_method
        self.count()

    def count(self):
        cprint('\n○●○●○● STARTING CALCULATING... ●○●○●○\n', 'cyan')
        if self.type_of_method == 1:
            cprint('●○●○●○ CALCULATING TRAPEZOID METHOD ○●○●○●', 'cyan')
            self.trapezoid()
        elif self.type_of_method == 2:
            cprint('●○●○●○ CALCULATING SIMPSON METHOD ○●○●○●', 'cyan')
            self.simpson()
        elif self.type_of_method == 3:
            cprint('●○●○●○ CALCULATING RECTANGLES METHOD ○●○●○●', 'cyan')
            self.rectangles()

    def F(self, x):
        try:
            if self.type_of_equation == 1:
                return x * (x ** 3 - 6 * x * x - 7 * x + 22) / 2
            elif self.type_of_equation == 2:
                return x * x / 2 + 3 * math.log(abs(x))
            elif self.type_of_equation == 3:
                return math.e ** (3*x) / 3 + 3 * x
            elif self.type_of_equation == 4:
                return (x - 3) * x ** 2 / 3
        except ZeroDivisionError:
            if self.type_of_equation == 2 and x == 0:
                cprint('\n◘ There is some math problems with equation, method diverges (zero exception) ◘', 'cyan')
            else:
                return self.F(x + 1e-8)
        except OverflowError:
            cprint('◘ There is some math problems with equation ◘', 'red')

    def f(self, x):
        try:
            if self.type_of_equation == 1:
                return 2 * math.pow(x, 3) - 9 * x * x - 7 * x + 11
            elif self.type_of_equation == 2:
                return 3 / x + x
            elif self.type_of_equation == 3:
                return math.pow(math.e, 3 * x) + 3
            elif self.type_of_equation == 4:
                return x * x - 2 * x
        except ZeroDivisionError:
            if self.type_of_equation == 2 and x == 0:
                cprint('\n◘ There is some math problems with equation, method diverges (zero exception) ◘', 'cyan')
            else:
                return self.f(x + 1e-8)
        except OverflowError:
            cprint('◘ There is some math problems with equation ◘', 'red')

    def f_(self, x):
        try:
            if self.type_of_equation == 1:
                return 6 * x * x - 9 * 2 * x - 7
            elif self.type_of_equation == 2:
                return 1 - 3 / (x * x)
            elif self.type_of_equation == 3:
                return 3 * math.pow(math.e, 3 * x)
            elif self.type_of_equation == 4:
                return 2 * x - 1
        except ZeroDivisionError:
            if self.type_of_equation == 2 and x == 0:
                cprint('◘ There is some math problems with equation, method diverges (zero exception) ◘', 'cyan')
                raise ValueError
            else:
                return self.f_(x + 1e-8)
        except OverflowError:
            cprint('◘ There is some math problems with equation ◘', 'red')

    def f__(self, x):
        try:
            if self.type_of_equation == 1:
                return 6 * 2 * x - 9 * 2
            elif self.type_of_equation == 2:
                return 6 / (x * x * x)
            elif self.type_of_equation == 3:
                return 9 * math.pow(math.e, 3 * x)
            elif self.type_of_equation == 4:
                return 2
        except ZeroDivisionError:
            if self.type_of_equation == 2 and x == 0:
                cprint('◘ There is some math problems with equation, method diverges (zero exception) ◘', 'cyan')
                raise ValueError
            else:
                return self.f__(x + 1e-8)
        except OverflowError:
            cprint('◘ There is some math problems with equation ◘', 'red')

    def f____(self, x):
        try:
            if self.type_of_equation == 1:
                return 0
            elif self.type_of_equation == 2:
                return 72 / (x * x * x * x * x)
            elif self.type_of_equation == 3:
                return 81 * math.pow(math.e, 3 * x)
            elif self.type_of_equation == 4:
                return 0
        except ZeroDivisionError:
            if self.type_of_equation == 2 and x == 0:
                cprint('◘ There is some math problems with equation, method diverges (zero exception) ◘', 'cyan')
                raise ValueError
            else:
                return self.f____(x + 1e-8)
        except OverflowError:
            cprint('◘ There is some math problems with equation ◘', 'red')

    def max_value(self):
        x = np.linspace(self.start, self.b, 100000)
        maximum = [abs(self.f__(i)) for i in x]
        return max(maximum)

    def max_value_for_simpson(self):
        x = np.linspace(self.start, self.b, 100000)
        maximum = [abs(self.f____(i)) for i in x]
        return max(maximum)

    def trapezoid(self):
        try:
            self.table = []
            self.xy = []
            self.result = 0
            self.inaccuracy = 0
            self.steps = 0
            self.n = self.choose_n_trapezoid()
            self.sum = 0
            self.h = (self.b - self.a) / self.n
            while self.steps != self.n + 1:
                self.xy.append([self.a, self.f(self.a)])
                self.table.append([self.steps, self.xy[self.steps][0], self.xy[self.steps][1]])
                if 0 < self.steps < self.n:
                    self.sum += self.xy[self.steps][1]
                self.a += self.h
                self.steps += 1
                if self.steps > 300000:
                    self.result = self.h * ((self.xy[0][1] + self.xy[-1][1]) / 2 + self.sum)
                    self.inaccuracy = abs(self.max_value() * math.pow(self.b - self.a, 3) / (12 * math.pow(self.n, 2)))
                    cprint('\nMethod Trapezoid:', 'red')
                    self.print_result()
                    cprint(f'There are too many steps, the value of integral is calculated from {self.start} to {self.xy[-1][0]}!', 'red')
                    raise ValueError
            self.result = self.h * ((self.xy[0][1] + self.xy[-1][1]) / 2 + self.sum)
            self.inaccuracy = abs(self.max_value() * math.pow(self.b - self.a, 3) / (12 * math.pow(self.n, 2)))
            # self.print_table()
            self.print_result()
        except TypeError or ValueError or ZeroDivisionError:
            cprint('◘ There is some troubles while calculating ◘', 'cyan')

    def choose_n_trapezoid(self):
        try:
            n = abs(math.pow(self.max_value() * math.pow(self.b - self.a, 3) / 12 / self.accuracy, 0.5)) // 1
            if n % 2 == 1:
                n += 1
            else:
                n += 2
            if n <= 4:
                return 4
            else:
                return int(n)
        except ValueError:
            return 4

    def simpson(self):
        try:
            f_new = 0
            f_old = 0
            self.result = 0
            self.inaccuracy = 0
            self.steps = 0
            self.xy = []
            self.table = []
            self.n = self.choose_n_simpson()
            self.h = (self.b - self.a) / self.n
            while self.steps != self.n + 1:
                self.xy.append([self.a, self.f(self.a)])
                self.table.append([self.steps, self.xy[self.steps][0], self.xy[self.steps][1]])
                if 0 < self.steps < self.n and self.steps % 2 == 1:
                    f_old += self.xy[self.steps][1]
                elif 0 < self.steps < self.n - 1 and self.steps % 2 == 0:
                    f_new += self.xy[self.steps][1]
                self.a += self.h
                self.steps += 1
                if self.steps > 300000:
                    self.result = self.h / 3 * (self.xy[0][1] + self.xy[-1][1] + 4 * f_old + 2 * f_new)
                    self.inaccuracy = abs(self.max_value_for_simpson() * math.pow(self.b - self.a, 5) / (180 * math.pow(self.n, 4)))
                    cprint('\nMethod Simpson:', 'red')
                    self.print_result()
                    cprint(f'There are too many steps, the value of integral is calculated from {self.start} to {self.xy[-1][0]}!', 'red')
                    raise ValueError
            self.result = self.h / 3 * (self.xy[0][1] + self.xy[-1][1] + 4 * f_old + 2 * f_new)
            self.inaccuracy = abs(self.max_value_for_simpson() * math.pow(self.b - self.start, 5) / (180 * math.pow(self.n, 4)))
            self.print_table()
            self.print_result()
        except TypeError or ValueError or ZeroDivisionError:
            cprint('◘ There is some troubles while calculating ◘', 'cyan')

    def choose_n_simpson(self):
        try:
            n = abs(math.pow(self.max_value_for_simpson() * math.pow(self.b - self.a, 5) / 180 / self.accuracy, 0.25)) // 1
            if n % 2 == 1:
                n += 1
            else:
                n += 2
            if n <= 4:
                return 4
            else:
                return int(n)
        except ValueError:
            return 4

    def rectangles(self):
        try:
            f_left = 0
            f_mid = 0
            f_right = 0
            self.steps = 0
            self.xy = []
            self.table = []
            self.previous_count = self.a
            self.n = self.choose_n_rectangles()
            self.h = (self.b - self.a) / self.n
            while self.steps != self.n + 1:
                self.xy.append([self.a, self.f(self.a)])
                if self.steps > 0:
                    self.average_x = (self.previous_count + self.a) / 2
                    self.average_xy.append([self.average_x, self.f(self.average_x)])
                    self.table.append([self.steps, self.xy[self.steps][0], self.xy[self.steps][1], self.average_xy[self.steps - 1][0], self.average_xy[self.steps - 1][1]])
                else:
                    self.table.append([self.steps, self.xy[self.steps][0], self.xy[self.steps][1], 0, 0])
                self.previous_count = self.a
                if 0 <= self.steps < self.n:
                    f_left += self.xy[self.steps][1]
                if 0 < self.steps <= self.n:
                    f_right += self.xy[self.steps][1]
                    f_mid += self.average_xy[self.steps - 1][1]
                self.a += self.h
                self.steps += 1
                if self.steps > 300000:
                    self.result0 = self.h * f_left
                    self.result1 = self.h * f_mid
                    self.result2 = self.h * f_right
                    self.inaccuracy0 = abs(self.max_value() * math.pow(self.b - self.a, 2) / (2 * self.n))
                    self.inaccuracy1 = abs(self.max_value() * math.pow(self.b - self.a, 3) / (24 * math.pow(self.n, 2)))
                    self.inaccuracy2 = abs(self.max_value() * math.pow(self.b - self.a, 2) / (2 * self.n))
                    cprint('\nMethod Rectangles:', 'red')
                    self.print_result()
                    cprint(f'There are too many steps, the value of integral is calculated from {self.start} to {self.xy[-1][0]}!', 'red')
                    raise ValueError
            self.result0 = self.h * f_left
            self.result1 = self.h * f_mid
            self.result2 = self.h * f_right
            self.inaccuracy0 = abs(self.max_value() * math.pow(self.b - self.a, 2) / (2 * self.n))
            self.inaccuracy1 = abs(self.max_value() * math.pow(self.b - self.a, 3) / (24 * math.pow(self.n, 2)))
            self.inaccuracy2 = abs(self.max_value() * math.pow(self.b - self.a, 2) / (2 * self.n))
            # self.print_table()
            self.print_result()
        except TypeError or ValueError or ZeroDivisionError:
            cprint('◘ There is some troubles while calculating ◘', 'cyan')

    def choose_n_rectangles(self):
        try:
            n = abs(math.pow(self.max_value() * math.pow(self.b - self.a, 3) / 24 / self.accuracy, 0.5)) // 1
            if n % 2 == 1:
                n += 1
            else:
                n += 2
            if n <= 4:
                return 4
            else:
                return int(n)
        except ValueError:
            return 4

    def print_table(self):
        if self.type_of_table == 1:
            cprint('\nMethod Trapezoid:', 'cyan')
            cprint(tabulate(self.table, headers=["№", "x", "f(x)"],
                            tablefmt="fancy_grid", floatfmt="2.5f"), 'cyan')
        elif self.type_of_table == 2:
            cprint('\nMethod Simpson:', 'cyan')
            cprint(
                tabulate(self.table, headers=["№", "x", "f(x)"],
                         tablefmt="fancy_grid", floatfmt="2.5f"), 'cyan')
        elif self.type_of_table == 3:
            cprint('\nMethod Rectangles:', 'cyan')
            cprint(
                tabulate(self.table, headers=["№", "x", "f(x)", "x(i-0.5)", "f(x(i-0.5))"],
                         tablefmt="fancy_grid", floatfmt="2.5f"), 'cyan')

    def print_result(self):
        template = '{:.15f}'
        if self.type_of_table == 1:
            cprint('\nResults of Trapezoid method:', 'cyan')
            cprint(f'I:  {template.format(self.result)}', 'cyan')
            cprint(f'R(n): {self.inaccuracy}', 'cyan')
            cprint(f'Accurate I: {self.F(self.xy[-1][0]) - self.F(self.start)}', 'cyan')
            cprint(f'n: {self.n}', 'cyan')
        elif self.type_of_table == 2:
            cprint('\nResults of Simpson method:', 'cyan')
            cprint(f'I:  {template.format(self.result)}', 'cyan')
            cprint(f'R(n): {self.inaccuracy}', 'cyan')
            cprint(f'Accurate I: {self.F(self.xy[-1][0]) - self.F(self.start)}', 'cyan')
            cprint(f'n: {self.n}', 'cyan')
        elif self.type_of_table == 3:
            cprint('\nResults of Rectangles method:', 'cyan')
            cprint(f'I (left):  {template.format(self.result0)}', 'cyan')
            cprint(f'I (mid):  {template.format(self.result1)}', 'cyan')
            cprint(f'I (right):  {template.format(self.result2)}', 'cyan')
            cprint(f'R(n) (left): {self.inaccuracy0}', 'cyan')
            cprint(f'R(n) (mid): {self.inaccuracy1}', 'cyan')
            cprint(f'R(n) (right): {self.inaccuracy2}', 'cyan')
            cprint(f'Accurate I: {self.F(self.xy[-1][0]) - self.F(self.start)}', 'cyan')
            cprint(f'n: {self.n}', 'cyan')


if __name__ == '__main__':
    cprint('♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n'
           '♦ Welcome to the Integral Calculator ♦\n'
           '♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦', 'green')
    while 1:
        try:
            new_input = Input()
            del new_input
            continue
        except TypeError and ValueError and ZeroDivisionError:
            cprint('There is some troubles while calculating', 'cyan')
