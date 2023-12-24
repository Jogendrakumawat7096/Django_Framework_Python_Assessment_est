from django.shortcuts import render, redirect
from .models import Admin, Category, User ,Policy,PolicyRecord,Policyapply,Question
import random ,requests

def index(request):    
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

# Admin Views

def admin_login(request):
    if 'username' in request.session:
        return render(request, "admin-policy.html")

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            admin = Admin.objects.get(username=username)
            if password == admin.password:
                request.session['username'] = admin.username
                return redirect('adminbase')
            else:
                passmsg = "Password Does Not Matched"
                return render(request, "admin-login.html", {'passmsg': passmsg})
        except Admin.DoesNotExist:
            msg = "Username Does Not Exist"
            return render(request, "admin-login.html", {'msg': msg})

    return render(request, "admin-login.html")

def admin_logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('admin-login')

def admin_category(request):
    return render(request, "admin-category.html")

def admin_policy(request):
    return render(request, "admin-policy.html")



def admin_customer_quetion(request):
    quetion=Question.objects.all()
    return render(request, "admin-customer-quetion.html",{'quetion':quetion})

def send_message(request,pk):
    quetion=Question.objects.get(pk=pk)
    quetion.admin_comment=request.POST['feedback']
    quetion.save()
    quetion=Question.objects.all()
    return render(request, "admin-customer-quetion.html",{'quetion':quetion})

def adminbase(request):
    user=User.objects.all().count()
    policy=Policy.objects.all().count()
    quetion=Question.objects.all().count()
    category=Category.objects.all().count() 
    policyapply=Policyapply.objects.all().count()
    approvepolicyholder= Policyapply.objects.filter(status='Approved').count()
    disapprovepolicyholder= Policyapply.objects.filter(status='Disapproved').count()
    Pendingpolicyholder= Policyapply.objects.filter(status='Pending').count()
    
    
          
    return render(request, "adminbase.html",{'user':user,'policy':policy,'quetion':quetion,'category':category,'policyapply':policyapply,'approvepolicyholder':approvepolicyholder,'disapprovepolicyholder':disapprovepolicyholder,'Pendingpolicyholder':Pendingpolicyholder})

def add_category(request):
    if request.method == "POST":
        category_name = request.POST.get('categoryName')
        try:
            Category.objects.get(name=category_name)
            msg = 'This Category Already Added'
            return render(request, "add-category.html", {'msg': msg})
        except Category.DoesNotExist:
            Category.objects.create(name=category_name)
            msg = 'Category Add Successfully'
            return render(request, "add-category.html", {'msg': msg})
    return render(request, "add-category.html")

def admin_view_category(request):
    category = Category.objects.all()
    return render(request, "admin-view-category.html", {'category': category})

def admin_update_category(request):
    category = Category.objects.all()
    return render(request, "admin-update-category.html", {'category': category})

def admin_delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('admin-update-category')

def admin_edit_category(request, pk):
    if request.method == "POST":
        category_name = request.POST.get('categoryName')
        category = Category.objects.get(pk=pk)
        category.name = category_name
        category.save()
        return redirect('admin-update-category')
    else:
        category = Category.objects.get(pk=pk)
        return render(request, "admin-edit-category.html", {'category': category})
    
def admin_customer(request):
    users=User.objects.all()
    return render(request, "admin-customer.html", {'users': users})

def admin_customer_edit(request,email):
    user=User.objects.get(email=email)
    if request.method == "POST":
        user.name=request.POST['name']
        user.email=request.POST['email']
        user.mobile=request.POST['mobile']        
        user.image=request.FILES['image']
        user.save()
        msg="edit Succesed"
        return render(request, "admin-customer-edit.html", {'user': user,'msg':msg})
        
    return render(request, "admin-customer-edit.html", {'user': user})

def admin_customer_delete(request,email):
    user=User.objects.get(email=email)
    user.delete()
    return redirect('admin-customer')

def admin_view_policy(request):
    policy = Policy.objects.all()
    return render(request, "admin-view-policy.html", {'policy': policy})

def admin_add_policy(request):
    categories = Category.objects.all()

    if request.method == "POST":
        category_name = request.POST['category']
        policy_name = request.POST['policy_name']
        policy_desc = request.POST['policy_desc']
        sum_insurance = request.POST['sum_insurance']
        premium = request.POST['premium']
        tenure = request.POST['tenure']

        try:
            category = Category.objects.get(name=category_name)
            Policy.objects.create(
                category=category,
                policy_name=policy_name,
                policy_desc=policy_desc,
                sum_insurance=sum_insurance,
                premium=premium,
                tenure=tenure,
            )
            categories = Category.objects.all()
            msg = "Policy added successfully"
            return render(request, "admin-add-policy.html", {'categories': categories, 'msg': msg})
        except Exception as e:
            msg = f"Failed to add policy. Error: {str(e), str(policy_name)}"
            return render(request, "admin-add-policy.html", {'categories': categories, 'msg': msg})

    return render(request, "admin-add-policy.html", {'categories': categories})

def admin_update_policy(request):
    policy = Policy.objects.all()
    return render(request, "admin-update-policy.html", {'policy': policy})

def admin_policy_delete(request,pk):
    policy=Policy.objects.get(pk=pk)
    policy.delete()
    return redirect('admin-update-policy')

