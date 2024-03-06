import pandas as pd

pd.set_option('display.max_rows', None)
column = ["Emendis", "Emendis Rosé", "Llopart Brut Nature", "Torello Brut Nature", "Juvé&Camps Nature R.S.V Familia","Gramona Impreium Brut G.R", "Agusti Torrello", "Llopart Ingeral BN 2018", "Recadero Nature Gran Reserva", "Torello 22 RVA", "Gramona Imperia II Lustro", "Juve & Camps Milesime", "KRPTA", "Charles Laffite", "Louis Roederer Brut Premier", "Veuve Clicquot", "Don Pérignon", "Montecillo Rosado", "Chivite Navarra Fincas", "Chivite Fincas Magnun", "Duc de foix Chardonnay", "Mireia", "Ermita d'Espiells", "Gramona Gessami", "Waltraud", "Montecillo Termpranillo", "Verdejo Marqués de Cáceres", "José Pariente", "José Pariente Barrica", "La Capilla", "Belondrade i Lurton", "Albariño de la casa", "Terras Gauda", "Pazo das Bruxas", "Santiago Ruiz", "Capricho Godello Bierzo", "Mar de Frades", "El jardín de Lucía", "Envidia Cochina", "Entrechuelos Chardonnay", "Los 30 del Cuadrado", "Camins del Priorat", "Abadal 3.9 Bages", "Les Terrasses", "Dofí", "Ulldemolins", "Chateldon", "Mas Codina", "Jeronimus Penedès Gara", "Finca Resalgo", "Venta Las Vacas"," La Capilla", "Pago Capellanes Roble", "Lopez Cristóbal Crianza", "Dehesa de los Canónigos", "Matarromera Crianza", "Carmelo Rodero Crianza"," Viña Pedrosa Crianza", "Bosque de Matasnos", "Abadia Retuerta", "Tomas Postigo", "Mauro Reserva", "Hacienda Monasterio", "Pago de Carrovejas"," Malleoulos", "PSI Dominio de Pingus", "Pintia Toro", "Alion", "Flor de Pingus", "Valbuena Vega Sicilia Único", "Pingus", "Ivanto Crianza", "Montecillo Crianza", "Ivanto Reserva", "Viña Pomal Reserva", "Viña Real Crianza", "Muga Crianza", "Sierra Cantabria", "La Montesa Palacio", "Remelluri Reserva", "Marqués de Vargas", "Contino Reserva", "Viña Ardanza Reserva", "Ramirez de Ganuza Fincas", "Muga Reserva", "200 Monges Reserva", "Gaudium 2016 Reserva", "904", "Macan Clasico", "Ramirez de Ganuza Reserva", "Trasnocho Ramirez de Ganuza", "Macan 2015 Reserva", "Enate Crianza"  ]
titled_columns = {"Nombre": column,
                 "Precio de Compra": [1,2,3,4,13.64,6,7,8,9,10,11,12,13,14,44.49,38.85,17,18,19,20,21,22,6.50,24,16.28,26,27,28,29,30,31.90,32,10.95,9.84,11.82,36,13.25,38,39,40,41,19.04,43,44,45,46,47,48,49,50,12,52,53,54,15.70,15.66,57,16.90,25.76,23.20,61,62,25.80,27.18,65,66,50.10,82.21,69,70,71,72,73,74,75,76,13.91,8.80,79,80,81,82,22.94,84,85,31.74,87,88,89,91,91,92,93], "Precio de Venta": [16,16,22,25.90,25.50,27,99,27.50,33,36,34,39,89,37,62,68,260,99,19.90,36,21,16.90,18.90,19.50,25.90,25.90,16.50,19.50,24.50,26.90,53,16,25,25.50,25.50,26,26.50,27.90,29.50,18.50,24,28.50,35.90,49,142,99,19,18.90,28,24,26.50,26.90,28,28.90,31,29.50,34.90,34,36,37.90,42,44,46,48,49,49,82,105,189,340,1290,14.50,18,18.90,19,19.50,29,27.90,28,30.90,29,31,32,84,44.90,48,65,68,76,84,110,98,17.90]}

data = pd.DataFrame(titled_columns)
select_column = data["Precio de Venta"][1]
select_row = data.iloc[1]

Tipo_de_Vino = ["Cava","Cava","Cava","Cava","Cava","Cava","Cava","Cava","Cava","Cava","Cava","Cava","Cava","Champagne","Champagne","Champagne","Champagne","Rosados","Rosados","Rosados","Blanco(Penedés)","Blanco(Penedés)","Blanco(Penedés)","Blanco(Penedés)","Blanco(Penedés)","Blanco(Rioja)","Blanco(Rueda)","Blanco(Rueda)","Blanco(Rueda)","Blanco(Rueda)","Blanco(Rueda)","Blanco(Rias Baixas)","Blanco(Rias Baixas)","Blanco(Rias Baixas)","Blanco(Rias Baixas)","Blanco(Rias Baixas)","Blanco(Rias Baixas)","Blanco(Rias Baixas)","Blanco(Rias Baixas)","Blanco(Andalucia)","Blanco(Andalucia)","Tinto(Priorat)","Tinto(Priorat)","Tinto(Priorat)","Tinto(Priorat)","Tinto(Montsant)","Tinto(Penedès)","Tinto(Penedès)","Tinto(Penedès)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Ribera del Duero)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Rioja)","Tinto(Somontano)"]
data["Tipo de Vino"] = Tipo_de_Vino

Margen = []
for i in range(len(data)):
    beneficio = data ["Precio de Venta"][i]-(data["Precio de Compra"][i])
    Margen.append(beneficio)

data["Margen"] = Margen

Margen_perc = []
for i in range(len(data)):
    percentage = data ["Precio de Venta"][i]/(data["Precio de Compra"][i])*100
    Margen_perc.append(percentage)

data["Margen %"] = Margen_perc

Unidades_Stock = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,91,92,93]
data["Unidades en Stock"] = Unidades_Stock

Posibles_Ganancias = []
for i in range(len(data)):
    Ganancias = data ["Margen"][i]*(data["Unidades en Stock"][i])
    Posibles_Ganancias.append(Ganancias)

data["Posibles Ganancias"] = Posibles_Ganancias

# Set option to None to display all columns or set a specific number

print(data)

data.to_excel('vinos.xlsx', index=False)