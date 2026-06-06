from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from products.models import Product
from branches.models import Branch

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = [{
            'id': p.id,
            'name': p.name,
            'image': p.image.url if p.image else None,
            'price': str(p.price),
            'calories': p.calories,
        } for p in products]
        return Response(data)
    
    if request.method == 'POST':
        if not request.user.is_staff:
            return Response({"detail": "Доступ заборонено"}, status=status.HTTP_403_FORBIDDEN)
        
        product = Product.objects.create(
            name=request.data.get('name'),
            price=request.data.get('price'),
            calories=request.data.get('calories'),
        )
        return Response(
            {"id": product.id, "detail": "Продукт створено"}, 
            status=status.HTTP_201_CREATED
        )


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        data = {
            'id': product.id,
            'name': product.name,
            'image': product.image.url if product.image else None,
            'price': str(product.price),
            'calories': product.calories,
        }
        return Response(data)

    if request.method == 'PUT':
        if not request.user.is_staff:
            return Response({"detail": "Доступ заборонено"}, status=status.HTTP_403_FORBIDDEN)
        
        product.name = request.data.get('name', product.name)
        product.price = request.data.get('price', product.price)
        product.calories = request.data.get('calories', product.calories)
        product.save()
        return Response({"detail": "Продукт оновлено"})

    if request.method == 'DELETE':
        if not request.user.is_staff:
            return Response({"detail": "Доступ заборонено"}, status=status.HTTP_403_FORBIDDEN)
        
        product.delete()
        return Response({"detail": "Продукт видалено"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def branches_list(request):
    if request.method == 'GET':
        branches = Branch.objects.all()
        data = [{
            'id': b.id,
            'name': b.name,
            'address': b.address,
            'phone': b.phone,
            'work_hours': b.work_hours,
            'special': b.special,
        } for b in branches]
        return Response(data)

@api_view(['GET'])
def branch_detail(request, pk):
    branch = get_object_or_404(Branch, pk=pk)

    if request.method == 'GET':
        data = {
            'id': branch.id,
            'name': branch.name,
            'address': branch.address,
            'phone': branch.phone,
            'work_hours': branch.work_hours,
            'special': branch.special,
        }
        return Response(data)