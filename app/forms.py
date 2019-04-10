from django import forms

from app.models import ExternalUsers, StageToFileMapping, StageActivities


class ExternalRegistration(forms.ModelForm):
    class Meta:
        model = ExternalUsers
        fields = ('ExternalUserName', 'EmailAddress', 'MobileNumber', 'Qualification','UserType', 'CompanyName', 'CurrentPosition',
                  'AreaOfInterest', 'Specialization')



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
