from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.db import connection, transaction
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ExternalUsers, LoginMaster, ProjectMembers, Projects, ProjectToStageMapping, StageMaster, \
    StageActivities, StageToFileMapping
from .forms import ExternalRegistration, FileUpload, ActivityApproval, LoginForm, RegisterStudent, \
    LoginRegistrationForm, ProjectRegistration
from datetime import datetime


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
        form.ActionTakenBy = 1
        print(form.errors)
        if form.is_valid():
            '''
            id = form.cleaned_data["ExternalUserName"]
            pwd = form.cleaned_data[""]
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO app_loginmaster ('LoginID','Password','DerivedUserFrom','StudentUserID','FacultyUserID','ExternalUserID','isActive') VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (str(id), str(pwd), usertype, 0, 0, uid, True))
            # form.save()
            transaction.commit()
            form.save()
            return HttpResponse("External Faculty Registered successfully")
            '''
            form.save()
            return redirect('/')
    form = ExternalRegistration()
    return render(request, 'reg_ext_user.html', {'form': form})


def viewExternalUser(request):
    extusr = ExternalUsers.objects.filter(ApprovalStatus=True)
    return render(request, 'view_ext_user.html', locals())


def studentRegistration(request):
    if request.method == "POST":
        form = RegisterStudent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = RegisterStudent()
    return render(request, 'reg_student.html', {'form': form})


def loginRegistration(request):
    if request.method == 'POST':
        form = LoginRegistrationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print(form.cleaned_data)
            id = form.cleaned_data['Login_ID']
            pwd = form.cleaned_data['Password']
            usertype = int(form.cleaned_data['User_Type'])
            uid = int(form.cleaned_data['User_ID'])
            cursor = connection.cursor()
            if usertype == 1:
                cursor.execute(
                    "INSERT INTO app_loginmaster ('LoginID','Password','DerivedUserFrom','StudentUserID','FacultyUserID','ExternalUserID','isActive') VALUES (%s,%s,%s,%s,%s,%s,%s)",
                    (str(id), str(pwd), usertype, uid, 0, 0, True))
                print(usertype)
                # form.save()
                transaction.commit()
                return HttpResponse("Student Registered successfully")
            if usertype == 2:
                cursor.execute(
                    "INSERT INTO app_loginmaster ('LoginID','Password','DerivedUserFrom','StudentUserID','FacultyUserID','ExternalUserID','isActive') VALUES (%s,%s,%s,%s,%s,%s,%s)",
                    (str(id), str(pwd), usertype, 0, uid, 0, True))
                print(usertype)
                # form.save()
                transaction.commit()
                return HttpResponse("Internal Faculty Registered successfully")
            if usertype == 3:
                cursor.execute(
                    "INSERT INTO app_loginmaster ('LoginID','Password','DerivedUserFrom','StudentUserID','FacultyUserID','ExternalUserID','isActive') VALUES (%s,%s,%s,%s,%s,%s,%s)",
                    (str(id), str(pwd), usertype, 0, 0, uid, True))
                # form.save()
                print(usertype)
                transaction.commit()
                return HttpResponse("External Faculty Registered successfully")

    form = LoginRegistrationForm()
    return render(request, 'reg_login.html', locals())


