from rest_framework import status
from rest_framework.response import Response
from helper.pagination import PaginatorWithPagesCount
from helper.paraMultiValues import paraMultiValues
from helper.requests import create, delete, getById, update ,getItemById
from datetime import date


def getAllWithPagination(model, serializer, filter={},context={}):
    paginator = PaginatorWithPagesCount()
    page_size=filter.pop('page_size',False)
    order_by=filter.pop('order_by',False)
    filter=paraMultiValues(filter)      
    c='cart_db'
    if order_by:
        items = model.objects.using(c).filter(**filter).all().order_by(order_by)
    else:
        items = model.objects.using(c).filter(**filter).all()
    if page_size:
        paginator.page_size = page_size
    request=context['request']
    result_page = paginator.paginate_queryset(items, request)
    serialize = serializer(result_page, many=True,context=context)
    return paginator.get_paginated_response(serialize.data)



def getAllItems(request,model, serializer):
    if request.method == 'GET':

        filter = {str(filter): request.GET.get(str(filter), '') for filter in request.GET if filter not in ["page","statusView"] }
        response = getAllWithPagination(filter=filter,model=model, serializer=serializer, context={'request': request})
    return response





def getAllWithoutPagination(model, serializer, filter={},context={}):
 
    order_by=filter.pop('order_by',False)
    filter=paraMultiValues(filter)      
 
    if order_by:
        items = model.objects.filter(**filter).all().order_by(order_by)
    else:
        items = model.objects.filter(**filter).all()
 
    serialize = serializer(items, many=True,context=context)
    return Response(serialize.data, status=status.HTTP_200_OK)


def getAllItemsWithoutPagination(request,model, serializer):
    if request.method == 'GET':

        filter = {str(filter): request.GET.get(str(filter), '') for filter in request.GET  }
        response = getAllWithoutPagination(filter=filter,model=model, serializer=serializer, context={'request': request})
    return response




def getItem( request,model, serializer ,id):
    try:
        
        item = getItemById(model=model, id=id)
    except:
        return Response({'message':f'{model._meta.model_name} not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        response = getById(serializer=serializer, item=item,context={'request': request})
    return Response(response['data'], response['status'])

def createItem(request,serializer):
    if request.method == 'POST':
        response = create(serializer=serializer, data=request.data,context={"request":request})
    return Response(response['data'], response['status'])


def updateItem( request,model, serializer ,id):
    try:
        item = getItemById(model=model, id=id)
    except:
        return Response({'message':f'{model._meta.model_name} not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        response = update(data=request.data, serializer=serializer, item=item,context={'request': request})
    return Response(response['data'], response['status'])


def deleteItem( request,model ,id):
    try:
   
        item = getItemById(model=model, id=id)
 
    except:
        return Response({'message':f'{model._meta.model_name} not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        response = delete(item=item)
    return Response(response['data'], response['status'])


def calculateAge(birthDate):
	days_in_year = 365.2425
	age = int((date.today() - birthDate).days / days_in_year)
	return age