from pywidevine.decrypt.wvdecrypt import WvDecrypt
import requests
import base64
import binascii


# # headers={}
# # pssh='AAAAp3Bzc2gAAAAA7e+LqXnWSs6jyCfc1R0h7QAAAIcSEFF0U4YtQlb9i61PWEIgBNcSEPCTfpp3yFXwptQ4ZMXZ82USEE1LDKJawVjwucGYPFF+4rUSEJAqBRprNlaurBkm/A9dkjISECZHD0KW1F0Eqbq7RC4WmAAaDXdpZGV2aW5lX3Rlc3QiFnNoYWthX2NlYzViZmY1ZGM0MGRkYzlI49yVmwY='
# # license_url='https://cwip-shaka-proxy.appspot.com/no_auth'

# #vmp test 
# pssh='AAAAXHBzc2gAAAAA7e+LqXnWSs6jyCfc1R0h7QAAADwIARIQ9MfslaUfVp6NHqbA5K1/ZxoIdXNwLWNlbmMiGDlNZnNsYVVmVnA2TkhxYkE1SzEvWnc9PSoAMgA='
# license_url='https://lic.glxplay.io/license-proxy-widevine/cenc/'
# headers={
    # 'dt-custom-data': 'eyJ1c2VySWQiOiI1M2QxYjNkYS1hZmU4LTQ3MGItODIwOS05OThlZGI3NjBjZDciLCJzZXNzaW9uSWQiOiJwcm9kdWN0aW9uXzA2ZGNmYTVlLWNlOGMtNGFjZC04NmZiLWE1ZTQ4N2MxOWIyYyIsIm1lcmNoYW50IjoiZmltcGx1cyJ9',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# cert=requests.post(license_url,b'\x08\x04').content

# wvdecrypt = WvDecrypt(pssh)

# wvdecrypt.set_certificate(base64.b64encode(cert))

# challenge = wvdecrypt.get_challenge()

# license=requests.post(license_url,challenge,headers=headers).content

# wvdecrypt.update_license(base64.b64encode(license))

# keys=wvdecrypt.start_process()

# for k in keys:
    # print(k)


pssh = 'AAAANHBzc2gAAAAA7e+LqXnWSs6jyCfc1R0h7QAAABQIARIQDRTCz7HXTuGlzTfMYhGHow=='
license_url = "https://drmtoday.vieon.vn/license-proxy-widevine/cenc/"
#cert=requests.post(license_url,b'\x08\x04').content
wvdecrypt = WvDecrypt(pssh)
license=requests.post(
    url=license_url,
    data=wvdecrypt.get_challenge(),
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
        "dt-custom-data": "eyJ1c2VySWQiOiI5OGFlMzZmNi00OTM1LTkwNzgtOTZkYi05NzQwM2QzNzRmNDgiLCJzZXNzaW9uSWQiOiJleUpoYkdjaU9pSklVekkxTmlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKbGVIQWlPakUyTURZMk5UZzNPVElzSW1wMGFTSTZJalptTVdGaU9UQmxaV0UzT0RWa1lUSmpOR0ZpTW1KaFlXVTJPRE00TkRZMklpd2lZWFZrSWpvaUlpd2lhV0YwSWpveE5qQTBNRFkyTnpreUxDSnBjM01pT2lKV2FXVlBiaUlzSW01aVppSTZNVFl3TkRBMk5qYzVNU3dpYzNWaUlqb2lPVGhoWlRNMlpqWXRORGt6TlMwNU1EYzRMVGsyWkdJdE9UYzBNRE5rTXpjMFpqUTRJaXdpYzJOdmNHVWlPaUpqYlRweVpXRmtJR05oY3pweVpXRmtJR05oY3pwM2NtbDBaU0JpYVd4c2FXNW5PbkpsWVdRaUxDSmthU0k2SWpReE16SXpNalV6TlNJc0luVmhJam9pVFc5NmFXeHNZUzgxTGpBZ0tGZHBibVJ2ZDNNZ1RsUWdNVEF1TURzZ1YybHVOalE3SUhnMk5Da2dRWEJ3YkdWWFpXSkxhWFF2TlRNM0xqTTJJQ2hMU0ZSTlRDd2diR2xyWlNCSFpXTnJieWtnUTJoeWIyMWxMemcyTGpBdU5ESTBNQzR4TVRFZ1UyRm1ZWEpwTHpVek55NHpOaUJGWkdjdk9EWXVNQzQyTWpJdU5URWlMQ0prZENJNkluZGxZaUlzSW0xMGFDSTZJbTF2WW1sc1pWOXNiMmRwYmlJc0ltMWtJam9pVjJsdVpHOTNjeUF4TUNJc0ltbHpjSEpsSWpvd2ZRLkVvVjM0cHM5OWt2YkIwLThCOUQwaDljR0JXdmppeExBbURNX2pTU2NyY1EiLCJtZXJjaGFudCI6ImR6b25lcyJ9",
    }).json()

license_b64 = license['license']
wvdecrypt.update_license(license_b64)

keys=wvdecrypt.start_process()

for key in keys:
    print(key)