def registerProject(request):
    if request.method == "POST":
        form = ProjectRegistration(request.POST)
        if form.is_valid():
            # form.save()
            cursor = connection.cursor()
            CollegeID_id = form.cleaned_data["College_ID"].pk
            DepartmentID_id = form.cleaned_data["Department_ID"].pk
            ProcessID_id = form.cleaned_data["Process_ID"].pk
            # print(ProcessID_id)
            TermID_id = form.cleaned_data["Term_ID"].pk
            # TermLead = form.cleaned_data["Term_Lead"]
            ProjectName = form.cleaned_data["Project_Name"]
            Subject = form.cleaned_data["Subject"]
            Description = form.cleaned_data["Description"]
            InternalGuide_id = form.cleaned_data["Internal_Guide"].pk
            HOD_id = form.cleaned_data["HOD"].pk
            Principal_id = form.cleaned_data["Principal"].pk
            ExternalGuide_id = form.cleaned_data["External_Guide"].pk
            Dean_id = form.cleaned_data["Dean"].pk
            IsExternalProject = str(form.cleaned_data["Is_External_Project"])
            TermLead = request.session["username"]
            form.Term_Lead = TermLead
            cursor.execute(
                "INSERT INTO app_projects (CollegeID_id,DepartmentID_id,ProcessID_id,TermID_id,TermLead,ProjectName, Subject, Description, InternalGuide_id, HOD_id, Principal_id, ExternalGuide_id, Dean_id, IsExternalProject,Status,IsActive,CreatedDate,ModifiedDate,CreatedBy,ModifiedBy) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s, %s, %s, %s, %s,0,1,%s,%s,1,1)",
                (CollegeID_id, DepartmentID_id, ProcessID_id, TermID_id, TermLead, ProjectName, Subject, Description,
                 InternalGuide_id, HOD_id, Principal_id, ExternalGuide_id, Dean_id, IsExternalProject, datetime.now(),
                 datetime.now()))
            transaction.commit()
            r1 = cursor.execute("select max(ProjectID) from app_projects")
            r1 = r1.fetchone()[0]
            print('r1: ', r1)
            row = cursor.execute("SELECT ProcessID_id FROM app_projects WHERE ProcessID_id = %s ",
                                 [str(form.cleaned_data['Process_ID'].pk)])
            row = row.fetchone()
            print('row', row[0])
            r2 = cursor.execute("select StageID,StageName from app_stagemaster where ProcessID_id = %s ", [row[0]])
            r2 = r2.fetchall()
            print(r2)
            r3 = []
            counter = 0
            for i in r2:
                if counter == 0:
                    cursor.execute(
                        "insert into app_projecttostagemapping (ProjectID_id,StageID_id,StageName) VALUES (%s,%s,%s)",
                        [r1, i[0], i[1]])
                    transaction.commit()
                    cursor.execute(
                        "insert into app_stageactivities (ProjectID_id,StageID_id,Status,ActivityType_id,CreatedDate,ModifiedDate,CreatedBy,ModifiedBy) VALUES (%s,%s,%s,%s,%s,%s,1,1)",
                        [r1, str(i[0]), counter, str(i[0]), str(datetime.now()), str(datetime.now())])
                    transaction.commit()
                    counter = -1
                else:
                    cursor.execute(
                        "insert into app_projecttostagemapping (ProjectID_id,StageID_id,StageName) VALUES (%s,%s,%s)",
                        [r1, i[0], i[1]])
                    transaction.commit()
                    cursor.execute(
                        "insert into app_stageactivities (ProjectID_id,StageID_id,Status,ActivityType_id,CreatedDate,ModifiedDate,CreatedBy,ModifiedBy) VALUES (%s,%s,-1,%s,%s,%s,1,1)",
                        [r1, str(i[0]), str(i[0]), str(datetime.now()), str(datetime.now())])
                    transaction.commit()

            return redirect('/app/studentDashboard')
    form = ProjectRegistration()
    return render(request, 'reg_project.html', {'form': form})


def studentDashboard(request):
    pid = Projects.objects.filter(TermLead=request.session['username']).values('ProjectID')
    print(pid)
    stuproj = []
    # pid_list.append(pid[0]['ProjectID'])
    # print(pid)
    stuproj = Projects.objects.filter(ProjectID__in=pid).only('CollegeID', 'ProjectName')
    # print('ProjectName: ',str(stuproj[0]).split(' ')[1])
    # print('CollegeID: ', str(stuproj[0]).split(' ')[0])
    # stuproj= Projects.objects.select_related('InternalGuide')
    # stuproj.LinkColumn('ProjectName')
    # print(stuproj['InternalGuide'])
    # print(stuproj)
    return render(request, 'student_dashboard.html', locals())


