from flask import Flask, render_template_string

app = Flask(__name__)

# Tus videos (despues podes agregar los que quieras)
videos = [
    {"titulo": "Mi primer video", "id": "dQw4w9WgXcQ"},
    {"titulo": "Tutorial Python", "id": "kqtD5dpn9s8"},
    {"titulo": "Video de Alberti", "id": "jNQXAC9IVRw"},
    {"titulo": "El Terror de Roblox está yendo MUY LEJOS | Monochrome", "id": "Q2ZMTPL39xQ"},
    {"titulo": "MI PROPIA SKIN EN QUARANTINE ZONE", "id": "N21Xay-fW0&t=922s"},
]

HTML = """
<h1 style="font-family:Arial; background:red; color:white; padding:15px;">MiTube 🔴</h1>
<div style="display:flex; flex-wrap:wrap; gap:20px; padding:20px;">
{% for v in videos %}
  <div style="width:300px;">
    <iframe width="300" height="170" src="https://www.youtube.com/embed/{{ v.id }}" frameborder="0" allowfullscreen></iframe>
    <h3 style="font-family:Arial;">{{ v.titulo }}</h3>
  </div>
{% endfor %}
</div>
"""

@app.route("/")
def inicio():
    return render_template_string(HTML, videos=videos)

app.run(debug=True)



