from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# serializers.py works similarly to forms.py
# this class defines the fields that get serialized/deserialized. 
class SnippetSerializer(serializers.ModelSerializer):  # ModelSerializer:  a shortcut for creating serializer classes:
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'}) # Like widget=widgets.Textarea on Django Form Class
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):

        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


#shell
'''

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



snippet = Snippet(code='foo = "bar"\n')
snippet.save()

serializer = SnippetSerializer(snippet)
serializer.data
# {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}

---> At this point we've translated the model instance into Python native datatypes. To finalize the serialization process we render the data into json.

content = JSONRenderer().render(serializer.data)
content
# b'{"id": 2, "title": "", "code": "print(\\"hello, world\\")\\n", "linenos": false, "language": "python", "style": "friendly"}


---->Deserialization is similar. First we parse a stream into Python native datatypes...

import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

---> then we restore those native datatypes into a fully populated object instance.
not sure but I think we created another instance???????????
serializer = SnippetSerializer(data=data)
serializer.is_valid()

# True

serializer.validated_data

# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])

serializer.save()
#  <Snippet: Snippet object>

---> We can also serialize querysets instead of model instances. To do so we simply add a many=True flag to the serializer arguments.

serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data
# [OrderedDict([('id', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', ''), ('code', 'print("hello, world")'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]
'''



'''
---> now with the modified version try this:
from snippets.serializers import SnippetSerializer

serializer = SnippetSerializer()
print(repr(serializer))
# You will see whole your serializer fields with details here


'''

