from django.db import models

Y_N_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

class ShoppingList(models.Model):
    item = models.CharField(max_length=100, verbose_name = 'Item')
    bought = models.CharField(max_length=10, choices=Y_N_CHOICES,default='N')

    def got_it(self):
      if self.bought == 'Y':
          return True
      else:
          return False
    got_it.boolean = True    
    class Meta:
        verbose_name = "Shopping List"
