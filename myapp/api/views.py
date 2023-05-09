from rest_framework import generics
from rest_framework.response import Response
from ..models import *
from .serializers import CitySerializer, CountrySerializer


class CityListView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all().order_by("name")

    def list(self, request):
        # query params
        params = request.query_params
        country = params.get("country", "")
        queryset = self.get_queryset().filter(country__name__icontains=country)
        s = self.get_serializer(queryset, many=True)
        return Response(s.data)


class CountryListView(generics.ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all().order_by("name")


