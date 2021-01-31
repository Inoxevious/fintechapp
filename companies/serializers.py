from rest_framework import serializers
from .models import Loan_History

class Loan_HistorySerializers(serializers.ModelSerializer):
	class Meta:
	    model = Loan_History
	    fields = '__all__'