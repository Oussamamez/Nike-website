# Nike eCommerce Store

A full-featured Nike-inspired eCommerce platform built with FastAPI.

## Stack
- **Backend**: FastAPI + Uvicorn (port 5000)
- **Database**: SQLite via SQLAlchemy ORM
- **Templates**: Jinja2 server-side rendering
- **Auth**: JWT tokens stored in HTTP-only cookies (python-jose + passlib/bcrypt)
- **Frontend**: Vanilla CSS/JS with Nike brand design system

## Project Structure
```
main.py              # FastAPI app entry point + home route
database.py          # SQLite DB engine + session factory
models.py            # SQLAlchemy models: User, Product, CartItem, Order, OrderItem
auth_utils.py        # JWT creation, password hashing, session utilities
seed_data.py         # 12 Nike product seed records
routers/
  auth_router.py     # /login, /register, /logout
  products.py        # /products, /products/{id}
  cart.py            # /cart, /cart/add, /cart/update, /cart/remove
  orders.py          # /checkout, /checkout/place-order, /orders, /orders/{id}/confirmation
templates/           # Jinja2 HTML templates (base, index, products, cart, checkout, etc.)
static/
  css/style.css      # Full Nike-inspired design system
  js/main.js         # Mobile menu, size validation, interaction polish
```

## Features
- Product catalog with 12 Nike products (shoes, clothing, accessories)
- Category/subcategory filtering and search
- User registration and login with JWT session cookies
- Shopping cart with quantity management
- Full checkout flow with shipping + payment form
- Mock payment processing (any card number accepted)
- Order confirmation with order number generation
- Order history page
- Responsive design (mobile-friendly)
- Free shipping on orders over $50

## Running
```bash
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```
