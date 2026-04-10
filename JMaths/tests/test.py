if __name__ == '__main__':
    from JMaths import *

    x = variable('x')

    f_x = function(x)
    f_x.set_equations("exp(x)")
    f_x.delta = .3
    f_x.calculate(1)
    # f_x.calculate([-3, 3])

    print(f"Domain: \n{f_x.domain}")
    print(f"Range: \n{f_x.range}")

    excelExport(f_x.domain, f_x.range, "Test2")



