import os

template = """
from z3 import *

s = Solver()

Activate = Bool('Activate')
S_ChannelA = Bool('S_ChannelA')
S_ChannelB = Bool('S_ChannelB')
Timer = Int('Timer')
DiscrepancyTime = Int('DiscrepancyTime')

s.add(%s, %s)

print(s.check(), end='')

"""

def Not_format(expr):
    if expr[0] != '!':
        print('error: Not_format error')
    return 'Not(%s)' % expr[1:]

def change_format(expr):
    if -1 != expr.find('&'):
        list_condt = expr.split('&')
        str_and = 'And('
        for condt in list_condt:
            if condt[0] == '!':
                condt = Not_format(condt)
            str_and += (condt + ',')
        str_and = str_and[0:-1] + ')'
        return str_and

    if -1 != expr.find('XOR'):
        list_condt = expr.split('XOR')
        str_or = 'Or('
        for condt in list_condt:
            if condt[0] == '!':
                condt = Not_format(condt)
            str_or += (condt + ',')
        str_or = str_or[0:-1] + ')'
        return str_or
    
    if expr[0] == '!':
        expr = Not_format(expr)
        return expr
    
    return expr

            


def get_two_exp_z3_ret(expr_one, expr_two):
    expr_one = change_format(expr_one)
    expr_two = change_format(expr_two)

    z3code = template % (expr_one, expr_two)
    TwoExpr_name = 'TwoExpr.py'
    with open(TwoExpr_name, 'w', encoding='utf-8') as f:
        f.write(z3code)

    # python TwoExpr.py
    cmd = r'python %s' % TwoExpr_name
    output = os.popen(cmd)
    if output.read()[0:3] == 'sat':
        return True
    else:
        return False

if __name__ == '__main__':
    print(get_two_exp_z3_ret("Activate", "Timer > 1"))
    print(get_two_exp_z3_ret("Timer < 1", "Timer > 1"))
