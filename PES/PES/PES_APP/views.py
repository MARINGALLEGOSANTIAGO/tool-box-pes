# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import os, sys, django
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from PES_APP.forms import addPerfilUserForms, addPerfilForms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from PES_APP.models import Profile, Profile_user
from django.contrib.auth.models import User
from django.db.models import Q

def login_page(request):
	print "login_page"
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('home'))

	data={}
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		print username, password
		user = authenticate(username=username, password=password)
		print user
		if user is not None:
			if user.is_active:
				print(login(request, user))
				data['success']="login correcto"
				print "success",data
				return HttpResponseRedirect(reverse('home'))
			else:
				data['error']="el usuario no esta activo"
				print "error",data
		else:
			data['error']="No es posible acceder a la plataforma, usuario o contraseña incorrectos. Si persiste el error, póngase en contacto con el administrador"
			print "error",data
	return render(request, "login.html", data)

@login_required(login_url='/')
def logout_page(request):
	print "logout"
	logout(request)
	return HttpResponseRedirect(reverse('home'))


#@login_required(login_url='/')
def home(request):
	return render(request, "home.html", {})

def about_view(request):
	return render(request, "about.html", {})


def create_user(request):
	#if request.user.profile.role != "A":
	#	return HttpResponseRedirect('/')
	data = request.POST.dict()
	data.update({"is_active": False})#que es?
	form = addPerfilUserForms(request.POST)
	message_success = None
	message_error = None

	if request.method == "POST":
		if form.is_valid():
			username = form.cleaned_data['username']
			document_type = form.cleaned_data['document_type']
			document_number = form.cleaned_data['document_number']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			password = form.cleaned_data['password']
			gender = form.cleaned_data['gender']
			email = form.cleaned_data['email']

			phone = form.cleaned_data['phone']
			payment = form.cleaned_data['payment']
			address = form.cleaned_data['address']
			city = form.cleaned_data['city']
			role = form.cleaned_data['role']
			is_active = form.cleaned_data['is_active']

			new_user=User(
				username=username,
				first_name=first_name,
				last_name=last_name,
				email=email,
				is_active=is_active
			)

			new_user.save()
			new_user.set_password(password)
			new_user.save()

			new_user_profile=Profile_user(
				user=new_user,
				document_type=document_type,
				document_number=document_number,
				gender=gender,
				phone=phone,
				payment=payment,
				address=address,
				city=city,
				role=role
			)

			new_user_profile.save()

			message_success = ("El usuario ha sido registrado exitosamente.")
		else:
			message_error = form.errors

	return render(request, "create_user.html", {
		"form": form,
		"message_success": message_success,
		"message_error": message_error
	})

def create_user_work(request):
	#if request.user.profile.role != "A":
	#	return HttpResponseRedirect('/')
	data = request.POST.dict()
	data.update({"is_active": False})#que es?
	form = addPerfilForms(request.POST)
	message_success = None
	message_error = None

	if request.method == "POST":
		if form.is_valid():
			username = form.cleaned_data['username']
			document_type = form.cleaned_data['document_type']
			document_number = form.cleaned_data['document_number']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			password = form.cleaned_data['password']
			gender = form.cleaned_data['gender']
			email = form.cleaned_data['email']

			phone = form.cleaned_data['phone']
			address = form.cleaned_data['address']
			city = form.cleaned_data['city']
			availability_monday = form.cleaned_data['availability_monday']
			availability_tuesday = form.cleaned_data['availability_tuesday']
			availability_wednesday = form.cleaned_data['availability_wednesday']
			availability_thursday = form.cleaned_data['availability_thursday']
			availability_friday = form.cleaned_data['availability_friday']
			availability_saturday = form.cleaned_data['availability_saturday']
			availability_sunday = form.cleaned_data['availability_sunday']
			certified = form.cleaned_data['certified']
			service_ce = form.cleaned_data['service_ce']
			service_plo = form.cleaned_data['service_plo']
			service_car = form.cleaned_data['service_car']
			service_elec = form.cleaned_data['service_elec']
			service_jar = form.cleaned_data['service_jar']
			service_pin = form.cleaned_data['service_pin']
			service_pla = form.cleaned_data['service_pla']
			service_techo = form.cleaned_data['service_techo']
			service_par = form.cleaned_data['service_par']
			
			role = form.cleaned_data['role']
			is_active = form.cleaned_data['is_active']

			new_user=User(
				username=username,
				first_name=first_name,
				last_name=last_name,
				email=email,
				is_active=is_active
			)

			new_user.save()
			new_user.set_password(password)
			new_user.save()

			new_user_profile=Profile(
				user=new_user,
				document_type=document_type,
				document_number=document_number,
				gender=gender,
				phone=phone,
				address=address,
				city=city,
				availability_monday=availability_monday,
				availability_tuesday=availability_tuesday,
				availability_wednesday=availability_wednesday,
				availability_thursday=availability_thursday,
				availability_friday=availability_friday,
				availability_saturday=availability_saturday,
				availability_sunday=availability_sunday,
				certified=certified,
				service_ce=service_ce,
				service_plo=service_plo,
				service_car=service_car,
				service_elec=service_elec,
				service_jar=service_jar,
				service_pin=service_pin,
				service_pla=service_pla,
				service_techo=service_techo,
				service_par=service_par,
				role=role
			)

			new_user_profile.save()

			message_success = ("El usuario trabajador ha sido registrado exitosamente.")
		else:
			message_error = form.errors

	return render(request, "create_user_work.html", {
		"form": form,
		"message_success": message_success,
		"message_error": message_error
	})

