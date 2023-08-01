from django.shortcuts import render
from django.http import *
from datetime import date
from .models import *
from matplotlib import pyplot as plt
from Profile.models import *

def complaintForm(request):                 # Rendering Complaint Form
    return render(request,'Addcomplaints/complaint.html')


def complaint(request):                     # Storing Complaint into Database
    if request.method=='POST':
        form_Data = request.POST

        Email = form_Data['email']
        type = form_Data['type']
        subject = form_Data['subject']
        complaint = form_Data['complaint']
        user = request.session['username']
        today = date.today()
        todays_Date = str(today.day)+'/'+str(today.month)+'/'+str(today.year)
        username = profile.objects.get(Email=Email)

        if type=='Exam':
            ExamComplaints(User=username,Subject=subject,Type_of_complaint=type,Description=complaint,Status='pending',Date=todays_Date,Email=Email).save()
        else:
            Complaints(User=username,Subject=subject,Type_of_complaint=type,Description=complaint,Status='pending',Date=todays_Date,Email=Email).save()      # Saving Complaint in Database
        return render(request,'Addcomplaints/complaint.html',{'msg':"Complaint Added Successfully!!"})
    else:
        return render(request,'Addcomplaints/complaint.html')
    


def anonymousComplaintForm(request):                      # Rendering Anonymous Complaint Form
    return render(request,'Addcomplaints/anonymous.html')


def anonymousComplaint(request):                          # Storing Anonymous Complain form data into DB
    if request.method == 'POST':
        form_Data = request.POST
        Name = form_Data['name']
        Email = form_Data['email']
        Department = form_Data['department']
        subject = form_Data['subject']
        complaint = form_Data['describe']

        today = date.today()
        todays_Date = str(today.day)+'/'+str(today.month)+'/'+str(today.year)
        
        # print(Name,type(Name))
        # print(Email,type(Email))
        # print(Department,type(Department))
        # print(subject,type(subject))
        # print(complaint,type(complaint))
        # print(todays_Date,type(todays_Date))
        cmt = AnonymousComplaint(Subject=subject,Description=complaint,Status='pending',Date=todays_Date)
        cmt.save()                                 # Saving anonymous form data into Database
        AnonymousComplaintUser(Name=Name,Email=Email).save()
        return render(request,'Addcomplaints/anonymous.html',{"MSG":"Complaint Added Successfully"})
    else:
        return render(request,'Addcomplaints/anonymous.html')


def solvedComplaints(request):                           # Display solved complaints data
    obj = Complaints.objects.filter(Email=request.session['username'],Status='solved')
    complaints = []
    id=1
    username = profile.objects.get(Email=request.session['username'])
    for complaint in obj:
        data = [username,complaint.Subject,complaint.Type_of_complaint,complaint.Description,complaint.Status,complaint.Date]
        complaints.append(data)
        id+=1    
    complaintsObj = {'complaints':complaints}
    return render(request,'Addcomplaints/solved.html',complaintsObj)
   

def unSolvedComplaints(request):                        # Display unsolved complaints data
    obj = Complaints.objects.filter(Email=request.session['username'],Status='pending')
    complaints = []
    id=1
    username = profile.objects.get(Email=request.session['username'])
    for complaint in obj:
        data = [username,complaint.Subject,complaint.Type_of_complaint,complaint.Description,complaint.Status,complaint.Date]
        complaints.append(data)
        id+=1    
    complaintsObj = {'complaints':complaints}
    return render(request,'Addcomplaints/unsolved.html',complaintsObj)
   

def inProcessComplaints(request):                       # Display in process complaints data
    obj = Complaints.objects.filter(Email=request.session['username'],Status='process')
    complaints = []
    id=1
    username = profile.objects.get(Email=request.session['username'])
    for complaint in obj:
        data = [username,complaint.Subject,complaint.Type_of_complaint,complaint.Description,complaint.Status,complaint.Date]
        complaints.append(data)
        id+=1    
    complaintsObj = {'complaints':complaints}
    return render(request,'Addcomplaints/processing.html',complaintsObj)
   
