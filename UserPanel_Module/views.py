from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest , JsonResponse
from django.shortcuts import render , redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from Account_Module.models import User
from Order_Module.models import Order , OrderDetail
from UserPanel_Module.forms import EditProfileModelForm , ChangePasswordForm
from utils.Custom_Methods import Get_CurrentOrder_And_Price


# Create your views here.

def GetCurrentUser( request: HttpRequest ):
    return User.objects.filter(id = request.user.id).first()


class UserPanelDashboardClass(TemplateView):
    template_name = 'UserPanel_Module/UserPanelDashboard.html'


class EditUserProfile(View):
    def get( self , request: HttpRequest ):
        current_user = GetCurrentUser(request)
        edit_form = EditProfileModelForm(instance = current_user)
        context = {
            'form': edit_form ,
        }
        return render(request , 'UserPanel_Module/EditProfile.html' , context)

    def post( self , request: HttpRequest ):
        current_user = GetCurrentUser(request)
        edit_form = EditProfileModelForm(request.POST , request.FILES , instance = current_user)
        if edit_form.is_valid():
            edit_form.save(commit = True)
        context = {
            'form': edit_form
        }

        return render(request , 'UserPanel_Module/EditProfile.html' , context)


class ChangePassword(View):
    def get( self , request: HttpRequest ):
        context = {
            'form': ChangePasswordForm
        }
        return render(request , 'UserPanel_Module/ChangePassword.html' , context)

    def post( self , request: HttpRequest ):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = GetCurrentUser(request)
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                form.add_error('password' , 'کلمه عبور وارد شده اشتباه میباشد')

        context = {
            'form': form
        }
        return render(request , 'UserPanel_Module/ChangePassword.html' , context)


@login_required
def UserPanelMenuComponent( request: HttpRequest ):
    current_user = GetCurrentUser(request)
    context = {
        'current_user': current_user
    }
    return render(request , 'UserPanel_Module/components/UserSidebar.html' , context)


def User_Basket( request: HttpRequest ):
    current_order , total_amount = Get_CurrentOrder_And_Price(request)

    # for order_detail in current_order.orderdetail_set.all():
    #     total_amount += order_detail.product.price * order_detail.count

    context = {
        'order': current_order ,
        'sum': total_amount
    }
    return render(request , 'UserPanel_Module/User_Basket.html' , context)


def remove_order_detail( request: HttpRequest ):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })

    deleted_count , deleted_dict = OrderDetail.objects.filter(id = detail_id , order__is_paid = False ,
                                                              order__user_id = request.user.id).delete()
    print(deleted_dict)

    if deleted_count == 0:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    current_order , total_amount = Get_CurrentOrder_And_Price(request)

    # detail = current_order.orderdetail_set.filter(id = detail_id).first()
    # detail.delete()

    # for order_detail in current_order.orderdetail_set.all().exclude(id=detail_id):
    #     total_amount += order_detail.product.price * order_detail.count

    context = {
        'order': current_order ,
        'sum': total_amount
    }

    return JsonResponse({
        'status': 'success' ,
        'body': render_to_string('UserPanel_Module/includes/user_basket_content.html' , context)
    })


def Change_Order_Count(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')
    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_or_state'
        })

    order_detail = OrderDetail.objects.filter(id = detail_id, order__user_id = request.user.id,order__is_paid = False).first()

    if order_detail is None:
        return JsonResponse({
            'status': 'not_found_detail_or_state'
        })

    if state == 'increase':
        order_detail.count += 1
        order_detail.save()

    elif state == 'decrease':
        if order_detail.count == 1:
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()
    else:
        return JsonResponse({
            'status': 'state_invalid'
        })

    current_order, total_amount = Get_CurrentOrder_And_Price(request)

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('UserPanel_Module/includes/user_basket_content.html' , context)
    })
