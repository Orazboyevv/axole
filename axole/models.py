from django.db import models

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=222)


    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=250)
    image = models.FileField(upload_to='blog/')
    body = models.TextField()
    tag = models.ManyToManyField(Tag, )

    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title



class About(models.Model):
    name = models.CharField(max_length=222)
    image = models.FileField(upload_to='about/')
    discription = models.CharField(max_length=240)
    title = models.CharField(max_length=250)
    body = models.TextField()

    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=250)
    message = models.TextField()

    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.first_name



class Subscription(models.Model):
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.email



class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    message = models.TextField()

    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.full_name


class Contacts(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    massage = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name