from django.shortcuts import render, redirect
from .models import student
from django.core.paginator import Paginator
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.contrib.auth import authenticate, get_user_model

# Create your views here.

def index(request):
    students = student.objects.all()
    paginator = Paginator(students, 10)  # 10 items per page

    page = request.GET.get('page')
    my_data = paginator.get_page(page)
    use_bootstrap = True  
    template_name = 'index.html' if use_bootstrap else 'tailwind_layout.html'
    return render(request, template_name,{'students':students, 'my_data':my_data})


def testMedia(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'testMedia.html',{'context':context})

def add(request):
    students = student.objects.all()
    return render(request, 'insert.html',{'students':students})

def insert(request):
    if request.method == 'POST':
        name = request.POST['username']
        age = request.POST['age']
        avatar = request.FILES.get('avatar')
        document_file = request.FILES.get('document_file')
        description = request.POST.get('description', '')
        if student.objects.filter(name=name).exists():
            error_message = "Tên sinh viên đã tồn tại. Vui lòng chọn tên khác."
            students = student.objects.all()
            return render(request, 'insert.html', {'students': students, 'error_message': error_message})
        else:
            new_student = student.objects.create(name= name, age=age, avatar=avatar, document_file=document_file, description=description)
            new_student.save()
    else:
        return redirect('add')
    return redirect('index')  

def remove(request, pk):
    if request.method == 'POST':
        post = student.objects.filter(id=pk)
        post.delete()
    return redirect('index') 

def update(request, pk):
    if request.method == 'POST':
        name = request.POST['username']
        age = request.POST['age']
        avatar = request.FILES.get('avatar')
        document_file = request.FILES.get('document_file')
        description = request.POST.get('description', '')
        up_st = student.objects.get(id=pk)

        # Check if a new avatar file is provided
        if avatar:
            up_st.avatar = avatar

        up_st.name = name
        up_st.age = age
        up_st.document_file = document_file
        up_st.description = description
        up_st.save()
    else:
        return redirect('edit')

    return redirect('index')    


def edit(request, pk):
    st = student.objects.get(id=pk)
    return render(request, 'edit.html', {'student': st})   

def main(request):
    return render(request, 'base.html')

def send(request):
    return render(request, 'sendEmail.html')

def send_custom_email(email, content):
    subject = 'Thông Báo'
    html_message = render_to_string('template_email.html', {'center_text': content})
    
    email = EmailMessage(
        subject,  # Tiêu đề email
        strip_tags(html_message),  
        settings.DEFAULT_FROM_EMAIL, 
        [email],  
    )
    
    # Thêm nội dung định dạng HTML
    email.content_subtype = 'html'
    email.body = html_message

    # Gửi email
    email.send()

def sendEmail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        content = request.POST.get('content')

        # Gọi hàm để gửi email
        send_custom_email(email, content)

        return render(request, 'sendEmail.html')

    return render(request, 'sendEmail.html')


def login(request):
    return render(request, 'login.html')

# def check_login(request):
#     if request.method == 'POST':
#         username_or_email = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username = username_or_email, password = password)
#         if user is not None:
#             return HttpResponse('Login successful')
#         else:
#             return HttpResponse('Login failed')

#     return render(request, 'login.html')

from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from django.shortcuts import render

def check_login(request):
    User = get_user_model()

    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        # Thực hiện xác thực với tên người dùng
        user = authenticate(request, username=username_or_email, password=password)

        # check_email = User.objects.get

        if user is not None:
            # Xác thực thành công
            return HttpResponse('Đăng nhập thành công')
        else:
            try:
                # Thử lấy người dùng bằng email
                user = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                # Xử lý trường hợp người dùng không tồn tại
                if not is_valid_email(username_or_email):
                    return HttpResponse('Đăng nhập thất bại - Email không hợp lệ')
                else:
                    return HttpResponse('Đăng nhập thất bại - email, username hoặc passwork sai')

            # Validate email (bạn có thể muốn sử dụng một phương pháp kiểm tra email phức tạp hơn)
            

            # Thực hiện xác thực với người dùng đã lấy được
            user = authenticate(request, username=user.username, password=password)

            if user is not None:
                # Xác thực thành công
                return HttpResponse('Đăng nhập thành công')
            else:
                # Xác thực thất bại
                return HttpResponse('Đăng nhập thất bại')

    return render(request, 'login.html')

def is_valid_email(email):
    return '@' in email

#username: kaio
#pass: Kaio2772k2@

