from django.shortcuts import render

# Create your views here.
def hello(request):
	return render(request, 'week3_app/hello.html')

import datetime 
def order(request):
    company_name = 'ABC Fruits'
    name = ['Veronica Jones', 'brian smith', 'Sarah Smith']
    ship_date = datetime.date(2018, 2, 14)
    item_list = ['Apples', 'Pears', 'Oranges', 'Dragonfruit']
    shipping_cost = 140
    context_data = {
        'company': company_name,
        'name_list': name,
        'ship_date': ship_date,
        'item_list': item_list,
        'ordered_warranty': True,
        'cod_cost': shipping_cost,
    }
    return render(request, 'week3_app/order.html', context_data)

