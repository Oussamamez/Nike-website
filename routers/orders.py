import uuid
import random
from datetime import datetime
from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
import models
import auth_utils

router = APIRouter()
templates = Jinja2Templates(directory="templates")


def generate_order_number():
    return f"NK-{datetime.now().strftime('%Y%m')}-{random.randint(100000, 999999)}"


@router.get("/checkout", response_class=HTMLResponse)
async def checkout_page(request: Request, db: Session = Depends(get_db)):
    user = auth_utils.get_current_user(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    items = db.query(models.CartItem).filter(models.CartItem.user_id == user.id).all()
    if not items:
        return RedirectResponse(url="/cart", status_code=302)

    subtotal = sum(item.product.price * item.quantity for item in items)
    shipping = 0.0 if subtotal >= 50 else 8.95
    tax = round(subtotal * 0.08, 2)
    total = round(subtotal + shipping + tax, 2)
    cart_count = sum(item.quantity for item in items)

    return templates.TemplateResponse(
        "checkout.html",
        {
            "request": request,
            "user": user,
            "items": items,
            "subtotal": round(subtotal, 2),
            "shipping": shipping,
            "tax": tax,
            "total": total,
            "cart_count": cart_count,
        },
    )


@router.post("/checkout/place-order")
async def place_order(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    address: str = Form(...),
    city: str = Form(...),
    state: str = Form(...),
    zip_code: str = Form(...),
    country: str = Form("US"),
    card_number: str = Form(...),
    card_expiry: str = Form(...),
    card_cvv: str = Form(...),
    card_name: str = Form(...),
    db: Session = Depends(get_db),
):
    user = auth_utils.get_current_user(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    items = db.query(models.CartItem).filter(models.CartItem.user_id == user.id).all()
    if not items:
        return RedirectResponse(url="/cart", status_code=302)

    subtotal = sum(item.product.price * item.quantity for item in items)
    shipping = 0.0 if subtotal >= 50 else 8.95
    tax = round(subtotal * 0.08, 2)
    total = round(subtotal + shipping + tax, 2)

    clean_card = card_number.replace(" ", "").replace("-", "")
    last4 = clean_card[-4:] if len(clean_card) >= 4 else "0000"

    card_brand = "Visa"
    if clean_card.startswith("5"):
        card_brand = "Mastercard"
    elif clean_card.startswith("3"):
        card_brand = "Amex"
    elif clean_card.startswith("6"):
        card_brand = "Discover"

    order = models.Order(
        order_number=generate_order_number(),
        user_id=user.id,
        status="confirmed",
        subtotal=round(subtotal, 2),
        shipping=shipping,
        tax=tax,
        total=total,
        shipping_first_name=first_name,
        shipping_last_name=last_name,
        shipping_address=address,
        shipping_city=city,
        shipping_state=state,
        shipping_zip=zip_code,
        shipping_country=country,
        payment_last4=last4,
        payment_brand=card_brand,
    )
    db.add(order)
    db.flush()

    for item in items:
        order_item = models.OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            size=item.size,
            quantity=item.quantity,
            unit_price=item.product.price,
        )
        db.add(order_item)
        db.delete(item)

    db.commit()
    db.refresh(order)

    return RedirectResponse(url=f"/orders/{order.id}/confirmation", status_code=302)


@router.get("/orders/{order_id}/confirmation", response_class=HTMLResponse)
async def order_confirmation(
    request: Request,
    order_id: int,
    db: Session = Depends(get_db),
):
    user = auth_utils.get_current_user(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    order = (
        db.query(models.Order)
        .filter(models.Order.id == order_id, models.Order.user_id == user.id)
        .first()
    )
    if not order:
        return RedirectResponse(url="/orders", status_code=302)

    cart_count = db.query(models.CartItem).filter(models.CartItem.user_id == user.id).count()

    return templates.TemplateResponse(
        "order_confirmation.html",
        {"request": request, "user": user, "order": order, "cart_count": cart_count},
    )


@router.get("/orders", response_class=HTMLResponse)
async def orders_page(request: Request, db: Session = Depends(get_db)):
    user = auth_utils.get_current_user(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    orders = (
        db.query(models.Order)
        .filter(models.Order.user_id == user.id)
        .order_by(models.Order.created_at.desc())
        .all()
    )
    cart_count = db.query(models.CartItem).filter(models.CartItem.user_id == user.id).count()

    return templates.TemplateResponse(
        "orders.html",
        {"request": request, "user": user, "orders": orders, "cart_count": cart_count},
    )
