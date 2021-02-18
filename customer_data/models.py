from django.db import models 
from django.core.validators import MinValueValidator
import pymongo

# Create your models here.
class CustomerInfo(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 10)
    age = models.IntegerField( validators = [MinValueValidator(1)])
    account_balance = models.IntegerField( validators = [MinValueValidator(7000)])


client = pymongo.MongoClient("mongodb+srv://vishnu:YHwvgPjn7XfDLxJL@cluster0.ragko.mongodb.net/mycustomers?retryWrites=true&w=majority")
db = client["mycustomers"]
collection = db["customers_data"]
data= collection.find()