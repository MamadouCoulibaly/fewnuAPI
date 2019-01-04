from django.db import models
from django.conf import settings

# Create your models here.


#class BlogUser(models.Model):
    #userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #usernames = models.CharField(max_length=20, null=True, blank=True)
    #password = models.CharField(max_length=15)
    #title = models.CharField(max_length=200, null=True, blank=True)
    #content = models.CharField(max_length=20, null=True, blank=True)
   # timestamp = models.DateTimeField(auto_now_add=True)
    #telephone = models.IntegerField()
    

    #def __str__(self):
       # return str(self.userid.username)


class Users(models.Model):
	nom = models.CharField(max_length=30)
	numero = models.CharField(primary_key=True,max_length=20)
	date=models.DateTimeField(auto_now_add=True)
    
  


class Ventes(models.Model):
    designation= models.CharField(max_length=30)
    prix= models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)


class Depenses(models.Model):
    designation= models.CharField(max_length=30)
    prix= models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)

class Prets(models.Model):
    nomclient= models.CharField(max_length=30)
    libelle=models.CharField(max_length=30)
    montant= models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)

class HistoriquePrets(models.Model):
    prets_id=models.ForeignKey(Prets,on_delete=models.CASCADE)

