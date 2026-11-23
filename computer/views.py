from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from computer.models import ComputerModel
from computer.serialazer import ComputerSerializer


# Create your views here.
class ComputerC(APIView):
    def get(self, *args, **kwargs):
        computer=ComputerModel.objects.all()
        serializer=ComputerSerializer(instance=computer,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request, *args, **kwargs):
        computer=request.data
        serializer = ComputerSerializer(data=computer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
class ComputerRUD(APIView):
    def get(self, *args, **kwargs):
        pk=kwargs['pk']
        try:
            computer=ComputerModel.objects.get(pk=pk)
            serializer=ComputerSerializer(instance=computer,many=False)
        except ComputerModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            computer = ComputerModel.objects.get(pk=pk)
            serializer=ComputerSerializer(instance=computer,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except ComputerModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def patch(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            computer = ComputerModel.objects.get(pk=pk)
            serializer=ComputerSerializer(instance=computer,data=request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except ComputerModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            ComputerModel.objects.get(pk=pk).delete()
        except:
            return Response(f"computer {pk} does not exist")
        return Response(status=status.HTTP_204_NO_CONTENT)