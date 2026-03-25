# Nike eCommerce Store

A full-featured Nike-inspired eCommerce platform built with FastAPI.

<img width="1460" height="773" alt="image" src="https://github.com/user-attachments/assets/6780d803-713d-41b2-8254-037785c0ab4e" />
<img width="1441" height="825" alt="Capture d&#39;écran 2026-03-25 125634" src="https://github.com/user-attachments/assets/c3a2f384-95bb-4179-be4f-8bf1da8cfd94" />
<img width="1447" height="821" alt="Capture d&#39;écran 2026-03-25 125652" src="https://github.com/user-attachments/assets/0db62bcb-777d-4643-bdb1-6ce42f2c68eb" />
<img width="1446" height="824" alt="Capture d&#39;écran 2026-03-25 125728" src="https://github.com/user-attachments/assets/6b3b476f-4e11-4bd3-940e-527310b8e61e" />
<img width="1447" height="820" alt="Capture d&#39;écran 2026-03-25 125746" src="https://github.com/user-attachments/assets/7eb21fa2-8798-440d-aa5f-362c9dab58d1" />
<img width="1313" height="706" alt="Capture d&#39;écran 2026-03-25 125610" src="https://github.com/user-attachments/assets/a3cba870-25f7-4dca-9d16-1a50031450c7" />
<img width="1450" height="821" alt="Capture d&#39;écran 2026-03-25 133444" src="https://github.com/user-attachments/assets/29973e7f-4552-4010-a06b-2c04703dc5fe" />
<img width="1453" height="804" alt="Capture d&#39;écran 2026-03-25 133458" src="https://github.com/user-attachments/assets/89f0420a-89d4-4269-98e6-4c481fa6de69" />
<img width="1437" height="817" alt="Capture d&#39;écran 2026-03-25 133431" src="https://github.com/user-attachments/assets/e5532b05-2149-4796-93a1-3997f7b6aecd" />




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
