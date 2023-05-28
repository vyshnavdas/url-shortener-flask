# url-shortener-flask
A Url Shortener Api Made With Flask And MongoDB

## Variables

- `DB_URL` Your [MongoDb](https://www.mongodb.com/) url


## Usage

<b>`Using Python`</b>
```python
import requests

base_url = ''  # Update with your API base URL
  
# Create a shortened URL
long_url = '' #Provide The Long url here
data = {'long_url': long_url}
response = requests.get(base_url + 'shorten', json=data)
  
if response.status_code == 201:
    shortened_url = response.json()['shortened_url']
    print('Shortened URL:', shortened_url)
else:
    print('Error creating shortened URL:', response.json())
```

