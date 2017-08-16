from requests_oauthlib import OAuth1, OAuth2
from requests import get,post
class TwitterApi(object):
	BASE_URL = "https://api.twitter.com/1.1/"
	HTTP_ERROR_CODES = {

	304 : "Not Modified",
	400 : "Bad Request", 
	401 : "Unauthorized", 
	403 : "Forbidden",
	404 : "Not Found",
	406 : "Not Acceptable",
	410 : "Gone",
	420 : "Enhance Your Calm",
	422 : "Unprocessable Entity",
	429 : "Too Many Requests",
	500 : "Internal Server Error",
	502 : "Bad Gateway",
	503 : "Service Unavailable",
	504 : "Gateway timeout"

	}

	ERROR_CODES = {

	32  : "Could not authenticate you",
	34  : "Sorry, that page does not exist",
	64  : "Your account is suspended and is not permitted to access this feature", 
	68  : "The Twitter REST API v1 is no longer active. Please migrate to API v1.1. https://dev.twitter.com/rest/public",
	88  : "Rate limit exceeded",
	89  : "Invalid or expired token",
	92  : "SSL is required",
	130 : "Over capacity",
	131 : "Internal error",
	135 : "Could not authenticate you",
	161 : "You are unable to follow more people at this time",
	179 : "Sorry, you are not authorized to see this status",
	185 : "User is over daily status update limit",
	187 : "Status is a duplicate",
	215 : "Bad authentication data",
	226 : "This request looks like it might be automated. To protect our users from span and other malicious activity, we can't complete this action right now.",
	231 : "User must verify login",
	251 : "This endpoint has been retired and should not be used.",
	261 : "Application cannot perform write actions.",
	271 : "You can't mute yourself.",
	272 : "You are not muting the specified user."
	}

	def __init__(self, consumer_key,consumer_secret,access_token_key,access_token_secret):
		keys = [consumer_key,consumer_secret,access_token_key,access_token_secret]
		if all(keys):
			self._auth = OAuth1(consumer_key,consumer_secret,access_token_key,access_token_secret)
		else:
			raise Exception("You should fill all keys")
