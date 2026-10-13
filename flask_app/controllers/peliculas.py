from flask_app import app
from flask import render_template, session
from flask_app.models.usuario import Usuario

@app.route('/cine')
def cine():
    print(session['usuario_id'])
    usuario_en_sesion= Usuario.get_one({'id': session['usuario_id']})
    return render_template('cine.html', usuario=usuario_en_sesion)