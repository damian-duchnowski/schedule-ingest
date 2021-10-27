from decouple import config
from ticktick.oauth2 import OAuth2
from ticktick.api import TickTickClient

auth_client = OAuth2(config('client_id'), config('client_secret'),
                     config('uri'))

client = TickTickClient(config('username'), config('password'), auth_client)
