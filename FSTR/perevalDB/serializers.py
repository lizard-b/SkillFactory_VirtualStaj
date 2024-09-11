from drf_writable_nested import WritableNestedModelSerializer, UniqueFieldsMixin

from .models import *
from rest_framework import serializers


class TouristSerializer(UniqueFieldsMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tourist
        fields = ['email', 'last_name', 'first_name', 'patronymic', 'phone']


class CoordinatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coordinates
        fields = ['latitude', 'longitude', 'elevation']


class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'spring', 'summer', 'autumn']


class PerevalImageSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.URLField()

    class Meta:
        model = PerevalImage
        fields = ['images', 'title']


class PerevalSerializer(WritableNestedModelSerializer):
    user = TouristSerializer()
    coords = CoordinatesSerializer()
    level = LevelSerializer()
    images = PerevalImageSerializer(many=True)
    add_time = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)

    class Meta:
        model = Pereval
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'status', 'user', 'coords',
                  'level', 'images']
        read_only_fields = ['status']

    def create(self, validated_data, **kwargs):
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        user, created = Tourist.objects.get_or_create(**user)
        coords = Coordinates.objects.create(**coords)
        level, created = Level.objects.get_or_create(**level)

        pereval = Pereval.objects.create(**validated_data, user=user, coords=coords, level=level, status="NW")

        for i in images:
            images = i.pop('images')
            title = i.pop('title')
            PerevalImage.objects.create(images=images, pereval=pereval, title=title)

        return pereval

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data.get('user')
            validating_user_fields = [
                instance_user.last_name != data_user['last_name'],
                instance_user.first_name != data_user['first_name'],
                instance_user.patronymic != data_user['patronymic'],
                instance_user.phone != data_user['phone'],
                instance_user.email != data_user['email'],

            ]

            if data_user is not None and any(validating_user_fields):
                raise serializers.ValidationError({'Отклонено': 'Нельзя изменять данные пользователя'})
        return data
