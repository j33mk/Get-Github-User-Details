import requests
try:
    gitHubUser = input('Enter github User: ')
    gitHubApi = 'https://api.github.com/users/'+gitHubUser+'/events/public'
    resp = requests.get(url=gitHubApi)
    # Check the JSON Response Content documentation below
    data = resp.json() if resp and resp.status_code == 200 else None
    if data is not None and len(data):
        userName = data[0]['payload']['commits'][0]['author']['name']
        userEmail = data[0]['payload']['commits'][0]['author']['email']
        print('User email is: {} and User Full name is {}'.format(
            userEmail, userName))
    else:
        print('The username provided is invalid or doesnot exists try again')
except Exception as e:
    print(e)
