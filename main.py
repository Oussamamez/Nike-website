from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import engine, get_db
import models
from routers import auth_router, products, cart, orders
from seed_data import seed_products
import auth_utils

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Nike Store", docs_url="/api/docs")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(auth_router.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)


@app.on_event("startup")
async def startup_event():
    db = next(get_db())
    seed_products(db)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    user = auth_utils.get_current_user(request, db)
    featured = db.query(models.Product).filter(models.Product.is_featured == True).limit(6).all()
    new_arrivals = db.query(models.Product).filter(models.Product.is_new == True).limit(4).all()
    sale_items = db.query(models.Product).filter(models.Product.is_sale == True).limit(4).all()

    cart_count = 0
    if user:
        cart_count = db.query(models.CartItem).filter(models.CartItem.user_id == user.id).count()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "user": user,
            "featured": featured,
            "new_arrivals": new_arrivals,
            "sale_items": sale_items,
            "cart_count": cart_count,
        },
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
