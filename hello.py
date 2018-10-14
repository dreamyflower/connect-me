from flask import Flask 
from flaskext.mysql import MySQL 

app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'DESKTOP-S9LGAIL'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'harry3026263'
app.config['MYSQL_DATABASE_DB'] = 'mydb'
mysql = MySQL(app)
	
@app.route('/art')
def art():
	cur = mysql.connect().cursor()
	#cur.execute('''SELECT post_id FROM post_has_interest WHERE interest = 'history''')
	#cur.execute('''SELECT name FROM post WHERE post_id = above)
	cur.execute('''SELECT post_id FROM post_has_interest WHERE interest_name = "Art"''')
	ids = cur.fetchall()
	names = []
	for id in ids:
		cur.execute("SELECT name FROM post WHERE id = " + str(id[0]))
		names.append(cur.fetchall()[0][0])
	names[0] = 
	return names[0] + " and " + names[1]
	
@app.route('/sports')
def sports():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT post_id FROM post_has_interest WHERE interest_name = "Sports"''')
	ids = cur.fetchall()
	names = []
	for id in ids:
		cur.execute("SELECT name FROM post WHERE id = " + str(id[0]))
		names.append(cur.fetchall()[0][0])
	return str(names)

@app.route('/entertainment')
def entertainment():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT post_id FROM post_has_interest WHERE interest_name = "Entertainment"''')
	ids = cur.fetchall()
	names = []
	for id in ids:
		cur.execute("SELECT name FROM post WHERE id = " + str(id[0]))
		names.append(cur.fetchall()[0][0])
	return str(names)

@app.route('/food')
def food():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT post_id FROM post_has_interest WHERE interest_name = "Food"''')
	ids = cur.fetchall()
	names = []
	for id in ids:
		cur.execute("SELECT name FROM post WHERE id = " + str(id[0]))
		names.append(cur.fetchall()[0][0])
	return str(names)

@app.route('/history')
def history():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT post_id FROM post_has_interest WHERE interest_name = "History"''')
	ids = cur.fetchall()
	names = []
	for id in ids:
		cur.execute("SELECT name FROM post WHERE id = " + str(id[0]))
		names.append(cur.fetchall()[0][0])
	return str(names)

@app.route('/music')
def music():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT post_id FROM post_has_interest WHERE interest_name = "Music"''')
	ids = cur.fetchall()
	names = []
	for id in ids:
		cur.execute("SELECT name FROM post WHERE id = " + str(id[0]))
		names.append(cur.fetchall()[0][0])
	return str(names)

@app.route('/outdoors')
def outdoors():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT post_id FROM post_has_interest WHERE interest_name = "Outdoors"''')
	ids = cur.fetchall()
	names = []
	for id in ids:
		cur.execute("SELECT name FROM post WHERE id = " + str(id[0]))
		names.append(cur.fetchall()[0][0])
	return str(names)

@app.route('/shopping')
def shopping():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT post_id FROM post_has_interest WHERE interest_name = "Shopping"''')
	ids = cur.fetchall()
	names = []
	for id in ids:
		cur.execute("SELECT name FROM post WHERE id = " + str(id[0]))
		names.append(cur.fetchall()[0][0])
	return str(names)









"""
@app.route('/addone/<string         :insert>')
def add(insert):
	cur = mysql.connect().cursor()
	cur.execute('''SELECT MAX(id) FROM example''')
	maxid = cur.fetchone() #(10,)
	cur.execute('''INSERT INTO example (id, data) VALUES (%s, %s)''', (maxid[0] + 1, insert))
	mysql.connect.commit()
	return "Done"


@app.route('/getall')
def getall():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM example''')
	returnvals = cur.fetchall() #((1, "ID1"), (2, "ID2"),...)

	printthis = ""
	for i in returnvals:
		printthis += i + "<br>"

	return printthis
"""


if __name__ == '__main__':
	app.run(debug=True)


