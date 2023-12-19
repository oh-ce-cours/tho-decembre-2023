import re
import json

# data loading
tests = json.load(open("../media/listing_mail.json"))["emails"]


def is_mail(mail):
    """Return True if mail is well formatted."""
    pattern = r"[a-z0-9._-]+@[a-z0-9._-]+\..{2,30}"
    return re.match(pattern, mail) is not None


mails = [mail for mail in tests if is_mail(mail)]
pattern_info = (
    r"(?P<identifiant>[a-z0-9._-]+)"
    r"@"
    r"(?P<domaine>[a-z0-9._-]+)\.(?P<tld>.{2,30})"
)
infos = [re.match(pattern_info, mail).groupdict() for mail in mails]
