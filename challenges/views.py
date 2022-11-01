from types import NoneType
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "Eat no Meat for the entire month",
    'february': 'Walk for atleast 20 minutes a day',
    'march': 'Learn Django for 20 minutes',
    'april': 'Learn Django for 20 minutes2',
    'may': 'Learn Django for 20 minutes3',
    'june': 'Learn Django for 20 minutes4',
    'july': 'Learn Django for 20 minutes5',
    'august': 'Learn Django for 20 minutes6',
    'september': 'Learn Django for 20 minutes7',
    'october': 'Learn Django for 20 minutes8',
    'november': 'Learn Django for 20 minutes9',
    'december': 'Learn Django for 20 minutes10', 
    
}

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        new_path = reverse('month-challenge', args=[month])
        list_items += f"<li><a href=\"{new_path}\">{capitalized_month}</a></li>"

    return_val = f"<ul>{list_items}</ul>"

    return render(request,'challenges/index.html', {
        'challenges': months
    } )

def monthly_challenge(request, month):
    # view_text = None

    # if month == 'january':
    #     view_text = "Eat no Meat for the entire month"
    # elif month == 'february':
    #     view_text = 'Walk for atleast 20 minutes a day'
    # elif month == 'march':
    #     view_text = 'Learn Django for 20 minutes'
    # else:
    #     return HttpResponseNotFound("This month is not supported")

    # return HttpResponse(view_text)
    try:
        challenge_text = monthly_challenges[month]
        # response_text = render_to_string('challenges/challenge.html')
        return render(request,'challenges/challenge.html', {
            "text": challenge_text,
            'month_name': month
        } )
    except:
        return HttpResponseNotFound("<h1>This month is not accepted</h1>")
    
    return HttpResponse(response_text)




def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("invalid month")
    forward_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[forward_month]) # /challenge/janaury
    return HttpResponseRedirect(redirect_path)
