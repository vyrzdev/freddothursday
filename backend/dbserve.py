import redis
from flask import Flask

r = redis.Redis('localhost')

app = Flask(__name__)

#Use 'keys *' to get all keys from the db
#The gather all keys with the specific class value

@app.route('/getClassMembers/<classname>')
def getClassMembers(classname):
	members = []
	keys = r.keys()
	for key in keys:
		hash = r.hgetall(key)
		if hash[b'class'] == classname:
			members.append(key)

	return members

@app.route('/getStudentData/<studentname>')
def getStudentData(studentname):
	data = r.hgetall(studentname)
	return data

if __name__ == '__main__':
	app.run(debug=True)
