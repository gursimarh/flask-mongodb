from os import name
from bson.objectid import ObjectId
from flask import render_template , request , redirect , flash
from flask.helpers import url_for
from main import app, db


app.config['SECRET_KEY'] = "code321"

@app.route('/homepage')
def homepage():
       return render_template("home.html")

@app.route('/dashboard')
def dashboard():
       all_data = db.customers.find()
       return render_template("index.html" , employees = all_data)

@app.route('/insert', methods = ['POST'])
def insert():
       data = {}
       if request.method == "POST":
              data['ID']  = request.form['id']
              data['Name'] = request.form['name']
              data['Email'] = request.form['email']
              data['Phone'] = request.form['phone']
              
              db.customers.insert_one(data)
              
              flash("Employee Inserted Successfully.")

       return redirect(url_for('dashboard'))

@app.route('/update', methods = ['GET' , 'POST'])
def update():
       
       if request.method == 'POST':
              name = request.form['name']
              email = request.form['email']
              phone = request.form['phone']
              
              myquery = { "Name": str(name) }
              newvalues = { "$set": { "Name": str(name), "Email": str(email), "Phone" : str(phone)  } }
              
              
              db.customers.update_many(myquery, newvalues)
              
              flash("Employee Entry Updated Successfully.")
              return redirect(url_for('dashboard'))
       
@app.route('/delete/<Name>/', methods = ['GET', 'POST'])
def delete(Name):
       my_data = { "Name" : str(Name)}
       db.customers.delete_one(my_data)
       flash("Employees Data Deleted Successfully.")
       
       return redirect(url_for('dashboard'))