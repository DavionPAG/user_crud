import requests
from pprint import pprint

URL = 'http://127.0.0.1:5000/users'

def deactivate_user(pk):
  current_user = requests.get('%s/%s' % (URL, pk))
  if current_user.status_code == 200:
    pprint(current_user.json())
  else:
    print('Try again')
  out = requests.delete('%s/%s' % (URL, pk))
  if out.status_code == 204:
    print('Success')
  else:
    print('Try agian')

if __name__ == '__main__':
  pk = int(input('User ID?: '))
  deactivate_user(pk)