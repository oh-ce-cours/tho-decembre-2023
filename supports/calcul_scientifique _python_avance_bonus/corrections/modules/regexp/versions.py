from collections import Counter
import re

python_version_pattern = "[P|p]ython (?P<major>\d*).(?P<minor>\d*)"
versions = open("../media/versions.txt").read()
extracted_python_versions = re.findall(python_version_pattern, versions)

major = [v[0] for v in extracted_python_versions]
minor = [v[1] for v in extracted_python_versions]
print(Counter([x[0] for x in major]))
