import pandas as pd

pd.set_option('display.max_rows', None)
column = ["PUENTES PEINADO, MANUEL", "REQUENA FERNANDEZ, Ma ISABEL", "SANTANA, SEBASTIAN", "SAN GREGORIO GALAN, VANESA", "SOTO MARTINEZ, AGUSTIN","LEO GARCIA, BORJA", "JIMENEZ VALDERRAMA, JAIRO ENRI", "MORENO GAMEZ, MANUEL", "LUGO TOVAR, PAULA ANDREA", "PONIATOWSKA, EWA", "SANCHEZ RUIZ, JEAN CARLO", "JIMENEZ LOPEZ, LAURA NATHALIA", "PASCUALENA GARCERAN, MARCEL", "ZIGHIGHI LAALIGUI, ROUKAYA", "RIBERA VARGAS, DIEGO", "CARBON PLASENCIA, ELENA", "IGLESIAS CENZANO, OSCAR"]
titled_columns = {"Nombre": column,
                 "Jornada": ["Completa","Completa","Completa","Completa","Completa","Completa","Completa","Completa","Completa","Completa","Completa","Completa","Completa","Media","Completa","Completa","Completa"], "Sexo": ["Hombre", "Mujer", "Hombre", "Mujer", "Hombre", "Hombre", "Hombre", "Hombre", "Mujer", "Mujer", "Hombre", "Mujer", "Hombre", "Mujer", "Hombre", "Mujer", "Hombre"]}

data = pd.DataFrame(titled_columns)
select_column = data["Sexo"][1]
select_row = data.iloc[1]

Edad = [1808.14, 2724.60, 1775.37, 1774.25, 1776.05, 1772.74, 1775.65, 1949.50, 1776.65, 1776.65, 1776.65, 1776.65, 885.03, 1773.89, 1773.89, 1776.63, 783.73]
data["Edad"] = Edad

Salario_Bruto = [1808.14, 2724.60, 1775.37, 1774.25, 1776.05, 1772.74, 1775.65, 1949.50, 1776.65, 1776.65, 1776.65, 1776.65, 885.03, 1773.89, 1773.89, 1776.63, 783.73]
data["Salario Bruto"] = Salario_Bruto

Salario_Neto = [1456.33, 1696.57, 1435.79, 1470.50, 1314.17, 1517.45, 1396.16, 1608.20, 1396.16, 1396.16, 1396.16, 1396.16, 800.39, 1481.72, 1481.72, 1395.62, 624.53]
data["Salario Neto"] = Salario_Neto
print(data)

data.to_csv('Trabajadores.csv', index=False)