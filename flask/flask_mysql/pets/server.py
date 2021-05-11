from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('first_flask')	        # call the function, passing in the name of our db
    pets = mysql.query_db('SELECT * FROM pets;')  # call the query_db function, pass in the query as a string
    print(pets)
    return render_template("index.html", all_pets=pets)

@app.route("/create_pet", methods=["POST"])
def add_friend_to_db():
    print(request.form)
    datos = {
        'name': request.form['name'],
        'type': request.form['type'],
    }
    query = 'INSERT INTO pets (name, type, created_at)' 
    query += 'VALUES (%(name)s, %(type)s, NOW());'

    mysql = connectToMySQL('first_flask')
    new_pet_id = mysql.query_db(query, datos)
    print('new_pet_id:', new_pet_id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
