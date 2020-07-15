from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# dispatch -> middleware , akan di eksekusi seblum masuk ke Welcome View
# @method_decorator(login_required,name='dispatch')
class WelcomeView(TemplateView):
    template_name = "index.html"

    # def get(self,request):
    #     return HttpResponse("Halo ini get")
    
    @method_decorator(login_required)
    def post(self,request):
        return HttpResponse('Hello Testing Post')