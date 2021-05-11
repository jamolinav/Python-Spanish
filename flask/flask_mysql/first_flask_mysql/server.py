from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('first_flask')	        # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html", all_friends=friends)

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    print(request.form)
    datos = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'occ': request.form['occ']
    }
    query = 'INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)' 
    query += 'VALUES (%(fname)s, %(lname)s, %(occ)s, NOW(), NOW());'

    mysql = connectToMySQL('first_flask')
    new_friend_id = mysql.query_db(query, datos)
    print('new_friend_id:',new_friend_id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
