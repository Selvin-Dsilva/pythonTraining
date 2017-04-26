import urllib2
import json


api_data=json.load(urllib2.urlopen("https://www.drupal.org/api-d7/node/2773581.json"))


print(api_data)