from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ExternalUsers, ProjectMembers, Projects, ProjectToStageMapping, StageMaster, StageActivities
from .forms import ExternalRegistration, FileUpload, ActivityApproval


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'reg_ext_user.html', args)


def externalRegistration(request):
    if request.method == "POST":
        form = ExternalRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ExternalRegistration()
    return render(request, 'reg_ext_user.html', {'form': form})

def viewExternalUser(request):
    extusr = ExternalUsers.objects.filter(ApprovalStatus=True)
    return render(request,'view_ext_user.html',locals())

def studentDashboard(request):
    pid = ProjectMembers.objects.filter(TeamMember = 1).values('ProjectID')
    print(pid)
    stuproj = []
        #pid_list.append(pid[0]['ProjectID'])
    #print(pid)
    stuproj = Projects.objects.filter(ProjectID__in = pid).only('CollegeID','ProjectName')
    print('ProjectName: ',str(stuproj[0]).split(' ')[1])
    print('CollegeID: ', str(stuproj[0]).split(' ')[0])
    #stuproj= Projects.objects.select_related('InternalGuide')
    #stuproj.LinkColumn('ProjectName')
    #print(stuproj['InternalGuide'])
    print(stuproj)
    return render(request, 'student_dashboard.html', locals())


def stageDetails(request,id):
    pid = id
    stageid = ProjectToStageMapping.objects.filter(ProjectID = pid).values('StageID')
    stage = StageMaster.objects.filter(StageID__in = stageid)
    status1 = StageActivities.objects.filter(ProjectID=pid).filter( StageID__in=stageid)
    print(stage)
    if request.method == 'POST':
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            f = str(form.cleaned_data['ProjectID'])+'_'+str(form.cleaned_data['StageID'])+'_'+str(form.cleaned_data['File'])
            print(f)
            handle_uploaded_file(request.FILES['File'],f)

            form.save()
            return HttpResponse("File uploaded successfully")
    form = FileUpload()


    return render(request,'stage_detail.html',locals())


def handle_uploaded_file(f,fn):
    namedest = 'app/upload/'+fn+'_'+f.name
    with open(namedest, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    #return namedest


def facultyDashboard(request):
    pid = Projects.objects.filter(InternalGuide = 1).values("ProjectID")
    stuproj = Projects.objects.filter(ProjectID__in=pid).only('CollegeID', 'ProjectName')
    return render(request,"faculty_dashboard.html",locals())


def facultyApproval(request,id):
    pid = id
    stageid = ProjectToStageMapping.objects.filter(ProjectID=pid).values('StageID')
    stage = StageMaster.objects.filter(StageID__in=stageid)
    status1 = StageActivities.objects.filter(ProjectID=pid).filter(StageID__in=stageid)



    if request.method == 'POST':

        form = ActivityApproval(request.POST)
        print(form.errors)

        if form.is_valid():
            from django.db import connection, transaction
            cursor = connection.cursor()
            if form.is_valid():
                status = form.cleaned_data

                #Data modifying operation - commit required
                #print(status["StageID"].pk)
                cursor.execute("UPDATE app_stageactivities SET Status = %s WHERE ProjectID_id = %s and StageID_id= %s",(str(status["Status"]), str(pid), str(status["StageID"].pk)))
                transaction.commit()


    #        print(form.cleaned_data)
     #       form.save
                return HttpResponse("Status Changed")
    form=ActivityApproval()
    return render(request, 'stageApproval.html', locals())

def my_custom_sql(request,id):
    pid = id
    stageid = ProjectToStageMapping.objects.filter(ProjectID=pid).values('StageID')

    status1 = StageActivities.objects.filter(ProjectID=pid).filter(StageID__in=stageid)
    form = ActivityApproval(request.POST)
    from django.db import connection, transaction
    cursor = connection.cursor()
    if(form.is_valid()):
        status=form.cleaned_data["Status"]
    # Data modifying operation - commit required
    cursor.execute("UPDATE StageActivities SET Status = %s WHERE ProjectID = %s and StageID= %s", [status1,pid,stageid])
    transaction.commit_unless_managed()

    return render(request, 'stageApproval.html', locals())