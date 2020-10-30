from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SchoolRegisterForm,SchoolUpdateForm,UserUpdateForm



def register(request):
    if request.method == 'POST':
        form = SchoolRegisterForm(request.POST)
        #s_profile_form = SchoolProfileForm(request.POST)
        if form.is_valid():#and s_profile_form.is_valid():
            form.save()
            #request.user.refresh_from_db()  
            #s_profile_form.full_clean()
            #s_profile_form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('dashboard')
    else:
        form = SchoolRegisterForm()
        #s_profile_form = SchoolProfileForm()
    return render(request, 'accounts/register.html', {'form': form })


# def register(request):
#     if request.method == 'POST':
#         form = SchoolRegisterForm(request.POST)
#         s_profile_form = SchoolProfileForm(request.POST)
#         if form.is_valid() and s_profile_form.is_valid():
#             form.save()
#             request.user.refresh_from_db()
#             s_profile_form = SchoolProfileForm(request.POST, instance=request.user.schoolprofile)
#             s_profile_form.full_clean()
#             s_profile_form.save()
            
#             messages.success(request, f'Your account has been created! You are now able to log in!')
#             return redirect('dashboard')

#             # if form.is_valid():
#             # instance = form.save(commit=False)
#             # instance.user = request.user
#             # instance.save()


#     else:
#         form = SchoolRegisterForm()
#         s_profile_form = SchoolProfileForm()
#     return render(request, 'accounts/register.html', {'form': form,'s_profile_form':s_profile_form})

@login_required
def profile(request):
    return render(request,'accounts/profile.html')


@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = SchoolUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.school)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = SchoolUpdateForm(instance=request.user.school)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }


    return render(request, 'accounts/profile-update.html',context)