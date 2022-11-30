from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from django.http import Http404

from .models import Product
from .serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None:
            content = title
        serializer.save(content = content)

product_create_view = ProductCreateAPIView.as_view()
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


Product_Detail_view =ProductDetailAPIView.as_view()


@api_view(['GET','POST'])
def product_alt_view(request, pk=None,*args, **kwargs):
    method = request.method 

    if method == 'GET':
        if pk is not None:
            # detail view
            obj =get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False)
            return Response()
            
        # list view
        queryset =Product.objects.all()
        data = ProductSerializer(queryset, many=True)
        return Response(data)
    if method == "POST":
        # create an item
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
    
            if content is None:
                content = title
                serializer.save(content = content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)
