
# Install Requirements

```
pip install -r requirements.txt
```

# Configure Properties file

A properties file needs to exist in the root directory of the project. This file is called ``twitter_keys.properties``.

The properties file needs to be configured with the Consumer Key, Consumer Secret, Access Token, Access Token Secret and the handle of the account that you want to base the tweets on. This will be under the Keys header. See the following format:
```
[Keys]
consumer_key=
consumer_secret=
access_token=
access_token_secret=
src_user_id=
```
