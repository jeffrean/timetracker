import requests
from requests.auth import HTTPBasicAuth
import sys

def test_post_timestamp(stamp_type):
	r = requests.post('http://localhost:5000/api/users/1/timestamps', auth=HTTPBasicAuth('amanj41', 'python'), json={'stamp_type': stamp_type})
	print(r.text)

def test_get_timestamps(start='', stop=''):
	r = requests.get(f'http://localhost:5000/api/users/1/timestamps?start={start}&stop={stop}', auth=HTTPBasicAuth('amanj41', 'python'))
	print(r.text)

test_get_timestamps(start='19-08-20T19-04-00', stop='19-08-20T19-07-30')
#test_post_timestamp('working')