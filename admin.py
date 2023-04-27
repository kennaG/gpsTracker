from django.contrib import admin
from . models import Vehicle,Driver,Employee
# Register your models here.
#admin.site.register(Employees)

# @admin.register(timerequests)
# class TimerequestsAdmin(admin.ModelAdmin):
# 	list_display = ('employee_id','manager_id','start_date','end_date','number_of_days','Notes','approved','session_date')
# 	list_filter = ('employee_id',)
# 	fields = ['employee_id','manager_id','start_date','end_date','number_of_days','Notes','approved','time_off_choice','session_date'] #changed monitor_name to monitor here
# 	inlines = [timerequests]

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
	list_display = ('licensePlate','plateType','vColor','vYear','vBrand','vRegistration',
'deviceNo','simNo','first_name','last_name','phoneNum','installationDate','installedby','enteredBy')
	fields = (('licensePlate',('plateType','vColor','vYear'),('vBrand','vRegistration'), ('deviceNo','simNo'),('first_name','last_name','phoneNum'),('installationDate','installedby'),'enteredBy'))

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('user','employeeNumber','first_name','last_name','startDate',
'endDate')
	fields = ('user',('employeeNumber','first_name','last_name'),('startDate',
'endDate'))

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
	list_display = ()
	fields = ('user',('first_name','last_name'))