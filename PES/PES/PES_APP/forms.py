#!/usr/bin/env python 
# -*- coding: utf-8 -*
from django import forms
from models import Profile_user,Profile


CODE_CHOICES = (('TI','Tarjeta de identidad'), ('CC','Cedula de ciudadanía'), ("CE", "Cedula de Extranjería"), ("NIT", "NIT"), ("Pst", "Pasaporte"), ("CD", "Carnet Dipomático"))
GENDER_CHOICES = (('M','Masculino'),('F','Femenino'),('LGTBI','LGTBI'))

ROLE_OPTIONS = (("Work", "Trabajador"), ("Aux", "Auxiliar"))
ROLE_OPTIONS_U = (("Work", "Trabajador"), ("User", "Usuario"))
PAYMENT_OPTIONS = (("Efe","Efectivo"),("Tcred","Tarjeta de crédito o débito"))
CITY_OPTIONS = (("Pei","Pereira"),("Ddas","Dosquebradas"))

class addPerfilForms(forms.Form):
    
    #user = models.OneToOneField(User, verbose_name="Usuario")
    username = forms.CharField(required=True, label="Nombre de usuario", widget=forms.TextInput(attrs={"title": "Nombre de usuario"}))
    document_type = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=CODE_CHOICES)
    document_number = forms.CharField(required=True, label="Número de documento", widget=forms.TextInput(attrs={"size": 30, "title": "Número de documento"}))    
    first_name = forms.CharField(required=True, label="Nombres", widget=forms.TextInput(attrs={"size": 20, "title": "Nombres"}))
    last_name = forms.CharField(required=True, label="Apellidos", widget=forms.TextInput(attrs={"size": 20, "title": "Apellidos"}))
    password = forms.CharField(required=True, label="Contraseña", widget=forms.PasswordInput())
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=GENDER_CHOICES)
    email = forms.EmailField(required=True, label="Email", widget=forms.TextInput())
    phone = forms.CharField(required=True, label="Número de teléfono", widget=forms.TextInput(attrs={"size": 30, "title": "Número de teléfono"}))

    address = forms.CharField(required=False, label="Número de teléfono", widget=forms.TextInput(attrs={"size": 30, "title": "Número de teléfono"}))
    city = forms.ChoiceField(required=False, widget=forms.RadioSelect, choices=CITY_OPTIONS)
    availability_monday = forms.BooleanField(required=False)
    availability_tuesday = forms.BooleanField(required=False)
    availability_wednesday = forms.BooleanField(required=False)
    availability_thursday = forms.BooleanField(required=False)
    availability_friday = forms.BooleanField(required=False)
    availability_saturday = forms.BooleanField(required=False)
    availability_sunday = forms.BooleanField(required=False)
    certified = forms.BooleanField(required=False)
    service_ce = forms.BooleanField(required=False)
    service_plo = forms.BooleanField(required=False)
    service_car = forms.BooleanField(required=False)
    service_elec = forms.BooleanField(required=False)
    service_jar = forms.BooleanField(required=False)
    service_pin = forms.BooleanField(required=False)
    service_pla = forms.BooleanField(required=False)
    service_techo = forms.BooleanField(required=False)
    service_par = forms.BooleanField(required=False)


    role = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=ROLE_OPTIONS)
    is_active = forms.BooleanField(required=False)

    #birthdate = forms.DateField(required=True, label="Fecha de nacimiento",input_formats=["%Y-%m-%d","%d/%m/%Y","%d/%m/%y"])    
    def clean(self):
    		return self.cleaned_data


class addPerfilUserForms(forms.Form):
    
    #user = models.OneToOneField(User, verbose_name="Usuario")
    username = forms.CharField(required=True, label="Nombre de usuario", widget=forms.TextInput(attrs={"title": "Nombre de usuario"}))
    document_type = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=CODE_CHOICES)
    document_number = forms.CharField(required=True, label="Número de documento", widget=forms.TextInput(attrs={"size": 30, "title": "Número de documento"}))    
    first_name = forms.CharField(required=True, label="Nombres", widget=forms.TextInput(attrs={"size": 20, "title": "Nombres"}))
    last_name = forms.CharField(required=True, label="Apellidos", widget=forms.TextInput(attrs={"size": 20, "title": "Apellidos"}))
    password = forms.CharField(required=True, label="Contraseña", widget=forms.PasswordInput())
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=GENDER_CHOICES)
    email = forms.EmailField(required=True, label="Email", widget=forms.TextInput())
    phone = forms.CharField(required=True, label="Número de teléfono", widget=forms.TextInput(attrs={"size": 30, "title": "Número de teléfono"}))
    
    payment = forms.ChoiceField(required=False, widget=forms.RadioSelect, choices=PAYMENT_OPTIONS)
    address = forms.CharField(required=False, label="Número de teléfono", widget=forms.TextInput(attrs={"size": 30, "title": "Número de teléfono"}))
    city = forms.ChoiceField(required=False, widget=forms.RadioSelect, choices=CITY_OPTIONS)
    role = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=ROLE_OPTIONS_U)
    is_active = forms.BooleanField(required=False)

    #birthdate = forms.DateField(required=True, label="Fecha de nacimiento",input_formats=["%Y-%m-%d","%d/%m/%Y","%d/%m/%y"])    
    def clean(self):
            return self.cleaned_data