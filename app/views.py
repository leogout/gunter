import datetime

from django.shortcuts import render

# Create your views here.
from app.forms import PurchaseForm
from app.models import Category, Purchase


def homepage(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PurchaseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data

            purchase = Purchase()

            purchase.category = data['category']
            purchase.price = data['price']

            purchase.save()

    form = PurchaseForm()
    categories = Category.objects.all()
    today = datetime.date.today()

    month = request.GET.get('month', today.month)
    year = request.GET.get('year', today.year)

    purchases = Purchase.objects.filter(date__year=year, date__month=month).order_by('-date')
    x = [category.name for category in categories]
    y = [category.total_in_month(today.month, today.year) for category in categories]
    limits = [category.limit for category in categories]
    colors = [category.color for category in categories]

    return render(
        request,
        'homepage.html',
        {
            'form': form,
            'today': today,
            'categories': categories,
            'purchases': purchases,
            'plot': {
                'x': x,
                'y': y,
                'colors': colors,
                'limits': limits,
                'total_limits': sum(limits),
                'xyc': zip(x, y, colors)
            }
        }
    )



