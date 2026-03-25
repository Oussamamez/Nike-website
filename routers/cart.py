from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
import models
import auth_utils

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/cart", response_class=HTMLResponse)
async def cart_page(request: Request, db: Session = Depends(get_db)):
    user = auth_utils.get_current_user(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    items = (
        db.query(models.CartItem)
        .filter(models.CartItem.user_id == user.id)
        .all()
    )
    subtotal = sum(item.product.price * item.quantity for item in items)
    shipping = 0.0 if subtotal >= 50 else 8.95
    tax = round(subtotal * 0.08, 2)
    total = round(subtotal + shipping + tax, 2)
    cart_count = sum(item.quantity for item in items)

    return templates.TemplateResponse(
        "cart.html",
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


@router.post("/cart/add")
async def add_to_cart(
    request: Request,
    product_id: int = Form(...),
    size: str = Form(...),
    quantity: int = Form(1),
    db: Session = Depends(get_db),
):
    user = auth_utils.get_current_user(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        return RedirectResponse(url="/products", status_code=302)

    existing = (
        db.query(models.CartItem)
        .filter(
            models.CartItem.user_id == user.id,
            models.CartItem.product_id == product_id,
            models.CartItem.size == size,
        )
        .first()
    )

    if existing:
        existing.quantity += quantity
    else:
        item = models.CartItem(
            user_id=user.id,
            product_id=product_id,
            size=size,
            quantity=quantity,
        )
        db.add(item)

    db.commit()
    return RedirectResponse(url="/cart", status_code=302)


@router.post("/cart/update")
async def update_cart(
    request: Request,
    item_id: int = Form(...),
    quantity: int = Form(...),
    db: Session = Depends(get_db),
):
    user = auth_utils.get_current_user(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    item = (
        db.query(models.CartItem)
        .filter(models.CartItem.id == item_id, models.CartItem.user_id == user.id)
        .first()
    )
    if item:
        if quantity <= 0:
            db.delete(item)
        else:
            item.quantity = quantity
        db.commit()

    return RedirectResponse(url="/cart", status_code=302)


@router.post("/cart/remove")
async def remove_from_cart(
    request: Request,
    item_id: int = Form(...),
    db: Session = Depends(get_db),
):
    user = auth_utils.get_current_user(request, db)
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    item = (
        db.query(models.CartItem)
        .filter(models.CartItem.id == item_id, models.CartItem.user_id == user.id)
        .first()
    )
    if item:
        db.delete(item)
        db.commit()

    return RedirectResponse(url="/cart", status_code=302)


@router.get("/cart/count")
async def cart_count(request: Request, db: Session = Depends(get_db)):
    user = auth_utils.get_current_user(request, db)
    if not user:
        return JSONResponse({"count": 0})
    count = db.query(models.CartItem).filter(models.CartItem.user_id == user.id).count()
    return JSONResponse({"count": count})