def home_user(request):
	if request.user.profile_user.role != "User":
		return HttpResponseRedirect('/')

	user_profile = User.objects.filter(is_active=True)

	return render(request, "home_user.html",{})

def home_aux(request):
	if request.user.profile.role != "Aux":
		return HttpResponseRedirect('/')

	user_profile = User.objects.filter(is_active=True)

	return render(request, "home_aux.html",{})

def home_work(request):
	if request.user.profile.role != "Work":
		return HttpResponseRedirect('/')

	user_profile = User.objects.filter(is_active=True)

	return render(request, "home_work.html",{})

def request_service(request):
	user_profile = User.objects.filter(is_active=True)
	if request.POST:
		firstName = request.POST.get("firstName")
		document = request.POST.get("document_number")
		from_email = request.POST.get("email")
		address = request.POST.get("address")
		phone = request.POST.get("phone")
		comment = request.POST.get("comment")
		print firstName
		print document
		print comment
		print phone
		print address
		print from_email
		subject = 'Alguien solicito el servicio de TOOL BOX PES'
		message = ("Hola, Admin!!!, éste usuario solicitó recientemente el servicio TOOL BOX PES.                                                              "
			"Los siguientes son los datos ingresados en el formulario para su respectiva verificacion y contacto para realizar el servicio:"
			"                                                                            "
			"Nombres y apellidos: {}                    Numero de documento: {}                                                Email ingresado: {}                                             Dirección ingresada: {}                   Teléfono ingresado: {}                                           Detalle del servicio, fecha y hora: {}".format(firstName, document, from_email, address, phone, comment))
			
		mail = EmailMessage(subject, message, from_email, ['toolboxpes@gmail.com'])#correo de destino
		mail.send()
		return redirect("request_service_done")
	else:
		return render(request, "request_service.html",{})

def request_service_done(request):
	return render(request, "request_service_done.html",{})

def restore_password(request):
	if request.POST:
		username = request.POST.get("username")
		document = request.POST.get("document_number")
		role = request.POST.get("role")
		from_email = request.POST.get("email")
		print username
		print document
		print role
		print from_email
		subject = 'Alguien solicito reestablecer la contraseña para la cuenta en TOOL BOX PES'
		message = ("Hola, Admin!!!, éste usuario solicitó recientemente reestablecer la contraseña de TOOL BOX PES.                                                              "
			"Los siguientes son los datos ingresados en el formulario para su respectiva verificacion:"
			"                                                                            "
			"Nombre de Usuario ingresado: {}                    Numero de documento ingresado: {}                                                Cargo ingresado: {}                                           Email ingresado: {}".format(username, document, role, from_email))
			
		mail = EmailMessage(subject, message, from_email, ['toolboxpes@gmail.com'])#correo de destino
		mail.send()
		return redirect("restore_password_done")
	else:
		return render(request, "restore_password.html", {})

def restore_password_done(request):
	return render(request, "password_reset_done.html",{})