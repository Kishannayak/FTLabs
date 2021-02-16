from django.shortcuts import render
from backendtest.models import *
from .models import *
from datetime import datetime
# datetime object containing current date and time
from django.http import HttpResponse


# Login view
def LoginView(request):
    return render(request, 'Login.html')

# Login view
def APIView(request):
    return HttpResponse("{'members':[{ 'id':'01','real_name':'kishan','tz':Udupi','start_activity':'12/02/2021 18:51:32','end_activity':'12/02/2021 19:32:32'},{ 'id':'01','real_name':'karthik','tz':'Mangalore','start_activity':'12/02/2021 19:31:42','end_activity':'12/02/2021 21:32:12'}]}")  


def HomepageView(request):
    if request.method == 'POST':
        real_name = request.POST['real_name']
        tz = request.POST['tz']
        now = datetime.now()
        # dd/mm/YY H:M:S
        start_activity =now.strftime("%d/%m/%Y %H:%M:%S")
    return render(request, 'Homepage.html',{'real_name':real_name,'tz':tz,'start_activity':start_activity},) 

