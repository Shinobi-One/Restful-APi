from djoser.serializers import UserCreateSerializer,UserSerializer


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id','first_name','password','email','username']

class UserShowSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id','first_name','username','email']