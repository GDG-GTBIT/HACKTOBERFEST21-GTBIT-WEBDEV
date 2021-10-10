from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from items.models import Item
from items.serializers import ItemSerializer
from rest_framework.decorators import api_view

import csv
import datetime
# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def all_items(request):
    if request.method == 'GET':
        items = Item.objects.all()
        
        product_id = request.query_params.get('product_id', None)
        if product_id is not None:
            items = items.filter(product_id__icontains=product_id)
        item_serializer = ItemSerializer(items, many=True)
        return JsonResponse(item_serializer.data, safe=False)
         
    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        item_serializer = ItemSerializer(data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            added_item = Item.objects.get(product_id = item_data['product_id'])
            add_to_update_sheet(added_item, added_item)
            return JsonResponse(item_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Item.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def single_item(request, product_id):

    try: 
        item = Item.objects.get(product_id = product_id) 
    except Item.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        item_serializer = ItemSerializer(item) 
        return JsonResponse(item_serializer.data) 
 
    elif request.method == 'PUT':
        
        item_before_update = Item.objects.get(product_id = product_id)

        item_data = JSONParser().parse(request) 
        item_serializer = ItemSerializer(item, data=item_data) 
        if item_serializer.is_valid(): 
            item_serializer.save()

            item_after_update = Item.objects.get(product_id = product_id)
            add_to_update_sheet(item_before_update, item_after_update) 

            return JsonResponse(item_serializer.data) 
        return JsonResponse(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        item.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
   
def updates(request):
    FinalJson = {"updates": []}
    with open('files/update.csv', 'r') as file:
        file_reader = csv.reader(file)
        count = 1
        for row in file_reader:
            if count == 1:
                count = count + 1
                continue
            count = count + 1
            l = {}
            try:
                if len(row)!=0:
                    l["product_id"] = row[0]
                    l["name"] = row[1]
                    l["updated_at"] = row[2]
                    l["qty_change"] = row[3]
                    l["qty_available"] = row[4]
                    l["old_price"] = row[5]
                    l["new_price"] = row[6]
                    l["updated_id"] = row[7]
                    FinalJson["updates"].append(l)
            except:
                print('still error persists!!')
    FinalJson["updates"].reverse()
    return JsonResponse(FinalJson)


def add_to_update_sheet(original_item, new_item):
    time = datetime.datetime.now()
    product_id = original_item.product_id
    name = original_item.name
    old_price = original_item.price
    new_price = new_item.price
    qty_change = new_item.quantity - original_item.quantity
    qty_available = new_item.quantity
    updated_at = time.strftime("%H")+":"+time.strftime("%M")+" "+time.strftime("%x")
    updated_by = 'will change to the user logged in'
    updated_list = [product_id,name, updated_at, qty_change, qty_available,old_price, new_price, updated_by]

    with open('files/update.csv', 'a', newline='') as file:
        file_writer = csv.writer(file)
        file_writer.writerow(updated_list)

    