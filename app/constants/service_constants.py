from enum import Enum


class BulkCreate(Enum):
    PRODUCTS_DATA = [
    {"product_name": "Smartphone", "product_price": 399.99, "product_available_quantity": 100},
    {"product_name": "Laptop", "product_price": 899.99, "product_available_quantity": 50},
    {"product_name": "Headphones", "product_price": 49.99, "product_available_quantity": 200},
    {"product_name": "Tablet", "product_price": 299.99, "product_available_quantity": 75},
    {"product_name": "Smartwatch", "product_price": 149.99, "product_available_quantity": 150},
    {"product_name": "Camera", "product_price": 599.99, "product_available_quantity": 40},
    {"product_name": "Desk Chair", "product_price": 129.99, "product_available_quantity": 30},
    {"product_name": "Gaming Console", "product_price": 299.99, "product_available_quantity": 60},
    {"product_name": "Coffee Maker", "product_price": 39.99, "product_available_quantity": 100},
    {"product_name": "Fitness Tracker", "product_price": 79.99, "product_available_quantity": 80},
    {"product_name": "Bluetooth Speaker", "product_price": 59.99, "product_available_quantity": 90},
    {"product_name": "Power Bank", "product_price": 29.99, "product_available_quantity": 120},
    {"product_name": "Dumbbell Set", "product_price": 49.99, "product_available_quantity": 50},
    {"product_name": "Ebook Reader", "product_price": 119.99, "product_available_quantity": 40},
    {"product_name": "Portable Grill", "product_price": 79.99, "product_available_quantity": 25},
    {"product_name": "Wireless Mouse", "product_price": 19.99, "product_available_quantity": 70},
    {"product_name": "Coffee Grinder", "product_price": 29.99, "product_available_quantity": 60},
    {"product_name": "Toaster", "product_price": 24.99, "product_available_quantity": 110},
    {"product_name": "External Hard Drive", "product_price": 89.99, "product_available_quantity": 45},
    {"product_name": "Blender", "product_price": 39.99, "product_available_quantity": 70},
    {"product_name": "Wireless Earbuds", "product_price": 69.99, "product_available_quantity": 80},
    {"product_name": "Digital Thermometer", "product_price": 9.99, "product_available_quantity": 150},
    {"product_name": "Backpack", "product_price": 49.99, "product_available_quantity": 65},
    {"product_name": "Yoga Mat", "product_price": 19.99, "product_available_quantity": 40},
    {"product_name": "Portable Charger", "product_price": 19.99, "product_available_quantity": 90},
    {"product_name": "Electric Toothbrush", "product_price": 34.99, "product_available_quantity": 55},
    {"product_name": "Air Purifier", "product_price": 79.99, "product_available_quantity": 30},
    {"product_name": "Wireless Router", "product_price": 59.99, "product_available_quantity": 50},
    {"product_name": "Gaming Mousepad", "product_price": 14.99, "product_available_quantity": 100},
    {"product_name": "Water Bottle", "product_price": 9.99, "product_available_quantity": 120}
    ]

class Status(Enum):
    INACTIVE = "inactive"
    ACTIVE = "active"

class UserType(Enum):
    UserType=["Admin","Customer"]