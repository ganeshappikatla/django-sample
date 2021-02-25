from django.shortcuts import render
from .models import destinations
# Create your views here.

def index(request):
      
    dest1= destinations()
    dest1.name='mumbai'
    dest1.price=700
    dest1.img='destination_4.jpg.'
    
    dest2= destinations()
    dest2.name= 'mumbai'
    dest2.price=700
    dest2.img='destination_5.jpg.'
    
    dest3= destinations()
    dest3.name= 'mumbai'
    dest3.price=700
    dest3.img= 'destination_1.jpg.'



    dests=[dest1, dest2, dest3]

    return render(request, "index.html",{'dests':dests})
