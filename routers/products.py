from fastapi import APIRouter, Request, Depends, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
import models
import auth_utils

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/products", response_class=HTMLResponse)
async def products_page(
    request: Request,
    category: str = None,
    subcategory: str = None,
    q: str = None,
    sort: str = "featured",
    db: Session = Depends(get_db),
):
    user = auth_utils.get_current_user(request, db)
    query = db.query(models.Product)

    if category:
        query = query.filter(models.Product.category == category)
    if subcategory:
        query = query.filter(models.Product.subcategory == subcategory)
    if q:
        search = f"%{q}%"
        query = query.filter(
            models.Product.name.ilike(search) | models.Product.description.ilike(search)
        )

    if sort == "price_asc":
        query = query.order_by(models.Product.price.asc())
    elif sort == "price_desc":
        query = query.order_by(models.Product.price.desc())
    elif sort == "newest":
        query = query.order_by(models.Product.created_at.desc())
    elif sort == "rating":
        query = query.order_by(models.Product.rating.desc())
    else:
        query = query.order_by(models.Product.is_featured.desc(), models.Product.created_at.desc())

    products = query.all()

    categories = db.query(models.Product.category).distinct().all()
    categories = [c[0] for c in categories]

    cart_count = 0
    if user:
        cart_count = db.query(models.CartItem).filter(models.CartItem.user_id == user.id).count()

    return templates.TemplateResponse(
        "products.html",
        {
            "request": request,
            "user": user,
            "products": products,
            "categories": categories,
            "selected_category": category,
            "selected_subcategory": subcategory,
            "q": q,
            "sort": sort,
            "cart_count": cart_count,
        },
    )


@router.get("/products/{product_id}", response_class=HTMLResponse)
async def product_detail(
    request: Request,
    product_id: int,
    db: Session = Depends(get_db),
):
    user = auth_utils.get_current_user(request, db)
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        from fastapi.responses import RedirectResponse
        return RedirectResponse(url="/products", status_code=302)

    related = (
        db.query(models.Product)
        .filter(
            models.Product.category == product.category,
            models.Product.id != product.id,
        )
        .limit(4)
        .all()
    )

    cart_count = 0
    if user:
        cart_count = db.query(models.CartItem).filter(models.CartItem.user_id == user.id).count()

    return templates.TemplateResponse(
        "product_detail.html",
        {
            "request": request,
            "user": user,
            "product": product,
            "related": related,
            "cart_count": cart_count,
        },
    )
