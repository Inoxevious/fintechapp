from rest_framework import serializers
from .models import Loan_History
from apps.endpoints.models import BehaviouralScores
from apps.endpoints.models import  RetentionScores
from apps.endpoints.models import  ApplicationScores


class Loan_HistorySerializers(serializers.ModelSerializer):
	class Meta:
	    model = Loan_History
	    fields = '__all__'


class RetentionScoresSerializer(serializers.ModelSerializer):
	class Meta:
		model = RetentionScores
		fields = '__all__'


class ApplicationScoresSerializer(serializers.ModelSerializer):
	class Meta:
		model = ApplicationScores
		fields = '__all__'


class BehaviouralScoresSerializer(serializers.ModelSerializer):
	class Meta:
		model = BehaviouralScores
		fields = '__all__'