import pandas as pd

# For Windows Kids
def excelExport(domain, range, name):
    data = {
        'Domain': domain,
        'Range': range
    }

    df = pd.DataFrame(data)
    df.to_excel(f"{name}.xlsx", sheet_name='PlotData', index=False)
    print(f"Successfully exported data to {name}")

# For Linux Chads
def libreExport():
    pass

