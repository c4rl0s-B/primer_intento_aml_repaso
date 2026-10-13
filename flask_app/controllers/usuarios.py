from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt #Importamos Bcrypt

bcrypt = Bcrypt(app) #Generamos un objeto llamado bcrypt

@app.route('/')
def inicio(): 
    return render_template('index.html')

#registro / crear usuario
@app.route('/crear_usuario', methods= ["POST"])
def crear_usuario():

    #para agregar un usuario lo primero que debo hacer es
    #recuperar la informacion desde el formulario
    #para hacer eso necesitamos el request.form
    #%(nombre)s, %(apellido)s, %(email)s,%(password)s

    #--- IMPORTANTE: TEORICAMENTE ANTES DE REGISTRAR UN NUEVO DATO
    #--- YO DEBERÍA VALIDAR QUE LOS DATOS INGRESADOS
    #--- SEAN VALIDOS

    if not Usuario.validar_registro(request.form):
        print("Usuario Invalido")
        return redirect('/')

    #--- VALIDACIONES ---

    #Hasheamos la contraseña

    pass_hasheado = bcrypt.generate_password_hash(request.form['password'])

    datos_usuario_registro= {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': pass_hasheado
    }

    nuevo_id = Usuario.save(datos_usuario_registro) #Recibiendo el ID del nuevo Usuario

    session['usuario_id'] = nuevo_id

    return redirect('/cine')

#inicio sesión 


#cerrar sesión
