from .models import Item
from .serializers import ItemSerializer
import json
from .serviceiteam import create_item, get_item_by_name, get_item_by_id, update_item ,delete_item_by_id
import ast
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create Item
class ItemCreate(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        # Print the raw JSON body
        raw_json = json.dumps(request.data)  # Access the raw JSON data
        print("Raw JSON data:", raw_json)  # Print to console
        if raw_json:
            raw_json = ast.literal_eval(raw_json)
            name = raw_json.get("name")
            description = raw_json.get("description")
            price = raw_json.get("price")
            quantity = raw_json.get("quantity")
            category = raw_json.get("category")
            if get_item_by_name(name):
                logger.error({"error": "Item already exists."})
                return Response({"error": "Item already exists."}, status=status.HTTP_400_BAD_REQUEST)
            create_item(name, description, price, quantity, category)
            item=get_item_by_name(name)
            if item:
                raw_json={"id":item[0],"name": item[1],"description": item[2], "price": item[3], "quantity": item[4], "category":item[5]}
                logger.debug(raw_json)
        # Call the superclass method to handle item creation
        return Response(raw_json, status=status.HTTP_201_CREATED)


# Retrieve Item by ID
class ItemDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        # Get the id (pk) from the URL
        item_id = kwargs.get('pk')
        logger.debug("Item ID from URL:", item_id)  # Print the ID to console
        if current_data := get_item_by_id(item_id):
            keys = ['id', 'name', 'description', 'price', 'quantity', 'category', 'created_at']

            # Convert the tuple to a dictionary
            current_data = dict(zip(keys, current_data))

            # Call the superclass method to handle the actual update
            logger.info({"massage": "Success message."})
            return Response(current_data, status=status.HTTP_200_OK)
        else:
            logger.error({"error": "Item not found."})
            return Response({"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND)

# Update Item by ID
class ItemUpdate(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        # Get the id (pk) from the URL
        item_id = kwargs.get('pk')
        logger.info("Item ID from URL:", item_id)  # Print the ID to console

        # Print the raw JSON body
        raw_json = json.dumps(request.data)  # Access the raw JSON data
        logger.debug("Raw JSON data:", raw_json)  # Print to console
        if raw_json:
            if current_data := get_item_by_id(item_id):
                # Define keys for the dictionary
                keys = ['id', 'name', 'description', 'price', 'quantity', 'category', 'created_at']

                # Convert the tuple to a dictionary
                current_data = dict(zip(keys, current_data ))
                raw_json = ast.literal_eval(raw_json)
                if raw_json.get("name"):
                    name = raw_json.get("name")
                else:
                    name = current_data.get("name")

                if raw_json.get("description"):
                    description = raw_json.get("description")
                else:
                    description = current_data.get("description")

                if raw_json.get("price"):
                    price = raw_json.get("price")
                else:
                    price = current_data.get("price")

                if raw_json.get("quantity"):
                    quantity = raw_json.get("quantity")
                else:
                    quantity = current_data.get("quantity")

                if raw_json.get("category"):
                    category = raw_json.get("category")
                else:
                    category = current_data.get("category")
                if update_item(item_id, name, description, price, quantity, category):
                    # Call the superclass method to handle the actual update
                    logger.info({"massage": "Success message."})
                    return Response(raw_json, status=status.HTTP_200_OK)
                else:
                    logger.error({"error": "Item not found."})
                    return Response({"error": "Item not found."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                logger.error({"error": "Item not found."})
                return Response({"error": "Item not found."}, status=status.HTTP_400_BAD_REQUEST)



# Delete Item by ID
class ItemDelete(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        # Get the id (pk) from the URL
        item_id = kwargs.get('pk')
        logger.info("Item ID from URL:", item_id)  # Print the ID to console
        if delete_item_by_id(item_id):
            logger.info({"massage": "Success message."})
            return Response({"massage": "Success message."}, status=status.HTTP_200_OK)
        else:
            logger.error({"error": "Item not found."})
            return Response({"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND)
