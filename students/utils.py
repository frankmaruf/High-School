from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

class DetailObjectMixin:
    mode = None
    template = None
    def get(self,request,birth_certificate):
        #obj = self.mode.object.get(birth_certificate__iexact=birth_certificate)
        obj = get_object_or_404(self.model,birth_certificate__iexact=birth_certificate)
        return render(request,self.template,context={self.model.__name__.lower():obj})