def admin_policy_edit(request,pk):
    policy=Policy.objects.get(pk=pk)
    categories = Category.objects.all()
    if request.method=='POST':
        category = Category.objects.get(name=request.POST['category'])
        policy.category = category
        policy.policy_name = request.POST['policy_name']
        policy.policy_desc = request.POST['policy_desc']
        policy.sum_insurance = request.POST['sum_insurance']
        policy.premium = request.POST['premium']
        policy.tenure = request.POST['tenure']
        policy.save()
        msg="Policy Edit Success"
        return render(request, "admin-policy-edit.html", {'policy': policy,'categories': categories,'msg':msg})
    
    return render(request, "admin-policy-edit.html", {'policy': policy,'categories': categories})

def admin_total_policy_holder(request):
    policyholder=Policyapply.objects.all()
    return render(request, "admin-total-policy-holder.html", {'policyholder': policyholder})

def admin_total_policy_approved_holder(request):
    policyholder=Policyapply.objects.filter(status='Approved')
    return render(request, "admin-total-policy-approved-holder.html", {'policyholder': policyholder})

def admin_total_policy_disaproved_holder(request):
    policyholder=Policyapply.objects.filter(status='Disapproved')

    return render(request, "admin-total-policy-disapproved-holder.html", {'policyholder': policyholder})

def admin_total_policy_pending_holder(request):
    policyholder=Policyapply.objects.filter(status='Pending')
    return render(request, "admin-total-policy-pending-holder.html", {'policyholder': policyholder})

def admin_approved_policy(request,pk):
    policyholder=Policyapply.objects.get(pk=pk)
    policyholder.status="Approved"
    policyholder.save()
    return redirect('admin-total-policy-holder')
# Customer Views

def customer_login(request):
    
    if 'email' in request.session:
        return render(request, "index.html") 

    if request.method == "POST":
        email= request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.password==password: 
                request.session['email'] = user.email                             
                request.session['profile_image'] = user.image.url
                return redirect('index') 
            else:
                msg="Password Does Not Matched"
                return render(request, "customer-login.html")
        except User.DoesNotExist:
                msg="email Does Not matched"
                return render(request, "customer-login.html")

    return render(request, "customer-login.html")

def customer_signup(request):
    if request.method == "POST":
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        try:
            User.objects.get(email=email)
            msg = "Email is already registered. Please enter another email id."
            return render(request, "customer-signup.html", {'msg': msg})
        except User.DoesNotExist:
            try:
                User.objects.get(mobile=mobile)
                msg = "Mobile number already registered. Please enter another mobile number."
                return render(request, "customer-signup.html", {'msg': msg})
            except User.DoesNotExist:
                if password == cpassword:
                    User.objects.create(
                        name=request.POST['name'],
                        image=request.FILES['profile_picture'],
                        email=email,
                        mobile=mobile,
                        password=password,
                    )
                    msg = "Sign up successful. Please log in."
                    return render(request, "customer-login.html", {'msg': msg})
                else:
                    msg = "Password and Confirm Password do not match."
                    return render(request, "customer-signup.html", {'msg': msg})

    return render(request, "customer-signup.html")

def customer_logout(request):
    if 'email' in request.session:
        del request.session['email']
        del request.session['profile_image']
    return redirect('customer-login')

def policies(request):
    policies=Policy.objects.all()
    customer = User.objects.get(email=request.session['email'])      
    return render(request, "policies.html", {'policies': policies})

def apply_policy(request, pk):
    policy = Policy.objects.get(pk=pk)
    customer = User.objects.get(email=request.session['email'])
    applied = Policyapply.objects.filter(policy=policy, customer=customer).exists()
    if not applied:
            Policyapply.objects.create(
            policy=policy,
            customer=customer,
        )

    policies = Policy.objects.all()
    return render(request, "policies.html", {'policies': policies, 'applied': applied})

def applied_policy(request):
    policies=Policyapply.objects.all()
    return render(request, "applied-policy.html",{'policies':policies})

def quetion_to_admin(request):
    user=User.objects.get(email=request.session['email'])
    quetion=Question.objects.all()
    return render(request, "quetion-to-admin.html",{'user':user,'quetion':quetion})

def submit_question(request):
    user=User.objects.get(email=request.session['email'])
    Question.objects.create(
        customer=user,
       description=request.POST['question'] 
    )
    msg="Message Sent Successfully" 
    quetion=Question.objects.all()   
    return render(request, "quetion-to-admin.html",{'user':user,'msg':msg,'quetion':quetion})

def forgot_password(request):
    if request.method == "POST":
        mobile = request.POST['mobile']
        user = User.objects.get(mobile=mobile)

        if user:
            otp = random.randint(1000, 9999)
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {
                "authorization": "VlO5sarhU8T76cPG0qMmvxHKYBiJ4DRZInEzfAF3L1pudekWCQf1t4D63AikUrC57TRZdJ8QMgGWbHYS",
                "variables_values": str(otp),
                "route": "otp",
                "numbers": mobile
            }
            headers = {'cache-control': "no-cache"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
            
            request.session['mobile'] = mobile
            return render(request, "otp.html", {'otp': otp})
        else:
            msg = "Mobile Number Not Exists"
            return render(request, "forgot-password.html", {'msg': msg})

    return render(request, "forgot-password.html")

def verify_otp(request):
    otp = request.POST['otp']
    if request.POST['uotp']==otp:
        return render(request,"new-password.html")
    else:
        msg = "Invalid otp"
        return render(request,"otp.html",{'msg':msg})

def new_password(request):
    if request.POST['password']==request.POST['cpassword']:
        mobile= request.session['mobile']
        user = User.objects.get(mobile=mobile)
        user.password=request.POST['password']
        user.save()
        return redirect('customer-login')
    else:
        msg= "password and confirm password does not matched"  
        return render(request,"new-password.html",{'msg':msg})