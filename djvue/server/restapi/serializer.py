from rest_framework import serializers
from .models import Extra_user_info, Country, Editor, Genre, Author, Book, Volume,Loan, Sezione 
from datetime import datetime
from django.contrib.auth.models import User




class Extra_user_infoSerializer(serializers.HyperlinkedModelSerializer):
  #  user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Extra_user_info
        fields = ['id','url','user', 'address', 'document_type', 'document_number', 'telephone_number']

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['id','url','name']

class EditorSerializer(serializers.HyperlinkedModelSerializer):
    country_id = serializers.StringRelatedField()
    class Meta:
        model = Editor
        fields = ['id','url','name', 'country']

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','url','type']

class SezioneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sezione
        fields = ['id','url','name']

"""class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    #country_id = serializers.SlugRelatedField(many=False,
     #   read_only=True,slug_field='name')
    class Meta:
        model = Author
        fields = ['id','url','first_name', 'last_name','birth_date','death_date','note','country_id']
"""
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    country_id = serializers.StringRelatedField()
    class Meta:
        model = Author
        fields = ['id','url','first_name', 'last_name','birth_date','death_date','note','country_id']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)
    editor = serializers.StringRelatedField()
    language =  serializers.StringRelatedField()
    book_image = serializers.ImageField(use_url=True) 
    sezione = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ['isbn','url','isbn','book_name','book_plot','book_pages_number','book_release_date','language','book_image','sezione','editor','author','genres']

class VolumeSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.StringRelatedField()
    class Meta:
        model = Volume
        fields = ['id','url','book', 'purchase_date','dismission_date']

"""class  PrenotationSerializer(serializers.HyperlinkedModelSerializer):
   # user_id = serializers.StringRelatedField(many=True)
    #volume_id = serializers.StringRelatedField(many=True)
    class Meta:
        model = Prenotation
        fields = ['id','url','date','user_id','volume_id']"""

class LoanSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.StringRelatedField()
    volume_id = serializers.StringRelatedField()

    class Meta:
        model = Loan
        fields = ['id','url','return_date','borrow_date','user_id','volume_id','prolungato']
