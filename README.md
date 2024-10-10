# **Django Project**

This project is a simple Django web application with two main apps: `store` and `order`. It demonstrates the basics of creating a Django project, creating models, managing migrations, and developing views with proper URL routing.

## **Project Overview**

The project includes:
- Default database migrations applied to set up the database.
- A superuser created for admin access.
- Two Django apps: `store` and `order`, each with logical views and proper URL routing.
- Two Django Models: `Category` and `Product`.
- Store app has two views `store_categories` and `store_products`, respectively returning list of categories and products with relevant details. 

## **Usage**

### **Run the Project:**
Use the following command to start the Django development server:

```bash
python manage.py runserver
```

### **Access the Admin Panel:**
Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in using the superuser credentials.

### **Store App:**
- View the store home page at `/store/`.
- View the categories list at `/store/categories/`.
- View the product list at `/store/products/`.

### **Order App:**
- View the order home page at `/order/`.
- View the order history at `/order/history`.
- View order details at `/order/<order_id>/`.

---

## **Dependencies**
- **Django 4.2.16**
- **SQLite** (default database)
- **Python 3.11**
