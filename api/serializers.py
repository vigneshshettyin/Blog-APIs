from rest_framework import serializers
from .models import Blog, Category


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class BlogSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(source='category_set',read_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
