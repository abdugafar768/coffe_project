from django.contrib import admin
from .models import *

admin.site.register([CustomerUser,Category,Product,Order])
# Register your models here.
