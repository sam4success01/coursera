from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from formtools.wizard.views import SessionWizardView
from .forms import GuestDetailForm, BusinessDetailForm, BookingDetailForm
from .models import Business, Booking, Guest



# Create your views here.

def show_business_form(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    return cleaned_data.get('is_business_guest')

class BookingWizardView(SessionWizardView):
    form_list = [GuestDetailForm, BusinessDetailForm, BookingDetailForm]
    template_name = 'index.html'
    condition_dict = {"1":show_business_form}
    
    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]

        # Initialize variables for instances
        guest = None
        business = None
        booking = None

        # Save Guest instance
        if len(form_list) > 0:
            guest_form = form_list[0]
            guest = guest_form.save()

        # Save Business instance if the form was displayed
        if show_business_form(self) and len(form_list) > 1:
            business_form = form_list[1]
            business = business_form.save()
            guest.business = business
            guest.save()  # Update Guest after adding Business

        # Save Booking instance
        if len(form_list) > 2:
            booking_form = form_list[2]
            booking = booking_form.save(commit=False)
            booking.guest = guest
            booking.save()

        messages.success(self.request, "File Submitted Successfully")
        return render(self.request, 'base.html')