def stageDetails(request, id):
    pid = id
    stageid = ProjectToStageMapping.objects.filter(ProjectID=pid).values('StageID')
    stage = StageMaster.objects.filter(StageID__in=stageid)
    status1 = StageActivities.objects.filter(ProjectID=pid).filter(StageID__in=stageid)
    from django.db import connection, transaction
    cursor = connection.cursor()
    try:
        row = cursor.execute("select grade from app_evaluationgrades where  StudentLoginID_id =%s",
                             [request.session['id']])
        row = row.fetchone()
        row = row[0]
    except:
        pass
    # print(status1)
    if request.method == 'POST':
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            f = str(form.cleaned_data['ProjectID'].pk) + '_' + str(form.cleaned_data['StageID'].pk) + '_' + str(
                form.cleaned_data['File'].name)
            # print(f)
            # form.FileName = request.FILES['File'].name
            # print(request.FILES['File'].path)
            ProjectID_id = str(form.cleaned_data['ProjectID'].pk)
            StageID_id = str(form.cleaned_data['StageID'].pk)
            FileName = str(ProjectID_id) + '_' + str(StageID_id) + '_' + str(request.FILES['File'].name)
            FilePath = handle_uploaded_file(request.FILES['File'], FileName)
            # UploadedBy = str(form.cleaned_data['UploadedBy'])

            # File = request.FILES['File']
            form.FileName = FileName
            from django.db import connection, transaction
            cursor = connection.cursor()
            # cursor.execute("INSERT INTO app_stagetofilemapping (FilePath, UploadedBy, ProjectID_id, StageID_id, FileName, File) VALUES (%s, %s, %s, %s, %s, %s)",
            # (FilePath, UploadedBy, ProjectID_id, StageID_id, FileName, File))
            cursor.execute("UPDATE app_stageactivities SET Status = '1' WHERE ProjectID_id = %s and StageID_id= %s",
                           (str(pid), str(form.cleaned_data["StageID"].pk)))
            transaction.commit()
            form.save()

            return HttpResponse("File uploaded successfully")
    form = FileUpload()

    return render(request, 'stage_detail.html', locals())


