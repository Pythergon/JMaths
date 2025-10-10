import JMaths as jm
jv = jm.variable
jf = jm.function

# g_x = eval('x**2', {'x': 2})
# print(g_x)

x = jv.variable('x')

f_x = jf.function(x)
f_x.set_equations("x**2")
f_x.delta = .2
print(f_x.calculate([-5, 5]))

print(f"Domain: \n{f_x.domain}")
print(f"Range: \n{f_x.range}")


import pandas as pd

# Your Python list(s)

# 1. Convert the list(s) into a dictionary structure
# This creates a structure where keys are column headers for the Excel file.
data = {
    'Domain': f_x.domain,
    'Range': f_x.range
}

# 2. Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# 3. Export the DataFrame to an Excel file
file_name = 'data_for_plot.xlsx'
df.to_excel(file_name, sheet_name='PlotData', index=False)

print(f"Successfully exported data to {file_name}")