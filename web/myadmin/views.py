from django.shortcuts import render

# Create your views here.

# 后台主页
def index(request):
	return render(request,'myadmin/index.html')


