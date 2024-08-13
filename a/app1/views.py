from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def silk(request,id):
    resham=[{"id":1,"name":"warp","level":"60","length":"20"},
            {"id":2,"name":"pagada","level":"10","length":"25"},
            {"id":3,"name":"resham","level":"3","length":"5"},
            {"id":4,"name":"polyster","level":"80","length":"1"}
            ]
    result=None
    for item in resham:
        if item["id"]==id:
            result=item
            break
    if result is not None:
        return HttpResponse(
            '''<p> The name of the product is {}<br>
            The level of the product is {}<br>
            The length of the product is {}<br>
            </p>.'''.format(result['name'],result['level'],result['length']))
    else:
        return("Sorrry the product is not found")