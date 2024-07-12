from django.views.generic.base import TemplateView
from .models import Personal, About, Experience, Description, Education, Technology, Portfolio
from .forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from operator import attrgetter
from django.db.models import Q
from django.http import JsonResponse

class HomePageView(TemplateView):
    template_name = 'portfolio/portfolio_main.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personal'] = Personal.objects.all()
        context['about'] = About.objects.all()
        context['technologies'] = Technology.objects.all()
        context['portfolio'] = Portfolio.objects.all()
        context['contact_form'] = ContactForm()
        context['message_sent'] = False
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            your_email = form.cleaned_data['your_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            email_body = f"Name: {your_name}\nEmail: {your_email}\nSubject: {subject}\n\n{message}"
            #print(email_body)

            # Your email sending logic here
            send_mail(
                subject,
                email_body,
                your_email,
                ['rubico.adrian@gmail.com'],
                fail_silently=False,
            )
            # Set message_sent to True
            message_sent = True

            return JsonResponse({'status': 'success', 'message_sent': message_sent})
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({'status': 'error', 'errors': errors})

class DigitalCVPageView(TemplateView):
    template_name = 'portfolio/digital_cv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        experiences = Experience.objects.all()

        for experience in experiences:
            descriptions = Description.objects.filter(experience=experience).order_by('order_number')
            experience.descriptions.set(descriptions)

        context['experiences'] = experiences
        context['personal'] = Personal.objects.all()
        context['education'] = Education.objects.all()
        context['technologies'] = Technology.objects.all()
        context['portfolio'] = Portfolio.objects.filter(
            Q(filter='filter-certification')
        )
        
        grouped_portfolio = {}
        portfolios = sorted(context['portfolio'], key=attrgetter('year'), reverse=True) 
        for item in portfolios:
            issuer_name = item.issuer.name if item.issuer else "Unknown Issuer"
            if issuer_name not in grouped_portfolio:
                grouped_portfolio[issuer_name] = []
            grouped_portfolio[issuer_name].append(item)

        context['grouped_portfolio'] = grouped_portfolio

        return context
    
    
def handle_not_found(request, exception):
    return render(request, "layouts/page-404.html")
    