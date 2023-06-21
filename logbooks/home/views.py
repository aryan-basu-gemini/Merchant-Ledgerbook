from django.shortcuts import render,redirect
from .models import Contact

 
# Create your views here.
def index(request):
    data=Contact.objects.all()
    main_data={
    'data':data
    }
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        description=request.POST.get('description')
        amount=request.POST.get('amount')
        phone=request.POST.get('phone')
        print(type(phone))
        print(type(name))
        primary=name+phone
        #if name==""or amount=="" or description=="":

        
        contact.name=name
        contact.amount=amount
        contact.primary=primary
        total=int(amount)
        for k in data:
            total+=k.amount
        print(total)
        contact.description=description
        contact.total=total
        contact.phone=phone
        contact.save()

        return redirect('table')

   
    return render(request,'index.html',{'data':data})

def settle(request,id):
    mymember = Contact.objects.get(id=id)
    context = {
    'mymember': mymember,
     }
    if request.method == "POST":
        amount=request.POST.get('amount')
      
        x=int(0 if amount is None else amount)
      
        
        mymember.amount-=x
        if mymember.amount<=0:
            mymember.delete()
        else:
            mymember.save()
        return redirect('home')
    return render(request,'settle.html',context)

def table(request):
    data=Contact.objects.all()
    return render(request,'table.html',{'data':data})
def script(request,id):
     mymember = Contact.objects.get(id=id)
     mymember.delete()
     return  redirect('table')

