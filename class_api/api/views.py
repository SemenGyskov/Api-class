from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProductSerializer, ProducerSerializer, CategorySerializer
from .models import Product, Producer, Category

class ProductAPIView(APIView):
    def get(self, request,pk):
        w = Product.objects.all()
        return Response({'products': ProductSerializer(w, many=True).data})

    def post(self, request,pk):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Product.objects.create(
            title = request.data['title'],
            size = request.data['size'],
            producer_id = request.data['producer_id'],
            cat_id = request.data['cat_id'],
            cost = request.data['cost'],
        )

        return Response({'post': ProductSerializer(post_new).data})
    def delete(self,request, *args,**kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'method DELETE not allowed '})

        w = Product.objects.get(pk=pk)
        w.delete()

        return Response({'post':"delete post" + str(pk)})

    def put(self,request,*args,**kwargs):
        pk=kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method Put not allowed'})
        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({'error':'Objects does not exists'})

        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})