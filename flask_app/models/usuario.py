#TODAS LAS CLASES IMPORTAN MYSQLCONNECTION
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
#exprecion regular r'^[a-zA-Z0-9.+_-]+@[a-zA-z0-9._-]+.[a-zA-Z]+$'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-z0-9._-]+.[a-zA-Z]+$')
class Usuario:

    #metodo constructor
    def __init__(self, data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data.get('email')
        self.password = data.get('password')     
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    #para guardar 1 registro
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s,%(password)s, NOW(), NOW())"

        return connectToMySQL('cinepedia').query_db(query, data)

    #metodo para ver todos los registros
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios"
        usuarios_en_db = connectToMySQL('cinepedia').query_db(query)
        #lista vacia de usuarios se llena con clase usuarios
        usuarios = []
        #por cada usuario que encuentre en usuarios_en_db
        for usuario in usuarios_en_db:
            #voy a crear una instancia de la clase Usuario al final de la lista usuarios

            usuarios.append(cls(usuario))

        return usuarios


    #metodo para ver 1 registro
    @classmethod
    def get_one(cls,datos):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        usuario_en_db = connectToMySQL('cinepedia').query_db(query,datos)

        return cls(usuario_en_db[0])

    #metodo para editar registro
    @classmethod
    def update(cls, datos):
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s, password=%(password)s WHERE id = %(id)s;"

        return connectToMySQL('cinepedia').query_db(query, datos)
    

    #metodo para eliminar registro
    @classmethod
    def delete(cls, datos):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL('cinepedia').query_db(query, datos)

    @classmethod
    def get_by_email(cls, datos):
        query = "SELECT * FROM usuarios WHERE email = %(email)s"
        usuario_en_db = connectToMySQL('CinePedia').query_db(query, datos)
        return cls(usuario_en_db[0])




    #creamos un metodo estatico para validar los formularios
    @staticmethod

    def validar_usuario(usuario):
        es_valido = True
        #por cada validacion se crea un if 
        #Revisa si el campo coincide con el 
        if not EMAIL_REGEX.match(usuario['email']):
        
            flash("E-mail invalido")

            es_valido = False

        if len (usuario['nombre'])<=2:
            flash("Nombre de usuario necesita al menos 2 carcteress", "usuario")
            es_valido = False
        if len (usuario['apellido'])<=2:
            flash("Apellido de usuario necesita al menos 2 carcteress", "usuario")
            es_valido = False
        #falta validacion de contraseña = confirmacion contraseña 
        if not usuario ['password'] == usuario['password_conf']:
            flash('la contraseña no coinside con la informacion','password')
            es_valido = False


        # if len(resultados) == 1:
        #    #Si existe el usuario
        #    usuario = cls(resultados[0])
        #    return usuario #Regreso la instancia del usuario con ese correo
        # else:
        #    return False
        if not Usuario.get_by_email({'email':usuario['email']}):
            flash('el correo no se encuentra disponible')
            es_valido = False
        return es_valido

    @staticmethod
    def validar_login(usuario):
        es_valido = True
        if not Usuario.get_by_email({'email':usuario['email']}):
            flash('el correo no se encuentra disponible')
            es_valido = False
        return es_valido
