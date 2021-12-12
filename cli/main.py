import cachetclient
from cachetclient.v1 import *

client = cachetclient.Client(
    endpoint='https://your.site.de/api/v1',
    api_token='Token',
)

if client.ping():
    print("Yes a connection")

issue = client.incidents.create(
    name='Test',
    message='Dieses Problem ist ein Test Problem',
    status=enums.INCIDENT_FIXED,
)
