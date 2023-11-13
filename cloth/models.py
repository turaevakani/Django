from django.db import models

class CustomerCL(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name
class TagCL(models.Model):
    name = models.CharField(max_length=100, verbose_name='Add hashtag')

    def __str__(self):
        return f'#{self.name}'

class ProductCL(models.Model):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Kids', 'Kids'),
        ('Uni', 'Uni'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True) #optional
    image = models.ImageField(upload_to='')
    sex = models.CharField(max_length=100, choices=SEX, default=SEX[0], null=True)
    size = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    tag = models.ManyToManyField(TagCL, related_name='content_name')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.created_at}'

class OrderCL(models.Model):
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductCL)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} by {self.customer.name}'
