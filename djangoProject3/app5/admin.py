from django.contrib import admin

# Register your models here.
from app5.models import Test

admin.site.register(Test)

from app5.models import qna

admin.site.register(qna)