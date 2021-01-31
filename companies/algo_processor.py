
class IncomeClassfierResultsView(ListView):
    template_name = 'dashboards/rf/index.html'
    def get_queryset(self, **kwargs):
        global cust_data, loan, user_name, input_data,acc_user
        user = self.request.user
        user_name = user.first_name
        acc_user = AccountUser.objects.get(user=user)
        print("Found USer", user_name)
        org = Organization.objects.get(id=1)
        client = Clients.objects.filter(insti=org)
        loan = Loan.objects.filter(signing_officer__insti = org)

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)

        # algorithm_status = self.request.query_params.get("status", "production")
        algorithm_status = "production"
        # algorithm_version = self.request.query_params.get("version")
        algorithm_version = None
        endpoint_name = 'income_classifier'
        print("End point name found", endpoint_name)
        algs = MLAlgorithm.objects.filter(parent_endpoint__name = endpoint_name, ml_algorithm_status__status = algorithm_status, ml_algorithm_status__active=True)

        if algorithm_version is not None:
            algs = algs.filter(version = algorithm_version)

        if len(algs) == 0:
            return Response(
                {"status": "Error", "message": "ML algorithm is not available"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # if len(algs) != 1 and algorithm_status != "ab_testing":
        #     return Response(
        #         {"status": "Error", "message": "ML algorithm selection is ambiguous. Please specify algorithm version."},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )
        alg_index = 0
        if algorithm_status == "ab_testing":
            alg_index = 0 if rand() < 0.5 else 1

        algorithm_object = registry.endpoints[algs[alg_index].id]
        query_object_data_dict = {}

        for ln in loan:
            query_object_data_dict[ln.client_id] = []
            query_object_data_dict[ln.client_id].append(model_to_dict(ln))
        print("query object data", query_object_data_dict)
        # qury_predict_dict_data = {}
        # for d_id, d_info in query_object_data_dict.items():
        #     print("\nQuery Data ID:", d_id)
        #     for key in d_info:
        #         qury_predict_dict_data[d_id] = []
                
        #         print(key) 
        #         prediction = algorithm_object.compute_prediction(key)
        #         qury_predict_dict_data[d_id].append(prediction)
        #     print("Query  Predictions data", qury_predict_dict_data)
        object_data_dict = {}
        for ln in loan:
            object_data_dict[ln.client_id] = []
            data ={'age': 32, 'workclass': 'Private', 'fnlwgt': 70984, 'education': 'Assoc-voc', 'education-num': 11, 'marital-status': 'Married-civ-spouse', 'occupation': 'Machine-op-inspct', 'relationship': 'Husband', 'race': 'White', 'sex': 'Male', 'capital-gain': 0, 'capital-loss': 0, 'hours-per-week': 40, 'native-country': 'United-States'},
            object_data_dict[ln.client_id].append(data)
            print("object data", object_data_dict)

        predict_dict_data = {}
        for d_id, d_info in object_data_dict.items():
            print("\nQuery Data ID:", d_id)
            for key in d_info:
                predict_dict_data[d_id] = []
                input_data = key
                prediction = algorithm_object.compute_prediction(key)
                prediction["cust_id"] = d_id
                print(prediction['probability'])
                if  prediction['probability'] > 0.67:
                    color = 'red'
                    text = 'high risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a high risk of defaulting the loan'.format(d_id))
                elif  prediction['probability'] > 0.33:
                    color = 'blue'
                    text = 'moderate risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a moderate risk of defaulting the loan'.format(d_id))
                else:
                    color = 'green'
                    text = 'low risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a low risk of defaulting the loan'.format(d_id))
                predict_dict_data[d_id].append(prediction)
            print( 'Prediction:', predict_dict_data)


        label = prediction["label"] if "label" in prediction else "error"
        ml_request = MLRequest(
            input_data=input_data,
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgorithm=algs[alg_index],
        )
        ml_request.save()
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # data = Loan_History.objects.all()
        # return_data = log.grade_avg(data)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data End ~~~~~~~~~~~~~~~~~~~~~~
        prediction["request_id"] = ml_request.id
        context = {
            'income_classifier_prediction': predict_dict_data,
            'loan': loan,
            'user_name':user_name,
            'acc_user':acc_user,
            # 'webdata':return_data
        }
        return context



