from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from .models import *

# Create your views here.
def home(request):
    return render(request,'homepage.htm')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the form to get the user instance
            Profile.objects.get_or_create(user=user)
            return redirect("login")
    elif request.user.is_authenticated:
        return redirect('dashboard')        
    else:
        form = RegistrationForm()
    return render(request, "register/register.html", {'form': form})


def login_user(request):
    if request.method == "POST" :
        log=LoginForm(request.POST)
        if log.is_valid():
            cl=log.cleaned_data.get
            username=cl('username')
            passwd=cl("password")
            user= authenticate(username=username,password=passwd)
            if user is not None:
                login(request,user)
                messages.success(request,f"{username},you have logged in successfully")
                return redirect('dashboard')
            else:
                messages.error(request,"username or password does not match")
        else:
            messages.error(request,"form is invalid")
    else:
        log=LoginForm()
    return render(request,'register/login.html',{'form':log})    

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    user = request.user
    # Use parentheses to call the count method
    post_count = Post.objects.count()
    cosm_count = Cosmetics.objects.count()
    posted_posts = Post.objects.all()
    lessons_count = Learning.objects.count()
    category_count = Category.objects.count()
    
    prof = None  # Initialize prof to None

    if user.is_authenticated:
       prof = get_object_or_404(Profile, user=request.user)

    context = {
        'post_count': post_count,
        'cosmetics_count': cosm_count,
        'posted_posts': posted_posts,
        'lessons_count': lessons_count,
        'category_count': category_count,
        'profile': prof
    } 
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def user_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserProfileForm(request.POST, instance=user.profile)

        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')  # Replace 'profile' with the actual URL name for the user profile page
        else:
            messages.error(request, 'Error updating profile. Please correct the errors below.')

    else:
        form = ProfileForm(instance=profile)
        user_form = UserProfileForm(instance=user.profile)

    context = {
        'form': form,
        'user_form': user_form,
        'profile':profile
    }

    return render(request, 'dashboard/profile.html', context)
@login_required
def Create_post(request):
    user=request.user
    if request.method=='POST':
        post=PostForm(request.POST,request.FILES)
        if post.is_valid():
            sav= post.save(commit=False)
            sav.author=user
            sav.save()
            return redirect('post_list')
        else:
            messages.error(request,'there are some missing fields')    
    else:
      post=PostForm()
    return render(request,'dashboard/create_post.htm',{'post':post})

def edit_post(request,id):
    pos=Post.objects.get(id=id)
    if request.method=='POST':
        post=PostForm(request.POST,request.FILES)
        if post.is_valid():
            post.save()
            return redirect('post_list')
        else:
            messages.error(request,'there are some missing fields')    
    else:
      post=PostForm(instance=pos)
    return render(request,'dashboard/post/edit_post.html',{'post':post})


def post_list(request):
    user=request.user
    post=Post.objects.all()
    return render(request,'dashboard/post/post_list.html',{'posts':post}) 

def delete_post(request,id):
    
    post=Post.objects.get(id=id)
    post.delete()

    return redirect('dashboard')

def post_detail(request,id):
    post=Post.objects.get(id=id)
    
    if request.method=='POST':
        comform=CommentForm(request.POST)
        if comform.is_valid():
            form=comform.save(commit=False)
            form.author=request.user.username
            form.post=post.title
            form.save()
    else:
        comform=CommentForm()  
    context={ 'post':post,
            
             'form':comform }         
    return render(request,'dashboard/post/post_detail.html',context)

def cosmetics_display(request):
    cosm=Cosmetics.objects.all()
    return render(request,'dashboard/cosmetics.html',{'cosmetics':cosm})

def cosmetics_edit(request):
    cosm=Cosmetics.objects.get(id=id)
    if request.method=="POST":
        cosmform=CosmeticsForm(request.POST,request.FILES)
        if cosmform.is_valid():
            cosmform.save()
    else:
        cosmform=CosmeticsForm(instance=cosm)        
    return render(request,'dashboard/edit_cosmetics.html',{'cosmetic':cosm,'form':cosmform})

def cosmetics_create(request):
    if request.method=="POST":
        cosmform=CosmeticsForm(request.POST,request.FILES)
        if cosmform.is_valid():
            cosmform.save()
    else:
        cosmform=CosmeticsForm()        
    return render(request,'dashboard/cosm/create_cosmetics.html',{'form':cosmform})


def delete_cosmetics(request,id):  
    cosmetics=Cosmetics.objects.get(id=id)
    cosmetics.delete()
    return redirect("learning_list") 


def learning_list(request):
    learnings = Learning.objects.all()
    return render(request, 'dashboard/learn/learning_list.html', {'learnings': learnings})

def learning_detail(request, pk):
    learning = Learning.objects.get(pk=pk)
    return render(request, 'dashboard/learn/learning_detail.html', {'learning': learning})

def learning_create(request):
    if request.method == 'POST':
        form = LearningForm(request.POST, request.FILES)
        if form.is_valid():
            learning = form.save(commit=False)
            learning.user = request.user
            learning.save()
            return redirect('learning_list')
    else:
        form = LearningForm()
    return render(request, 'dashboard/learn/learning_form.html', {'form': form})

def learning_edit(request, pk):
    learning = Learning.objects.get(pk=pk)
    if request.method == 'POST':
        form = LearningForm(request.POST, request.FILES, instance=learning)
        if form.is_valid():
            form.save()
            return redirect('learning_list')
    else:
        form = LearningForm(instance=learning)
    return render(request, 'dashboard/learn/learning_form.html', {'form': form})

def learning_delete(request, pk):
    learning = Learning.objects.get(pk=pk)
    learning.delete()
    return redirect('learning_list')
    