# Initialise the Database

To initialise the database all you need to do it run the `initdb.py` script and it will auto populate a redis database with all of the users in a `students.txt` file. This assumes you have a redis server running.

It may be worth using `redis-cli` to `FLUSHALL` when ***re***-initialising the database as strange things may occur.
