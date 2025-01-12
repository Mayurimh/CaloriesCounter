from django.db import models
from django.contrib.auth.models import User    
    
class FoodItems(models.Model):
    name = models.CharField(max_length=200)
    calorie=models.DecimalField(max_digits=5,decimal_places=2,default=0,blank=True)
    carbohydrate = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    fats = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    protein = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    # quantity = models.IntegerField(default=1,null=True,blank=True)
    
    def __str__(self):
        return str(self.name)
    class Meta:
        db_table="fooditems"
        
class consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(FoodItems, on_delete=models.CASCADE)
     
    class Meta:
        db_table="calories_consume"

# class UserFooditem(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     food_item = models.ForeignKey(FoodItems, on_delete=models.CASCADE)
#     # date = models.DateField()
#     quantity = models.FloatField()
  

#     def __str__(self):
#         return f"{self.user.username} - {self.food_item.name}"
#         # return f"{self.user.username} - {self.food_item.name} - {self.date}"


