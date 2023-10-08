import requests
from django.conf import settings
from django.http import HttpRequest
import json

if settings.SANDBOX:
    environment = 'sandbox'

else:
    environment = 'www'

ZP_API_REQUEST = f"https://{environment}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{environment}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{environment}.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
email = 'pransermi@gmail.com'  # Optional
# Important: need to edit for really server.
CallbackURL = 'http://127.0.0.1:8080/order/verify-payment/'


def Send_Request(request: HttpRequest):
    try:

        response = Send_Request_For_ZarinPal(flag = True , ZarinPal_Api = ZP_API_REQUEST)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return {'status': True , 'url': ZP_API_STARTPAY + str(response['Authority']) ,
                        'authority': response['Authority']}
            else:
                return {'status': False , 'code': str(response['Status'])}

        return response
    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}


def Verify(authority):
    response = Send_Request_For_ZarinPal(authority = authority , ZarinPal_Api = ZP_API_VERIFY)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            return {'status': True, 'RefID': response['RefID']}
        else:
            return {'status': False, 'code': str(response['Status'])}

    return response


def Send_Request_For_ZarinPal(authority, ZarinPal_Api, flag = False):
    if flag:
        data = {
            'MerchantID': settings.MERCHANT,
            'Amount': amount,
            'Description': description,
            'Phone': phone,
            'CallbackURL': CallbackURL,
        }
    else:
        data = {
            'MerchantID': settings.MERCHANT,
            'Amount': amount,
            'Authority': authority
        }

    data = json.dumps(data)

    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    response = requests.post(ZarinPal_Api, data = data, headers = headers, timeout = 10 if flag else None)

    return response
