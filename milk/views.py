from rest_framework import generics
from .models import ( User,Milk,Subscription,MilkCategory,
                MilkCompany,MilkCompanyCategory,Order,Payment,Country,State,City,DeliveryTime,
                Address,FarmerProduct,DailyNeedProduct,DailyPCategory)

from .serializers import ( UserSerializer, MilkSerializer,SubscriptionSerializer,MilkCategorySerializer,MilkCompanySerializer,
                    MilkCompanyCategorySerializer,OrderSerializer,PaymentSerializer,CountrySerializer,StateSerializer,
                    CitySerializer,DeliveryTimeSerializer,AddressSerializer,FarmerProductSerializer,
                    LoginSerializer,DailyNeedProductSerializer,DailyPCategorySerializer)
from rest_framework.views import APIView
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)

#User
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'


class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'

#Milk
class MilkListView(generics.ListAPIView):
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer

class MilkCreateView(generics.CreateAPIView):
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer

class MilkUpdateView(generics.UpdateAPIView):
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer
    lookup_field = 'milk_id'

class MilkDeleteView(generics.DestroyAPIView):
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer
    lookup_field = 'milk_id'

class MilkRetrieveView(generics.RetrieveAPIView):
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer
    lookup_field = 'milk_id'

#Subscription
class SubscriptionListView(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionCreateView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionUpdateView(generics.UpdateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    lookup_field = 'payment_id'

class SubscriptionDeleteView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    lookup_field = 'payment_id'

class SubscriptionRetrieveView(generics.RetrieveAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    lookup_field = 'payment_id'

#MilkCategory
class MilkCategoryListView(generics.ListAPIView):
    queryset = MilkCategory.objects.all()
    serializer_class = MilkCategorySerializer

class MilkCategoryCreateView(generics.CreateAPIView):
    queryset = MilkCategory.objects.all()
    serializer_class = MilkCategorySerializer

class MilkCategoryUpdateView(generics.UpdateAPIView):
    queryset = MilkCategory.objects.all()
    serializer_class = MilkCategorySerializer
    lookup_field = 'c_id'

class MilkCategoryDeleteView(generics.DestroyAPIView):
    queryset = MilkCategory.objects.all()
    serializer_class = MilkCategorySerializer
    lookup_field = 'c_id'

class MilkCategoryRetrieveView(generics.RetrieveAPIView):
    queryset = MilkCategory.objects.all()
    serializer_class = MilkCategorySerializer
    lookup_field = 'c_id'

#MilkCompany
class MilkCompanyListView(generics.ListAPIView):
    queryset = MilkCompany.objects.all()
    serializer_class = MilkCompanySerializer

class MilkCompanyCreateView(generics.CreateAPIView):
    queryset = MilkCompany.objects.all()
    serializer_class = MilkCompanySerializer

class MilkCompanyUpdateView(generics.UpdateAPIView):
    queryset = MilkCompany.objects.all()
    serializer_class = MilkCompanySerializer
    lookup_field = 'name'

class MilkCompanyDeleteView(generics.DestroyAPIView):
    queryset = MilkCompany.objects.all()
    serializer_class = MilkCompanySerializer
    lookup_field = 'name'

class MilkCompanyRetrieveView(generics.RetrieveAPIView):
    queryset = MilkCompany.objects.all()
    serializer_class = MilkCompanySerializer
    lookup_field = 'name'

#MilkCompanyCategory
class MilkCompanyCategoryListView(generics.ListAPIView):
    queryset = MilkCompanyCategory.objects.all()
    serializer_class = MilkCompanyCategorySerializer

class MilkCompanyCategoryCreateView(generics.CreateAPIView):
    queryset = MilkCompanyCategory.objects.all()
    serializer_class = MilkCompanyCategorySerializer

class MilkCompanyCategoryUpdateView(generics.UpdateAPIView):
    queryset = MilkCompanyCategory.objects.all()
    serializer_class = MilkCompanyCategorySerializer
    lookup_field = 'milk_category_id'

class MilkCompanyCategoryDeleteView(generics.DestroyAPIView):
    queryset = MilkCompanyCategory.objects.all()
    serializer_class = MilkCompanyCategorySerializer
    lookup_field = 'milk_category_id'

class MilkCompanyCategoryRetrieveView(generics.RetrieveAPIView):
    queryset = MilkCompanyCategory.objects.all()
    serializer_class = MilkCompanyCategorySerializer
    lookup_field = 'milk_category_id'

#Order
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class =OrderSerializer
    lookup_field = 'user_id'

class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class =OrderSerializer
    lookup_field = 'user_id'

class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class =OrderSerializer
    lookup_field = 'user_id'

#Payment
class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentUpdateView(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'user_id'

class PaymentDeleteView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'user_id'

class PaymentRetrieveView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'user_id'

#Country
class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryCreateView(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryUpdateView(generics.UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'country_code'

class CountryDeleteView(generics.DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'country_code'

class CountryRetrieveView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'country_code'

#State
class StateListView(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateCreateView(generics.CreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateUpdateView(generics.UpdateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    lookup_field = 'state_name'

class StateDeleteView(generics.DestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    lookup_field = 'state_name'

class StateRetrieveView(generics.RetrieveAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    lookup_field = 'state_name'

#City
class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityCreateView(generics.CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityUpdateView(generics.UpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'city_name'

class CityDeleteView(generics.DestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'city_name'

class CityRetrieveView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'city_name'

#DeliveryTime
class DTListView(generics.ListAPIView):
    queryset = DeliveryTime.objects.all()
    serializer_class = DeliveryTimeSerializer

class DTCreateView(generics.CreateAPIView):
    queryset = DeliveryTime.objects.all()
    serializer_class = DeliveryTimeSerializer

class DTUpdateView(generics.UpdateAPIView):
    queryset = DeliveryTime.objects.all()
    serializer_class = DeliveryTimeSerializer
    lookup_field = 'user_id'

class DTDeleteView(generics.DestroyAPIView):
    queryset = DeliveryTime.objects.all()
    serializer_class = DeliveryTimeSerializer
    lookup_field = 'user_id'

class DTRetrieveView(generics.RetrieveAPIView):
    queryset = DeliveryTime.objects.all()
    serializer_class = DeliveryTimeSerializer
    lookup_field = 'user_id'

#FarmerProduct
class FPListView(generics.ListAPIView):
    queryset = FarmerProduct.objects.all()
    serializer_class = FarmerProductSerializer

class FPCreateView(generics.CreateAPIView):
    queryset = FarmerProduct.objects.all()
    serializer_class = FarmerProductSerializer

class FPUpdateView(generics.UpdateAPIView):
    queryset = FarmerProduct.objects.all()
    serializer_class = FarmerProductSerializer
    lookup_field = 'name'

class FPDeleteView(generics.DestroyAPIView):
    queryset = FarmerProduct.objects.all()
    serializer_class = FarmerProductSerializer
    lookup_field = 'name'

class FPRetrieveView(generics.RetrieveAPIView):
    queryset = FarmerProduct.objects.all()
    serializer_class = FarmerProductSerializer
    lookup_field = 'name'

#DailyNeedProduct
class DPListView(generics.ListAPIView):
    queryset = DailyNeedProduct.objects.all()
    serializer_class = DailyNeedProductSerializer

class DPCreateView(generics.CreateAPIView):
    queryset = DailyNeedProduct.objects.all()
    serializer_class = DailyNeedProductSerializer

class DPUpdateView(generics.UpdateAPIView):
    queryset = DailyNeedProduct.objects.all()
    serializer_class = DailyNeedProductSerializer
    lookup_field = 'name'

class DPDeleteView(generics.DestroyAPIView):
    queryset = DailyNeedProduct.objects.all()
    serializer_class = DailyNeedProductSerializer
    lookup_field = 'name'
    
class DPRetrieveView(generics.RetrieveAPIView):
    queryset = DailyNeedProduct.objects.all()
    serializer_class = DailyNeedProductSerializer
    lookup_field = 'name'

#DailyPCategory
class DPCListView(generics.ListAPIView):
    queryset = DailyPCategory.objects.all()
    serializer_class = DailyPCategorySerializer

class DPCCreateView(generics.CreateAPIView):
    queryset = DailyPCategory.objects.all()
    serializer_class = DailyPCategorySerializer

class DPCUpdateView(generics.UpdateAPIView):
    queryset = DailyPCategory.objects.all()
    serializer_class = DailyPCategorySerializer
    lookup_field = 'd_id'

class DPCDeleteView(generics.DestroyAPIView):
    queryset = DailyPCategory.objects.all()
    serializer_class = DailyPCategorySerializer
    lookup_field = 'd_id'

class DPCRetrieveView(generics.RetrieveAPIView):
    queryset = DailyPCategory.objects.all()
    serializer_class = DailyPCategorySerializer
    lookup_field = 'd_id'