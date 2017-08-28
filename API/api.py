import json
from requests_oauthlib import OAuth1, OAuth2
from requests import get,post

class TwitterApi(object):
	BASE_URL = "https://api.twitter.com/1.1/"

	def __init__(self, consumer_key,consumer_secret,access_token_key,access_token_secret):
		keys = [consumer_key,consumer_secret,access_token_key,access_token_secret]
		if all(keys):
			self._auth = OAuth1(consumer_key,consumer_secret,access_token_key,access_token_secret)
		else:
			raise Exception("You should fill all keys")

	def __str__(self):
		return "ok"

	def __searchById(self,ids):
		searchById = get("https://api.twitter.com/1.1/users/lookup.json",auth=self._auth,params={"user_id":ids})
		blockedUsers = dict()
		for i in searchById.json():
			blockedUsers[i['name']] = i['screen_name']
		return blockedUsers	

	def getBlockedUsers(self):
		blocked = get(self.BASE_URL+"blocks/ids.json",auth=self._auth)
		ids = json.loads(blocked.text)
		li = []
		for i in ids['ids']:
			li.append(i)
		return self.__searchById(li)


s = TwitterApi('QVI8HY6oxhJoYVD4VGQehCH20', '8h32mUOEaOw3K6d9HMNf6tmyJ1qbBVGTzghHy3MdqWo8xamokW',
               '145610074-5y5BerqXWWQh8PCbVVYj6c79AlRauzoVRW2gAHhJ', 'uRPc8Rify0LHHVyPAHp5I5Ew7NsBzeBaslW2KRdjY0qVR')


#print(s.getBlockedUsers())
