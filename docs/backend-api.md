# Backend API

### `/getClassMembers/<classname>`

- Used to gather all the members of a given class (like in a school not in the programmatic sense)

- An example class would be `12VCo1` and would be placed into the URL such that `/getClassMembers/12VCo1` 

- This should return JSON data with the class members within it

  ```json
  localhost:5000/getClassMembers/12VCo1 :
  [
    "23f2ad7debff6656787dec7e17a340e5888f89ae781b86bc8d066b5ac4855e6a", 
    "47b700080bc03f4a06fb89e52298234b9535dd3c3f6b49c1bee4f852cf5015a6", 
    "583c74551951d8b06528cef8d585e7d437d9f8416e3f5721d3f2c4552bf3649b", 
    "4b63f235650336c7fe97b0dfd7518c7653f6781a26cf02f4824c6dbb1143e889", 
    "ba1b3a938602803b07e9229a8b432125de64e03cd73e7728dc5cdc177ca36f5f", 
    "64891aacc750d81549eeac3f236ee81612ea1d2194e19a908917bf9954bf109a", 
    "ab151caaca41960252c12221d787e6f6ca006d7e4d9a95c01ca54b10f905e817", 
    "9be135317eb1cc0de1702a5ec449aaab0b89ae0ac717180d9a37e6a773335951", 
    "776f5c01bd35d0272b8b0e6c69be382291c0679a604f0b6caf36d497209d3567", 
    "fc166e12b18f77e48f25e99c29d0cb45f95aed805ec89667e97d09237431988e", 
    "87fa4133b37616ca0ca85273e8e5ef9f0404aefa636f974275c8af891b6bba89", 
    "71e6dfcb81aadffe14123ad90a06faebbfb7d81634c695171e8c54ac2b1b52b3", 
    "bbb2fea3bd3fe89dc9ba59a2259da0276a3193b1197e9b2019dfa54271e0a4cc", 
    "cd608a24a0750fc5a7715f5debb9a24639d85e6ae38d5eb81e03d5799a3a829c"
  ]
  ```

- Class members are stored as a list of UUIDs (a list of SHA256 hashes of names)

### `/getStudentData/<studentname>` 

- This is very simple, just pass in the students UUID into the URL and it will return the students data

  ```json
  localhost:5000/getStudentData/cd608a24a0750fc5a7715f5debb9a24639d85e6ae38d5eb81e03d5799a3a829c
  {
    "class": "12VCo1", 
    "studentName": "Arthur Jarvis", 
    "totalContribution": "0.00", 
    "weekContribution": "0.00"
  }
  ```

### `/updateWeekTotal/<studentname>?contrib=<floatvalue>`

- Use this method to post the amount to update the students contribution 

  ``` text
  localhost:5000/updateWeekTotal/cd608a24a0750fc5a7715f5debb9a24639d85e6ae38d5eb81e03d5799a3a829c?contrib=0.50
  Contribution updated by: 0.50
  ```

### `/updateUUID/<uuid>`

- I rly cba to do this rn

### `/registerUser/?studentname=<studentname>&class=<class>`

- As the end-point reads, this URL registers a user

- You must pass a student name and class, the contribution values are auto initialised to 0.00 and a SHA256 UUID is assigned automagickally 

  ```text
  http://localhost:5000/registerUser/?studentname=Jon%20Doe&class=None :
  New user created with key 03a1970e9972b543424f763c00eb48b06f92e0f44f0ea0d46882bf5449d2d3e1
  ```

  