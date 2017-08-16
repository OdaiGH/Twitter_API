from requests_oauthlib import OAuth1
from requests import get,post
auth = OAuth1('QVI8HY6oxhJoYVD4VGQehCH20', '8h32mUOEaOw3K6d9HMNf6tmyJ1qbBVGTzghHy3MdqWo8xamokW',
                                     '145610074-5y5BerqXWWQh8PCbVVYj6c79AlRauzoVRW2gAHhJ', 'uRPc8Rify0LHHVyPAHp5I5Ew7NsBzeBaslW2KRdjY0qVR')
g = get("https://api.twitter.com/1.1/followers/ids.json",auth=auth)
print(g.json())