# Generiere Zufällige Rechenaufgabe in Postfix / Reverse polish Notation. Verwendet +,-,*,/

from random import randrange
from random import uniform

from sympy import primefactors


# Get to the number using n operations (in reverse polish/ postfix notation)
# Converter: https://rosettacode.org/wiki/Parsing/RPN_to_infix_conversion#Python
def n_ops(solution, n):
    if n == 0:
        return str(solution)
    factors = primefactors(solution)
    n1 = randrange(0, n)
    n2 = n - n1 - 1
    if len(factors) > 1 and uniform(0, 1) < 0.25:
        i = randrange(len(factors))
        num1 = factors[i]
        num2 = int(solution / num1)
        return n_ops(num1, n1) + " " + n_ops(num2, n2) + " * "
    elif solution > 20 and uniform(0, 1) < 0.33:
        num1 = randrange(5, solution - 4)
        num2 = solution - num1
        return n_ops(num1, n1) + " " + n_ops(num2, n2) + " + "
    elif uniform(0, 1) < 0.5:
        num1 = randrange(15, 150)
        return n_ops(num1 + solution, n1) + " " + n_ops(num1, n2) + " - "
    else:
        num2 = randrange(15, 150)
        return n_ops(solution * num2, n1) + " " + n_ops(num2, n2) + " / "


prec_dict = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2}
assoc_dict = {'^': 1, '*': 0, '/': 0, '+': 0, '-': 0}


class Node:
    def __init__(self, x, op, y=None):
        self.precedence = prec_dict[op]
        self.assocright = assoc_dict[op]
        self.op = op
        self.x, self.y = x, y

    def __str__(self):
        """
        Building an infix string that evaluates correctly is easy.
        Building an infix string that looks pretty and evaluates
        correctly requires more effort.
        """
        # easy case, Node is unary
        if self.y == None:
            return '%s(%s)' % (self.op, str(self.x))

        # determine left side string
        str_y = str(self.y)
        if self.y < self or (self.y == self and self.assocright) or (str_y[0] == '-' and self.assocright):
            str_y = '(%s)' % str_y
        # determine right side string and operator
        str_x = str(self.x)
        str_op = self.op
        if self.op == '+' and not isinstance(self.x, Node) and str_x[0] == '-':
            str_x = str_x[1:]
            str_op = '-'
        elif self.op == '-' and not isinstance(self.x, Node) and str_x[0] == '-':
            str_x = str_x[1:]
            str_op = '+'
        elif self.x < self or (self.x == self and not self.assocright and getattr(self.x, 'op', 1) != getattr(self, 'op', 2)):

            str_x = '(%s)' % str_x
        return ' '.join([str_y, str_op, str_x])

    def __repr__(self):
        return 'Node(%s,%s,%s)' % (repr(self.x), repr(self.op), repr(self.y))

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.precedence < other.precedence
        return self.precedence < prec_dict.get(other, 9)

    def __gt__(self, other):
        if isinstance(other, Node):
            return self.precedence > other.precedence
        return self.precedence > prec_dict.get(other, 9)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.precedence == other.precedence
        return self.precedence > prec_dict.get(other, 9)


def rpn_to_infix(s):

    stack = []
    for token in s.replace('^', '^').split():
        if token in prec_dict:
            stack.append(Node(stack.pop(), token, stack.pop()))
        else:
            stack.append(token)

    return str(stack[0])


def rand_ops(solution, i):
    return rpn_to_infix(n_ops(solution, (i+5)*2)), i < 3
