from django import forms

from app.models import ExternalUsers, StageToFileMapping, StageActivities, Students, LoginMaster, Projects


class ExternalRegistration(forms.ModelForm):
    class Meta:
        model = ExternalUsers
        fields = ('ExternalUserName', 'EmailAddress', 'MobileNumber', 'Qualification','UserType', 'CompanyName', 'CurrentPosition',
                  'AreaOfInterest', 'Specialization')

class RegisterStudent(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('StudentName','CollegeID','DepartmentID','ProgramID','StreamID','EnrollmentNumber','FirstName','MiddleName','LastName','EmailID')

class LoginRegistrationForm(forms.Form):
    Login_ID= forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput)
    User_Type = forms.ChoiceField(choices=((1,'Student'),(2,'Internal Faculty'),(3,'External Faculty')))
    User_ID = forms.CharField()


class FileUpload(forms.ModelForm):
    class Meta:
        model = StageToFileMapping

        fields=('ProjectID','FileName','File','FilePath','StageID','UploadedBy')
        widgets={'ProjectID': forms.HiddenInput(),'FileName': forms.HiddenInput(),'StageID': forms.HiddenInput(),'FilePath': forms.HiddenInput() }

class ActivityApproval(forms.ModelForm):
    class Meta:
        model=StageActivities
        fields=('ProjectID','StageID','ActivityType','Status','ModifiedBy','CreatedBy')
        widgets={'ProjectID': forms.HiddenInput(),'ActivityType': forms.HiddenInput(), 'StageID':forms.HiddenInput(),'CreatedBy':forms.HiddenInput(),'ModifiedBy': forms.HiddenInput()}

class LoginForm(forms.Form):
    Login_ID= forms.CharField(max_length=11)
    Password = forms.CharField(widget=forms.PasswordInput())

class ProjectRegistration(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('CollegeID','DepartmentID','ProcessID','TermID','TermLead','ProjectName','Subject','Description','InternalGuide','HOD','Principal','ExternalGuide','Dean','IsExternalProject')