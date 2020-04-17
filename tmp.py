# import ssl
# import OpenSSL
# import requests
# resp = requests.get('https://market.seatable.cn/', verify=False)
# cert = ssl.get_server_certificate(('market.seatable.cn', 443))

# print(cert)

# x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
# print(x509.get_subject())
# res = x509.get_subject().get_components()
# print(res)

import urllib3
import requests
import traceback
# res = requests.get('https://dev.seafile.com/seahub/')
try:
    res = requests.get('https://market.seatable.io/')
except Exception as e:
    traceback.print_exc()
    print('E = {}'.format(e))
# res = requests.get('https://market.seatable.io/api/plugins/timeline/')
# print(res.content)