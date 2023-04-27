from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import re
from datetime import datetime
from django.db import models
# Create your models here.

class AuthGroup(models.Model):
	name = models.CharField(unique=True, max_length=80)

	class Meta:
		managed = False
		db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
	group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
	permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

	class Meta:
		managed = False
		db_table = 'auth_group_permissions'
		unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
	name = models.CharField(max_length=255)
	content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
	codename = models.CharField(max_length=100)

	class Meta:
		managed = False
		db_table = 'auth_permission'
		unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
	password = models.CharField(max_length=128)
	last_login = models.DateTimeField(blank=True, null=True)
	is_superuser = models.IntegerField()
	username = models.CharField(unique=True, max_length=150)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=150)
	email = models.CharField(max_length=254)
	is_staff = models.IntegerField()
	is_active = models.IntegerField()
	date_joined = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'auth_user'


class AuthUserGroups(models.Model):
	user = models.ForeignKey(AuthUser, models.DO_NOTHING)
	group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

	class Meta:
		managed = False
		db_table = 'auth_user_groups'
		unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
	user = models.ForeignKey(AuthUser, models.DO_NOTHING)
	permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

	class Meta:
		managed = False
		db_table = 'auth_user_user_permissions'
		unique_together = (('user', 'permission'),)

class DjangoContentType(models.Model):
	app_label = models.CharField(max_length=100)
	model = models.CharField(max_length=100)

	class Meta:
		managed = False
		db_table = 'django_content_type'
		unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
	app = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	applied = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'django_migrations'


class DjangoSession(models.Model):
	session_key = models.CharField(primary_key=True, max_length=40)
	session_data = models.TextField()
	expire_date = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'django_session'

######################################## Non Admin Models Start Here ###################

class Vehicle(models.Model):
	vid = models.AutoField(primary_key=True)
	licensePlate = models.CharField(max_length=20,null=True)
	plateType = models.CharField(max_length=40,null=True)#gov't, private, taxi..etc
	vColor = models.CharField(max_length=20,null=True)
	vYear = models.CharField(max_length=20,null=True)
	vBrand = models.CharField(max_length=20,null=True)
	vRegistration = models.CharField(max_length=20,null=True)
	deviceNo = models.CharField(max_length=20,null=True)
	simNo = models.CharField(max_length=20,null=True)
	first_name = models.CharField(max_length=20,null=True)
	last_name = models.CharField(max_length=20,null=True)
	phoneNum = models.CharField(max_length=20,null=True)
	installationDate = models.DateField(null=True)
	installedby = models.ForeignKey(User, models.DO_NOTHING,null=True,blank=True,related_name='installedby')
	enteredBy = models.ForeignKey(User, models.DO_NOTHING,null=True,blank=True,related_name='enteredBy')

	class Meta:
		managed=True
		db_table = 'Vehicle'

class Employee(models.Model):
	user = models.OneToOneField(User,on_delete=models.DO_NOTHING,default=None)
	eid = models.AutoField(primary_key=True)
	employeeNumber = models.IntegerField(null=True)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	startDate = models.CharField(max_length=20)
	endDate = models.CharField(max_length=20)

	class Meta:
		managed=True
		db_table = 'Employee'

class Driver(models.Model):
	did = models.AutoField(primary_key=True)
	user = models.OneToOneField(User,on_delete=models.DO_NOTHING,default=None)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	class Meta:
		managed:True
		db_table = 'Driver'





