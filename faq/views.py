from django.shortcuts import render, get_object_or_404
from .models import GeneralQuestion, PaymentQuestion, UpgradeQuestion


# Create your views here.

def faq(request):
    Gen_Questions    =   GeneralQuestion.objects.all()
    Pay_Questions    =   PaymentQuestion.objects.all()
    Upg_Questions    =   UpgradeQuestion.objects.all()


    context =   {
        'Gen_Questions': Gen_Questions,
        'Pay_Questions' :   Pay_Questions,
        'Upg_Questions' :   Upg_Questions,
    }
    return render(request, 'pages/faq.html', context)
