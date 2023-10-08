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


def Send_Request( request: HttpRequest ):
    data = {
        'MerchantID': settings.MERCHANT ,
        'Amount': amount ,
        'Description': description ,
        'Phone': phone ,
        'CallbackURL': CallbackURL ,
    }

    data = json.dumps(data)

    headers = {'content-type': 'application/json' , 'content-length': str(len(data))}

    try:

        response = requests.post(ZP_API_REQUEST , data = data , headers = headers , timeout = 10)

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
