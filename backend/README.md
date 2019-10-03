***ToDo***

- Redis Server (Running locally on Pi, hosting on 127.0.0.1)
- Python script: 
    - Format Data as an iterable list of student objects with scores/monetary value as attributes.
    - Handle modification of said data.
    - NFC Card/User enrollment Ui/Utility.
    

***To Be Considered***
- Potentially, Redis may not be the best option for this. With the current system, the entire list of students will have to be fetched and then overwritten every time a single student's data needs to be modified. 

* ^^ Hashes in redis nullify this problem https://stackoverflow.com/a/21347503 EG:

  ```redis
  redis 127.0.0.1:6379> hmset Sam id 1 contribution 0.03 totalcontribution 1.73
  OK
  redis 127.0.0.1:6379> hgetall Sam
  1) "id"
  2) "1"
  3) "contribuiton"
  4) "0.03"
  5) "totalcontribution"
  6) "1.73"
  ```