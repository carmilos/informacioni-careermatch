import requests
import json
import os

base = 'http://localhost:8000'

print('1) Checking /jobs...')
r = requests.get(f'{base}/jobs')
print('status:', r.status_code)

print('\n2) Registering HR user (may fail if exists)...')
try:
    r = requests.post(f'{base}/auth/register', json={'email':'hr@example.com','password':'secret','is_hr':True})
    print('register status', r.status_code)
    try:
        print(r.json())
    except Exception:
        print(r.text)
except Exception as e:
    print('register exception', e)

print('\n3) Logging in...')
r = requests.post(f'{base}/auth/login', json={'username':'hr@example.com','password':'secret'})
print('login status', r.status_code)
print(r.text)
if r.status_code != 200:
    raise SystemExit('login failed')

token = r.json().get('access_token')
headers = {'Authorization': f'Bearer {token}'}
print('TOKEN:', token)

print('\n4) Creating job...')
job_payload = {'title':'Backend Dev','company':'Acme','location':'Remote','description':'Test job'}
r = requests.post(f'{base}/jobs', json=job_payload, headers=headers)
print('create job status', r.status_code)
print(r.text)
if r.status_code != 200:
    raise SystemExit('create job failed')
job = r.json()
jobid = job.get('id')
print('Job ID:', jobid)

print('\n5) Preparing CV and applying...')
os.makedirs('backend', exist_ok=True)
with open('backend/test_cv.txt','w') as f:
    f.write('Test CV content')
files = {'cv': open('backend/test_cv.txt','rb')}
data = {'name':'Alice','email':'alice@example.com'}
r = requests.post(f'{base}/jobs/{jobid}/apply', data=data, files=files)
print('apply status', r.status_code)
print(r.text)
if r.status_code != 200:
    raise SystemExit('apply failed')

print('\n6) Fetching applicants...')
r = requests.get(f'{base}/jobs/{jobid}/applicants', headers=headers)
print('applicants status', r.status_code)
print(r.text)
