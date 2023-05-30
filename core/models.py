from django.db import models

class Company(models.Model):
    company_name = models.TextField(max_length=200, null=False)

class User(models.Model):
    username = models.EmailField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class PermissionGroup(models.Model):
    
    _C = 'C'
    _R = 'R'
    _U = 'U'
    _D = 'D'
    
    access_levels=[
    (_C, 'ADD'),
    (_R, 'READ'),
    (_U, 'EDIT'),
    (_D, 'DELETE'),]
    
    group_name = models.TextField(max_length=200, null=False)
    permission_description = models.TextField(max_length=200)
    resource_name = models.TextField(max_length=200)
    access_level = models.CharField(max_length=6, choices=access_levels, default=_R)
    username = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    company_name = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.permission_description}'


