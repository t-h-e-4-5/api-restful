#  Importations
import pymysql
from app import app
from conf import mysql
from flask import request, render_template, jsonify

@app.route("/user/add", methods=['POST'])
def add_user():
    try:
        json = request.json
        #id = json['id']
        nom = json['nom']
        prenom = json['prenom']
        tel = json['tel']
        password = json['password']
        email = json['email']
        login = json['login']
    
        #if nom and prenom and request.method =='POST':
        if nom and prenom and tel and password and email and login and request.method =='POST':
            con = mysql.connect()
            cursor = con.cursor(pymysql.cursors.DictCursor)
            query = 'insert into user(nom,prenom,login,password,tel,email)VALUES(%s,%s,%s,%s,%s,%s)'
            bind_data = (nom,prenom,login,password,tel,email)
            #bindData = (nom,prenom)
            cursor.execute(query,bind_data)
            con.commit()
            response = jsonify('Utilisateur ajouté avec succès')
            response.status_code = 200
            return response
        else:
            message = {'status':404, 'message':'Entrée(s) invalide'}
            response = jsonify(message)
            response.status_code = 404
            return response
    except Exception as e:
        print(e) 
        message = {'status':404, 'message':'error please '}
        return message

    finally:
        cursor.close()
        con.close()


@app.route("/login")
def login():
   return render_template("login.html",name= __name__)

@app.route("/user/get/<int:id>")
def get_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = 'select * from user where id = %s'
        #bind_data = (nom,prenom,login,password,tel,email)
        #bindData = (nom,prenom)
        cursor.execute(query,id)
        user_row = cursor.fetchone()
        print(user_row)
        response = jsonify({"user": user_row,"status_code" : 200})
        
        #response.status_code = 200
        return response
    except Exception as e:
        print(e) 
        message = {'status':404, 'message':'error please '}
        return message

    finally:
        cursor.close()
        conn.close()

@app.route("/user/getbyid")
def get_user_by_id():
    try:
        json = request.json
        id = json["id"]
        print(id)
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = 'select * from user where id = %s'
        #bind_data = (nom,prenom,login,password,tel,email)
        #bindData = (nom,prenom)
        cursor.execute(query,id)
        user_row = cursor.fetchone()
        print(user_row)
        response = jsonify({"user": user_row,"status_code" : 200})
        
        #response.status_code = 200
        return response
    except Exception as e:
        print(e) 
        message = {'status':404, 'message':'error please '}
        return message

    finally:
        cursor.close()
        conn.close()



@app.route("/user/get/all")
def get_all_user():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = 'select * from user'
        #bind_data = (nom,prenom,login,password,tel,email)
        #bindData = (nom,prenom)
        cursor.execute(query)
        user_row = cursor.fetchall()
        #print(user_row)
        response = jsonify({"users": user_row,"status_code" : 200})
        
        #response.status_code = 200
        return response
    except Exception as e:
        print(e) 
        message = {'status':404, 'message':'error please '}
        return message

    finally:
        cursor.close()
        conn.close()



@app.route("/user/update", methods=['PUT'])
def update_user():
    try:
        json = request.json
        id = json['id']
        nom = json['nom']
        prenom = json['prenom']
        tel = json['tel']
        password = json['password']
        email = json['email']
        login = json['login']
    
        #if nom and prenom and request.method =='POST':
        if id and nom and prenom and tel and password and email and login and request.method =='PUT':
            con = mysql.connect()
            cursor = con.cursor(pymysql.cursors.DictCursor)
            query = 'update user set nom = %s,prenom = %s,login = %s,password = %s,tel = %s,email = %s where id = %s'
            bind_data = (nom,prenom,login,password,tel,email,id)
            #bindData = (nom,prenom)
            cursor.execute(query,bind_data)
            con.commit()
            response = jsonify('Utilisateur a été mis à jour avec succès')
            response.status_code = 200
            return response
        else:
            message = {'status':404, 'message':'Entrée(s) invalide'}
            response = jsonify(message)
            response.status_code = 404
            return response
    except Exception as e:
        print(e) 
        message = {'status':404, 'message':'error please '}
        return message

    finally:
        cursor.close()
        con.close()

@app.route("/user/changepwd", methods=['PUT'])
def change_password():
    try:
        json = request.json
        #id = json['id']
        #nom = json['nom']
        #prenom = json['prenom']
        #tel = json['tel']
        login = json['login']
        password = json['password']
        nwpassword = json['password']
        #email = json['email']
    
        #if nom and prenom and request.method =='POST':
        if  login and password  and nwpassword  and request.method =='PUT':
            con = mysql.connect()
            cursor = con.cursor(pymysql.cursors.DictCursor)
            #query = 'update user set password = %s  where id = %s and password = %s'
            #query = 'update user set password = %s  where id = %s and password = %s'
            #query = 'UPDATE user SET password = %s WHERE login = %s and  EXISTS  (SELECT * from user WHERE login = %s AND password = %s LIMIT 1)'
            query = 'select * from user where login = %s and password = %s'
            bind_data = (login,password)
            #bindData = (nom,prenom)
            cursor.execute(query,bind_data)
            bien = cursor.fetchone()
            if bien is None:
                return jsonify({'error': 'Invalid login or password'})
            else:
                query_r = 'update user set password = %s where login = %s'
                bind_data_r = (nwpassword,login)
                cursor.execute(query_r,bind_data_r)
                con.commit()
            response = jsonify('Utilisateur a été mis à jour avec succès')
            response.status_code = 200
            return response
        else:
            message = {'status':404, 'message':'Entrée(s) invalide'}
            response = jsonify(message)
            response.status_code = 404
            return response
    except Exception as e:
        print(e) 
        message = {'status':404, 'message':'error please '}
        return message

    finally:
        cursor.close()
        con.close()


@app.route("/user/delete/<int:id>", methods=['DELETE'])
def delete_user(id):
    try:
        
        #if nom and prenom and request.method =='POST':
        if id and request.method =='DELETE':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = 'delete from user where id = %s'
            #bind_data = (nom,prenom,login,password,tel,email)
            #bindData = (nom,prenom)
            cursor.execute(query,id)
            conn.commit()
            response = jsonify('Utilisateur ajouté avec succès')
            response.status_code = 200
            return response
        else:
            message = {'status':404, 'message':'Entrée(s) invalide'}
            response = jsonify(message)
            response.status_code = 404
            return response
    except Exception as e:
        print(e) 
        message = {'status':404, 'message':'error please '}
        return message

    finally:
        cursor.close()
        conn.close()


if(__name__ == '__main__'):
    app.run()


