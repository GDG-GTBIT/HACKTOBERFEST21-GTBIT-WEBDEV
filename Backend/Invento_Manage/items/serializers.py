from rest_framework import serializers 
from items.models import Item
 
 
class ItemSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Item
        fields = ('id',
                  'name',
                  'description',
                  'price', 'quantity', 'category', 'product_id')


#We will have to make one for Inventory_User as well. 
#Will do later on if need be.