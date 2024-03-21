from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    is_agent = models.BooleanField(default=False)
    telegram_username = models.CharField(max_length=50, blank=True, null=True)

    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='media/default_profile.jpg', upload_to='media/profiles')

    def __str__(self):
        return f'{self.user.username} Profile'
