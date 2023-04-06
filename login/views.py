from django.shortcuts import render
import mysql.connector as sql #pip install mysql-conector-python

# Create your views here.
def loginaction(request):
    if request.method == "POST":
        # abrir conexion a la BD de mysql
        cn = sql.connect(host="localhost", user="root",passwd="root", database='bdatos')
        # crear cursor
        cursor = cn.cursor()
        #obtiene datos de la pagina html
        dic = request.POST 
        print(dic)
        
        for key, value in dic.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value
        # comando select
        com = "select * from usuario where email='{}' and password='{}'".format(em, pwd)
        cursor.execute(com)
        #convertir a tupla
        usuarios = tuple(cursor.fetchall())
        if usuarios == ():
            return render(request, 'error.html')
        else:
            return render(request, "welcome.html")

    return render(request, 'login_page.html')
