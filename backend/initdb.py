import redis
import random

r = redis.Redis(host='localhost', port=6379, db=0)

students = []

def create12VCo1db():
	#Opens a list of names and makes a list out of them
	f = open('students.txt', 'r')
	for line in f:
	    students.append(line.strip('\n'))
	
	#sets the base values for everyone
	data = {"weekContribution":"0.00", "totalContribution":"0.00", 'class':'12VCo1'}

	#writes names and data to the database
	for i in range(0, len(students)):
		r.hmset(students[i], data)

create12VCo1db()

#Prints a value from the newly entered data
student = students[random.randint(0, len(students) -1)]
print(student + ' : ' + str(r.hgetall(student)))


