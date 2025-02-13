from config.app import *
import pandas as pd

from config.app import *
import pandas as pd

#Tarea: Generar la misma información con pandas
def GenerateReportVentas(app: App):
    conn = app.bd.getConection()

    # 1er paso: Cargar los datos desde SQLite a pandas
    df_ventas = pd.read_sql_query("SELECT * FROM VENTAS", conn)
    df_postal = pd.read_sql_query("SELECT * FROM POSTALCODE", conn)

    # 2️do paso: Unir las tablas usando merge en pandas
    df_merge = df_ventas.merge(df_postal, how="left", left_on="postal_code", right_on="code")

    # 3️er paso: Agrupar por país y producto, sumando la cantidad vendida
    df_report = df_merge.groupby(["pais", "product_id"], as_index=False)["quantity"].sum()

    # 4to pas: Ordenar de mayor a menor cantidad vendida
    df_report = df_report.sort_values(by="quantity", ascending=False)

    # 5️to paso: Guardar el reporte en un archivo CSV nombre personalizado
    path = "/workspaces/PythonDATUX/proyecto1/files/data-01.csv"
    df_report.to_csv(path, index=False)

    # 6to paso: Se envía el reporte por correo
    sendMail(app, path)

def sendMail(app: App, data):
    app.mail.send_email('from@example.com', 'Reporte_Kevin_Lescano_Banda', 'Reporte_Kevin_Lescano_Banda', data)
