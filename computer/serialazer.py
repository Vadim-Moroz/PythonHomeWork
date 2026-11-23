from rest_framework import serializers

from computer.models import ComputerModel


class ComputerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=20)
    price=serializers.FloatField()
    status=serializers.BooleanField(default=False)
    color=serializers.CharField(max_length=20)

    def create(self,validated_data):
        computer=ComputerModel.objects.create(**validated_data)
        return computer
    def update(self,instance,validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance