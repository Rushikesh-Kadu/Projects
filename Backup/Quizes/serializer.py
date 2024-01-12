from rest_framework import serializers
from .models import Quize

class Quizeserializer(serializers.ModelSerializer):         # we are specifying which fields we are serielize from the model
    class Meta:
        model = Quize
        fields = '__all__'
        # exclude = ['']
