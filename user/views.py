import json

from django.shortcuts import render, redirect
import hashlib
from .models import UserModel
from django.http import HttpResponse
# Create your views here.


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/index.html')

def sign_up(request):
    if request.method == 'POST':
        data = json.load(request)
        email = data['email']
        password = data['password']
        hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()
        print(email)
        if '@' not in email:
            return HttpResponse('이메일 형식이 아닙니다.')
        elif len(password) < 8:
            return HttpResponse('비밀번호가 8자미만입니다!')
        else:
            new_user = UserModel()
            new_user.email = email
            new_user.password = hashed_pw
            new_user.save()
            return HttpResponse('회원가입 완료!')

