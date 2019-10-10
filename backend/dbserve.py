import redis
from flask import Flask, requests

r = redis.Redis('localhost')

app = Flask(__name__)

#Use 'keys *' to get all keys from the db
#The gather all keys with the specific class value

def byteCodeDictToStr(diction):
	newdict = {}
	for key in diction.keys():
		newdict[key.decode("utf-8")] = diction[key].decode("utf-8")
	return newdict

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

@app.route('/updateWeekTotal/<studentname>')
def updateStudentData(studentusername):
	if request.args.get('contrib'):
		weeklyContribToAdd = request.args.get('contrib')
		student = r.hgetall(studentname)
		student['weeklyContribution'] = student['weeklyContribution'] + weeklyContribToAdd
		student['totalContribution'] = student['totalContribution'] + weeklyContribToAdd
		r.hmset(studentname, student)

#uuid update
#register user

if __name__ == '__main__':
	app.run(debug=True)
