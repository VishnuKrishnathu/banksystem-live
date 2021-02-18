from django.shortcuts import render
from django.http import HttpResponse
import pymongo

# Create your views here.
def home(request):
    return render(request, "home.html")

def customers(request):
    '''
    client = pymongo.MongoClient("mongodb+srv://vishnu:YHwvgPjn7XfDLxJL@cluster0.ragko.mongodb.net/mycustomers?retryWrites=true&w=majority")
    db = client["mycustomers"]
    collection = db["customers_data"]
    '''
    data = collection.find()
    return render(request, "customers.html", {'datas': data})
    #return render(request, "customers.html")


def customer_data(request, first_name):
    if request.POST:
        return render(request, "paymentdone.html",{'data': data})
    else:
        data = collection.find({"first_name":first_name})
        return render(request, "details.html",{'data': data })

def paymentdone(request, first_name):
    try:
        amount = int(request.POST["amount"])
    except:
        amount = 0
    data = collection.find({"first_name":first_name})
    if(amount > 50):
        collection.update({'first_name': first_name}, {'$inc':{'account_balance': amount}})
        return render(request, "paymentdone.html")
    else:
        error = True
        return render(request, "details.html",{'data': data , 'error': error})



client = pymongo.MongoClient("mongodb+srv://vishnu:YHwvgPjn7XfDLxJL@cluster0.ragko.mongodb.net/mycustomers?retryWrites=true&w=majority")
db = client["mycustomers"]
collection = db["customers_data"]