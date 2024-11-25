from django.shortcuts import get_object_or_404, render, redirect
from mongoengine import DoesNotExist
from .models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bson import ObjectId


@login_required
def delete_user(request, user_id):
    current_user = request.user
    try:
        user_to_delete = User.objects.get(id=ObjectId(user_id))
    except DoesNotExist:
        messages.error(request, 'المستخدم غير موجود.')
        return redirect('user_list')

    if current_user.is_admin:  # تأكد من أن المستخدم هو أدمن
        if request.method == 'POST':
            user_to_delete.delete()
            messages.success(request, 'تم حذف المستخدم بنجاح.')
            return redirect('user_list')
        else:
            # عرض صفحة التأكيد
            return render(request, 'confirm_delete.html', {'user_id': user_id})
    else:
        messages.error(request, 'ليس لديك الصلاحيات الكافية لحذف هذا المستخدم.')
        return redirect('user_list')


def login_user(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                # قم بإزالة التحقق من حالة التفعيل (is_verified)
                return redirect('home', username=username, user_id=user.id)
            else:
                error_message = "كلمة المرور غير صحيحة."
        except DoesNotExist:
            error_message = "اسم المستخدم غير موجود."
        except Exception as e:
            error_message = str(e)

    return render(request, 'registration/login.html', {'error_message': error_message})


def register_user(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # تحقق من أن اسم المستخدم والبريد غير موجودين
            if User.objects(username=username).first() or User.objects(email=email).first():
                error_message = "اسم المستخدم أو البريد الإلكتروني موجود بالفعل."
                return render(request, 'registration/register.html', {'error_message': error_message})

            # إنشاء حساب جديد
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save()

            # تحقق من أن المتغيرات غير فارغة
            if new_user.username and new_user.id:
                # إعادة التوجيه إلى صفحة home مع username و user_id
                return redirect('home', username=new_user.username, user_id=str(new_user.id))
            else:
                error_message = "حدث خطأ، يرجى المحاولة مرة أخرى."
                return render(request, 'registration/register.html', {'error_message': error_message})

        except Exception as e:
            error_message = str(e)

    return render(request, 'registration/register.html', {'error_message': error_message})

# def user_list(request):
#     users = User.objects.all()
#     return render(request, 'registration/user_list.html', {
#         'users': users,
#         'current_user': request.user,  # تأكد من تمرير المستخدم الحالي
#     })



def home_view(request, username, user_id):
   
    if not username or not user_id:
        return redirect('user_list') 
    users = User.objects.all()
    return render(request, 'registration/home.html', {
        'username': username,
        'users': users,
        'user_id': user_id
    })
def index(request):
    return render(request, 'registration/index.html')

def confirm_delete(request, user_id):
    # منطق تأكيد الحذف هنا
    pass





# def verify_user(request, user_id):
#     try:
#         user = User.objects.get(id=user_id)
        
#         if request.method == "POST":
#             verification_code = request.POST.get('verification_code')

#             if verification_code == user.verification_code:
#                 user.is_verified = True
#                 user.save()
#                 messages.success(request, "تم التحقق بنجاح!")
#                 return redirect('home', username=user.username, user_id=user.id)
#             else:
#                 messages.error(request, "كود التحقق غير صحيح.")
        
#         return render(request, 'verification/enter_code.html', {'user': user})

#     except User.DoesNotExist:
#         messages.error(request, "المستخدم غير موجود.")
#         return redirect('user_list')
