from rest_framework import serializers
from nid_validator.services import NIDValidtor

class NationalIDSerializer(serializers.Serializer):
    national_id = serializers.CharField(max_length=14)

    def validate_national_id(self, value):
        is_valid, result = NIDValidtor().validate_national_id(value)
        if not is_valid:
            raise serializers.ValidationError(result)
        return value

    def to_representation(self, instance):
        # Extract details from validated National ID
        is_valid, result = NIDValidtor().validate_national_id(instance['national_id'])
        if is_valid:
            return result
        return {'error': result}