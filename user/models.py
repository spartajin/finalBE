import random
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

class UserManager(BaseUserManager):
    def create_user(self, username, password):
        user = self.model(
            username=username,
            password=password,
            nickname=f"{username}!#%@$@!@$)!_{random.randint(1000000, 9999999)}!$!@$",
            email=f"{username}!#%@$@!@$)!_{random.randint(1000000, 9999999)}!$!@$@admin.com",
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)

        return True

# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField("계정", max_length=30, unique=True)
    password = models.CharField("비밀번호", max_length=255)
    email = models.EmailField("이메일", unique=True)
    fullname = models.CharField("이름", max_length=20)
    nickname = models.CharField("닉네임", max_length=20, unique=True)
    birthday = models.DateField("생일",null=True, blank=True)
    join_date = models.DateTimeField("가입일", auto_now_add=True)
    is_admin = models.BooleanField("운영자 여부", default=True)
    is_active = models.BooleanField("계정 활성화 여부", default=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS =[]

    #user관련 명령어를 할때 아래 함수를 따른다는 뜻
    objects = UserManager()


    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, perm, obj=None):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin