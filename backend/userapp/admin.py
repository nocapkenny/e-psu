from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from userapp.models import CustomUser, TeacherProfile, StudentProfile
from userapp.forms import CustomUserCreationForm, CustomUserChangeForm


class TeacherProfileInline(admin.StackedInline):
    model = TeacherProfile
    can_delete = False
    verbose_name_plural = 'Учительский профиль'
    extra = 0

class StudentProfileInline(admin.StackedInline):
    model = StudentProfile
    can_delete = False
    verbose_name_plural = 'Студенческий профиль'
    extra = 0


class CustomUserAdmin(BaseUserAdmin):  
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    inlines = (TeacherProfileInline, StudentProfileInline)

    list_display = ('mail', 'last_name', 'first_name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'role')

    fieldsets = (
        (None, {'fields': ('mail', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'middle_name', 'photo', 'role')}),
        ('Права', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mail', 'first_name', 'last_name', 'role', 'password1', 'password2')}
         ),
    )

    search_fields = ('mail', 'first_name', 'last_name')
    ordering = ('mail',)
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(CustomUser, CustomUserAdmin)
