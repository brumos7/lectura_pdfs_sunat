import webbrowser
import msal
import os

def generate_access_token(app_id, scopes):
    access_token_cache = msal.SerializableTokenCache()
    
    # read the token file
    if os.path.exists('api_token_access.json'):
        access_token_cache.deserialize(open('api_token_access.json', 'r').read())

    client = msal.PublicClientApplication(client_id=app_id, token_cache=access_token_cache)
    accounts = client.get_accounts()
    
    if accounts:
        token_response = client.acquire_token_silent(scopes , accounts[0])
    else:
        flow = client.initiate_device_flow(scopes=scopes)
        print('user code: ' + flow['user_code'])
        webbrowser.open(flow['verification_uri'])
        token_response = client.acquire_token_by_device_flow(flow)
        print(token_response)

    with open('api_token_access.json','w') as _f:
        _f.write(access_token_cache.serialize())
        
    return token_response

    if __name__ == '__main__':
        APP_ID = '20e05918-f02c-413a-9c3c-87f12d01af61'
        SCOPES = ['User.Read']
        
        token_response = generate_access_token(APP_ID, SCOPES)
        print(token_response['access_token'])