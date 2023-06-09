from typing import Any, Dict, Optional, Type
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .forms import (CustomLoginForm, ChangePass,
                    RegistrationForm, UpdateUser,
                    customPasswordResetForm)
from django.contrib.auth.views import LoginView, PasswordResetView
from django.views.generic import FormView, TemplateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from .models import Students, ResultU2018
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from rest_framework.decorators import APIView
# from .serializer import ResultSerializer
# from django.contrib.auth import views as auth_views

# Create your views here.

class SignUp(FormView):
    form_class = RegistrationForm
    success_url = reverse_lazy('dashboard')
    template_name='sign_up.html'

    def form_valid(self, form):
        user_log_in = form.save()
        if user_log_in is not None :
            login(self.request, user_log_in)
        return super(SignUp,self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super(SignUp,self).get(request, *args, **kwargs)

class SignIn(LoginView):
    template_name='sign_in.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('dashboard')
    authentication_form = CustomLoginForm


class UpdateProfile(UpdateView):
    form_class = UpdateUser
    template_name='settings_page.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["passform"] = ChangePass(self.request.user)
        return context


class Index(TemplateView):
    template_name='index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super(Index,self).get(request, *args, **kwargs)
    

class ResultPage(DetailView):
    template_name='result.html'
    model = Students
    year = 0

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.year = kwargs.get('year')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["results"] = ResultU2018.objects.filter(mat_number=self.object.mat_number,year=self.year)
        context["sum_first_sem"] = sum([i.mark for i in context["results"] if i.semester == 1])
        context["sum_second_sem"] = sum([i.mark for i in context["results"] if i.semester == 2])
        context["year"] = self.year
        return context
    
    def get_object(self):
        return self.request.user
    
class Stats(DetailView):
    template_name='stats.html'
    model = Students

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        Result_stats = {"year1":{"sum_mark_1":0,"sum_cu_1":0,"sum_mark_2":0,"sum_cu_2":0,"year":1},
                        "year2":{"sum_mark_1":0,"sum_cu_1":0,"sum_mark_2":0,"sum_cu_2":0,"year":2},
                        "year3":{"sum_mark_1":0,"sum_cu_1":0,"sum_mark_2":0,"sum_cu_2":0,"year":3},
                        "year4":{"sum_mark_1":0,"sum_cu_1":0,"sum_mark_2":0,"sum_cu_2":0,"year":4}}
        result = ResultU2018.objects.filter(mat_number=self.object.mat_number)
        for val in result:
            grade_mark = 0
            match val.grade:
                case "A":
                    grade_mark = 5
                case "B":
                    grade_mark = 4
                case "C":
                    grade_mark = 3
                case "D":
                    grade_mark = 2
                case "E":
                    grade_mark = 1
                case "F":
                    continue
                case _:
                    pass

            Result_stats[f"year{val.year}"][f"sum_mark_{val.semester}"] += grade_mark * val.credit_unit
            Result_stats[f"year{val.year}"][f"sum_cu_{val.semester}"] += val.credit_unit
        context["stats"]= []
        context["stats"].append(Result_stats["year1"])
        context["stats"].append(Result_stats["year2"])
        context["stats"].append(Result_stats["year3"])
        context["stats"].append(Result_stats["year4"])
        return context
    
    def get_object(self):
        return self.request.user
    
# class ResultApi(APIView):
#     def get(self, request):
#         users = Students.objects.all()
#         res = ResultSerializer(users, many=True)
#         return Response(res.data)

class resetPassword(PasswordResetView):
    template_name="forgot-password.html"
    success_url = reverse_lazy("password_reset_done")
    form_class = customPasswordResetForm


    
def mail(request):
        if request.method == "POST":
            data = request.POST
            # send_mail(data["subject"],data["message"],
            # settings.EMAIL_HOST_USER,
            # ['ebufinbar10@gmail.com'],fail_silently=False)
            return JsonResponse({"subject":data["subject"]})
        return render(request,"contact.html",)

# def update_record(request):
#     results = ResultU2018.objects.get(student_mat=None,result_matno="U2018/6005076",course_code="ECO 101.1")
#     users = Students.objects.get(mat_number="U2018/6005076")
#     results.student_mat = users
#     results.save()

#     results = ResultU2018.objects.filter(student_mat=None)
#     if results:
#         for res in results:
#             users = Students.objects.filter(mat_number=res.result_matno)
#             for usr in users:
#                 res.student_mat = usr
#                 res.save()
#         return JsonResponse({"Work":"Done"})
#     return JsonResponse({"Work":"Nothing"})

#     users = Students.objects.all()
#     if users:
#         for usr in users:
#             results = ResultU2018.objects.filter(result_matno=usr.mat_number)
#             if results:
#                 for res in results:
#                     res.student_mat = usr
#                     res.save()
#         return JsonResponse({"Work":"Done"})
#     return JsonResponse({"Work":"Nothing"})


# @api_view(['GET'])
# def apiAllLinks(request):
#     users = Students.objects.all()
#     res = ResultSerializer(users, many=True)
#     return Response(res.data)

