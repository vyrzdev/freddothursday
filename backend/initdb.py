import redis
import random
import hashlib

r = redis.Redis(host='localhost', port=6379, db=0)

students = []

def create12VCo1db():
	#Opens a list of names and makes a list out of them
	f = open('students.txt', 'r')
	for line in f:
	    students.append(line.strip('\n'))

	#writes names and data to the database
	for i in range(0, len(students)):
		data = {"weekContribution":"0.00", "totalContribution":"0.00", 'studentName':students[i] ,'class':'12VCo1'}
		r.hmset(hashlib.sha256(bytes(students[i], 'utf-8')).hexdigest(), data)

create12VCo1db()

#Prints a value from the newly entered data
student = students[random.randint(0, len(students) -1)]
print(student + ' : ' + str(r.hgetall(student)))


