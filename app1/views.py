from django.shortcuts import render,redirect
from .models import user,categry,subcategory,expert_tbl,question,Pending,tbl_answer

from django.contrib import messages
# Create your views here.
def indez(request):
    return render (request,"indez.html")


def login(request):
    request.session['email']='null'
    request.session['password'] = 'null'
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if user.objects.filter( email=email,password=password ).exists():
            request.session['email']=email
            request.session['password'] =password
            return redirect ('user/')
        elif expert_tbl.objects.filter(email=email, password=password, status=1).exists():
            request.session['email'] = email
            request.session['password'] = password
            return redirect('expert/')
        else:
            messages.error(request, '!!!invaild login credentials')
            return redirect('/login/')

    return render (request,"LOGIN.html")

def reg1(request):
    request.session['email']='null'
    request.session['password']='null'
    category={
        'c_det':categry.objects.all(),
    }

    if request.method == "POST":
        f_name = request.POST.get("f_name")

        mobile = request.POST.get("m_number")
        email = request.POST.get("email")
        password = request.POST.get("password")
        category1 = request.POST.get("category1")
        interest = request.POST.get("interest")
        fileToUpload = request.FILES.get("fileToUpload")
        if expert_tbl.objects.filter(email=email).exists():
            messages.info(request, "email already exist")
            redirect('/reg1/')
        else:

          new_reg = expert_tbl.objects.create(f_name=f_name, mobile=mobile, password=password, email=email, interest=interest, cat=category1, fileToUpload=fileToUpload)
          new_reg.save()
          messages.info(request, "successfully registered")
          return redirect('/')

    return render (request,"REGISTER1.html",category)
def reg2(request):
    if request.method=="POST":
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        mobile = request.POST.get("m_number")
        email = request.POST.get("email")
        password = request.POST .get("password")
        gender = request.POST .get("gender")
        if user.objects.filter(email=email).exists():
            messages.info(request,"email already exist")
            redirect('/reg2/')
        else:
            new_reg = user(f_name=f_name, l_name=l_name, mobile=mobile,password=password, email=email, gender=gender)
            new_reg.save()
            messages.info(request, "successfully registered")
            return redirect('/')
    return render (request,"REGISTER2.html")

def expert(request):
    if  request.session['email'] == 'null':
        return redirect('/login/')
    email=request.session['email']
    content= {
        'email':email
    }
    return render (request,"expert_index.html",content)

def expert_profile(request):

    if request.session['email']=='null':
        return redirect('/login/')
    else:
     email=request.session['email']
     content={
        'r_det':expert_tbl.objects.get(email=email)
         }


    return render (request,"expert_profile.html",content)


def expert_eprofile(request):
    if request.session['email']=='null':
        return redirect('/login/')
    else:

     email=request.session['email']
     if request.method == "POST":
         f_name = request.POST.get("f_name")
         l_name = request.POST.get("l_name")
         mobile = request.POST.get("m_number")

         person = user.objects.get(email=email)
         person.f_name=f_name
         person.l_name = l_name
         person.mobile = mobile

         person.save()
         return redirect('/public_profile/')
     content={
        'r_det':expert_tbl.objects.get(email=email)
     }
    return render (request,"public_eprofile.html",content)

def question_list(request):
    if request.session['email'] == 'null':
        return redirect('/login/')
    else:
        email = request.session['email']
        exp=expert_tbl.objects.get(email=email)
        a=exp.cat
        b=categry.objects.get(cat=a)
        qs=question.objects.filter( categry=b,question_status=0)
        content={
            'qs_list':qs

        }

        return render(request, "qs_list.html", content)



def pending(request,id):
    if request.session['email'] == 'null':
        return redirect('/login/')
    else:
        email = request.session['email']
        exp=expert_tbl.objects.get(email=email)
        question1=question.objects.get(id=id)
        pen=Pending(expert=exp,question=question1)
        pen.save()
        return redirect('/question_list/')


def pending_question(request):
    if request.session['email'] == 'null':
        return redirect('/login/')
    else:
        email = request.session['email']
        exp = expert_tbl.objects.get(email=email)
        # a = exp.cat
        # b = categry.objects.get(cat=a)
        qs = Pending.objects.filter(expert=exp,status=1)
         # final_qs = Pending.objects.filter(expert=exp,question=qs)

        content = {
            'qs_list': qs

        }

        return render(request, "pending_question.html", content)

