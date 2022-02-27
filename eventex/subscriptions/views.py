from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscritionForm


def subscribe(request):
    if request.method == "POST":
        return create(request)
    else:
        return new(request)

def create(request):
    form = SubscritionForm(request.POST)

    if not form.is_valid():
        context = {'form': form}
        return render(request, 'subscriptions/subscription_form.html', context)

    #Send email
    form.full_clean()
    _send_email('Confirmação de inscrição',
                settings.DEFAULT_FROM_EMAIL,
                form.cleaned_data['email'],
                'subscriptions/subscription_email.txt',
                form.cleaned_data)

    #Success feedback
    messages.success(request, 'Inscrição realizada com sucesso!')

    return HttpResponseRedirect('/inscricao/')

def new(request):
    context = {'form': SubscritionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)

def _send_email(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])