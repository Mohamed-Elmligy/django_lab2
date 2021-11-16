from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http.response import JsonResponse
my_task_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'todo-1',
        'priority': 1,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'todo-2',
        'priority': 4,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'todo-3',
        'priority': 5,
        'description': "hello iam studying at iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
    {
        'index': 3,
        'id': 4,
        'name': 'todo-4',
        'priority': 10,
        'description': "iti sahdjka shkdj sahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffffhsadjksahdjkashkdjsahjkfghdadsgfadfadsgasdfasfffffffffffff",
    },
]

def _get_target_task(target_id):
    # Filter the list based on the task id 
    # sent and compare it toward each dictionary item in the list
    filter_result = filter(lambda d: d.get('id') == target_id, my_task_list)
    final_list = list(filter_result)
    # Getting index of the required task from my_task_list
    index_of_task = my_task_list.index(final_list[0])
    return index_of_task

def index(request):
    args={'name': "mohamed",'age': 25}
    return render(request, 'todo/todo_index.html', args)
    
def showAll(request):
    #return HttpResponse(f"Hello, {name}!")
    #return render(request, templateName, context=None, content_type=None)
    #return redirect(to,*args,**kwargs)
    # return JsonResponse({'todo_name': 'John Wick','production_year':2014})
    # return  render_to_string('todo/todo_show_all.html', context=my_task_list,request=request)
    items_list=['item1','item2','item3','item4',]
    my_context= {'items':items_list}
    return  render(request, 'todo/todo_show_list.html', context=my_context)

def create(request):
    return HttpResponse("create")

def showOne(request,**kwargs):
    #print(kwargs.get('user_id','not found args'))
    # return HttpResponse("task id is {}".format(kwargs))
    my_context= {
        'name':kwargs.get('item_name'),
        'id':kwargs.get('item_id'),
        'priority':5,
    }
    return  render(request, 'todo/todo_details.html', context=my_context)

def edit(request,**kwargs):
    # pprint()                      # Pretty print
    # print(request.is_ajax())      # print methon name 
    # print(request.is_secure())
    # print(request.path)           # print url
    # print(request.body)           # print form data
    # print(request.GET)            # print query string
    # print(request.POST)
    # pprint(request.META)
    return  render(request, 'todo/edit.html', context=kwargs)

def update(request,**kwargs):
    return HttpResponse("update")
    
def delete(request,**kwargs):
    return HttpResponse("delete")