def qs_approve(request,id):
    if request.session['email'] == 'null':
        return redirect('/login/')
    else:
        # email = request.session['email']
        # exp = expert_tbl.objects.get(email=email)

        p_qs=Pending.objects.get(id=id)
        p_qs.status=0
        p_qs.save()
        qs=p_qs.question
        qs.question_status=1
        qs.expert=p_qs.expert.email
        qs.save()
        new_ans=tbl_answer.objects.create(pending=p_qs)
        new_ans.save()
        # qs = Pending.objects.filter(expert=exp)
         # final_qs = Pending.objects.filter(expert=exp,question=qs)
    return redirect ('/user_req_ques/')

def approved_qs(request):
    if request.session['email'] == 'null':
        return redirect('/login/')
    else:
        email = request.session['email']
        exp = expert_tbl.objects.get(email=email)
        qs = tbl_answer.objects.filter(pending__expert=exp)
        content={
            'qs_list':qs
        }

    return render(request, "qs_approved.html", content)




def answering(request,id):
    if request.session['email'] == 'null':
        return redirect('/login/')
    qs=tbl_answer.objects.get(id=id)
    if request.method=="POST":
        ans= request.POST.get("ans")
        qs.answer=ans
        qs.status=1
        qs.save()
    return redirect('/approved_qs/')




def delete_pending_question(request,id):
    if request.session['email'] == 'null':
        return redirect('/login/')
    else:
        Pending.objects.get(id=id).delete()
        return redirect ('/pending_question/')


def logout(request):
    request.session['email'] = 'null'
    request.session['password'] = 'null'
    return redirect('/login/')

def passwrd(request):

    return render (request,"passwrd.html")

def user1(request):
    email = request.session['email']
    category = {
        'r_det': user.objects.get(email=email),
    }

    return render (request,"index.html",category)




def answer(request):
    if request.session['email']=='null':
        return redirect('/login/')
    else:
      email=request.session['email']
      if request.method == "POST":
            user1=user.objects.get(email=email)
            catgry = request.POST.get("category1")
            cate = categry.objects.get(cat=catgry)
            qus = request.POST.get("questions")

            datee = request.POST.get("duration")

            new_qs = question(person=user1, question=qus,   e_date=datee, categry=cate)
            new_qs.save()
            return redirect('/answer/')
      cat={
        'c_det':categry.objects.all(),
      }

    return render (request,"answer.html",cat)

def user_added_questions(request):
    if request.session['email']=='null':
        return redirect('/login/')
    else:
      email=request.session['email']
      person=user.objects.get(email=email)
      qs={
          "ques":question.objects.filter(person=person)
      }

      return render (request,"user_added_qs.html",qs)


def de_user_ques(request,id):
    if request.session['email'] == 'null':
        return redirect('/login/')
    else:
        question.objects.get(id=id).delete()
        return redirect ('/user_added_questions/')

def user_req_ques(request):
    if request.session['email']=='null':
        return redirect('/login/')
    else:
      email=request.session['email']
      person=user.objects.get(email=email)
      qs={
          "ques":Pending.objects.filter(question__person=person)
      }

      return render (request,"user_req_ques.html",qs)

def user_ans_ques(request):
    if request.session['email']=='null':
        return redirect('/login/')
    else:
      email=request.session['email']
      person=user.objects.get(email=email)
      qs={
          "ques":tbl_answer.objects.filter(pending__question__person=person, status = 1 )
      }

      return render (request,"user_ans_ques.html",qs)


def public_profile(request):
    if request.session['email']=='null':
        return redirect('/login/')
    else:
     email=request.session['email']
     content={
        'r_det':user.objects.get(email=email)
         }


    return render (request,"public_profile.html",content)


def public_eprofile(request):
    if request.session['email']=='null':
        return redirect('/login/')
    else:

     email=request.session['email']
     if request.method == "POST":
         f_name = request.POST.get("f_name")
         l_name = request.POST.get("l_name")
         mobile = request.POST.get("m_number")

         person = user.objects.get(email=email)
         person.f_name=f_name
         person.l_name = l_name
         person.mobile = mobile

         person.save()
         return redirect('/public_profile/')
     content={
        'r_det':user.objects.get(email=email)
     }



    return render (request,"public_eprofile.html",content)













