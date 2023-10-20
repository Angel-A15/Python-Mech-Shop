from django.conf import settings
from django.db import models
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('W', 'Wrench'),
    ('B', 'Bolts'),
    ('BR', 'Brakes')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


    # List and link items to other classes
class Item(models.Model):
    title=models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES,  max_length=2)
    label = models.CharField(choices=CATEGORY_CHOICES, max_length=2) 
    slug= models.SlugField()

    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })
 
    # Pass items into order processing
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    def _str_(self):
        return self.title
    
    # Identify product was ordered
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def _str_(self):
        return self.user.username