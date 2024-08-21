from urllib.parse import urlparse

# original version
def domain_name(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc
    domain_name = domain_name.replace('www.', '')
    main_domain = domain_name.split('.')[0]
    return main_domain

# condensed version
def domain_name(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return urlparse(url).netloc.replace('www.', '').split('.')[0]