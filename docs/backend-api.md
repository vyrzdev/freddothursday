# Backend API

### `/getClassMembers/<classname>`

- Used to gather all the members of a given class (like in a school not in the programmatic sense)

- An example class would be `12VCo1` and would be placed into the URL such that `/getClassMembers/12VCo1` 

- This should return JSON data with the class members within it

- ```json
  localhost:5000/getClassMembers/12VCo1 :
  [
    "Samuel Huddart", 
    "Giles Baker", 
    "Ellie Anstis", 
    "Jedd Goulson", 
    "Lily May Gauntlett", 
    "Zac Haghighat", 
    "Joe Howell", 
    "Ben Parsons-Willis", 
    "Max Stanford-Taylor", 
    "Toby Shelford", 
    "Arthur Jarvis", 
    "Rowan Avis", 
    "Jack Fenton-Jones", 
    "Thomas Hooper"
  ]
  ```

- 