from flask import Flask, render_template


app = Flask(__name__)

title = {'Noticias': 'Noticias', 'registro':'Registro de Usuario', 
     'usuario': 'Lista de Usuarios', 'menu':'Menu Inicio'} 

@app.route('/')
def Menu():  
    return render_template('Menu.html', title = title)

@app.route('/noticias')
def Noticias():
    noticias = [
        {'title':'Gonzalo Castillo ejerce su derecho al voto', 
        'parrafo':''' El candidato presidencial del Partido de la Liberación Dominicana (PLD), Gonzalo Castillo, ejerció su derecho al voto a las 9:30 de la mañana en el colegio Quisqueya, ubicado en la avenida 27 de febrero casi esquina calle Carmen Mendoza de Cornielle,
                    en las elecciones municipales extraordinarias de este domingo 15 de marzo. El candidato oficialista sufragó en pocos segundos.En los pasados comicios del 16 de febrero, a su salida del recinto electoral, el candidato presidencial del
                    PLD, fue abucheado por los votantes presentes. Dichos comicios fueron suspendidos luego de que el sistema del voto automatizados presentara fallas.'''} , 

        {'title' : 'Gobierno llama a votar en tranquilidad porque en el país no circula el coronavirus', 
        'parrafo':'''El Gobierno dominicano aseguró este sábado previo a las elecciones del 15 de marzo que las medidas de suspensión de viajes a Europa, China, Corea e Irán, así como el aislamiento domiciliario a las personas que en los últimos 15 días estuvieron en estos
                    países, son disposiciones preventivas ya que en el país no circula el coronavirus y todos los 11 casos que se han reportado hasta ahora son importados. Según Montalvo "el número de casos en el país permanece igual: existen 11 casos,
                    todos ellos importados, es decir, provenientes de personas que fueron contagiadas en el exterior". Por esta razón, leyó el ministro de la Presidencia, Gustavo Montalvo, los dominicanos pueden ir a votar este domingo en tranquilidad.'''}, 
        
        {'title': 'Dominicanos que viajaron en un crucero piden ser sometidos a prueba del coronavirus tras presentar síntomas', 
        'parrafo' : '''Varios dominicanos, incluido algunos empleados de una AFP local, exigieron este viernes a las autoridades de Salud Pública ser sometidos a la prueba del coronavirus, debido a que presentan síntomas de afección respiratoria aguda luego de viajar, la pasada
                    semana, en un crucero en el que se encontraban personas de varios países donde circula la enfermedad. En denuncia a Diario Libre, los afectados informaron que se pusieron en contacto con la Dirección de Epidemiología del Ministerio
                    de Salud Pública para que le aplicaran la prueba, tras presentar tos, fiebre, dolor de cabeza y otros síntomas.'''}
        
    ]    
    return render_template('Noticias.html', noticias = noticias, title=title) 


@app.route('/registro')
def Registro():
    return render_template('Registro.html', title=title) 

@app.route('/usuarios')
def Usuarios():
    usuarios = [
        {'nombres': 'Jorge Luis', 'apellidos': 'Liberata Garcia', 'edad': '30', 'sexo':'Masculino', 'telefono':'809-555-6644','email':'jorgeliberata@gmail.com ','ciudad':'Santo Domingo Norte','info':'No'},
        {'nombres': 'Juana Michel', 'apellidos': 'Loraine Brown', 'edad': '19', 'sexo':'Femenino', 'telefono':'829-544-24444','email':'loraine34@gmail.com','ciudad':'Distrito Nacional','info':'No'},
        {'nombres': 'Jose Miguel', 'apellidos': 'Artidor Suero', 'edad': '25', 'sexo':'Masculino', 'telefono':'849-857-5635','email':'michale25@hotmail.com','ciudad':'San Cristobal','info':'Si'}
        ]
      
    return render_template('Usuarios.html', usuarios = usuarios, title = title) 


