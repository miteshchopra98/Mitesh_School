from django.shortcuts import *
from users.forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
User = get_user_model()

# Create your views here.

def StudentProfileView(request, pid):
    orders = Order.objects.filter(order_by = request.user.id)
    studentuser = Student.student.get(id=pid)
    studentsports = StudentCompetition.objects.filter(comp=pid)
    # print(studentsports)
    l=[]
    for i in studentsports:
        if i.sport not in l:
            l.append(i.sport)
    print(l)
    # print(studentsports.distinct())
    studentprof = StudentProfile.objects.get(user=pid)
    prepopulatedmks = StudentMarks.objects.get(st_mk=pid)
    form = StudentMarksForm(request.POST or None, instance = prepopulatedmks)
    
    
    
    if request.method == 'POST':
        if form.is_valid():
            english = form.data.get('English')
            hindi = form.data.get('Hindi')
            marathi = form.data.get('Marathi')
            maths = form.data.get('Maths')
            science = form.data.get('Science')
            total = form.data.get('Total')
            
            StudentMarks.objects.filter(st_mk=pid).update(English = english, Hindi = hindi,Marathi = marathi,Maths = maths,Science = science,
                                    Total = total)
            
        
        return redirect('schoolapp:studentlist')
    studentmks = StudentMarks.objects.get(st_mk=pid)
    context ={
        'orders':orders,
        'studentuser':studentuser,
        'studentprof':studentprof,
        'studentmks':studentmks,
        'studentsports':l,
        'form':form
        }

    return render(request, 'users/studentprofile.html', context)

def TeacherProfileView(request, pid):
    teacheruser = Teacher.teacher.get(id=pid)
    teacherprof = TeacherProfile.objects.get(user=pid)
    context ={
        'teacheruser':teacheruser,
        'teacherprof':teacherprof
        }

    return render(request, 'users/teacherprofile.html', context)

def AdminProfileView(request, pid):
    user = User.objects.get(id=pid)
    context ={
        'user':user,
        }

    return render(request, 'users/adminprofile.html', context)

def Student_Register(request):

    
    form = StudentRegisterForm(request.POST or None)

    if request.method == 'POST':
        
        if form.is_valid():
            role = form.data.get('role')
            password1 = form.cleaned_data.get('password1')
            username1 = form.data.get('username')
            fname = form.data.get('first_name')
            lname = form.data.get('last_name')
            email = form.data.get('email')
            dob = form.data.get('dob')
            
            if role == 'STUDENT':
                Student.objects.create_user(username = username1, password = password1,
                                            first_name = fname, last_name = lname, email = email, dob=dob)
                
                messages.success(
                request,
                'You have successfully registered for Student Role'
            )
                return redirect('schoolapp:index')
            else:
             messages.success(
                    request,
                    'Choose Student role only'
                   )
             return redirect('users:studentreg')
        else:
            username1 = form.data.get('username')
            password1 = form.data.get('password1')
            password2 = form.data.get('password2')
            role = form.data.get('role')

            userexists = User.objects.filter(username = username1).exists()

            if userexists:
                        messages.success(
                        request,
                        'Username already exists'
                    )
            elif password1 != password2:
                        messages.success(
                        request,
                        'Password does not match'
                    )

        
        

    context={
        'form':form
        }

    return render(request, 'users/student-form.html', context)

def Teacher_Register(request):

    
    form = TeacherRegisterForm(request.POST or None)

    if form.is_valid():
        role = form.data.get('role')
        password1 = form.cleaned_data.get('password1')
        username1 = form.data.get('username')
        fname = form.data.get('first_name')
        lname = form.data.get('last_name')
        email = form.data.get('email')
        dob = form.data.get('dob')
            
        if role == 'TEACHER':
            Teacher.objects.create_user(username = username1, password = password1,
                                        first_name = fname, last_name = lname, email = email, dob=dob)
            messages.success(
                    request,
                    'You have successfully registered  for Teacher Role'
                   )    
            return redirect('schoolapp:index')
        else:
             messages.success(
                    request,
                    'Choose Teacher role only'
                   )
             return redirect('users:teacherreg')
    else:
        username1 = form.data.get('username')
        password1 = form.data.get('password1')
        password2 = form.data.get('password2')
        role = form.data.get('role')

        userexists = User.objects.filter(username = username1).exists()

        if userexists:
                    messages.success(
                    request,
                    'Username already exists'
                   )
        elif password1 != password2:
                    messages.success(
                    request,
                    'Password does not match'
                   )

        
    context={
        'form':form
        }

    return render(request, 'users/teacher-form.html', context)

