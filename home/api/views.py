from rest_framework.decorators import api_view, permission_classes
from helper.mainFunc import createItem, deleteItem, getAllItems, getItem, updateItem
from home.models import Product
from home.api.serializers import ProductSerializer


######################### crud for Product ###############################
@api_view(['GET'])
def products(request):
        return getAllItems(request=request, model=Product, serializer=ProductSerializer )

@api_view(['POST'])
def createProduct(request):
    return createItem(request,ProductSerializer)

@api_view(['PUT'])
def updateProduct(request, id):
    return updateItem(request=request, model=Product, serializer=ProductSerializer, id=id)

@api_view(['GET'])
def getProduct(request, id):
    return getItem(request=request,model=Product, serializer=ProductSerializer ,id=id)


@api_view(['DELETE'])
def deleteProduct(request, id):

    return deleteItem(request=request,model=Product, id=id)

