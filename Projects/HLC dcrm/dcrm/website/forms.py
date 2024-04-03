from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
from .models import UsheringData

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label=''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label=''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><small><li>Your password can\'t be too similar to your personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password</li><li>Your password can\'t be entirely numeric.</li></small></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label=''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


# Create Add Record Form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"Last Name", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"Email", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"Phone", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"Address", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"City", "class":"form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"State", "class":"form-control"}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"Zipcode", "class":"form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)


# Create Add Record Form
class MainAttendance(forms.ModelForm):
    sessions = [
        ("Single Service", "Single Service"),
        ("First Service", "First Service"),
        ("Second Service", "Second Service")
    ]

    date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={'placeholder':"Date", "class":"form-control", "type":"date"}), label="")
    session = forms.ChoiceField(required=True, choices=sessions, widget=forms.widgets.Select(attrs={'placeholder':"Sevice Session", "class":"form-control"}), label="")
    minister = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"Minister", "class":"form-control"}), label="")
    message = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"Message", "class":"form-control"}), label="")
    no_of_male = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Male", "class":"form-control"}), label="")
    no_of_female = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Female", "class":"form-control"}), label="")
    no_of_boys = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Boys", "class":"form-control"}), label="")
    no_of_girls = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Girls", "class":"form-control"}), label="")
    skip_yoruba_attendance = forms.BooleanField(required=False, label='Skip Yoruba Attendance?')
    skip_children_attendance = forms.BooleanField(required=False, label='Skip Children Attendance?')
    skip_teenagers_attendance = forms.BooleanField(required=False, label='Skip Teenagers Attendance?')
    skip_online_attendance = forms.BooleanField(required=False, label='Skip Online Attendance?')

    class Meta:
        model = UsheringData
        fields = ('date', 'session', 'minister', 'no_of_male', 'no_of_female', 'no_of_boys', 'no_of_girls','skip_yoruba_attendance', 'skip_children_attendance', 'skip_teenagers_attendance', 'skip_online_attendance')


class YorubaAttendance(forms.ModelForm):

    no_of_ymale = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Male", "class":"form-control"}), label="")
    no_of_yfemale = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Female", "class":"form-control"}), label="")
    no_of_yboys = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Boys", "class":"form-control"}), label="")
    no_of_ygirls = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Girls", "class":"form-control"}), label="")

    class Meta:
        model = UsheringData
        fields = ('no_of_ymale', 'no_of_yfemale', 'no_of_yboys', 'no_of_ygirls')

class ChildrenAttendance(forms.ModelForm):

    no_of_cmale = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Male", "class":"form-control"}), label="")
    no_of_cfemale = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Female", "class":"form-control"}), label="")
    no_of_cboys = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Boys", "class":"form-control"}), label="")
    no_of_cgirls = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Girls", "class":"form-control"}), label="")

    class Meta:
        model = UsheringData
        fields = ('no_of_cmale', 'no_of_cfemale', 'no_of_cboys', 'no_of_cgirls')


class TeenagersAttendance(forms.ModelForm):

    no_of_tmale = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Male", "class":"form-control"}), label="")
    no_of_tfemale = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Female", "class":"form-control"}), label="")
    no_of_tboys = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Boys", "class":"form-control"}), label="")
    no_of_tgirls = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of Girls", "class":"form-control"}), label="")

    class Meta:
        model = UsheringData
        fields = ('no_of_tmale', 'no_of_tfemale', 'no_of_tboys', 'no_of_tgirls')


class OnlineAttendance(forms.ModelForm):

    instagram = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of viewers", "class":"form-control"}), label="")
    youtube = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of viewers", "class":"form-control"}), label="")
    mixlr = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of viewers", "class":"form-control"}), label="")
    facebook = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of viewers", "class":"form-control"}), label="")
    website = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"No of viewers", "class":"form-control"}), label="")
   
    class Meta:
        model = UsheringData
        fields = ('instagram', 'youtube', 'mixlr', 'facebook', 'website')

class Offering(forms.ModelForm):

    offering_main = forms.FloatField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"Total Cash Offering", "class":"form-control"}), label="")
    tithe = forms.FloatField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"Total Cash Tithe", "class":"form-control"}), label="")
    seed = forms.FloatField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"Total Cash Seed", "class":"form-control"}), label="")
    vow = forms.FloatField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"Total Cash Vow", "class":"form-control"}), label="")
    firstfruit = forms.FloatField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"Total Cash FirstFruit Offering", "class":"form-control"}), label="")
    cheque = forms.FloatField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"Total Cheque", "class":"form-control"}), label="")
    pos = forms.FloatField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"Total POS Amount", "class":"form-control"}), label="")
    offering_children = forms.FloatField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"Total Children Offering", "class":"form-control"}), label="")
    offering_teenagers = forms.FloatField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder':"Total Teenagers Offering", "class":"form-control"}), label="")
    foreign_currency = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"Total Offering in Foreign Currency", "class":"form-control"}), label="")

    class Meta:
        model = UsheringData
        fields = ('offering_main', 'tithe', 'seed', 'vow', 'firstfruit', 'cheque', 'pos', 'offering_children', 'offering_teenagers', 'foreign_currency')