from django.shortcuts import render, get_object_or_404,redirect 
from django.shortcuts import render
from .models import Employee,Vehicle
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
import requests
import json
#from .forms import timerequest

def jsession():
	session = requests.get('http://120.79.23.85:8088/StandardApiAction_login.action?account=moonwalk&password=test1')
	res=session.json()
	return res

def online(session,devIdno):
	online_address = 'http://120.79.23.85:8088/StandardApiAction_getDeviceOlStatus.action?' +'jsession=' + session['jsession'] + '&devIdno=' + str(devIdno)
	#print(online_address)
	status = requests.get(online_address)
	data = status.json()
	return data
 
def location_map(devIdno):
	location_map = 'http://120.79.23.85:8088/808gps/open/map/vehicleMap.html?account=moonwalk&password=test1' + '&devIdno=' + str(devIdno)
	return location_map

## Create your views here.

def streamvid(jsession):
	location_map = 'http://120.79.23.85:8088/808gps/open/map/vehicleMap.html?account=test1&password=test1' + '&devIdno=' + str(devIdno)
	return streamvid


@login_required()
def homepage(request):
	user = request.user.get_username()
	res=jsession()
	print(res)
	user_id = request.user
	employee = Employee.objects.all().filter(user=user_id)
	vehicle = Vehicle.objects.all()
	status = []
	onlinedata = []
	val0 = online(res,vehicle[0].deviceNo)
	print(vehicle[0].deviceNo)
	val1 = online(res,vehicle[1].deviceNo)
	print(vehicle[1].deviceNo)
	val2 = online(res,vehicle[2].deviceNo)
	print(vehicle[2].deviceNo)
	# val3 = online(res,vehicle[3].deviceNo)
	# print(val3,vehicle[3])
	# val4 = online(res,vehicle[2].deviceNo)
	# print(val4,vehicle[4])

	# for i in range(len(vehicle)):
	# 	val = online(res,vehicle[i].deviceNo)
	# 	print(vehicle[i])
	# 	if online(res,vehicle[i].deviceNo)['onlines'] is not None:

	# 		print(online(res,vehicle[i].deviceNo))
	# 		status.extend(online(res,vehicle[i].deviceNo)['onlines'])
	# 	else:
	# 		status.extend(['32'])
	# 	onlinedata.append({
	# 		'lplate': vehicle[i].licensePlate,
	# 		'onlinestatus': status[i]['online'],
	# 		'clientphone': vehicle[i].phoneNum,
	# 		'vcolor': vehicle[i].vColor,
	# 		'locationmap':location_map(vehicle[i].deviceNo)
	# 		#'streamvid':streamvid(vehicle[i].deviceNo)
	# 		})

	return render(request,'hrapp/Employee.html',{'onlinedata':onlinedata})


# # def logout(request):
# # 	return render(request,'hrapp/login.html')
# @login_required()
# def holidays(request):
# 	holiday = Holidays.objects.all()
# 	return render(request,'hrapp/holidays.html',{'holiday':holiday})

# def _search_user(req,username):
# 	user = get_object_or_404(User,username=username)
# 	if username != req.user.username:
# 		user = None
# 	return user

# @login_required()
# def timelog(request,username):
# 	user = _search_user(request,username)
	
# 	if str(request.user.username) != str(username):
# 		return render(request,'hrapp/404.html')
	
# 	user_id = request.user
# 	employee_id = Employees.objects.all().filter(user=user_id)[0]
# 	print(employee_id)
# 	timelog = Timelogs.objects.all().filter(employee_id=employee_id)
# 	print(timelog)
# 	return render(request,'hrapp/timelog.html',{'user':user,'timelog':timelog})

# @login_required()
# def save_timelog(request,username):
# 	row = {}
# 	user = get_object_or_404(User,username=username)
# 	employee_id = 1
	
# 	if str(request.user.username) != str(username):
# 		return render(request,'hrapp/404.html')

# 	# for each in request.POST:
# 	# 	print(request.POST)
	
# 	# print(request.POST['date_worked'])
# 	# print(request.POST['dayhour'])
# 	# print(request.POST['notes'])
# 	formlist = ['date_worked','dayhour','notes']
# 	valid = True

# 	for each in formlist:
# 		if each not in request.POST:
# 			return HttpResponse('The form you entered is invalid! Please fill every field.')
# 			break
	
# 	user_id = request.user
# 	employee = Employees.objects.all().filter(user=user_id)[0]

# 	if request.method == 'POST':
# 		row['date_worked'] = request.POST['date_worked']
# 		row['hours_worked'] = request.POST['dayhour']
# 		row['notes'] = request.POST['notes']
# 		row['employee_id'] = employee

# 	myhours = Timelogs(**row)
# 	myhours.save()

# 	return redirect('timelog',username=username)

# @login_required()
# def timerequest(request,username):
# 	user = _search_user(request,username)
# 	if str(request.user.username) != str(username):
# 		return render(request,'hrapp/404.html')
# 	return render(request,'hrapp/timerequest.html',{'user':user})

# @login_required()
# def save_timerequest(request,username):
# 	row = {}
# 	user_id = request.user
# 	print(user_id)

# 	employee = Employees.objects.all().filter(user=user_id)[0]
# 	manager_id = employee.manager_id
# 	print('manager_id: ', manager_id)
	
# 	formlist = ['startdate','enddate','daycount','notes']


# 	if request.method == 'POST':
# 		for field in formlist:
# 			if field not in request.POST:
# 				return HttpResponse('The form you entered is invalid. Please fill all the required fields.')

# 		row['employee_id'] = employee
# 		row['start_date']  =request.POST['startdate']
# 		row['end_date'] = request.POST['enddate']
# 		row['number_of_days'] = request.POST['daycount']
# 		row['Notes'] = request.POST['notes']
# 		row['manager_id'] = manager_id


# 	if str(request.user.username) != str(username):
# 		return render(request,'hrapp/404.html')

# 	return redirect('timerequest',username=username)

# @login_required()
# def timelog(request,username):
# 	user = _search_user(request,username)
	
# 	if str(request.user.username) != str(username):
# 		return render(request,'hrapp/404.html')
	
# 	user_id = request.user
# 	employee_id = Employees.objects.all().filter(user=user_id)[0]
# 	timerequests = timerequests.objects.all().filter(employee_id=employee_id)
# 	return render(request,'hrapp/timerequests.html',{'user':user,'timerequests':timerequests})