from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscritionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscritionForm(request.POST)
        if form.is_valid():
            form.full_clean()
            body = render_to_string('subscriptions/subscription_email.txt', form.cleaned_data)
            mail.send_mail('Confirmação de inscrição', body, 'contato@eventex.com.br',
                           ['contato@eventex.com.br', form.cleaned_data['email']])

            messages.success(request, 'Inscrição realizada com sucesso!')

            return HttpResponseRedirect('/inscricao/')
        else:
            context = {'form': form}
            return render(request, 'subscriptions/subscription_form.html', context)
    else:
        context = {'form': SubscritionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)
