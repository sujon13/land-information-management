from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response


from lands.forms import SignUpForm
from lands.models import Land,Tax
from lands.models import User as mUser

# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):


    return render(request,'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=mUser()

            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user.user_id=username
            user.password=raw_password
            user.email=form.cleaned_data.get('email')
            user.full_name=form.cleaned_data.get('full_name')
            user.address = form.cleaned_data.get('address')
            user.city = form.cleaned_data.get('city')
            user.state = form.cleaned_data.get('state')
            user.country = form.cleaned_data.get('country')
            user.save()


            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})






def myland(request):
    userid=request.user.username
    user=mUser.objects.filter(user_id=userid)

    land_results=Land.objects.filter(
        owners=user
    )
    return render_to_response('myLands.html', {'results': land_results,'curUser':userid})

def changeSaleStatus(request, land_id):
    try:
        land = Land.objects.get(pk=land_id)
    except:
        Http404("ERROR")
    userid = request.user.username
    user = mUser.objects.filter(user_id=userid)
    if land.up_for_sale=="yes":
        land.up_for_sale="no"
    else:
        land.up_for_sale="yes"

    land.save()
    land_results = Land.objects.filter(owners=user)

    return HttpResponseRedirect('/mylands/', {'results': land_results, 'curUser': userid})

def myProfile(request):

    user=mUser.objects.filter(user_id=request.user.username)

    return render_to_response('profile.html', {'result': user})

def searchland(request):
    try:
        lands = Land.objects.filter(up_for_sale='yes')
    except:
        Http404("ERRROR")



    if request.POST.get('form_type') == "searchland":
        division = request.POST.get('division')
        dist = request.POST.get('dist')
        upazilla = request.POST.get('upazilla')
        mouja = request.POST.get('mouja')
        dag = request.POST.get('dag')
        catagory = request.POST.get('catagory')
        area = request.POST.get('area')

        selected = []
        for land in lands:
           if  (division is not None and division==land.division or division) and\
               (dist is not None and dist == land.zilla or dist) and\
               (upazilla is not None and upazilla == land.upazilla or upazilla) and\
               (mouja is not None and mouja == land.mouja or mouja) and\
               (dag is not None and dag == land.dag_no or dag) and\
               (catagory is not None and catagory == land.catagory or catagory) and\
               (area is not None and area == land.area or area):

                selected.append(land)
        return render(request, 'searchLand.html', {'lands': selected})


    return render(request, 'searchLand.html', {'lands':lands})


