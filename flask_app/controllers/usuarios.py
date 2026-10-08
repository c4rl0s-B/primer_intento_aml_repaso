from flask_app import app
from flask import render_template, session, redirect, request,flash
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt #Importamos Bcrypt


bcrypt = Bcrypt(app) #Generamos un objeto llamado bcrypt


@app.route('/')
def inicio(): 
    return render_template('index.html')

#registro / crear usuario
@app.route('/crear_usuario', methods=["POST"])
def crear_usuario():

    #para agregar un nuevo usuario es recuperar la informacion desde el form
    #para hacer eso nesesitamos el request.form

   


    #---INPORTANTE: TEORICAMENTE ANTES DE REGISTRAR UN NUEVO DATO
    #---YO DEBERIA VALIDAR QUE LOS DATOS INTEGRADOS
    #---SEAN VALIDOS

    if not Usuario.validar_usuario(request.form):
        flash("El correo es obligatorio","correo")
        return redirect('/')

    #----VALIDACIÓN----

    #haseamos la contraseña
    pass_hasheado = bcrypt.generate_password_hash(request.form['password'])    
    # (%(nombre)s, %(apellido)s, %(email)s,%(password)s
    
    nombre_apellido_email_paswword= {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password':pass_hasheado
    }
    nuevo_id = Usuario.save(nombre_apellido_email_paswword)
    
    session['usuario_id'] = nuevo_id

    return redirect ('/cine')

#inicio sesión 


#cerrar sesión
