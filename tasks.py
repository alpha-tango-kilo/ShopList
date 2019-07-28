import pickle                                           # for storing credentials
import os.path                                          # checking for the existence of files
from google.auth.transport.requests import Request      # allows you to login
from google_auth_oauthlib.flow import InstalledAppFlow  # used to load credentials from a .json
from googleapiclient.discovery import build             # used to open connection to Tasks

"""
Valid scopes are:
Read/Write  - https://www.googleapis.com/auth/tasks
Read        - https://www.googleapis.com/auth/tasks.readonly
"""
SCOPES = ["https://www.googleapis.com/auth/tasks"]
def main():
    creds = None
    # check for credentials
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    
    # login if needed
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # TODO: Make arg-based
            flow = InstalledAppFlow.from_client_secrets_file("./tasksapiconfig.json", SCOPES)
            creds = flow.run_local_server(port = 0)
        
        # save credentials
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token, pickle.HIGHEST_PROTOCOL)
    
    # create a means of interacting with the API
    service = build("tasks", "v1", credentials = creds)
    
    # talk to the API
    results = service.tasklists().list(maxResults = 100).execute()
    items = results.get("items", [])

    if not items:
        print('No task lists found.')
    else:
        print('Task lists:')
        for item in items:
            print(u'{0} ({1})'.format(item['title'], item['id']))

if __name__ == '__main__':
    main()