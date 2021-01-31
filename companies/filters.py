from .serializers import Loan_HistorySerializers
from .models import *

#Get mortage Loan Filter
def getFilter(datamodel, field):
    # get all the school loans from the database excluding 
    # null and blank values
    print("MOdel", datamodel)
    data = model.objects.exclude(field__isnull=True).\
        exclude(field__exact='').order_by(field).values_list(field).distinct()
    data = [i[0] for i in list(data)]
    data = {
        "data": data, 
    }
    return JsonResponse(data, status = 200)