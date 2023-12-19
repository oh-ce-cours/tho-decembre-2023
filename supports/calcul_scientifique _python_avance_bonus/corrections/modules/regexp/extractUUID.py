import re

url_a = "id/04ec7dd5-8b24-4e38-a37a-8dc6df53e29e/review"
url_b = "id/233b6a88-fd22-4e28-a636-6ebea175dc34/review"

pattern = "id/(?P<uuid>[\w-]*)/review"
re.find(pattern, url_a)["uuid"]
re.find(pattern, url_b)["uuid"]
