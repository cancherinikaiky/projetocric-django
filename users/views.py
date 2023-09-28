from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone 
from event.models import Enrollment, Bond
from datetime import datetime
from .models import PersonalData
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.decorators import api_view

def check_session(request):
    if request.session.get('user_id'):
        return redirect('users:profile')
    return False

def push_data(request):
    return {
        'username' : request.POST.get('username'),
        'first-name' : request.POST.get('first_name'),
        'last_name' : request.POST.get('last_name'),
        'email' : request.POST.get('email'),
        'password' : request.POST.get('password'),
        'password_confirm' : request.POST.get('password_confirm')
    }

def validations(request, user):
    try:
        validate_email(user.email)
    except:
        messages.error(request, 'Email já cadastrado!')
    
    if user.password != user.password_confirm:
        messages.error(request, 'As senhas informadas são diferentes!')

    if len(user.password) < 8:
        messages.error(request, 'As senhas devem conter mais que 8 caracteres!')

    if User.objects.filter(username=user.username).exists():
        messages.error(request, 'Username já cadastrado!')
    
    if messages.error == '':
        return True
    
    return render(request, 'users/register.html')

@api_view(['GET'])
def register(request):
    return render(request, 'users/register.html')


@api_view(['POST'])
def register(request):
    if not check_session(request):
        user = push_data(request)

        for data in user:
            if data == '':
                messages.error(request, 'Todos os campos devem ser preenchidos!')
                return render(request, 'users/register.html')

        if validations(request, user):
            user_model = User.objects.create_user(username=user.username, email=user.email, password=user.password, first_name=user.first_name, last_name=user.last_name)
            user_model.save()

            messages.success(request, 'Usuario cadastrado com sucesso!')

            user_model = auth.authenticate(request, email=user.email, password=user.password)
            
            if not user_model:
                return render(request, 'users/register.html')
            else:
                auth.login(request, user_model)
                request.session['user_id'] = user_model.id
                return redirect('users:edit_user', user_id=user_model.id)

def login(request):
    if request.session.get('user_id'):
        return redirect('users:profile')

    if request.method != 'POST':
        return render(request, 'users/login.html')
    
    email_or_username = request.POST.get('email')
    password = request.POST.get('password')

    user = auth.authenticate(request, email=email_or_username, password=password)

    if not user:
        user = auth.authenticate(request, username=email_or_username, password=password)

    if not user:
        messages.error(request, 'Senha ou email inválido')
        return render(request, 'users/login.html')
    else:
        auth.login(request, user)
        request.session['user_id'] = user.id

        return redirect('users:profile')

def logout(request):
    auth.logout(request)
    return redirect('users:login')

@login_required(login_url='users:login')
def profile(request):
    user = User.objects.get(id=request.session.get('user_id'))
    enrollments = Enrollment.objects.filter(user=user)

    return render(request,'users/profile.html', {'user': user, 'enrollments': enrollments})

@login_required(login_url='users:login')
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.session.get('user_id') != user_id:
        return redirect('users:profile')

    if request.method != 'POST':
        bond = Bond.objects.all()
        return render(request, 'users/edit_user.html', {'user': user, 'bond': bond})

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        
        if not hasattr(user, 'personaldata') or user.personaldata is None:
            personal_data = PersonalData()
            personal_data.user = user
            personal_data.save()
        
        user.personaldata.social_network = request.POST.get('social_network')
        user.personaldata.date_of_birth = datetime.strptime(request.POST.get('date_of_birth'), '%d/%m/%Y').date()

        bond_choice_id = request.POST.get('bond_choice')
        user.personaldata.bond_choice = get_object_or_404(Bond, id=bond_choice_id) 

        user.personaldata.rg = request.POST.get('rg')
        
        user.personaldata.save()

        user.save()
        return redirect('users:profile')

@login_required(login_url='users:login')
@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        uploaded_image = request.FILES.get('image')

        if user_id and uploaded_image:
            user = User.objects.get(id=user_id)

            if not hasattr(user, 'personaldata') or user.personaldata is None:
                personal_data = PersonalData()
                personal_data.user = user
                personal_data.save()

            user_profile = user.personaldata

            img = PILImage.open(uploaded_image)

            width, height = img.size
            size = min(width, height)
            left = (width - size) / 2
            top = (height - size) / 2
            right = (width + size) / 2
            bottom = (height + size) / 2

            img = img.crop((left, top, right, bottom))

            img = img.resize((200, 200), PILImage.ANTIALIAS)

            uploaded_image_name = f"profile_picture_{user.username}_{timezone.now().strftime('%Y%m%d%H%M%S')}.jpg"

            buffer = BytesIO()
            img.save(buffer, format='JPEG')  
            buffer.seek(0)
            processed_image = SimpleUploadedFile(
                uploaded_image_name, buffer.read(), content_type='image/jpeg'
            )

            user_profile.profile_picture = processed_image
            user_profile.save()

            return JsonResponse({'message': 'Image uploaded successfully.'})

    return JsonResponse({'error': 'Invalid request.'}, status=400)
