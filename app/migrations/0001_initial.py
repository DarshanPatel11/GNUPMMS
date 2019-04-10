# Generated by Django 2.1.7 on 2019-04-05 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('CertificateID', models.AutoField(primary_key=True, serialize=False)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('CertificateType', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CollegeMaster',
            fields=[
                ('CollegeID', models.AutoField(primary_key=True, serialize=False)),
                ('CollegeCode', models.CharField(max_length=50, null=True)),
                ('CollegeName', models.CharField(max_length=50, null=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentMaster',
            fields=[
                ('DepartmentID', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentCode', models.CharField(max_length=50)),
                ('DepartmentName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationGrades',
            fields=[
                ('EvaluationID', models.AutoField(primary_key=True, serialize=False)),
                ('Grade', models.IntegerField()),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
                ('CollegeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CollegeMaster')),
            ],
        ),
        migrations.CreateModel(
            name='ExternalUsers',
            fields=[
                ('ExternalUserID', models.AutoField(primary_key=True, serialize=False)),
                ('ExternalUserName', models.CharField(max_length=50)),
                ('EmailAddress', models.EmailField(max_length=254)),
                ('Qualification', models.CharField(max_length=50)),
                ('Specialization', models.CharField(max_length=50)),
                ('CompanyName', models.CharField(max_length=50)),
                ('CurrentPosition', models.CharField(max_length=50)),
                ('AreaOfInterest', models.CharField(max_length=50)),
                ('MobileNumber', models.CharField(max_length=15)),
                ('UserType', models.IntegerField()),
                ('ApprovalStatus', models.BooleanField()),
                ('IsActive', models.BooleanField(default=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyMaster',
            fields=[
                ('FacultyID', models.AutoField(primary_key=True, serialize=False)),
                ('FacultyName', models.CharField(max_length=50)),
                ('EmailAddress', models.EmailField(max_length=254)),
                ('Designation', models.CharField(max_length=50)),
                ('RoleID', models.IntegerField()),
                ('IsActive', models.BooleanField(default=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoginMaster',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('LoginID', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=200)),
                ('DerivedUserFrom', models.IntegerField()),
                ('FacultyUserID', models.IntegerField()),
                ('ExternalUserID', models.IntegerField()),
                ('StudentUserID', models.IntegerField()),
                ('IsActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessMaster',
            fields=[
                ('ProcessID', models.AutoField(primary_key=True, serialize=False)),
                ('ProcessName', models.CharField(max_length=50)),
                ('ProjRegToBeDoneBy', models.IntegerField()),
                ('ProjHasToBe', models.IntegerField()),
                ('ProjShallBeDoneBy', models.IntegerField()),
                ('NumberOfStages', models.IntegerField()),
                ('InternalFacultyInvolvementNeeded', models.BooleanField(default=True)),
                ('FacultyRequired', models.BooleanField(default=True)),
                ('HODRequired', models.BooleanField()),
                ('PrincipalRequired', models.BooleanField()),
                ('PanelReviewRequired', models.BooleanField()),
                ('ExternalGuideNeeded', models.BooleanField()),
                ('FundingToBeProvided', models.BooleanField()),
                ('ExpenseTrakingRequired', models.BooleanField()),
                ('MaterialToBeProvided', models.BooleanField()),
                ('FinalSubmissionEvaluated', models.BooleanField()),
                ('EvaluationRole', models.IntegerField()),
                ('ProcessReviewed', models.IntegerField()),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateProcessMaster', to='app.LoginMaster')),
                ('ModifiedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyProcessMaster', to='app.LoginMaster')),
                ('ProcessReviewedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginReviewProcessMaster', to='app.LoginMaster')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessMasterHistory',
            fields=[
                ('ProcessHistoryID', models.AutoField(primary_key=True, serialize=False)),
                ('ProcessName', models.CharField(max_length=50)),
                ('ProjRegToBeDoneBy', models.IntegerField()),
                ('ProjHasToBe', models.IntegerField()),
                ('ProjShallBeDoneBy', models.IntegerField()),
                ('NumberOfStages', models.IntegerField()),
                ('InternalFacultyInvolvementNeeded', models.BooleanField(default=True)),
                ('FacultyRequired', models.BooleanField(default=True)),
                ('HODRequired', models.BooleanField()),
                ('PrincipalRequired', models.BooleanField()),
                ('PanelReviewRequired', models.BooleanField()),
                ('ExternalGuideNeeded', models.BooleanField()),
                ('FundingToBeProvided', models.BooleanField()),
                ('ExpenseTrakingRequired', models.BooleanField()),
                ('MaterialToBeProvided', models.BooleanField()),
                ('FinalSubmissionEvaluated', models.BooleanField()),
                ('EvaluationRole', models.IntegerField()),
                ('ProcessReviewed', models.IntegerField()),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateProcessMasterHistory', to='app.LoginMaster')),
                ('ModifiedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyProcessMasterHistory', to='app.LoginMaster')),
                ('ProcessID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProcessMaster')),
                ('ProcessReviewedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginReviewProcessMasterHistory', to='app.LoginMaster')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessOwner',
            fields=[
                ('ProcessOwnerID', models.AutoField(primary_key=True, serialize=False)),
                ('ProcessOwner', models.IntegerField()),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateProcessOwner', to='app.LoginMaster')),
                ('ModifiedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyProcessOwner', to='app.LoginMaster')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessOwnerHistory',
            fields=[
                ('ProcessOwnerHistoryID', models.AutoField(primary_key=True, serialize=False)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdateBunchID', models.IntegerField()),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateProcessOwnerHistory', to='app.LoginMaster')),
                ('ProcessOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.LoginMaster')),
                ('ProcessOwnerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProcessMaster')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessToProgramMapping',
            fields=[
                ('ProgMappingID', models.AutoField(primary_key=True, serialize=False)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateProcessToProgramMapping', to='app.LoginMaster')),
                ('ModifiedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyProcessToProgramMapping', to='app.LoginMaster')),
                ('ProcessID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProcessMaster')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessToProgramMappingHistory',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateProcessToProgramMappingHistory', to='app.LoginMaster')),
                ('ModifiedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyProcessToProgramMappingHistory', to='app.LoginMaster')),
                ('ProcessID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProcessMaster')),
                ('ProgMappingID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProcessToProgramMapping')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramMaster',
            fields=[
                ('ProgramID', models.AutoField(primary_key=True, serialize=False)),
                ('ProgramName', models.CharField(max_length=50)),
                ('ProgramAlias', models.CharField(max_length=50)),
                ('IsActive', models.BooleanField(default=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateProgramMaster', to='app.LoginMaster')),
                ('ModifiedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyProgramMaster', to='app.LoginMaster')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMembers',
            fields=[
                ('MemberID', models.AutoField(primary_key=True, serialize=False)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateProjectMembers', to='app.LoginMaster')),
                ('ModifiedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyProjectMembers', to='app.LoginMaster')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPanelMembers',
            fields=[
                ('PrjPanelMemberID', models.AutoField(primary_key=True, serialize=False)),
                ('PanelMember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.LoginMaster')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('ProjectID', models.AutoField(primary_key=True, serialize=False)),
                ('ProjectName', models.CharField(max_length=50)),
                ('Subject', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=200)),
                ('InternalGuide', models.IntegerField()),
                ('HOD', models.IntegerField()),
                ('Principal', models.IntegerField()),
                ('ExternalGuide', models.IntegerField()),
                ('Mentor', models.IntegerField()),
                ('Dean', models.IntegerField()),
                ('IsExternalProject', models.BooleanField()),
                ('TermLead', models.IntegerField()),
                ('Status', models.CharField(max_length=50)),
                ('AddStudentApprovalRights', models.IntegerField()),
                ('RemoveStudentApprovalRights', models.IntegerField()),
                ('ChangeInternalGuideRights', models.IntegerField()),
                ('ChangeExternalGuideRights', models.IntegerField()),
                ('ChangeMentorGuideRights', models.IntegerField()),
                ('IsActive', models.BooleanField()),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
                ('CollegeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CollegeMaster')),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateProjects', to='app.LoginMaster')),
                ('DepartmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.DepartmentMaster')),
                ('ModifiedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyProjects', to='app.LoginMaster')),
                ('ProcessID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProcessMaster')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectToStageMapping',
            fields=[
                ('PrjStageMappingID', models.AutoField(primary_key=True, serialize=False)),
                ('StageName', models.CharField(max_length=50)),
                ('ProjectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Projects')),
            ],
        ),
        migrations.CreateModel(
            name='StageActivities',
            fields=[
                ('StageActivityID', models.AutoField(primary_key=True, serialize=False)),
                ('Status', models.IntegerField()),
                ('ActivityType', models.IntegerField()),
                ('ActivityUpload', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateStageActivities', to='app.LoginMaster')),
                ('ModifiedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyStageActivities', to='app.LoginMaster')),
                ('ProjectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Projects')),
            ],
        ),
        migrations.CreateModel(
            name='StageActivitiesApprovals',
            fields=[
                ('StageApprovalID', models.AutoField(primary_key=True, serialize=False)),
                ('ApprovalMember', models.IntegerField()),
                ('ApprovalStatus', models.IntegerField()),
                ('ProjectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Projects')),
                ('StageActivityID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StageActivities')),
            ],
        ),
        migrations.CreateModel(
            name='StageActivitiesApprovalsHistory',
            fields=[
                ('ApprovalHistoryID', models.AutoField(primary_key=True, serialize=False)),
                ('ApprovalMember', models.IntegerField()),
                ('ApprovalStatus', models.IntegerField()),
                ('StageApprovalID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StageActivitiesApprovals')),
            ],
        ),
        migrations.CreateModel(
            name='StageMaster',
            fields=[
                ('StageID', models.AutoField(primary_key=True, serialize=False)),
                ('StageName', models.CharField(max_length=50)),
                ('StageSeq', models.IntegerField()),
                ('ReqAnyUpload', models.BooleanField(default=True)),
                ('ActivityType', models.IntegerField()),
                ('RequireAnyApproval', models.BooleanField(default=True)),
                ('InternalApprovalNeeded', models.BooleanField(default=True)),
                ('InternalApprovalType', models.IntegerField()),
                ('IsWorkflowDriven', models.BooleanField(default=True)),
                ('ExternalGuideApprovalNeeded', models.BooleanField(default=True)),
                ('MentorApprovalNeeded', models.BooleanField(default=True)),
                ('PanelApprovalNeeded', models.BooleanField(default=True)),
                ('DeanApprovalNeeded', models.BooleanField(default=True)),
                ('RequireNoDueCertificate', models.BooleanField(default=True)),
                ('CompletionCertiIssuedForStage', models.BooleanField(default=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateStageMaster', to='app.LoginMaster')),
                ('ModifiedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyStageMaster', to='app.LoginMaster')),
                ('ProcessID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProcessMaster')),
            ],
        ),
        migrations.CreateModel(
            name='StageMasterHistory',
            fields=[
                ('StageHistoryID', models.AutoField(primary_key=True, serialize=False)),
                ('StageName', models.CharField(max_length=50)),
                ('StageSeq', models.IntegerField()),
                ('ReqAnyUpload', models.BooleanField(default=True)),
                ('ActivityType', models.IntegerField()),
                ('RequireAnyApproval', models.BooleanField(default=True)),
                ('InternalApprovalNeeded', models.BooleanField(default=True)),
                ('InternalApprovalType', models.IntegerField()),
                ('IsWorkflowDriven', models.BooleanField(default=True)),
                ('ExternalGuideApprovalNeeded', models.BooleanField(default=True)),
                ('MentorApprovalNeeded', models.BooleanField(default=True)),
                ('PanelApprovalNeeded', models.BooleanField(default=True)),
                ('DeanApprovalNeeded', models.BooleanField(default=True)),
                ('RequireNoDueCertificate', models.BooleanField(default=True)),
                ('CompletionCertiIssuedForStage', models.BooleanField(default=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginStageMasterHistory', to='app.LoginMaster')),
                ('ProcessID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProcessMaster')),
                ('StageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StageMaster')),
            ],
        ),
        migrations.CreateModel(
            name='StageWorkFlowStates',
            fields=[
                ('ApprovalStateID', models.AutoField(primary_key=True, serialize=False)),
                ('ApprovalFacultyRole', models.IntegerField()),
                ('ApprovalSequence', models.IntegerField()),
                ('ApprovalType', models.IntegerField()),
                ('ProcessID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProcessMaster')),
                ('StageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StageMaster')),
            ],
        ),
        migrations.CreateModel(
            name='StageWorkflowStatesHistory',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('ApprovalFacultyRole', models.IntegerField()),
                ('ApprovalSequence', models.IntegerField()),
                ('ApprovalType', models.IntegerField()),
                ('UpdateBunchID', models.IntegerField(default=models.AutoField(primary_key=True, serialize=False))),
                ('ApprovalStateID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StageWorkFlowStates')),
                ('ProcessID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProcessMaster')),
                ('StageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StageMaster')),
            ],
        ),
        migrations.CreateModel(
            name='StreamMaster',
            fields=[
                ('StreamID', models.AutoField(primary_key=True, serialize=False)),
                ('StreamName', models.CharField(max_length=50)),
                ('StreamAlias', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateStreamMaster', to='app.LoginMaster')),
                ('ModifiedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyStreamMaster', to='app.LoginMaster')),
                ('ProgramID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProgramMaster')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('StudentID', models.AutoField(primary_key=True, serialize=False)),
                ('StudentName', models.CharField(max_length=50)),
                ('EnrollmentNumber', models.IntegerField()),
                ('FirstName', models.CharField(max_length=50)),
                ('MiddleName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('EmailID', models.EmailField(max_length=254)),
                ('Status', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('DeactivationReason', models.TextField(max_length=300)),
                ('ApprovedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginApproveStudents', to='app.LoginMaster')),
                ('CollegeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CollegeMaster')),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateStudents', to='app.LoginMaster')),
                ('DepartmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.DepartmentMaster')),
                ('ModifiedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyStudents', to='app.LoginMaster')),
                ('ProgramID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProgramMaster')),
                ('StreamID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StreamMaster')),
            ],
        ),
        migrations.CreateModel(
            name='TermMaster',
            fields=[
                ('TermID', models.AutoField(primary_key=True, serialize=False)),
                ('TermName', models.CharField(max_length=50)),
                ('TermAlias', models.CharField(max_length=50)),
                ('ProgramID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProgramMaster')),
                ('StreamID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StreamMaster')),
            ],
        ),
        migrations.AddField(
            model_name='stageactivities',
            name='StageID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StageMaster'),
        ),
        migrations.AddField(
            model_name='projecttostagemapping',
            name='StageID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StageMaster'),
        ),
        migrations.AddField(
            model_name='projects',
            name='StageID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StageMaster'),
        ),
        migrations.AddField(
            model_name='projects',
            name='TermID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TermMaster'),
        ),
        migrations.AddField(
            model_name='projectpanelmembers',
            name='ProjectID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Projects'),
        ),
        migrations.AddField(
            model_name='projectmembers',
            name='ProjectID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Projects'),
        ),
        migrations.AddField(
            model_name='projectmembers',
            name='TeamMember',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginMemberProjectMembers', to='app.LoginMaster'),
        ),
        migrations.AddField(
            model_name='processtoprogrammappinghistory',
            name='ProgramID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProgramMaster'),
        ),
        migrations.AddField(
            model_name='processtoprogrammappinghistory',
            name='StreamID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StreamMaster'),
        ),
        migrations.AddField(
            model_name='processtoprogrammappinghistory',
            name='TermID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TermMaster'),
        ),
        migrations.AddField(
            model_name='processtoprogrammapping',
            name='ProgramID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProgramMaster'),
        ),
        migrations.AddField(
            model_name='processtoprogrammapping',
            name='StreamID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StreamMaster'),
        ),
        migrations.AddField(
            model_name='processtoprogrammapping',
            name='TermID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TermMaster'),
        ),
        migrations.AddField(
            model_name='facultymaster',
            name='CollegeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.LoginMaster'),
        ),
        migrations.AddField(
            model_name='facultymaster',
            name='CreatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateFacultyMaster', to='app.LoginMaster'),
        ),
        migrations.AddField(
            model_name='facultymaster',
            name='DepartmentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.DepartmentMaster'),
        ),
        migrations.AddField(
            model_name='facultymaster',
            name='ModifiedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyFacultyMaster', to='app.LoginMaster'),
        ),
        migrations.AddField(
            model_name='facultymaster',
            name='ProgramID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProgramMaster'),
        ),
        migrations.AddField(
            model_name='facultymaster',
            name='StreamID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StreamMaster'),
        ),
        migrations.AddField(
            model_name='externalusers',
            name='ActionTakenBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.LoginMaster'),
        ),
        migrations.AddField(
            model_name='evaluationgrades',
            name='CreatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateEvaluationGrades', to='app.LoginMaster'),
        ),
        migrations.AddField(
            model_name='evaluationgrades',
            name='CurrentTerm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TermMaster'),
        ),
        migrations.AddField(
            model_name='evaluationgrades',
            name='DepartmentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.DepartmentMaster'),
        ),
        migrations.AddField(
            model_name='evaluationgrades',
            name='ProjectID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Projects'),
        ),
        migrations.AddField(
            model_name='evaluationgrades',
            name='StageActivityID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StageActivities'),
        ),
        migrations.AddField(
            model_name='evaluationgrades',
            name='StudentLoginID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.LoginMaster'),
        ),
        migrations.AddField(
            model_name='departmentmaster',
            name='CreatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateDepartmentMaster', to='app.LoginMaster'),
        ),
        migrations.AddField(
            model_name='departmentmaster',
            name='ModifiedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyDepartmentMaster', to='app.LoginMaster'),
        ),
        migrations.AddField(
            model_name='departmentmaster',
            name='collegeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CollegeMaster'),
        ),
        migrations.AddField(
            model_name='collegemaster',
            name='CreatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginCreateCollegeMaster', to='app.LoginMaster'),
        ),
        migrations.AddField(
            model_name='collegemaster',
            name='ModifiedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoginModifyCollegeMaster', to='app.LoginMaster'),
        ),
        migrations.AddField(
            model_name='certificates',
            name='CollegeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CollegeMaster'),
        ),
        migrations.AddField(
            model_name='certificates',
            name='CurrentTerm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TermMaster'),
        ),
        migrations.AddField(
            model_name='certificates',
            name='DepartmentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.DepartmentMaster'),
        ),
        migrations.AddField(
            model_name='certificates',
            name='LoginID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.LoginMaster'),
        ),
        migrations.AddField(
            model_name='certificates',
            name='ProjectID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Projects'),
        ),
        migrations.AddField(
            model_name='certificates',
            name='StageActivityID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StageActivities'),
        ),
    ]
