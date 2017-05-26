# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    CODE_CHOICES = (('CC','Cedula de ciudadanía'), ("CE", "Cedula de Extranjería"), ("NIT", "NIT"), ("Pst", "Pasaporte"), ("CD", "Carnet Dipomático"))
    GENDER_CHOICES = (('M','Masculino'), ('F','Femenino'), ('O','LGTBI'))
    ROLE_OPTIONS = (("Work", "Trabajador"), ("Aux", "Auxiliar"))
    CITY_OPTIONS = (("Pei","Pereira"),("Ddas","Dosquebradas"))
    #SERVICE_OPTIONS =  (('CE','Cerrajería'), ("PLO", "Plomería"), ("CAR", "Carpintería"), ("ELEC", "Electricidad"), ("JAR", "Jardinería"), ("PIN", "Pintura"), ("PLA", "Plagas"), ("TECHO", "Techos"), ("PAREDES", "Paredes y Pisos"))

    user = models.OneToOneField(User, verbose_name="Usuario")
    document_type = models.CharField(max_length=20, choices = CODE_CHOICES, default='CC', verbose_name="Tipo de documento", blank=False, null=False)
    document_number = models.CharField(max_length = 30, verbose_name="Número de Identificación", blank=False, null=False)
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES, default='M', verbose_name="Género", blank=False, null=False)
    phone = models.CharField(max_length=30, verbose_name="Teléfono", blank=False, null=False)
    address = models.CharField(max_length=30, verbose_name="Dirección", blank=False, null=False)
    city = models.CharField(max_length=15, choices = CITY_OPTIONS, default='Pei', verbose_name="Ciudad", blank=False, null=False)

    availability_monday = models.BooleanField(verbose_name="Disponibilidad lunes", default=False)
    availability_tuesday = models.BooleanField(verbose_name="Disponibilidad martes",default=False)
    availability_wednesday = models.BooleanField(verbose_name="Disponibilidad miércoles",default=False)
    availability_thursday = models.BooleanField(verbose_name="Disponibilidad jueves",default=False)
    availability_friday = models.BooleanField(verbose_name="Disponibilidad viernes",default=False)
    availability_saturday = models.BooleanField(verbose_name="Disponibilidad sabado",default=False)
    availability_sunday = models.BooleanField(verbose_name="Disponibilidad domingo",default=False)
    certified = models.BooleanField(verbose_name="Certificado",default=False)
    service_ce = models.BooleanField(verbose_name="Cerrajería",default=False)
    service_plo = models.BooleanField(verbose_name="Plomería",default=False)
    service_car = models.BooleanField(verbose_name="Carpintería",default=False)
    service_elec = models.BooleanField(verbose_name="Electricidad",default=False)
    service_jar = models.BooleanField(verbose_name="Jardinería",default=False)
    service_pin = models.BooleanField(verbose_name="Pintura",default=False)
    service_pla = models.BooleanField(verbose_name="Plagas",default=False)
    service_techo = models.BooleanField(verbose_name="Techos",default=False)
    service_par = models.BooleanField(verbose_name="Paredes y Pisos",default=False)

    #service = models.CharField(max_length=15, choices = SERVICE_OPTIONS, default='CE', verbose_name="Servicio", blank=False, null=False)
    role = models.CharField(max_length=15, choices = ROLE_OPTIONS, default='Work', verbose_name="Cargo", blank=False, null=False)

    #is_active = models.BooleanField(default=False, blank=False)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return "%s"%(self.user)

class Profile_user(models.Model):
    CODE_CHOICES = (('CC','Cedula de ciudadanía'), ("CE", "Cedula de Extranjería"), ("NIT", "NIT"), ("Pst", "Pasaporte"), ("CD", "Carnet Dipomático"))
    GENDER_CHOICES = (('M','Masculino'), ('F','Femenino'), ('O','LGTBI'))
    ROLE_OPTIONS_U = (("Work", "Trabajador"), ("User", "Usuario"))
    PAYMENT_OPTIONS = (("Efe","Efectivo"),("Tcred","Tarjeta de crédito o débito"))
    CITY_OPTIONS = (("Pei","Pereira"),("Ddas","Dosquebradas"))

    user = models.OneToOneField(User, verbose_name="Usuario")
    document_type = models.CharField(max_length=20, choices = CODE_CHOICES, default='CC', verbose_name="Tipo de documento", blank=False, null=False)
    document_number = models.CharField(max_length = 30, verbose_name="Número de Identificación", blank=False, null=False)
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES, default='M', verbose_name="Género", blank=False, null=False)
    phone = models.CharField(max_length=30, verbose_name="Teléfono", blank=False, null=False)
    payment = models.CharField(max_length=15, choices = PAYMENT_OPTIONS, default='Efe', verbose_name="Pago", blank=False, null=False)
    address = models.CharField(max_length=30, verbose_name="Dirección", blank=True, null=False)
    city = models.CharField(max_length=15, choices = CITY_OPTIONS, default='Pei', verbose_name="Ciudad", blank=False, null=False)
    role = models.CharField(max_length=15, choices = ROLE_OPTIONS_U, default='User', verbose_name="Cargo", blank=False, null=False)
    #is_active = models.BooleanField(default=False, blank=False)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return "%s"%(self.user)