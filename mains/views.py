from django.shortcuts import render,get_object_or_404
from django.core.mail import send_mail
from .models import *
from .forms import *




def index(request):
    profiles=Profile.objects.order_by('pk')
    icecream=Icecream.objects.all()
    context={
        'title':'text',
        'profiles':profiles,
        'icecream':icecream,
    }
    return render(request,'mains/index.html',context=context)

def icecream_detail(request,adress):
    icecream_card=Icecream.objects.get(slug=adress)
    # icecream_card=get_object_or_404(Icecream,slug=adress)
    context={
        'icecream_card':icecream_card,
    }
    return render(request,'mains/icecream_detail.html',context=context)

def send_form(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # Получаем данные из формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            to = form.cleaned_data['to']
            comments = form.cleaned_data.get('comments', '')
            uploaded_file = request.FILES['file']
            # Получение изображения из запроса для поля image
            uploaded_image = request.FILES['image']

            # Формируем тему и текст письма
            subject = f"Message from {name}"
            message = f"From: {name}\nEmail: {email}\nTo: {to}\nComments: {comments}\nФайл: {uploaded_file}\nФото: {uploaded_image}"

            # Отправляем письмо
            send_mail(subject, message, email, [to])

            # Контекст для отображения успешной отправки формы
            context = {'success': True}
            return render(request, 'mains/mail_form.html', context)
    else:
        # Если запрос не POST, создаем пустую форму
        form = EmailForm()

    # Контекст для передачи формы в шаблон
    context = {'form': form}
    return render(request, 'mains/mail_form.html', context)