def Admin_Register(request):

    
    form = AdminRegisterForm(request.POST or None)

    if request.method == 'POST':
        
        if form.is_valid():
            role = form.data.get('role')
            password1 = form.cleaned_data.get('password1')
            username1 = form.data.get('username')
            fname = form.data.get('first_name')
            lname = form.data.get('last_name')
            email = form.data.get('email')
            dob = form.data.get('dob')
            
            if role == 'ADMIN':
                User.objects.create_user(username = username1, password = password1,
                                            first_name = fname, last_name = lname, email = email, dob=dob)
                
                messages.success(
                request,
                'You have successfully registered for Admin Role'
            )
                return redirect('schoolapp:index')
            else:
             messages.success(
                    request,
                    'Choose Admin role only'
                   )
             return redirect('users:adminreg')
        else:
            username1 = form.data.get('username')
            password1 = form.data.get('password1')
            password2 = form.data.get('password2')
            role = form.data.get('role')

            userexists = User.objects.filter(username = username1).exists()

            if userexists:
                        messages.success(
                        request,
                        'Username already exists'
                    )
            elif password1 != password2:
                        messages.success(
                        request,
                        'Password does not match'
                    )

        
        

    context={
        'form':form
        }

    return render(request, 'users/admin-form.html', context)

def Login_view(request):

    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print(user)

        if user is None:
            messages.success(
                request,
                'Username or Password is not valid'
            )
            return redirect('users:login')

        elif user.is_superuser:
            login(request, user)
            messages.success(
                request,
                'Admin {}, you have been successfully logged in'.format(username)
            )
            return redirect('schoolapp:index')

        elif user.role == "TEACHER":
            login(request, user)
            messages.success(
                request,
                '{} Teacher, you have been successfully logged in'.format(username)
            )
            return redirect('schoolapp:index')
        
        elif user.role == 'STUDENT':
            login(request, user)
            messages.success(
                request,
                '{} Student, you have been successfully logged in'.format(username)
            )
            return redirect('schoolapp:index')
        
        elif user is not None:
            login(request, user)
            messages.success(
                request,
                '{}, you have been successfully logged in'.format(username)
            )
            return redirect('schoolapp:index')

            
        
        
    context = {

        }
    return render(request, 'users/login.html', context)

def Logout_view(request):
    

    if request.method == 'POST':
        logout(request)
        messages.success(
            request,
            'You have been logged out'
        )
        return redirect('schoolapp:index')

    return render(request, 'users/logout.html')

def CompetitionForm(request):
    form = StudentCompetitionForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        
        if form.is_valid():
            # sname = form.data.get('sport')
            # sdesc = form.data.get('sport_desc')
            # simage = form.data.get('sport_image')
            # StudentCompetition.objects.create(sport=sname, sport_desc=sdesc,sport_image=simage)
            form.save()
        
        return redirect('schoolapp:index')
    
    
    context ={
        # 'studentuser':studentuser,
        # 'studentprof':studentprof,
        
        'form':form

        }

    return render(request, 'users/compform.html', context)

def CompetitionApply(request,pid):
    form = StudentCompetitionForm(request.POST or None)
    stid=request.user.id
    student = Student.student.get(id=stid)
    s = StudentCompetition.objects.get(pk=pid)
    sport = s.sport
    sport_desc = s.sport_desc
    sport_image = s.sport_image
    StudentCompetition.objects.create(comp=student, sport = sport, sport_desc = sport_desc,  sport_image = sport_image)
    context = {
        'form':form,
        's':s
        }

    return render(request, 'users/compapplyform.html', context)

