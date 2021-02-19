from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tblcommonmasters(models.Model):
    autoid=models.AutoField(primary_key=True)
    title=models.TextField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    isactive=models.IntegerField(blank=True,null=True,default=1)
    image_url=models.ImageField(blank=True,null=True)
    type=models.TextField(blank=True,null=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE,null=True,default="")
    createdon=models.DateTimeField(blank=True,null=True)
    otherfield=models.CharField(blank=True,null=True,max_length=350)
    
    def __str__(self):
        return self.title
    def time_pretty(self):
        return self.time.strftime('%d %e , %Y')



class Tblsubscription(models.Model):
    title=models.TextField(blank=True,null=True,max_length=150)
    price=models.CharField(blank=True,null=True,max_length=150)
    validity=models.IntegerField(blank=True,null=True)
    isactive=models.IntegerField(blank=True,null=True,default=1)
  
    def __str__(self):
        return self.title
    def time_pretty(self):
        return self.time.strftime('%d %e , %Y')



class Tbloptions(models.Model):
    optionid=models.AutoField(primary_key=True)
    title=models.TextField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    image_url=models.ImageField(blank=True,null=True)
    email=models.TextField(blank=True,null=True)
    mobile=models.TextField(blank=True,null=True)
    alternate_phone=models.TextField(blank=True,null=True)
    facebook_link=models.TextField(blank=True,null=True)
    twitter_link=models.TextField(blank=True,null=True)
    instagram_link=models.TextField(blank=True,null=True)
    linkedin_link=models.TextField(blank=True,null=True)
    github_link=models.TextField(blank=True,null=True)
    google_var_id=models.TextField(blank=True,null=True)
    google_ana_script=models.TextField(blank=True,null=True)
    facebook_script=models.TextField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    meta_title=models.TextField(blank=True,null=True)
    meta_keywords=models.TextField(blank=True,null=True)
    meta_description=models.TextField(blank=True,null=True)
    createdon=models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.title
    def time_pretty(self):
        return self.time.strftime('%d %e , %Y')


class Tbluserdetails(models.Model):
    detailid=models.AutoField(primary_key=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE,null=True,default="")
    subscription=models.ForeignKey('Tblsubscription',on_delete=models.CASCADE,null=True)
    purchasedate = models.DateTimeField(blank=True, null=True)
    expiredate = models.DateTimeField(blank=True, null=True)

    orderid=models.TextField(blank=True,null=True)
    paymentid=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.orderid
    def time_pretty(self):
        return self.time.strftime('%d %e , %Y')


class Userpdfs(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE,null=True,default="")
    filename = models.TextField(blank=True,null=True)
    filesize = models.TextField(blank=True,null=True)

    files = models.FileField(null=True,upload_to='documents/')
    createdon=models.DateTimeField(blank=True,null=True,auto_now=True)
    def __str__(self):
        return self.filename
    def time_pretty(self):
        return self.time.strftime('%d %e , %Y')
 