from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']

'''
serializer: convets complex data types such as querysets and model instances into native Python datatypes that can then be easily rendered into JSON, XML or other content types. It also provides deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
ModelSerializer: A ModelSerializer is a type of serializer that provides a shortcut for creating serializers that deal with model instances and querysets. It automatically generates a set of fields based on the model and includes simple implementations of the create() and update() methods.
In the above code, we define a BookSerializer that inherits from serializers.ModelSerializer. We specify
the model we want to serialize (Book) and the fields we want to include in the serialization (id, title, author, published_date). This serializer can now be used to convert Book instances into JSON format and vice versa.

'''