class ApplicationAnalyticsResultsView(ListView):
    template_name = 'dashboards/application/index.html'
    def get_queryset(self, **kwargs):
        global cust_data, loan, user_name, input_data,acc_user
        user = self.request.user
        user_name = user.first_name
        acc_user = AccountUser.objects.get(user=user)
        print("Found USer", user_name)
        org = Organization.objects.get(id=1)
        client = Clients.objects.filter(insti=org)
        loan = Loan.objects.filter(signing_officer__insti = org)

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)

        # algorithm_status = self.request.query_params.get("status", "production")
        algorithm_status = "production"
        # algorithm_version = self.request.query_params.get("version")
        algorithm_version = None
        endpoint_name = 'income_classifier'
        print("End point name found", endpoint_name)
        algs = MLAlgorithm.objects.filter(parent_endpoint__name = endpoint_name, ml_algorithm_status__status = algorithm_status, ml_algorithm_status__active=True)

        if algorithm_version is not None:
            algs = algs.filter(version = algorithm_version)

        if len(algs) == 0:
            return Response(
                {"status": "Error", "message": "ML algorithm is not available"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # if len(algs) != 1 and algorithm_status != "ab_testing":
        #     return Response(
        #         {"status": "Error", "message": "ML algorithm selection is ambiguous. Please specify algorithm version."},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )
        alg_index = 0
        if algorithm_status == "ab_testing":
            alg_index = 0 if rand() < 0.5 else 1

        algorithm_object = registry.endpoints[algs[alg_index].id]
        query_object_data_dict = {}

        for ln in loan:
            query_object_data_dict[ln.client_id] = []
            query_object_data_dict[ln.client_id].append(model_to_dict(ln))
        print("query object data", query_object_data_dict)
        # qury_predict_dict_data = {}
        # for d_id, d_info in query_object_data_dict.items():
        #     print("\nQuery Data ID:", d_id)
        #     for key in d_info:
        #         qury_predict_dict_data[d_id] = []
                
        #         print(key) 
        #         prediction = algorithm_object.compute_prediction(key)
        #         qury_predict_dict_data[d_id].append(prediction)
        #     print("Query  Predictions data", qury_predict_dict_data)
        object_data_dict = {}
        for ln in loan:
            object_data_dict[ln.client_id] = []
            data ={'age': 32, 'workclass': 'Private', 'fnlwgt': 70984, 'education': 'Assoc-voc', 'education-num': 11, 'marital-status': 'Married-civ-spouse', 'occupation': 'Machine-op-inspct', 'relationship': 'Husband', 'race': 'White', 'sex': 'Male', 'capital-gain': 0, 'capital-loss': 0, 'hours-per-week': 40, 'native-country': 'United-States'},
            object_data_dict[ln.client_id].append(data)
            print("object data", object_data_dict)

        predict_dict_data = {}
        for d_id, d_info in object_data_dict.items():
            print("\nQuery Data ID:", d_id)
            for key in d_info:
                predict_dict_data[d_id] = []
                input_data = key
                prediction = algorithm_object.compute_prediction(key)
                prediction["cust_id"] = d_id
                print(prediction['probability'])
                if  prediction['probability'] > 0.67:
                    color = 'red'
                    text = 'high risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a high risk of defaulting the loan'.format(d_id))
                elif  prediction['probability'] > 0.33:
                    color = 'blue'
                    text = 'moderate risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a moderate risk of defaulting the loan'.format(d_id))
                else:
                    color = 'green'
                    text = 'low risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a low risk of defaulting the loan'.format(d_id))
                predict_dict_data[d_id].append(prediction)
            print( 'Prediction:', predict_dict_data)


        label = prediction["label"] if "label" in prediction else "error"
        ml_request = MLRequest(
            input_data=input_data,
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgorithm=algs[alg_index],
        )
        ml_request.save()
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # data = Loan_History.objects.all()
        # return_data = log.grade_avg(data)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data End ~~~~~~~~~~~~~~~~~~~~~~
        prediction["request_id"] = ml_request.id
        context = {
            'income_classifier_prediction': predict_dict_data,
            'loan': loan,
            'user_name':user_name,
            'acc_user':acc_user,
            # 'webdata':return_data
        }
        return context






