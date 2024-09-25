from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 

from .models import Inventory_model
from .serializers import Inventory_serializers
# Create your views here.

class ItemDetail(APIView):
    def get_object (self,id_id):
        try:
            items=Inventory_model.objects.get(id=id_id)
            return items 
        except Inventory_model.DoesNotExist:
            return None
        
    def get(self,request):
        items=Inventory_model.objects.all()
        ser=Inventory_serializers(items,many=True)
        return Response(ser.data)
    
    def post(self,request):
        ser= Inventory_serializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id_id):
        items=self.get_object(id_id)
        if items is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        ser = Inventory_serializers(items , data = request.data )
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)        
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id_id):
        items = self.get_object(id_id)
        if items is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    