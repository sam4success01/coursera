from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, MainAttendance, YorubaAttendance, ChildrenAttendance, TeenagersAttendance, OnlineAttendance, Offering
from .models import Record, UsheringData
import csv, io
from django.http import HttpResponse
from io import TextIOWrapper
from datetime import datetime
from django.template.loader import render_to_string
from weasyprint import HTML
import pandas as pd
from io import BytesIO
from django.utils.timezone import now
from reportlab.pdfgen import canvas


from formtools.wizard.views import SessionWizardView

# Create your views here.

def home(request):
    records = Record.objects.all()
    return render(request, 'home.html', {'records':records})

def report(request):
    records = Record.objects.all()
    if request.user.is_authenticated:
        return render(request, 'report.html', {'records':records})
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')

def reports(request):
    if request.user.is_authenticated:
        return render(request, 'reports.html')
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')

def attendance(request):
    if request.user.is_authenticated:
        return render(request, 'attendance.html')
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')


def show_yoruba_attendance_form(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('main_attendance') or {}
    return not cleaned_data.get('skip_yoruba_attendance', False)

def show_children_attendance_form(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('main_attendance') or {}
    return not cleaned_data.get('skip_children_attendance', False)

def show_teenagers_attendance_form(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('main_attendance') or {}
    return not cleaned_data.get('skip_teenagers_attendance', False)

def show_online_attendance_form(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('main_attendance') or {}
    return not cleaned_data.get('skip_online_attendance', False)

class MainAttendanceWizard(SessionWizardView):
    form_list = [
        ('main_attendance', MainAttendance),
        ('yoruba_attendance', YorubaAttendance),
        ('children_attendance', ChildrenAttendance),
        ('teenagers_attendance', TeenagersAttendance),
        ('online_attendance', OnlineAttendance),
        ('offering', Offering),
    ]

    condition_dict = {
        'yoruba_attendance': show_yoruba_attendance_form,
        'children_attendance': show_children_attendance_form,
        'teenagers_attendance': show_teenagers_attendance_form,
        'online_attendance': show_online_attendance_form,
    }

    # Mapping of step names to template paths
    TEMPLATES = {
        "main_attendance": "main_attendance.html",
        "yoruba_attendance": "yoruba_attendance.html",
        "children_attendance": "children_attendance.html",
        "teenagers_attendance": "teenagers_attendance.html",
        "online_attendance": "online_attendance.html",
        "offering": "offering.html",
    }

    def get_template_names(self):
        return [self.TEMPLATES[self.steps.current]]
    
    def done(self, form_list, **kwargs):
        ushering_instance = UsheringData()  # Create a new instance of your model

        # Process data from each form that was displayed
        for form in form_list:
            if isinstance(form, MainAttendance):
                # Direct mapping from MainAttendance form to model
                for field, value in form.cleaned_data.items():
                    setattr(ushering_instance, field, value)
            elif isinstance(form, (YorubaAttendance, ChildrenAttendance, TeenagersAttendance, OnlineAttendance)):
                # For other attendance forms, update the instance with form data if displayed
                for key, value in form.cleaned_data.items():
                    setattr(ushering_instance, key, value)
            elif isinstance(form, Offering):
                # Similar handling for the Offering form
                for field, value in form.cleaned_data.items():
                    setattr(ushering_instance, field, value)

        # Check and set default values for potentially skipped forms
        default_values = {
            'no_of_ymale': 0,
            'no_of_yfemale': 0,
            'no_of_yboys': 0,
            'no_of_ygirls': 0,
            'no_of_cmale': 0,
            'no_of_cfemale': 0,
            'no_of_cboys': 0,
            'no_of_cgirls': 0,
            'no_of_tmale': 0,
            'no_of_tfemale': 0,
            'no_of_tboys': 0,
            'no_of_tgirls': 0,
            'no_of_boys': 0,
            'no_of_girls': 0,
            'instagram': 0,
            'youtube': 0,
            'mixlr': 0,
            'facebook': 0,
            'website': 0,
            # Add more fields as necessary
        }

        for field, default in default_values.items():
            if not hasattr(ushering_instance, field) or getattr(ushering_instance, field) is None:
                setattr(ushering_instance, field, default)

        # Final save of the model instance after setting all fields
        ushering_instance.save()

        # Display a success message to the user
        messages.success(self.request, "Your submission has been processed successfully.")

            # Redirect to a 'success' URL or render a completion template
            # Adjust 'success_url_name' to the actual name of your success URL
        return render(self.request, 'home.html', {'form_data': [form.cleaned_data for form in form_list]})


def edit_record(request, record_id):
    # Get the record instance to be edited
    ushering_instance = get_object_or_404(UsheringData, pk=record_id)

    # Create form instances for editing. Initialize them with instance data.
    main_attendance_form = MainAttendance(instance=ushering_instance)
    yoruba_attendance_form = YorubaAttendance(instance=ushering_instance)
    children_attendance_form = ChildrenAttendance(instance=ushering_instance)
    teenagers_attendance_form = TeenagersAttendance(instance=ushering_instance)
    online_attendance_form = OnlineAttendance(instance=ushering_instance)
    offering_form = Offering(instance=ushering_instance)

    if request.method == 'POST':
        # Recreate forms with POST data
        main_attendance_form = MainAttendance(request.POST, instance=ushering_instance)
        yoruba_attendance_form = YorubaAttendance(request.POST, instance=ushering_instance)
        children_attendance_form = ChildrenAttendance(request.POST, instance=ushering_instance)
        teenagers_attendance_form = TeenagersAttendance(request.POST, instance=ushering_instance)
        online_attendance_form = OnlineAttendance(request.POST, instance=ushering_instance)
        offering_form = Offering(request.POST, instance=ushering_instance)

        # Check if all forms are valid
        if (main_attendance_form.is_valid() and yoruba_attendance_form.is_valid() and
            children_attendance_form.is_valid() and teenagers_attendance_form.is_valid() and
            online_attendance_form.is_valid() and offering_form.is_valid()):

            # Save all forms
            main_attendance_form.save()
            yoruba_attendance_form.save()
            children_attendance_form.save()
            teenagers_attendance_form.save()
            online_attendance_form.save()
            offering_form.save()

            messages.success(request, "Record updated successfully.")
            return redirect('attendance')  # Replace 'your_success_url' with the name of your desired redirect URL

    return render(request, 'edit_Ushering.html', {
        'main_attendance_form': main_attendance_form,
        'yoruba_attendance_form': yoruba_attendance_form,
        'children_attendance_form': children_attendance_form,
        'teenagers_attendance_form': teenagers_attendance_form,
        'online_attendance_form': online_attendance_form,
        'offering_form': offering_form,
        'record_id': record_id,
    })

def delete_records(request, record_id):
    # Your delete logic here
    record = get_object_or_404(UsheringData, pk=record_id)
    record.delete()
    messages.success(request, 'Record deleted successfully.')
    return redirect('attendance')

def download_report(request):
    # Filter records as per your existing logic
    records = UsheringData.objects.all()  # Add your filtering logic here

    download_format = request.GET.get('format')

    if download_format == 'pdf':
        # Convert the Django QuerySet to HTML string
        html_string = render_to_string('mainattendance_report.html', {'records': records})
        html = HTML(string=html_string)
        pdf = html.write_pdf()

        # Create the HTTP response
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        return response

    elif download_format == 'excel':
        # Convert the Django QuerySet to a DataFrame
        records_list = list(records.values())
        df = pd.DataFrame(records_list)

        # Ensure datetime columns are timezone-naive
        for column in df.select_dtypes(include=['datetime64[ns, UTC]']).columns:
            if df[column].dt.tz is not None:  # Check if the column is timezone-aware
                df[column] = df[column].dt.tz_localize(None)

        # Create an Excel file in memory
        excel_file = BytesIO()
        with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Sheet1', index=False)
            # No need for writer.save(), it's handled automatically
        excel_file.seek(0)  # Reset the pointer to the beginning of the stream

        # Create the HTTP response
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="report.xlsx"'
        return response

    else:
        # Redirect or show an error if the format is not supported
        return redirect('mainattendance_report')
    


def mainattendance_report(request):
    if not request.user.is_authenticated:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')

    time_filter = request.GET.get('timeFilter', 'all')
    sort_by = request.GET.get('sort', 'date')  # Assuming 'date' is a default sort field

    # Retrieve all records by default
    records = UsheringData.objects.all()

    # Apply time filtering based on the user's selection
    if time_filter == 'currentMonth':
        records = records.filter(date__year=now().year, date__month=now().month)
    elif time_filter == 'year':
        records = records.filter(date__year=now().year)
    elif time_filter == 'custom':
        start_date = request.GET.get('start')
        end_date = request.GET.get('end')
        if start_date and end_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            records = records.filter(date__range=[start_date, end_date])

    # Handling the sort direction toggle
    last_sort = request.session.get('last_sort')
    if last_sort == sort_by:
        # If the same column is sorted again, toggle the direction
        sort_by = '-' + sort_by
        request.session['last_sort'] = '-' + sort_by
    else:
        request.session['last_sort'] = sort_by

    # Apply sorting to the queryset
    records = records.order_by(sort_by)

    return render(request, 'mainattendance_report.html', {'records': records})


    
def yorubaattendance_report(request):
    records = UsheringData.objects.all()
    if request.user.is_authenticated:
        return render(request, 'yorubaattendance_report.html', {'records':records})
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')

def childrenattendance_report(request):
    records = UsheringData.objects.all()
    if request.user.is_authenticated:
        return render(request, 'childrenattendance_report.html', {'records':records})
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')
    
def teenagersattendance_report(request):
    records = UsheringData.objects.all()
    if request.user.is_authenticated:
        return render(request, 'teenagersattendance_report.html', {'records':records})
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')
    
def onlineattendance_report(request):
    records = UsheringData.objects.all()
    if request.user.is_authenticated:
        return render(request, 'onlineattendance_report.html', {'records':records})
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')

def offering_report(request):
    records = UsheringData.objects.all()
    if request.user.is_authenticated:
        return render(request, 'offering_report.html', {'records':records})
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')


def import_csv(request):
    if request.method == "POST":
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'The wrong file type was uploaded.')
            return redirect('mainattendance_report')  # Ensure this is the correct URL

        file_data = TextIOWrapper(csv_file.file, encoding=request.encoding)
        csv_reader = csv.reader(file_data)
        next(csv_reader, None)  # Skip the header row

        for row in csv_reader:
            # Assuming the CSV columns match the order of your model fields and the date format is dd-mmm-yy
            try:
                # Parsing the date assuming the format in the CSV is as specified (e.g., 05-Jan-23)
                date = datetime.strptime(row[0], '%d-%b-%y').date()

                # For integer fields, convert to int if present, else None
                def to_int(val):
                    return int(val) if val else None

                # For float fields, convert to float if present, else None
                def to_float(val):
                    return float(val) if val else None

                # Within your try block in the import_csv view function

                UsheringData.objects.create(
                    date=date,
                    session=row[1],
                    minister=row[2],
                    message=row[3],
                    no_of_male=to_int(row[4]),
                    no_of_female=to_int(row[5]),
                    no_of_boys=to_int(row[6]),
                    no_of_girls=to_int(row[7]),
                    no_of_ymale=to_int(row[8]),
                    no_of_yfemale=to_int(row[9]),
                    no_of_yboys=to_int(row[10]),
                    no_of_ygirls=to_int(row[11]),
                    no_of_cmale=to_int(row[12]),
                    no_of_cfemale=to_int(row[13]),
                    no_of_cboys=to_int(row[14]),
                    no_of_cgirls=to_int(row[15]),
                    no_of_tmale=to_int(row[16]),
                    no_of_tfemale=to_int(row[17]),
                    no_of_tboys=to_int(row[18]),
                    no_of_tgirls=to_int(row[19]),
                    instagram=to_int(row[20]),
                    youtube=to_int(row[21]),
                    mixlr=to_int(row[22]),
                    facebook=to_int(row[23]),
                    website=to_int(row[24]),
                    offering_main=to_float(row[25]),
                    tithe=to_float(row[26]),
                    seed=to_float(row[27]),
                    vow=to_float(row[28]),
                    firstfruit=to_float(row[29]),
                    cheque=to_float(row[30]),
                    pos=to_float(row[31]),
                    offering_children=to_float(row[32]),
                    offering_teenagers=to_float(row[33]),
                    foreign_currency=row[34]
                )

            except Exception as e:
                messages.error(request, 'There was an error processing your file: {}'.format(e))
                return redirect('attendance')  # Ensure this is the correct URL

        messages.success(request, 'Records imported successfully.')
        return redirect('attendance')  # Ensure this is the correct URL
    else:
        messages.error(request, "Method not allowed.")
        return redirect('attendance')  # Ensure this is the correct URL






def login_user(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully Login")
            return redirect('dashboard')
        else:
            messages.success(request, "There was an Error Loggin In, Please Try Again...")
            return redirect('login')
    else:
        return render(request, 'login.html')



def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out...")
    return redirect('home')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Welcome!, You have successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Records Deleted Successfully")
        return redirect('report')
    else:
        messages.success(request, "You must be logged in to Do that...")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('report')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged In...")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged In...")
        return redirect('home')