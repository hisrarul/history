from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:example1234@db/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


@app.route('/')
def Index():
    all_data = Data.query.all()
    return render_template("index.html", employees = all_data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']  # name is the name of input type - mymodal
        email = request.form['email']  # email is the name of input type mymodal in index.html file
        phone = request.form['phone']  # phone is the name of input type mymodal in index.html file

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash('Employee inserted successfully!')
        return redirect(url_for('Index'))   # Index is the name of function

@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))    # row.id is defined in index.html file

        my_data.name = request.form['name']  # name is the name of input type modaledit in index.html file
        my_data.email = request.form['email']  # name is the name of input type modaledit in index.html file
        my_data.phone = request.form['phone']  # name is the name of input type modaledit in index.html file

        db.session.commit()
        flash("Employee Updated Successfully!")
        return redirect(url_for('Index'))


@app.route('/delete/<id>/', methods = ['GET','POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash('Employee deleted Successfully!')
    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    app.run(debug=True)