from rest_framework import status


def getAll(model, serializer):
    items = model.objects.all()
    serialize = serializer(items, many=True)
    return {'data': serialize.data, 'status': status.HTTP_200_OK}


def getByParam(filter, model, serializer):
    items = model.objects.filter(**filter).all()
    serialize = serializer(items, many=True)
    return {'data': serialize.data, 'status': status.HTTP_200_OK}


def create(serializer, data):
    serialize = serializer(data=data)
    if serialize.is_valid():
        serialize.save()
        return {'data': serialize.data, 'status': status.HTTP_201_CREATED}

    return {'data': serialize.errors, 'status': status.HTTP_400_BAD_REQUEST}


def createMany(serializer, data):
    serialize = serializer(data=data, many=True)
    if serialize.is_valid():
        serialize.save()
        return {'data': serialize.data, 'status': status.HTTP_201_CREATED}

#### remove from many to many relation
def remove(item):
    item.remove()
    return {'data': {"message":'Successfully deleted'}, 'status': status.HTTP_204_NO_CONTENT}


def getItemById(model, id):
    try:
        item = model.objects.get(id=id)  
    except :
        raise
    return item 


def getById(item, serializer,context={}):
    serialize = serializer(item,context=context)
    return {'data': serialize.data, 'status': status.HTTP_200_OK}

def create(serializer, data,context={}):
    serialize = serializer(data=data,context=context)
    if serialize.is_valid():
        serialize.save()
        return {'data': serialize.data, 'status': status.HTTP_201_CREATED}
    return {'data':serialize.errors, 'status': status.HTTP_400_BAD_REQUEST}


def update(item, serializer, data,context={}):
    serialize = serializer(item, data=data,context=context, partial=True)
    if serialize.is_valid():
        serialize.save()
        return {'data': serialize.data, 'status': status.HTTP_200_OK}
    return {'data': serialize.errors, 'status': status.HTTP_400_BAD_REQUEST}

def delete(item):
    item.delete()
    return {'data': {'message': 'Successfully deleted'}, 'status': status.HTTP_204_NO_CONTENT}


