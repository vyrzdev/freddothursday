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
* ^^ Backend auth could be done using a combination of hashes and encryption. E.g. Storing encrpyted data under username, storing encryption key under a hash of the pass. 
Python-style-psuedocode:
```python3
#USER ENROLLMENT
username = userinput()
hashedpass = hashof(userinput())
data_to_be_encrypted = {contributions:"$12000", lastpi:"pi-1", filelocation:"/ftp/user1/", apikey:"ajshkasdkjfal7373821mlmdjhdmnsdhffshKSs"}
encrypteddata, privkey = encrypt(data_to_be_encrypted)
dict.append(username:encrypteddata)
dict.append(hashedpass:privkey)


#Data Fetch
username = userinput()
hashedpass = hashof(userinput())
encrypted_data = dict[username]
privkey = dict[hashedpass]
decrypted_data = decrypt(encrypted_data, privkey)
```
