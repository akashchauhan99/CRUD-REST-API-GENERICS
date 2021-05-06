from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import fields
from rest_framework.fields import ImageField, SerializerMethodField
from rest_framework.serializers import ModelSerializer, Serializer, CharField
from ..models import Blog, User


class BlogSerializer(ModelSerializer):
    user_email= SerializerMethodField()
    firstname= SerializerMethodField()
    products = SerializerMethodField()

    def get_user_email(self, instance):
        return instance.createdBy.email

    def get_firstname(self, instance):
        return instance.createdBy.firstName

    def get_products(self, instance):
        return Blog.objects.values_list('blogText','blogImg')

    class Meta:
        model = Blog
        fields=['id','blogText','user_email','firstname','blogImg','createdBy','pubDate','products']


class BlogSerailzer2(Serializer):
    blogText= CharField(error_messages={'required':'blogText key is required', 'blank':'blogText is required'})
    blogImg= ImageField(error_messages={'required':'blogImg key is required', 'blank':'blogImg is required'})
    createdBy= CharField(error_messages={'required':'createdBy key is required', 'blank':'createdBy is required'})
    message2 = CharField(read_only=True)

    def validate(self, data):
        blogText = data.get('blogText')

        if len(blogText) < 5:
            raise ValidationError('blogText length should be atleast 5')

        return data

    def create(self, validated_data):
        user=''
        try:
            user = User.objects.get(id=validated_data['createdBy'])
        except:
            pass
        blog = Blog(blogText=validated_data['blogText'], blogImg=validated_data.get('blogImg'), createdBy=user)
        blog.save()
        validated_data['message2'] = "my new message"
        return validated_data
