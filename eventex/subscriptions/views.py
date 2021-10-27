from django.shortcuts import render
from eventex.subscriptions.forms import SubscritionForm

def subscribe (request):
        context = {'form': SubscritionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)