def generate_graph(request):                    # Generate Statistics
    classroom_total = len(Complaints.objects.filter(Type_of_complaint='Classroom'))+len(ExamComplaints.objects.filter(Type_of_complaint='Classroom'))
    classroom_solved = len(Complaints.objects.filter(Type_of_complaint='Classroom',Status='solved'))+len(ExamComplaints.objects.filter(Type_of_complaint='Classroom',Status='solved'))
    classroom_unsolved = len(Complaints.objects.filter(Type_of_complaint='Classroom',Status='pending'))+len(ExamComplaints.objects.filter(Type_of_complaint='Classroom',Status='pending'))
    classroom_process = len(Complaints.objects.filter(Type_of_complaint='Classroom',Status='process'))+len(ExamComplaints.objects.filter(Type_of_complaint='Classroom',Status='process'))

    teacher_total = len(Complaints.objects.filter(Type_of_complaint='Teacher'))+len(ExamComplaints.objects.filter(Type_of_complaint='Teacher'))
    teacher_solved = len(Complaints.objects.filter(Type_of_complaint='Teacher',Status='solved'))+len(ExamComplaints.objects.filter(Type_of_complaint='Teacher',Status='solved'))
    teacher_unsolved =  len(Complaints.objects.filter(Type_of_complaint='Teacher',Status='pending'))+len(ExamComplaints.objects.filter(Type_of_complaint='Teacher',Status='pending'))
    teacher_process = len(Complaints.objects.filter(Type_of_complaint='Teacher',Status='process'))+len(ExamComplaints.objects.filter(Type_of_complaint='Teacher',Status='process'))

    management_total = len(Complaints.objects.filter(Type_of_complaint='Management'))+len(ExamComplaints.objects.filter(Type_of_complaint='Management'))
    management_solved = len(Complaints.objects.filter(Type_of_complaint='Management',Status='solved'))+len(ExamComplaints.objects.filter(Type_of_complaint='Management',Status='solved'))
    management_unsolved = len(Complaints.objects.filter(Type_of_complaint='Management',Status='pending'))+len(ExamComplaints.objects.filter(Type_of_complaint='Management',Status='pending'))
    management_process = len(Complaints.objects.filter(Type_of_complaint='Management',Status='process'))+len(ExamComplaints.objects.filter(Type_of_complaint='Management',Status='process'))

    college_total = len(Complaints.objects.filter(Type_of_complaint='College'))+len(ExamComplaints.objects.filter(Type_of_complaint='College'))
    college_solved = len(Complaints.objects.filter(Type_of_complaint='College',Status='solved'))+len(ExamComplaints.objects.filter(Type_of_complaint='College',Status='solved'))
    college_unsolved = len(Complaints.objects.filter(Type_of_complaint='College',Status='pending'))+len(ExamComplaints.objects.filter(Type_of_complaint='College',Status='pending'))
    college_process = len(Complaints.objects.filter(Type_of_complaint='College',Status='process'))+len(ExamComplaints.objects.filter(Type_of_complaint='College',Status='process'))


    exam_total = len(Complaints.objects.filter(Type_of_complaint='Exam'))+len(ExamComplaints.objects.filter(Type_of_complaint='Exam'))
    exam_solved = len(Complaints.objects.filter(Type_of_complaint='Exam',Status='solved'))+len(ExamComplaints.objects.filter(Type_of_complaint='Exam',Status='solved'))
    exam_unsolved = len(Complaints.objects.filter(Type_of_complaint='Exam',Status='pending'))+len(ExamComplaints.objects.filter(Type_of_complaint='Exam',Status='pending'))
    exam_process = len(Complaints.objects.filter(Type_of_complaint='Exam',Status='process'))+len(ExamComplaints.objects.filter(Type_of_complaint='Exam',Status='process'))


    other_total = len(Complaints.objects.filter(Type_of_complaint='Other'))+len(ExamComplaints.objects.filter(Type_of_complaint='Other'))
    other_solved = len(Complaints.objects.filter(Type_of_complaint='Other',Status='solved'))+len(ExamComplaints.objects.filter(Type_of_complaint='Other',Status='solved'))
    other_unsolved = len(Complaints.objects.filter(Type_of_complaint='Other',Status='pending'))+len(ExamComplaints.objects.filter(Type_of_complaint='Other',Status='pending'))
    other_process = len(Complaints.objects.filter(Type_of_complaint='Other',Status='process'))+len(ExamComplaints.objects.filter(Type_of_complaint='Other',Status='process'))


    no_of_comp = [x for x in range(0,max(classroom_total,teacher_total,management_total,college_total,exam_total,other_total)+2)]
    # print(max(classroom_total,teacher_total,management_total,college_total,exam_total,other_total))
    total = [classroom_total,teacher_total,management_total,college_total,exam_total,other_total]
    solved = [classroom_solved,teacher_solved,management_solved,college_solved,exam_solved,other_solved]
    unsolved = [classroom_unsolved,teacher_unsolved,management_unsolved,college_unsolved,exam_unsolved,other_unsolved]
    process = [classroom_process,teacher_process,management_process,college_process,exam_process,other_process]

    xlabel = ['Class','Teacher','Management','College','Exam','Other']
    plt.bar([i-0.2 for i in no_of_comp],total,width=0.2,label='total')
    plt.bar([i for i in no_of_comp],solved,width=0.2,label='solved')
    plt.bar([i+0.2 for i in no_of_comp],unsolved,width=0.2,label='unsolved')
    plt.bar([i+0.4 for i in no_of_comp],process,width=0.2,label='process')
    
    plt.ylabel("No of Complaints")
    plt.title("Complaints Statistics")
    plt.legend()
    plt.show()
    return HttpResponseRedirect('http://localhost:8000/Profile/')