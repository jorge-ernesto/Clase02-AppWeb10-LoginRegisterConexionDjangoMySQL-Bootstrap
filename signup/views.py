from django.shortcuts import render
import mysql.connector as sql  #pip instalar mysql-conector-python
#import sqlite3

# Create your views here.
# cn = sqlite3.connect("db.sqlite3)

def signaction(request):
    if request.method == "POST":
        cn = sql.connect(host="localhost", user="root",passwd="root",database='bdatos')
        x = cn.cursor()
        
        dic = request.POST
        
        for key, value in dic.items():
            if key == "nombre":
                nom = value
            if key == "apellidos":
                ape = value
            if key == "sexo":
                sx = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        com = "insert into usuario values('{}','{}','{}','{}','{}')".format(nom, ape, sx, em, pwd)
        x.execute(com)
        cn.commit()

    return render(request, 'signup_page.html')

