from django.shortcuts import render,HttpResponse
from .models import Contact
# Create your views here.
def index(request):
    data=Contact.objects.all()
    main_data={
    'data':data
    }
    print(main_data)
    #print(main_data)
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        description=request.POST.get('description')
        amount=request.POST.get('amount')
        contact.name=name
        contact.amount=amount
        contact.description=description
        contact.save()
      
   # print(data.name)
       
        return render(request,'index.html',main_data)
        #return HttpResponse("<h1>Thanks for contact us</h1>")
        
    return render(request,'index.html',main_data)