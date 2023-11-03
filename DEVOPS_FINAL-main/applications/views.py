from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from .models import User,CandidateForm,EducationalDetailsForm
from django.contrib.auth import authenticate, login,logout
from django.template.loader import render_to_string
import pdfkit

# Create your views here.
def home(request):
    return render(request,'applications/home.html')

def downloadPdf(request):
    path=r'/usr/local/bin/wkhtmltopdf'
    config=pdfkit.configuration(wkhtmltopdf=path)
    data=CandidateForm.objects.filter(appid=request.user)[0]
    html = render_to_string('applications/pdf.html', {'name':data.candidateName,'cno':data.contactNo,'dob':data.dateOfBirth,'gender':data.gender,'fname':data.fatherName,'focc':data.foccupation,'Mname':data.motherName,'mocc':data.moccupation,'mstat':data.martialStat,'adno':data.AdhaarNo,'peraddress':data.phouseno,'perstreet':data.pstreetcolony,'perstate':data.pstate,'pinno':data.ppincode,'phno':data.prehouseno,'pstreet':data.prestreetcolony,'pstate':data.prestate,'pinno2':data.prepincode})
    pdf=pdfkit.from_string(html,configuration=config,options={"enable-local-file-access": ""})
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ApplicationForm.pdf"'
    return response

def logoutUser(request):
    logout(request)
    return redirect(reverse('home_page'))

def submitApplication(request):
    return render(request,'applications/submit.html')

'''
def uploadDocumentsForm(request):
    if request.method=='POST'and request.FILES['uploadimage','up10thmarkscard',
                                               'up12thmarkscard','upIncomecaste','up12thstudycertificate']:
        image=request.FILES['uploadimage']
        marks10th=request.FILES['up10thmarkscard']
        marks12th=request.FILES['up12thmarkscard']
        incomecert=request.FILES['upIncomecaste']
        studycard=request.FILES['up12thstudycertificate']

        return render(request,'applications/submit.html')
    
    return render(request,'applications/uploadDocuments.html')
'''
def educationalDetailsForm(request):
    if request.method=='POST':
        user=request.user
        sch10=request.POST.get('school10')
        scboard=request.POST.get('board')
        schrollNo=request.POST.get('rollno10th')
        schpercent=request.POST.get('percent10')
        clgname=request.POST.get('clgName')
        clgboard=request.POST.get('clgBoard')
        clgrollNo=request.POST.get('rollno12th')
        clgpercent=request.POST.get('percent12')
        emailId=request.POST.get('email')
        finance=request.POST.get('income')

        edu_details=EducationalDetailsForm(
            candidateId=user,
            tenthSchool=sch10,
            tenthBoard=scboard,
            tenthRollNo=schrollNo,
            tenthPercent=schpercent,
            clg12th=clgname,
            clgBoard=clgboard,
            rollNo12th=clgrollNo,
            pecentage12th=clgpercent,
            emailid=emailId,
            annualIncome=finance
        )

        edu_details.save()
        return redirect(reverse('submit_page'))

    return render(request,'applications/applicationForm2.html')


def personalFormsPage(request):
    if request.method=='POST':
        user=request.user
        cname=request.POST.get('name')
        cno=request.POST.get('cno')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        fname=request.POST.get('fname')
        focc=request.POST.get('focc')
        mname=request.POST.get('mname')
        mocc=request.POST.get('mocc')
        martialStats=request.POST.get('mstatus')
        ano=request.POST.get('ano')
        hno=request.POST.get('hno')
        stname=request.POST.get('stname')
        pcity=request.POST.get('pcity')
        pstate=request.POST.get('state')
        pPin=request.POST.get('pin')
        prehno=request.POST.get('prehno')
        preStreet=request.POST.get('prestname')
        precity=request.POST.get('precity')
        prestate=request.POST.get('prestate')
        prepin=request.POST.get('prepin')

        new_candidate=CandidateForm(
            appid=user,
            candidateName=cname,
            contactNo=cno,
            dateOfBirth=dob,
            gender=gender,
            fatherName=fname,
            foccupation=focc,
            motherName=mname,
            moccupation=mocc,
            martialStat=martialStats,
            AdhaarNo=ano,
            phouseno=hno,
            pstreetcolony=stname,
            pstate=pstate,
            ppincode=pPin,
            prehouseno=prehno,
            prestreetcolony=preStreet,
            prestate=prestate,
            prepincode=prepin
        )

        new_candidate.save()
        return redirect(reverse('educational_form_page'))

    return render(request,'applications/applicationForm.html')


def loginHandler(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pwd=request.POST.get('pwd')

        user=authenticate(request,email=email,password=pwd)
        if not user:
            return HttpResponse("you are not a registered applicant,register yourself now!!")

        login(request,user)    
        return redirect(reverse('personal_form_page'))
        

        
    

def registerHandler(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pwd1=request.POST.get('pwd1')
        pwd2=request.POST.get('pwd2')

        if pwd1!=pwd2:
            return HttpResponse('Enter Same password!!!')

        user = User.objects.create_user( email, pwd1,name=name)
        user.save()
        login(request,user) 
        return redirect(reverse('personal_form_page'))


def about(request):
    return HttpResponse('about')

def authPage(request):
    return render(request,'applications/login.html')