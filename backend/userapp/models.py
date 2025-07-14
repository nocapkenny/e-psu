from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 


class CustomUserManager(BaseUserManager):
    
    
    def create_user(self, mail, first_name, password = None, **extra_fields):
        if not mail:
            raise ValueError('Введите mail !')
        
        user = self.model(
            mail=self.normalize_email(mail),
            first_name=first_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, mail, first_name, password=None, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'Admin')
        
        return self.create_user(mail, first_name, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    ROLE_CHOICES = [
        ('Student', 'Ученик'),
        ('Admin', 'Админ'),
        ('Teacher', 'Учитель')
    ]
    
    
    mail = models.EmailField(unique = True)
    first_name = models.CharField(max_length = 50, null=True, blank=True,verbose_name="Имя")
    last_name = models.CharField(max_length = 50, null=True, blank=True,verbose_name="Фамилия")
    middle_name = models.CharField(max_length = 50, null=True, blank=True,verbose_name="Отчество")
    photo = models.ImageField(upload_to='avatars/', null = True, blank = True, verbose_name="Фотография")
    role = models.CharField(max_length = 20, choices = ROLE_CHOICES, default = 'Student', verbose_name="Роль")
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    REQUIRED_FIELDS = ['first_name']
    USERNAME_FIELD = 'mail'
    
    
    def __str__(self):
        return f'{self.last_name} {self.first_name}'
    
    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
    
    class Meta:
        verbose_name = ('Пользователь')  
        verbose_name_plural = ('Пользователи')  
    
        
class TeacherProfile(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    work_experience = models.IntegerField(default=0)
    awards = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'
    

            
class StudentProfile(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    parents_contacts = models.TextField()
    enrollment_date = models.DateField()
    
    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'
    