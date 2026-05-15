from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Clave secreta necesaria para usar session
app.secret_key = 'mi_clave_secreta_super_segura'

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ==========================================
# TABLA CARD
# ==========================================
class Card(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    subtitle = db.Column(db.String(100), nullable=False)

    text = db.Column(db.Text, nullable=False)

    user_email = db.Column(db.String(100), nullable=False)

    def __init__(self, title, subtitle, text, user_email):

        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.user_email = user_email


# ==========================================
# TICKET #1: TABLA USER
# ==========================================
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(100), nullable=False)

    password = db.Column(db.String(100), nullable=False)

    def __init__(self, email, password):

        self.email = email
        self.password = password


# ==========================================
# TICKET #2: CREAR BD
# ==========================================
with app.app_context():

    db.create_all()


# ==========================================
# TICKET #4: LOGIN
# ==========================================
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():

    error = ''

    if request.method == 'POST':

        form_email = request.form['email']
        form_password = request.form['password']

        # Obtener usuarios
        users_db = User.query.all()

        # Verificar usuario
        for user in users_db:

            if form_email == user.email and form_password == user.password:

                # Guardar sesión
                session['user_email'] = user.email

                # Redirigir
                return redirect('/index')

        error = 'Nombre de usuario o contraseña incorrectos'

    return render_template('login.html', error=error)


# ==========================================
# TICKET #3: REGISTRO
# ==========================================
@app.route('/reg', methods=['GET', 'POST'])
def reg():

    if request.method == 'POST':

        email = request.form['email']

        password = request.form['password']

        # Crear usuario
        user = User(email=email, password=password)

        # Guardar usuario
        db.session.add(user)

        db.session.commit()

        return redirect('/login')

    return render_template('registration.html')


# ==========================================
# INDEX
# ==========================================
@app.route('/index')
def index():

    # Protección
    if 'user_email' not in session:

        return redirect('/login')

    # Mostrar solo tarjetas del usuario
    cards = Card.query.filter_by(
        user_email=session['user_email']
    ).order_by(Card.id).all()

    return render_template('index.html', cards=cards)


# ==========================================
# CREAR TARJETA
# ==========================================
@app.route('/form_create', methods=['GET', 'POST'])
def form_create():

    if 'user_email' not in session:

        return redirect('/login')

    if request.method == 'POST':

        title = request.form['title']

        subtitle = request.form['subtitle']

        text = request.form['text']

        # Crear tarjeta
        card = Card(
            title=title,
            subtitle=subtitle,
            text=text,
            user_email=session['user_email']
        )

        db.session.add(card)

        db.session.commit()

        return redirect('/index')

    return render_template('create_card.html')


# ==========================================
# VER TARJETA
# ==========================================
@app.route('/card/<int:id>')
def card(id):

    if 'user_email' not in session:

        return redirect('/login')

    card = Card.query.get_or_404(id)

    return render_template('card.html', card=card)


# ==========================================
# CREATE
# ==========================================
@app.route('/create')
def create():

    if 'user_email' not in session:

        return redirect('/login')

    return render_template('create_card.html')


# ==========================================
# LOGOUT
# ==========================================
@app.route('/logout')
def logout():

    session.pop('user_email', None)

    return redirect('/login')


# ==========================================
# RUN
# ==========================================
if __name__ == "__main__":

    app.run(debug=True)