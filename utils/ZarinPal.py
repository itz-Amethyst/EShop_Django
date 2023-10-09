import requests
from django.conf import settings
from django.http import HttpRequest
import json

from django.shortcuts import redirect , render

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
CallbackURL = 'http://127.0.0.1:8000/order/verify-payment/'


def Send_Request_For_ZarinPal( total_price , ZarinPal_Api , authority = None , flag = False ):
    if flag:
        data = {
            'MerchantID': settings.MERCHANT,
            # Note: If price was rial multiply it by 10
            'Amount': total_price,
            'Description': description,
            'Phone': phone,
            'CallbackURL': CallbackURL,
        }
    else:
        data = {
            'MerchantID': settings.MERCHANT,
            'Amount': total_price,
            'Authority': authority,
            'CallbackURL': CallbackURL
        }

    data = json.dumps(data)

    headers = {'content-type': 'application/json' , 'content-length': str(len(data))}
    response = requests.post(ZarinPal_Api , data = data , headers = headers , timeout = 10 if flag else None)

    return response


def Send_Request(request: HttpRequest, total_price):
    try:

        response = Send_Request_For_ZarinPal(total_price , flag = True , ZarinPal_Api = ZP_API_REQUEST)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                # return {'status': True , 'url': ZP_API_STARTPAY + str(response['Authority']) ,
                #         'authority': response['Authority']}

                return redirect(ZP_API_STARTPAY + str(response['Authority']))
            else:
                return {'status': False , 'code': str(response['Status'])}

        return response
    except requests.exceptions.Timeout:
        return {'status': False , 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False , 'code': 'connection error'}


def Verify( authority , total_price ):
    response = Send_Request_For_ZarinPal(total_price , authority = authority , ZarinPal_Api = ZP_API_VERIFY)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            return {'success': f'تراکنش شما با کد پیگیری {response["data"]["ref_id"]} با موفقیت انجام شد'}
            # return {'status': True, 'RefID': response['RefID']}
            # return render(request, 'Order_Module/Payment_Result.html', {
            #     'success': f'تراکنش شما با کد پیگیری {response["data"]["ref_id"]} با موفقیت انجام شد'
            # })
        elif response['Status'] == 101:
            data = {'info': 'این تراکنش قبلا ثبت شده است'}
            return data
        # return {'status': False, 'code': str(response['Status'])}
        # return render(request, 'Order_Module/Payment_Result.html', {
        #     'error': str(response["data"]['message'])
        # })
        else:
            return {'error': str(response["data"]["message"])}

    return response
