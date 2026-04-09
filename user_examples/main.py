from JMaths import *

x = jmath.variable('x')

f_x = jmath.function(x)

f_x.set_equations("sin(x)")
f_x.delta = .3
f_x.calculate([-7, 7])

print(f"Domain: \n{f_x.domain}")
print(f"Range: \n{f_x.range}")

export.excelExport(f_x.domain, f_x.range, "Test2")
