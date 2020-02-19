from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponse

from .forms import DonorForm
from .models import Donor, DonorHistory
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.models import  User
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
# Create your views here.
from django.views.generic import ListView , UpdateView , CreateView ,DetailView


#ddef home(request):
#    return render(request, 'home.html')

def index(request):
    if request.session.has_key('donor_email'):
        return render(request, 'index.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def register(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            return HttpResponse("hello")
        else:
            return HttpResponse("hi")
    else:
        return HttpResponse("hi")
        #return HttpResponse("hello")
        #return render(request, 'ibd/register.html')


def registersucess(request):
    if request.method == 'POST':
        donor_name = request.POST['Full_Name']
        blood_group = request.POST['Blood_Group']
        donor_std = request.POST['stdcode_id']
        donor_zip = request.POST['Pincode']
        donor_phone = request.POST['Mobile_Number']
        donor_email = request.POST['Email']
        donor_pass = request.POST['pwd']
        Donor.objects.create(donor_name=donor_name, blood_group=blood_group, donor_std=donor_std, donor_zip=donor_zip,
                             donor_phone=donor_phone, donor_email=donor_email,donor_pass=donor_pass)
        return render(request, 'ibd/registersuccess.html')
    else:
        error = 'Something went wrong'
    return render(request, 'ibd/index.html')

def detail(request, donor_id):
    donor = get_object_or_404(Donor, pk=donor_id)
    return render(request, 'ibd/detail.html', {'donor': donor})

class DonorList(ListView):
    model = Donor

class DonorDetail(DetailView):
    model = Donor

class UpdateDonor(UpdateView):
    model = Donor
    fields = ['donor_name','blood_group','donor_std','donor_zip','donor_phone','donor_email']
    success_url = '/'

class AddDonor(CreateView):
    model = Donor
    template_name = 'ibd/register.html'
    fields = ['donor_name','blood_group','donor_std','donor_zip','donor_phone','donor_email']
    success_url = '/'

def welcome (request):

    if request.session.has_key('donor_email'):
        donor_email = request.session['donor_email']
        d = get_object_or_404(Donor, donor_email=donor_email)
        donor = get_object_or_404(Donor, pk=d.id)
        return render(request, 'ibd/welcome.html', {'donor': donor})
    else:
        if request.method == 'POST':
            donor_email = request.POST['mobilenumber']
            donor_pass = request.POST['password']
            request.session['donor_email'] = donor_email
            try:
                d = get_object_or_404(Donor, donor_email=donor_email,donor_pass=donor_pass)
            except:
                return render(request, 'ibd/notfound.html')
            donor = get_object_or_404(Donor, pk=d.id)
            return render(request, 'ibd/welcome.html', {'donor': donor})

        else:
            error = 'Something went wrong'
        return render(request,'ibd/index.html')

def unsubscribe(request):
    return render(request, 'ibd/unsubscribe.html')

def forgetpwd(request):
    return render(request, 'ibd/forgetpwd.html')

def poster(request):
    return render(request, 'ibd/poster.html')

def privacypolicy(request):
    return render(request, 'ibd/privacypolicy.html')

def index(request):
    return render(request, 'ibd/index.html')

def thankyou(request):
    donor_phone = request.POST['txtno']
    donor_pass = request.POST['txtpwd']
    try:
         get_object_or_404(Donor, donor_phone=donor_phone,donor_pass=donor_pass)
    except:
        return render(request, 'ibd/notfound.html')
    Donor.objects.filter(donor_phone=donor_phone,donor_pass=donor_pass).delete()
    return render(request, 'ibd/thankyou.html')

def note(request):
    return render(request, 'ibd/note.html')

def update_profile(request,pk):
    donor = get_object_or_404(Donor, pk=pk)
    return render(request, 'ibd/update_profile.html', {"donor": donor})

def updatesucess(request,pk):
    if request.method == 'POST':
        donor_name = request.POST['Full_Name']
        blood_group = request.POST['Blood_Group']
        donor_std = request.POST['stdcode_id']
        donor_zip = request.POST['Pincode']
        donor_phone = request.POST['Mobile_Number']
        donor_email = request.POST['Email']
        try:
            d =  get_object_or_404(Donor, id=pk)
        except:
            return render(request, 'ibd/notfound.html')
        Donor.objects.filter(pk=d.id).update(donor_name=donor_name,blood_group=blood_group,donor_std=donor_std,donor_zip=donor_zip,donor_phone=donor_phone,donor_email=donor_email)
        return render(request, 'ibd/updatesuccess.html')
    else:
        error = 'Something went wrong'
        return render(request,'ibd/update_profile.html')

def chng_pwd(request,pk):
    donor = get_object_or_404(Donor, pk=pk)
    return render(request, 'ibd/chng_pwd.html', {"donor": donor})

def pwdchangesucess(request,pk):
    npwd = request.POST['npwd']
    cpwd = request.POST['cpwd']

    try:
        d = get_object_or_404(Donor, id=pk)
    except:
        return render(request, 'ibd/notfound.html')
    if npwd == cpwd :
        Donor.objects.filter(pk=d.id).update(donor_pass = npwd)
        return render(request, 'ibd/pwdchangesucess.html')
    else:
        return render(request, 'ibd/notmatch.html')


def user_history(request,pk):
    donor = get_object_or_404(Donor, pk=pk)
    result = DonorHistory.objects.filter(donors_hist=donor.id)
    context = {'donor':donor,'result':result}
    return  render(request, 'ibd/user_history.html', context)


def notmatch(request):
    return render(request, 'ibd/notmatch.html')

def inthenews(request):
    return render(request, 'ibd/inthenews.html')

def donorsfaqs(request):
    return render(request, 'ibd/donorsfaqs.html')


def logout(request):
    try:
        del request.session['donor_email']
    except KeyError:
        pass

    return render(request, 'ibd/logout.html')