def Products(request):
    products = Product.objects.all()
    order = Order.objects.all()
    context={
        'products':products,
        'order':order
        }
    return render(request, 'users/product.html',context)

def Orders(request,pid):
    orders = Order.objects.all()
    products = Product.objects.all()
    p = Order.objects.filter(prod_ordered=pid)
    a = Product.objects.get(id=pid)
    
    uid=request.user.id
    p1 = Order.objects.filter(order_by=uid).exists()
    p2 = Order.objects.filter(order_by=uid,prod_ordered=pid).exists()
    # print(p1)
    # print(p2)


    if p1:
        if p2:
            if request.method == 'POST':
                Order.objects.filter(order_by=uid,prod_ordered=pid).update(order_by = request.user, prod_ordered=a,order_count = request.POST.get('count'))
    
        else:
            Order.objects.create(order_by = request.user, prod_ordered=a)
            
    else:
        Order.objects.create(order_by = request.user, prod_ordered=a)



      
    price = Product.objects.filter(id=pid).values()
    prod_price = price[0]
  

    
    quantity = Order.objects.filter(order_by=uid).values()
    print(quantity)
   
    a=quantity[0]
    
    Total_price =0
    l = []
    
    for i in quantity[:]:
        prod = Product.objects.filter(id = i['prod_ordered_id']).values()
        pri = prod[0]
        
        price = pri['prod_price']
        sum1 = i['order_count']
        

        Total_price = price * sum1
        l.append(Total_price)
    print(l)
    Final_price = sum(l)
    print(Final_price)
    # count =quantity[0]
    # print(count['order_count'])


    orders = Order.objects.filter(order_by=uid)

  
    # for i in order:
    #     print('UID =',uid)
    #     print(i['order_by_id'])
    #     print('PID =',pid)
    #     print(i['prod_ordered_id'])
        
    #     if i['order_by_id'] == uid:
    #         if i['prod_ordered_id'] == pid:
    #             print('1st if block')
    #             print('UID =',uid)
    #             print('PID =',pid)
    #             continue
               
    #         else:
    #             p = Product.objects.get(prod_id=pid)
    #             Order.objects.create(order_by=request.user,prod_ordered=p)
    #             print('1st else block')
    #             print('UID =',uid)
    #             print('PID =',pid)
    #             break
    # else:
    #     print('for loop else block')
    #     print('UID =',uid)
    #     print('PID =',pid)
    #     if order_name in order:
    #         print('for loop else if else block')
    #         print('UID =',uid)
    #         print('PID =',pid)
    #         pass
    #     else:
    #         print('for loop el if else else block')
    #         print('UID =',uid)
    #         print('PID =',pid)
    #         p = Product.objects.get(prod_id=pid)
    #         Order.objects.create(order_by=request.user,prod_ordered=p)
            
    
    # # print(price)




        
    context={
        # 'order_name':order_name,
        'p':p,
        'p1':p,
        # 'price':price,
        'total':Final_price,
        'orders':orders,
        'products':products,
        }
    return render(request ,'users/order.html',context)

def CreateProducts(request):

    form  = ProductForm(request.POST or None, request.FILES or None)
    context={
        'form':form
        }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # added_by = request.user
            # prodid = form.data.get('prod_id')
            # prodname = form.data.get('prod_name')
            # proddesc = form.data.get('prod_desc')
            # prodprice = form.data.get('prod_price')
            # prodimg = form.data.get('prod_img')

            # Product.objects.create(added_by=added_by, prod_id = prodid, prod_name=prodname, prod_desc=proddesc, prod_price=prodprice, prod_img=prodimg)
           
    return render(request, 'users/product-form.html',context)

def UpdateProducts(request):

    context={
        }
    return render(request, 'users/product-form.html',context)

def DeleteProducts(request):

    context={
        }
    return render(request, 'users/product-delete.html',context)