def handle_uploaded_file(f, fn):
    namedest = 'app/upload/' + fn
    with open(namedest, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return namedest


def facultyDashboard(request):
    pid = Projects.objects.filter(InternalGuide=request.session['id']).values("ProjectID")
    stuproj = Projects.objects.filter(ProjectID__in=pid).only('CollegeID', 'ProjectName')
    return render(request, "faculty_dashboard.html", locals())


def externalFacultyDashboard(request):
    print("External Id:", request.session['id'])
    pid = Projects.objects.filter(ExternalGuide=request.session['id']).values("ProjectID")
    print("pid", pid)
    stuproj = Projects.objects.filter(ProjectID__in=pid).only('CollegeID', 'ProjectName')
    return render(request, "external_faculty_dashboard.html", locals())


def facultyApproval(request, id):
    pid = id
    stageid = ProjectToStageMapping.objects.filter(ProjectID=pid).values('StageID')
    stage = StageMaster.objects.filter(StageID__in=stageid)
    status1 = StageActivities.objects.filter(ProjectID=pid).filter(StageID__in=stageid)
    current_stage = StageActivities.objects.filter(ProjectID=pid).filter(StageID__in=stageid).filter(Status=1).values(
        "StageID")
    try:
        current_stage = current_stage[0]['StageID']
        print("current stage", current_stage)
        current_stage = StageMaster.objects.filter(pk=str(current_stage))
        print(pid, current_stage)
        file = StageToFileMapping.objects.filter(ProjectID=pid, StageID=current_stage[0].pk).values("uploadID",
                                                                                                    "FilePath", "File")
    # print(file[0]["uploadID"])
    except:
        pass
    try:
        file = file[0]["uploadID"]
    except:
        pass
    # print("FilePath", file[0]["FilePath"], "File", file[0]["File"])
    # file = file[0]["File"]
    if request.method == 'POST':

        form = ActivityApproval(request.POST)
        from django.db import transaction, connection
        cursor = connection.cursor()
        row = cursor.execute(
            "Select CollegeID_id,TermLead,DepartmentID_id,TermID_id from app_projects where ProjectID = %s", [pid])
        row = row.fetchone()
        print(row)
        # print('abc : ',status1.values("StageActivityID")[0]['StageActivityID'])
        try:
            form.StageID = r1 = current_stage[0].pk
            form.StageActivityID = r2 = status1.values("StageActivityID")[0]['StageActivityID']
            form.StudentLoginID = r3 = row[1]
            form.CollegeID = r4 = row[0]
            form.DepartmentID = r5 = row[2]
            form.CurrentTerm = r6 = row[3]
            form.CreatedBy = request.session['username']
            print('r1-6: ', r1, r2, r3, r4, r5, r6)
            row = cursor.execute("select StudentID from app_students where EnrollmentNumber = %s", [r3]).fetchone()
            r3 = row[0]
            print('r3 : ', r3)
            print(form.errors)
            print(form.errors)

            print("test: ", form.cleaned_data)
        except:
            pass

        if form.is_valid():
            status = form.cleaned_data
            # print("cs : ",current_stage[0].pk)
            csp1 = current_stage[0].pk + 1
            # form.Grade = status["Grade"]
            # Data modifying operation - commit required
            # print(status["StageID"].pk)
            print("form clean data : ", form.cleaned_data)
            cursor.execute("UPDATE app_stageactivities SET Status = %s WHERE ProjectID_id = %s and StageID_id= %s",
                           (str(status["Status"]), str(pid), str(current_stage[0].pk)))
            transaction.commit()
            cursor.execute("UPDATE app_stageactivities SET Status = 0 WHERE ProjectID_id = %s and StageID_id = %s",
                           (str(pid), str(csp1)))
            transaction.commit()
            #        print(form.cleaned_data)
            #       form.save
            cursor.execute(
                "insert into app_evaluationgrades (Grade,CreatedDate,ModifiedDate,CollegeID_id,CurrentTerm_id,DepartmentID_id,ProjectID_id,StageActivityID_id,StudentLoginID_id,CreatedBy) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                [status["Grade"], datetime.now(), datetime.now(), r4, r6, r5, pid, r2, r3, request.session['username']])
            transaction.commit()

            return HttpResponse("Status Changed")
    form = ActivityApproval()

    return render(request, 'stageApproval.html', locals())


def my_custom_sql(request, id):
    pid = id
    stageid = ProjectToStageMapping.objects.filter(ProjectID=pid).values('StageID')

    status1 = StageActivities.objects.filter(ProjectID=pid).filter(StageID__in=stageid)
    form = ActivityApproval(request.POST)
    from django.db import connection, transaction
    cursor = connection.cursor()
    if (form.is_valid()):
        status = form.cleaned_data["Status"]
    # Data modifying operation - commit required
    cursor.execute("UPDATE StageActivities SET Status = %s WHERE ProjectID = %s and StageID= %s",
                   [status1, pid, stageid])
    transaction.commit_unless_managed()

    return render(request, 'stageApproval.html', locals())


def login(request):
    # username = id
    # passsword = pwd
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.errors)
        if form.is_valid():
            id = form.cleaned_data['Login_ID']
            pwd = form.cleaned_data['Password']

            flag = LoginMaster.objects.filter(LoginID=id, Password=pwd)
            if flag:
                request.session['username'] = id
                role = LoginMaster.objects.filter(LoginID=id, Password=pwd).values("DerivedUserFrom")
                print(role[0]['DerivedUserFrom'])
                if role[0]['DerivedUserFrom'] == 1:
                    request.session['id'] = \
                        LoginMaster.objects.filter(LoginID=id, Password=pwd).values("StudentUserID")[0]["StudentUserID"]
                    return redirect('/app/studentDashboard')
                elif role[0]['DerivedUserFrom'] == 2:
                    request.session['id'] = \
                        LoginMaster.objects.filter(LoginID=id, Password=pwd).values("FacultyUserID")[0]["FacultyUserID"]
                    return redirect('/app/facultyDashboard')
                elif role[0]['DerivedUserFrom'] == 3:
                    request.session['id'] = \
                        LoginMaster.objects.filter(LoginID=id, Password=pwd).values("ExternalUserID")[0][
                            "ExternalUserID"]
                    return redirect('/app/externalFacultyDashboard')

    form = LoginForm()
    return render(request, 'login.html', locals())


def logout(request):
    try:
        del request.session['username']
        del request.session['id']
    except:
        pass
    return redirect('/app/login')


def download(request, file):
    from app.models import StageToFileMapping
    from django.http import FileResponse
    from django.utils.text import slugify
    import os

    item = get_object_or_404(StageToFileMapping, pk=file)
    file_name, file_extension = os.path.splitext(item.File.file.name)
    file_extension = file_extension[1:]  # removes dot
    response = FileResponse(item.File.file,
                            content_type="file/%s" % file_extension)
    response["Content-Disposition"] = "attachment;" \
                                      "filename=%s.%s" % (slugify(item.File.name)[:100], file_extension)
    return response
