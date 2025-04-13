from flask import Flask, render_template, request, redirect,session,url_for
from flask_mysqldb import MySQL
import yaml,re
from constants import *

import pymysql
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb

app = Flask(__name__)
app.secret_key = 'DBKEY'
# Configure db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)

        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        
        # Fetch one record and return result
        account = cursor.fetchone()
        print(account)
        if account:
            print('if')
            print(session)
            session['loggedin'] = True
            session['id'] = account['User_ID']
            session['username'] = account['Username']

            # Redirect to doctor patient or admin home page
            if 'AD' in session['id']:
                return redirect(url_for('admin_home'))
            
            return render_template('index.html', msg = "Successfully logged in")
            #elif PAT in session['id']:
              #  return redirect(url_for('pat_home'))
            #elif ADMIN in session['id']:
               # return redirect(url_for('admin_home'))
            #else: 
            #    return render_template('index.html')

        else:
            print("else")
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    #print(msg)
    return render_template('index.html', msg=msg)


@app.route('/login/admin_home/')
def admin_home():
    if 'loggedin' in session:
        # Admin home page display the doctor details
        admin_ssn = session['id']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT User_ID, Fname,Lname FROM customer where AD_SSN=%s",[admin_ssn])
        records = cursor.fetchall()
        print(records)
        return render_template('admin_home.html', username=session['username'], doctor_records = records)
    
    return redirect(url_for('login'))

@app.route('/login/admin_suppliers/')
def admin_suppliers():
    pass 

@app.route('/login/admin_orders/')
def admin_orders():
    pass 

@app.route('/login/admin_profile/')
def admin_profile():
    pass 

@app.route('/login/logout/')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # Redirect to login page
    return redirect(url_for('login'))

@app.route('/login/add_supplier/',methods = ['GET', 'POST'])
def add_supplier():
    pass 

@app.route('/login/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        fname = request.form['fname']
        lname =  request.form['lname']
        phonenumber =  request.form['phonenumber']
        address =  request.form['address']
        state =  request.form['state']
        city = request.form['city']
        ssn =  request.form['ssn']
        usertype =  request.form['usertype']
        gender = request.form['gender']
        dob = request.form['dob']

        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE Username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
       
        else:
            if usertype == 'Admin':
                #specialization =  request.form['specialization']
                cursor.execute("SELECT user_id FROM ecommerce_db_project.accounts where User_ID like 'AD%' ORDER BY user_id  DESC LIMIT 1;")
                records = cursor.fetchall()
                if records is None:
                    user_ID = ADMIN + "_1"
                else:
                    last_user_id = records[0]['user_id']
                    last_user_id_count = int(last_user_id.split('_')[1])
                    user_ID = ADMIN + '_' + str(last_user_id_count + 1 )

                address += " "+ state + " " + city
                cursor.execute('INSERT INTO accounts VALUES(%s, %s, %s)', (user_ID, username, password))
                cursor.execute('INSERT INTO admin VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', 
                                (ssn,user_ID, fname, lname, dob, gender, phonenumber, address))
                mysql.connection.commit()
                msg = 'You have successfully registered!'
                
            else:
                if usertype == "Customer" :
                    cursor.execute("SELECT user_id FROM telemedicine.accounts where User_ID like 'CUS%' ORDER BY user_id  DESC LIMIT 1;")
            
                elif usertype == "Supplier":
                    cursor.execute("SELECT user_id FROM telemedicine.accounts where User_ID like 'SUP%' ORDER BY user_id  DESC LIMIT 1;")
                
                records = cursor.fetchall()

                # if its the first patient
                if records is None:
                    user_ID = CUS + "_1"
                else:
                    last_user_id = records[0]['user_id']
                    last_user_id_count = int(last_user_id.split('_')[1])
                    user_ID = CUS + '_' + str(last_user_id_count + 1 )

                address += " "+ state + " " + city
                cursor.execute('INSERT INTO accounts VALUES(%s, %s, %s)', (user_ID, username, password))

                cursor.execute("SELECT SSN FROM Admin ORDER BY RAND ( ) LIMIT 1")
                records = cursor.fetchall()
                assigned_admin_id = records[0]['SSN']

                if usertype == "Customer" :
                    cursor.execute('INSERT INTO patient VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)', 
                                (user_ID, ssn, fname, lname, gender, phonenumber, dob, address,assigned_admin_id))
            
                elif usertype == "Supplier":
                    cursor.execute('INSERT INTO patient VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s)', 
                                (user_ID, ssn, fname, lname, dob, gender, phonenumber, address,"5.0",assigned_admin_id))
                    
                mysql.connection.commit()
                msg = 'You have successfully registered!'
    
    elif request.method == 'POST':
        msg = 'Please fill out the form!'


    return render_template('register.html', msg=msg)


@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)