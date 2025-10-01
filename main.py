import JMaths as jm
jv = jm.variable
jf = jm.function

# g_x = eval('x**2', {'x': 2})
# print(g_x)

x = jv.variable('x')

f_x = jf.function(x)
f_x.set_equations("x**2")
f_x.delta = 1
print(f_x.calculate([-1, 1]))

print(f"Domain: {f_x.domain}")
print(f"Range: {f_x.range}")



jm.graph.root.mainloop()