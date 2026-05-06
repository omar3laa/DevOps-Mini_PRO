from flask import Flask, request, redirect
import mysql.connector

app = Flask(__name__)


@app.route('/')
def index():
    return """
    <h2>Add User</h2>
    <form action="/add" method="post">
        <input type="text" name="name" placeholder="Name" required><br><br>
        <input type="email" name="email" placeholder="Email" required><br><br>
        <button type="submit">Save</button>
    </form>
    <br>
    <a href="/data">View Data</a>
    """

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']

    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='12345',
        database='mydb'
    )
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    conn.close()

    return redirect('/data')

# عرض البيانات
@app.route('/data')
def data():
    conn = mysql.connector.connect(host='mysql5744',
        user='root',
        password='12345',
        database='data'
    )
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()

    html = """
    <h2>Users</h2>
    <a href="/">Back</a>
    <br><br>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
        </tr>
    """

    for user in users:
        html += f"""
        <tr>
            <td>{user[0]}</td>
            <td>{user[1]}</td>
            <td>{user[2]}</td>
        </tr>
        """

    html += "</table>"

    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
