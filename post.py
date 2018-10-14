from flask import Flask, render_template
from flaskext.mysql import MySQL 

app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'DESKTOP-S9LGAIL'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'harry3026263'
app.config['MYSQL_DATABASE_DB'] = 'mydb'
mysql = MySQL(app)
	
@app.route('/')
def index():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "1"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]	
	return render_template('recommendation.html', image=img)
	return render_template('recommendation.html', nam=name)
	return render_template('recommendation.html', desc = bio)

@app.route('/2')
def index2():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "2"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/3')
def index3():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "3"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/4')
def index4():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "4"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]	
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/5')
def index5():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "5"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/6')
def index6():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "6"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/7')
def index7():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "7"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/8')
def index8():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "8"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]	
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/9')
def index9():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "9"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/10')
def index10():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "10"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]	
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/11')
def index11():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "11"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]	
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/12')
def index12():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "12"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]	
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/13')
def index13():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "13"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/14')
def index14():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "14"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/15')
def index15():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "15"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/16')
def index16():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "16"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

@app.route('/17')
def index17():
	cur = mysql.connect().cursor()
	cur.execute('''SELECT * FROM post WHERE id = "17"''')
	rv = cur.fetchall() 
	for row in rv:
		name = row[1]
		bio = row[2]
		price = row[3]
		address = row[4]
		month = row[5]
		day = row[6]
		img = row[7]	
	return render_template('explore.html', image=img)
	return render_template('explore.html', nam=name)
	return render_template('explore.html', desc = bio)

if __name__ == "__main__":
	app.run(debug=True)
