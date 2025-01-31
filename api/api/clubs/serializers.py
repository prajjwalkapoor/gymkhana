from rest_framework import serializers

from api.clubs.models import Club


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'category', 'logo', 'description', 'email', 'slug']
        extra_kwargs = {'id': {'read_only': True},
                        'slug': {'read_only': True}
                        }