class RetentionAnalyticsResultsView(ListView):
    template_name = 'dashboards/application/index.html'
    def get_queryset(self, **kwargs):
        global cust_data, loan, input_data
        org = Organization.objects.get(id=1)
        client = Clients.objects.filter(insti=org)
        loan = Loan.objects.filter(signing_officer__insti = org)

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)

        # algorithm_status = self.request.query_params.get("status", "production")
        algorithm_status = "production"
        # algorithm_version = self.request.query_params.get("version")
        algorithm_version = None
        endpoint_name = 'income_classifier'
        print("End point name found", endpoint_name)
        algs = MLAlgorithm.objects.filter(parent_endpoint__name = endpoint_name, ml_algorithm_status__status = algorithm_status, ml_algorithm_status__active=True)

        if algorithm_version is not None:
            algs = algs.filter(version = algorithm_version)

        if len(algs) == 0:
            return Response(
                {"status": "Error", "message": "ML algorithm is not available"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # if len(algs) != 1 and algorithm_status != "ab_testing":
        #     return Response(
        #         {"status": "Error", "message": "ML algorithm selection is ambiguous. Please specify algorithm version."},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )
        alg_index = 0
        if algorithm_status == "ab_testing":
            alg_index = 0 if rand() < 0.5 else 1

        algorithm_object = registry.endpoints[algs[alg_index].id]
        query_object_data_dict = {}

        for ln in loan:
            query_object_data_dict[ln.client_id] = []
            query_object_data_dict[ln.client_id].append(model_to_dict(ln))
        print("query object data", query_object_data_dict)
        # qury_predict_dict_data = {}
        # for d_id, d_info in query_object_data_dict.items():
        #     print("\nQuery Data ID:", d_id)
        #     for key in d_info:
        #         qury_predict_dict_data[d_id] = []
                
        #         print(key) 
        #         prediction = algorithm_object.compute_prediction(key)
        #         qury_predict_dict_data[d_id].append(prediction)
        #     print("Query  Predictions data", qury_predict_dict_data)
        object_data_dict = {}
        for ln in loan:
            object_data_dict[ln.client_id] = []
            data ={'age': 32, 'workclass': 'Private', 'fnlwgt': 70984, 'education': 'Assoc-voc', 'education-num': 11, 'marital-status': 'Married-civ-spouse', 'occupation': 'Machine-op-inspct', 'relationship': 'Husband', 'race': 'White', 'sex': 'Male', 'capital-gain': 0, 'capital-loss': 0, 'hours-per-week': 40, 'native-country': 'United-States'},
            object_data_dict[ln.client_id].append(data)
            print("object data", object_data_dict)

        predict_dict_data = {}
        for d_id, d_info in object_data_dict.items():
            print("\nQuery Data ID:", d_id)
            for key in d_info:
                predict_dict_data[d_id] = []
                input_data = key
                prediction = algorithm_object.compute_prediction(key)
                prediction["cust_id"] = d_id
                print(prediction['probability'])
                if  prediction['probability'] > 0.67:
                    color = 'red'
                    text = 'high risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a high risk of defaulting the loan'.format(d_id))
                elif  prediction['probability'] > 0.33:
                    color = 'blue'
                    text = 'moderate risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a moderate risk of defaulting the loan'.format(d_id))
                else:
                    color = 'green'
                    text = 'low risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a low risk of defaulting the loan'.format(d_id))
                predict_dict_data[d_id].append(prediction)
            print( 'Prediction:', predict_dict_data)


        label = prediction["label"] if "label" in prediction else "error"
        ml_request = MLRequest(
            input_data=input_data,
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgorithm=algs[alg_index],
        )
        ml_request.save()
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # data = Loan_History.objects.all()
        # return_data = log.grade_avg(data)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data End ~~~~~~~~~~~~~~~~~~~~~~
        prediction["request_id"] = ml_request.id
        context = {
            'income_classifier_prediction': predict_dict_data,
            'loan': loan,
        }
        return context

