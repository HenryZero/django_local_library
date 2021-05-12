from django.db import models
from django.contrib import admin

# Create your models here.
class Accountdb(models.Model):
    day = models.CharField(max_length = 20) # 日子
    time = models.CharField(max_length = 20) # 何時
    port = models.CharField(max_length = 10,default="") # 何時
    username = models.CharField(max_length = 30) # 帳號
    password = models.CharField(max_length = 30) # 密碼
    website = models.CharField(max_length = 1000) # 地址

    # 覆寫 __str__
    def __str__(self):
        return self.username

@admin.register(Accountdb)
class AccountdbAdmin(admin.ModelAdmin):
    #list_display = [field.name for field in Accountdb._meta.fields]
    list_display = ( 'day','time','port','username','password','website')
    list_filter = ('day','port')
    search_fields = ('day', 'port','username','website')
    ordering = ('day',)