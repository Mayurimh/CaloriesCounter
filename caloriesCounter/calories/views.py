from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate,logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        initial_data={'username':'','password1':'','password2':''}
        form = SignUpForm(initial=initial_data)
    return render(request, 'myapp/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'home.html')


# @login_required
def add_food(request):
    if request.method == 'POST':
        form = fooditemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = fooditemForm()
    return render(request, 'myapp/add_food.html', {'form': form})

# @login_required
def add_user_entry(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        userConsume = FoodItems.objects.get(name=food_consumed)
        user = request.user
        userConsume = consume(user=user, food_consumed=userConsume)
        userConsume.save()
        foods= FoodItems.objects.all()
    else:
        foods= FoodItems.objects.all()
    consumed_food = consume.objects.filter()
    return render(request, 'myapp/addUserFood.html', {'foods': foods, 'consumed_food': consumed_food})

# @login_required
def select_food(request):
    food_items = FoodItems.objects.all()
    return render(request, 'myapp/select_food.html', {'food_items': food_items})


def delete_consume(request, id):
    consumed_food = consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('add_user_entry')
    return render(request, 'myapp/delete.html')  


# def calculate_calorie(request):
#     fooditems=FoodItems.objects.all()
#     myfilter =fooditemFilter(request.GET,queryset=fooditems)
#     fooditems=myfilter.qs
#     userfood=consume.objects.all()
#     myfooditems=userfood.filter()
#     cnt=myfooditems.count()
#     querysetFood=[]
#     for food in myfooditems:
#         querysetFood.append(food.food_by_user.all())
#     finalFoodItems=[]
#     for items in querysetFood:
#         for food_items in items:
#             finalFoodItems.append(food_items)
#     totalCalories=0
#     for foods in finalFoodItems:
#         totalCalories+=foods.calorie
#     CalorieLeft=200-totalCalories
#     context={'CalorieLeft':CalorieLeft,'totalCalories':totalCalories,'cnt':cnt,'foodlist':finalFoodItems,'fooditem':fooditems,'myfilter':myfilter}
#     return render(request,'myapp/calCalories.html',context)


    # return render(request, 'myapp/calCalories.html')
# def calculate_calorie(request):
#     added_food=FoodItems.objects.all()
#     food_items = UserData.objects.all()
#     if added_food.name==food_items.food_by_user:
        
    
    
    
    
    
    # exitfood=added_food.name
    # userfood=food_items.food_by_user
#     for i in added_food:
#         total_calories = 0
#         selected_foods = []
#         index = 0
#         food_items_list = list(food_items)
#         # Use while loop to sum calories until the total is 200 or more
#         while index < len(food_items_list) and total_calories < 200:
#             food = food_items_list[index]
#             if total_calories + food.calorie < 200:
#                 total_calories += food.calorie
#                 selected_foods.append(food)
#                 index += 1
#                 context = {
#                     'selected_foods': selected_foods,
#                     'total_calories': total_calories
#                 }
#         return render(request, 'myapp/calCalories.html', context) 
#     else:
#         return HttpResponse("item is not in list")

            

# # # def calculate_calories(request):
# # #     userfood=userEntry.fooditem
# # #     food_in_items = FoodItems.objects.all()

# # #     total_calories = 0
# # #     consumed_foods = []

# # #     for food in userfood:
# # #         if userEntry.fooditem == food_in_items.name:
# # #             if total_calories + food['calories'] < 200:
# # #                 total_calories += food['calories']
# # #                 consumed_foods.append(food)
# # #             else:
# # #                 break

# # #     context = {
# # #         'food_items': consumed_foods,
# # #         'total_calories': total_calories
# # #     }

# #     return render(request, 'dashboard.html', context)

