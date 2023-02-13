from djoser.serializers import UserCreateSerializer

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id','first_name','password','email','username']