class BehavioralAnalyticsResultsView(ListView):
    template_name = 'dashboards/application/index.html'
    def get_queryset(self, **kwargs):
        global cust_data, loan, input_data
        org = Organization.objects.get(id=1)
        client = Clients.objects.filter(insti=org)
        loan = Loan.objects.filter(signing_officer__insti = org)

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)

        # algorithm_status = self.request.query_params.get("status", "production")
        algorithm_status = "production"
        # algorithm_version = self.request.query_params.get("version")
        algorithm_version = None
        endpoint_name = 'income_classifier'
        print("End point name found", endpoint_name)
        algs = MLAlgorithm.objects.filter(parent_endpoint__name = endpoint_name, ml_algorithm_status__status = algorithm_status, ml_algorithm_status__active=True)

        if algorithm_version is not None:
            algs = algs.filter(version = algorithm_version)

        if len(algs) == 0:
            return Response(
                {"status": "Error", "message": "ML algorithm is not available"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # if len(algs) != 1 and algorithm_status != "ab_testing":
        #     return Response(
        #         {"status": "Error", "message": "ML algorithm selection is ambiguous. Please specify algorithm version."},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )
        alg_index = 0
        if algorithm_status == "ab_testing":
            alg_index = 0 if rand() < 0.5 else 1

        algorithm_object = registry.endpoints[algs[alg_index].id]
        query_object_data_dict = {}

        for ln in loan:
            query_object_data_dict[ln.client_id] = []
            query_object_data_dict[ln.client_id].append(model_to_dict(ln))
        print("query object data", query_object_data_dict)
        # qury_predict_dict_data = {}
        # for d_id, d_info in query_object_data_dict.items():
        #     print("\nQuery Data ID:", d_id)
        #     for key in d_info:
        #         qury_predict_dict_data[d_id] = []
                
        #         print(key) 
        #         prediction = algorithm_object.compute_prediction(key)
        #         qury_predict_dict_data[d_id].append(prediction)
        #     print("Query  Predictions data", qury_predict_dict_data)
        object_data_dict = {}
        for ln in loan:
            object_data_dict[ln.client_id] = []
            data ={'age': 32, 'workclass': 'Private', 'fnlwgt': 70984, 'education': 'Assoc-voc', 'education-num': 11, 'marital-status': 'Married-civ-spouse', 'occupation': 'Machine-op-inspct', 'relationship': 'Husband', 'race': 'White', 'sex': 'Male', 'capital-gain': 0, 'capital-loss': 0, 'hours-per-week': 40, 'native-country': 'United-States'},
            object_data_dict[ln.client_id].append(data)
            print("object data", object_data_dict)

        predict_dict_data = {}
        for d_id, d_info in object_data_dict.items():
            print("\nQuery Data ID:", d_id)
            for key in d_info:
                predict_dict_data[d_id] = []
                input_data = key
                prediction = algorithm_object.compute_prediction(key)
                prediction["cust_id"] = d_id
                print(prediction['probability'])
                if  prediction['probability'] > 0.67:
                    color = 'red'
                    text = 'high risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a high risk of defaulting the loan'.format(d_id))
                elif  prediction['probability'] > 0.33:
                    color = 'blue'
                    text = 'moderate risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a moderate risk of defaulting the loan'.format(d_id))
                else:
                    color = 'green'
                    text = 'low risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a low risk of defaulting the loan'.format(d_id))
                predict_dict_data[d_id].append(prediction)
            print( 'Prediction:', predict_dict_data)


        label = prediction["label"] if "label" in prediction else "error"
        ml_request = MLRequest(
            input_data=input_data,
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgorithm=algs[alg_index],
        )
        ml_request.save()
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # data = Loan_History.objects.all()
        # return_data = log.grade_avg(data)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data End ~~~~~~~~~~~~~~~~~~~~~~
        prediction["request_id"] = ml_request.id
        context = {
            'income_classifier_prediction': predict_dict_data,
            'loan': loan,
        }
        return context