from flask import Flask, render_template,request,redirect
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'interview'
}

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/users')
def list_users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Id,Name,Email ,role FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()  
    return render_template('users.html', users=users)

@app.route ('/new_user', methods=['GET','POST'])
def new_user():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        role = request.form ['role']

        conn=mysql.connector.connect(**db_config) 
        cursor=conn.cursor()
        # cursor.execute("INSERT INTO student(ID,Name,Email)VALUES(%s,%s,%s)"(id,name,email))
        cursor.execute("INSERT INTO users(ID,Name,Email,role) VALUES (%s, %s, %s,%s)", (id, name, email,role))

        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/users')
    return render_template('new_user.html')



@app.route('/user/<id>', methods=['GET', 'POST'])
def new_user_by_id(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return render_template('user_details.html', user=user)
    else:
        return "User not found", 404



if __name__ == '__main__':
    app.run(debug=True)

