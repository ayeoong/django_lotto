from django.contrib import admin

# from lotto.models import GuessNumbers
from .models import GuessNumbers  # 동일한 폴더에 있으면 폴더명 생략 가능

# Register your models here.
admin.site.register(GuessNumbers)
