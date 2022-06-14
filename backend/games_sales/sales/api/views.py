from django.core.exceptions import FieldError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Sale
from .serializers import SaleSerializer

from core.permissions import IsAdminOrIsAuthenticatedReadOnly


class SaleListAPIView(APIView, LimitOffsetPagination):
    permission_classes = (IsAdminOrIsAuthenticatedReadOnly, )
    page_size = 2

    def get(self, request, *args, **kwargs):
        sales = Sale.objects.all()
        query_data = request.query_params

        if query_data:
            sales = self.search_filter(sales, query_data)

        if 'ordering' in query_data:
            ordering = query_data.get('ordering')
            try:
                sales = sales.order_by(ordering)
            except FieldError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        if 'page_size' in query_data:
            page_size = query_data.get('page_size')
            if page_size.isdigit():
                self.page_size = page_size

        paginator = Paginator(sales, self.page_size)

        if 'page' in query_data:
            page_number = query_data.get('page')
        else:
            page_number = 1

        try:
            paginator_page = paginator.page(page_number)
        except (PageNotAnInteger, EmptyPage) as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

        serializer = SaleSerializer(
            paginator_page,
            many=True,
            context={'request': request}
        )

        return Response({
            'sales': serializer.data,
            'num_pages': paginator.num_pages
        },
            status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Possibly rework to use django-filter and generics view?
    def search_filter(self, sales, query_data):
        if 'value' in query_data:
            sales = sales.filter(
                Q(game__name__icontains=query_data['value']) |
                Q(game__platform__icontains=query_data['value']) |
                Q(game__publisher__icontains=query_data['value']) |
                Q(game__developer__icontains=query_data['value'])
            )
        if 'yor_lt' in query_data:
            sales = sales.filter(
                Q(game__year_of_release__lte=query_data['yor_lt'])
            )
        if 'yor_gt' in query_data:
            sales = sales.filter(
                Q(game__year_of_release__gte=query_data['yor_gt'])
            )
        return sales


class SaleDetailAPIView(APIView):
    permission_classes = (IsAdminOrIsAuthenticatedReadOnly, )

    def get(self, request, uuid, format=None):
        sale = get_object_or_404(Sale, uuid=uuid)
        serializer = SaleSerializer(sale, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, uuid, format=None):
        sale = get_object_or_404(Sale, uuid=uuid)
        serializer = SaleSerializer(sale, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid, format=None):
        data = {}

        sale = get_object_or_404(Sale, uuid=uuid)
        sale_name = sale.game.name
        sale.delete()

        data['response'] = f'Sale ${sale_name} has successfully been deleted'
        return Response(data, status=status.HTTP_204_NO_CONTENT)
