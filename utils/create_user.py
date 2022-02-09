import requests

URL = 'http://127.0.0.1:5000/users'

EXAMPLE_JSON = {
"first_name": "Jon",
"last_name": "Doe",
"hobbies": "Gaming"
}

def create_user(first_name, last_name, hobbies):
  user_json = EXAMPLE_JSON
  user_json['first_name'] = first_name
  user_json['last_name'] = last_name
  user_json['hobbies'] = hobbies

  out = requests.post(URL, json=user_json)
  if out.status_code == 201:
    print('User created')
  else:
    print('Something went wrong, try again')

if __name__ == '__main__':
  first_name = input('First name?: ')
  last_name = input('Last name?: ')
  hobbies = input('Hobbie(s)?: ')
  create_user(first_name, last_name, hobbies)