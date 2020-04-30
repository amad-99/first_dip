from flask import Flask, render_template, url_for, request, redirect, flash
# from flask_mysqldb import MySQL
import csv

app = Flask(__name__)

def writ_into_csv(data) :
    with open('database.csv', mode='a') as database :
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_write = csv.writer(database,delimiter='|', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_PORT'] = 3306
# app.config['MYSQL_USER'] = "id13490626_message_contact_db"
# app.config['MYSQL_PASSWORD'] = "uJK|^Iuo>64b9Uz7"
# app.config['MYSQL_DB'] = "id13490626_message_contact"

# mysql = MySQL(app)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def about_me(page_name):
    page = page_name+'.html'
    print(page)
    return render_template(page)

@app.route('/form_submit', methods=['POST', 'GET'])
def form_submit() :
    # cursor = mysql.connection.cursor()
    if request.method == 'POST' :
        # data = {
        #     "email":request.form["email"],
        #     "subject":request.form["subject"],
        #     "message":request.form["message"]
        # }
        try:
            data = request.form.to_dict()
            writ_into_csv(data)
            # cursor.excute('''INSERT INTO messages VALUES('dasdasd','asdasdasd','dfngfgedhfuo',now())''')
            # mysql.connection.commit()
            return render_template('callback.html')
        
        except:
            return 'error while saving data'
        
    else :
        return "error lodding it"
    
    




