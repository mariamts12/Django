# **Django Project**

This project is a simple Django web application with two main apps: `store` and `order`. It demonstrates the basics of creating a Django project, creating models, managing migrations, developing views with proper URL routing and simple HTML rendering.

## **Project Overview**

The project includes:
- Default database migrations applied to set up the database.
- A superuser created for admin access.
- Two Django apps: `store` and `order`, each with logical views and proper URL routing.
- Two Django Models: `Category` and `Product`.

## **Features**
### 1. Category Listing Page (`/category/`)
- Displays all categories that do not have a parent category (top-level categories).
- Next to each category name, is displayed the total count of products within that category, including its subcategories.
- Each category name is clickable, linking to the **Category Products Listing Page**.

### 2. Category Products Listing Page (`/category/{category_id}/products/`)
- Lists the names of all products within the selected category and its subcategories.
- Displays the total stock value of each product (calculated as `quantity * price`).
- Includes the following statistics for the products in the category:
  - **Most expensive product** price.
  - **Least expensive product** price.
  - **Average product** price.
  - **Total value of all products** (considering the quantity of each product).
- Products are paginated to avoid displaying all on one page.
- Each product name is clickable, leading to the **Product Detail Page**.

### 3. Product Detail Page
- Displays all fields of the selected product, including its image.

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
- View the categories list at `/store/category/`.
- View the product list for category at `/store/category/{category_id}/products/`.
- View the product details at `/store/{product_id}/`.

### **Order App:**
- View the order home page at `/order/`.
- View the order history at `/order/history`.
- View order details at `/order/<order_id>/`.

### **Models Structure:**
- `Category`:
  - Id
  - Name
  - Description
  - Parent Category


- `Product`:
  - Id
  - Name
  - Description
  - Image
  - Price
  - Category
  - Quantity

---

## **Dependencies**
- **Django 4.2.16**
- **SQLite** (default database)
- **Python 3.11**
- **Django Debug Toolbar**
