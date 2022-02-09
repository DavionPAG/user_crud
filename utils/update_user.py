from pprint import pprint
import requests

URL = 'http://127.0.0.1:5000/users'

EXAMPLE_JSON = {
"first_name": "Jon",
"last_name": "Doe",
"hobbies": "Gaming"
}

def update_user(pk, first_name, last_name, hobbies):
  user_json = EXAMPLE_JSON
  user_json['first_name'] = first_name
  user_json['last_name'] = last_name
  user_json['hobbies'] = hobbies
  current_user = requests.get('%s/%s' % (URL, pk))
  if current_user.status_code == 200:
    pprint(current_user.json())
  else:
    print('Try again')
  out = requests.put('%s/%s' % (URL, pk), json=user_json)
  if out.status_code == 204:
    print('Success')
  else:
    print('Try agian')

if __name__ == '__main__':
  pk = int(input('User ID?: '))
  first_name = input('First name?: ')
  last_name = input('Last name?: ')
  hobbies = input('Hobbie(s)?: ')
  update_user(pk,first_name, last_name, hobbies)
