from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests
import csv

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
  "type": "service_account",
  "project_id": "fine-citadel-367221",
  "private_key_id": "ffe30f17755a68c1a4b55c5f3feecc4fabb0284c",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDvP0s/X7KIaML/\n9y0MS3Buxvm//GLp6BtbmualSwO6T15NZs8QmuomYLNZVQ3RJCO51eOhhARptKod\n8UYPxkCe+biAIHZnQm4MSU5TQMlr7h4wN5sWHHfyU2PPx8IAvtCSqxy5OUIXHLpf\nS4HZfWEiVQTYhzmvMcvkRNUvPK4VWMaSPVFTWFudBNtm25DLi2sr5g9Kwt6ZYl9F\nX13SgGmdei0z+pVdaw3SA62AHFhfjNEJ7UoERIdyR6fYJ3rQ8aUAMBB7wBbDq8Hu\nrYh9CrIYNiopesJplDafvWqD2uDaQJVn8/phy7NXOx1OT1U+aDMiEwGtfR0fOt0b\nODznERthAgMBAAECggEAAlmXFLLZz/Q+3+Q2uFY4dXjlaXZ4po1engXnQh3t756G\naBP5Q9n246rdCoTDrc3XmH4Sd74L8lmOQ+l6AgWbkaKVQBPuWczZt1Ig6SYu74Bi\nohMpWUk52Xxdpv2YyRu9GuDmcRoDM7MqNpPcXTo/+Gx8ArnCtJCOIEQK6uuv7/RF\ncAmH0n6nPLxEQ0dYSVs9Bfk9N9QEGCwc8vrTM2OJ9SVecpsFXHjnPr3pbsFq8cEk\n+yDmWKINCWImCPtkgMkSuSHEBIofS/wndqYFzF1cdyAS9zTLgMaM9ovulT6peCC1\nHbnEDZeK93qRgJ5fWxcSY0wnS3A4KNOXflp51JEpmQKBgQD/RPHct5O5ZFmT+32u\nqy71GICMlkMgILjxseRfYQntli3xZ/lNxxBGu8d3BQtfipMcKRP7U9ToanAyYI6f\nDGwsUdllbvSDEEpjhij2hDLamQmlAbzr2KE75Z05bhvym/gZ/WXkMF0tzRa92p4j\nSrjI5cbiRAne9fadusxChGAX2QKBgQDv7pvLSzd7gFIKAjnB6dQfdIQqXMGNTVxg\nvl8DuhggB69W3A3cFfI4JArFUog1QuZsswDeAwvdLNolVNQR3x24yS/N9GlBMrBh\nKUL2nIG7IJayHxPnTPQT2hd4fRinHxBru/foxjoxV03PKC6EFC9b7lq9ol+MXh5U\niRFDNuYyyQKBgBiX4d1r6lWQL3ksX512bJ28cJYa2/i6blcK1n/B75zuPRrm84Pk\ny9KkwMDcwY3A4g9yfbRXDUofBxQzbUoxfjJ+6Dz3haMi7KfOAyBM+EFLQTyegD8Q\nregBZTZlP1gOYsbOPQTRDAkfmzNLXrTzu/3O9WxTNcg/VjU4C/nUmxVxAoGACkt2\nq9ZiXw42du95gvSBgYgCU77/Hwz+tbf1Y7eMaXNq9pMilRrr9bS2MZlE9uQT9v4H\nP39p9ueBxLBLGSk1oUQgpPmjuoRuRPz8PpCgkGLplGL4+6e1oVRuRWE4uZL/pV+/\nV2GKBav1TroupMQo9AzaH+DjsKYpLv9imju0zOECgYEAkKqdb53ZIBgD0FxWoSle\nv6Y+IFYPyYGVpqHKw2lCJFKpGy+I5g9Tzsp0lk2iIGkBi6dInf671zcjzclkcgpG\nJTBuqMY9hC8Wn0qKhLDuH8eOmIeBrFrIRYEdPHaLY0MXzqvzD+qOXx4WkvSaI7us\n4jw+u3AxckJibilXi1kjl6c=\n-----END PRIVATE KEY-----\n",
  "client_email": "ex-gitaction-thiagoaraujo@fine-citadel-367221.iam.gserviceaccount.com",
  "client_id": "107998853557243693156",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ex-gitaction-thiagoaraujo%40fine-citadel-367221.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


try:

  """Uploads a file to the bucket."""
  credentials = service_account.Credentials.from_service_account_info(credentials_dict)
  storage_client = storage.Client(credentials=credentials)
  bucket = storage_client.get_bucket('ex_gitaction') ### Nome do seu bucket
  blob = bucket.blob('aopaaaaaaaaa_uhul.csv')

  pages = []
  names = "Name \n"

  for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

  for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
      names = names + artist_name.contents[0] + "\n"

    blob.upload_from_string(names, content_type="text/csv")

except Exception as ex:
  print(ex) 
