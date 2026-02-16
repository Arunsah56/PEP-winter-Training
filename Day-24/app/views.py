from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data["email"]
            name = form.cleaned_data["name"]

            # Send auto greeting email
            send_mail(
                subject="Thanks for contacting us!",
                message=f"Hi {name},\n\nThank you for reaching out. We will get back to you soon 😊",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user_email],
            )

            return render(request, "contact_success.html")

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
