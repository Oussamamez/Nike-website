from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

PRODUCTS = [
    {
        "name": "Air Jordan 1 Retro High OG",
        "sku": "AJ1-HIGH-001",
        "category": "Shoes",
        "subcategory": "Basketball",
        "price": 180.00,
        "original_price": 180.00,
        "description": "The Air Jordan 1 Retro High OG brings the iconic silhouette back in premium materials. Featuring classic Nike Air cushioning and a high-top design, it delivers both style and performance. The perforated toe box and padded ankle collar provide comfort and support.",
        "image_url": "/static/images/placeholder.svg",
        "images": [
            "/static/images/placeholder.svg"
        ],
        "available_sizes": ["7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "12", "13"],
        "colors": ["Black/White", "Red/Black"],
        "stock": 50,
        "is_featured": True,
        "is_new": True,
        "rating": 4.9,
        "reviews_count": 2847,
    },
    {
        "name": "Nike Air Force 1 '07",
        "sku": "AF1-07-002",
        "category": "Shoes",
        "subcategory": "Lifestyle",
        "price": 115.00,
        "original_price": 115.00,
        "description": "The radiance lives on in the Nike Air Force 1 '07, a basketball classic that puts a fresh spin on what you know best: durably stitched overlays, clean finishes, and the perfect amount of flash to make you shine.",
        "image_url": "/static/images/placeholder.svg",
        "images": [
            "/static/images/placeholder.svg"
        ],
        "available_sizes": ["6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "12"],
        "colors": ["White", "Black", "Triple White"],
        "stock": 120,
        "is_featured": True,
        "is_new": False,
        "rating": 4.8,
        "reviews_count": 15623,
    },
    {
        "name": "Nike Dunk Low Retro",
        "sku": "DUNK-LOW-003",
        "category": "Shoes",
        "subcategory": "Lifestyle",
        "price": 110.00,
        "original_price": 110.00,
        "description": "Created for the hardwood but taken to the streets, the Nike Dunk Low Retro returns with crisp overlays and original team colors. This basketball icon channels '80s vibes with its padded, low-cut collar.",
        "image_url": "/static/images/placeholder.svg",
        "images": [
            "/static/images/placeholder.svg"
        ],
        "available_sizes": ["6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "12"],
        "colors": ["Panda", "Green/White", "Navy/White"],
        "stock": 80,
        "is_featured": True,
        "is_new": False,
        "rating": 4.7,
        "reviews_count": 8921,
    },
    {
        "name": "Nike Air Max 270",
        "sku": "AM270-004",
        "category": "Shoes",
        "subcategory": "Running",
        "price": 160.00,
        "original_price": 160.00,
        "description": "Nike's first lifestyle Air unit is its tallest yet, offering enhanced cushioning for all-day wear. The Nike Air Max 270 is inspired by the Air Max icons of the past, designed as a day-long comfort shoe.",
        "image_url": "/static/images/placeholder.svg",
        "images": [
            "/static/images/placeholder.svg"
        ],
        "available_sizes": ["7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "12", "13"],
        "colors": ["Black/Red", "White/Blue", "Triple Black"],
        "stock": 95,
        "is_featured": False,
        "is_new": False,
        "rating": 4.6,
        "reviews_count": 6234,
    },
    {
        "name": "Nike ZoomX Vaporfly NEXT% 2",
        "sku": "VAPORFLY-005",
        "category": "Shoes",
        "subcategory": "Running",
        "price": 250.00,
        "original_price": 250.00,
        "description": "When every second counts, the Nike ZoomX Vaporfly NEXT% 2 is the fast you've never seen before. It uses Nike's most responsive foam and fast-feeling plate geometry for the smoothest ride yet.",
        "image_url": "/static/images/placeholder.svg",
        "images": [
            "/static/images/placeholder.svg"
        ],
        "available_sizes": ["6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11"],
        "colors": ["Pink/Yellow", "Black/White", "Green"],
        "stock": 30,
        "is_featured": True,
        "is_new": True,
        "rating": 4.9,
        "reviews_count": 3412,
    },
    {
        "name": "Nike Pegasus 40",
        "sku": "PEG40-006",
        "category": "Shoes",
        "subcategory": "Running",
        "price": 130.00,
        "original_price": 130.00,
        "description": "The Nike Pegasus 40 continues a beloved series with an ultra-responsive foam midsole, breathable mesh upper, and reliable cushioning. Perfect for daily training runs.",
        "image_url": "/static/images/placeholder.svg",
        "images": [
            "/static/images/placeholder.svg"
        ],
        "available_sizes": ["6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "12"],
        "colors": ["Blue/White", "Black", "Orange/White"],
        "stock": 200,
        "is_featured": False,
        "is_new": False,
        "rating": 4.7,
        "reviews_count": 9876,
    },
    {
        "name": "Nike Sportswear Tech Fleece Hoodie",
        "sku": "TF-HOODIE-007",
        "category": "Clothing",
        "subcategory": "Hoodies",
        "price": 130.00,
        "original_price": 130.00,
        "description": "Engineered for warmth with a layer of Nike Tech Fleece, this hoodie uses a unique three-layer construction to trap body heat without the bulk. A full zip lets you vent when needed.",
        "image_url": "/static/images/placeholder.svg",
        "images": [
            "/static/images/placeholder.svg"
        ],
        "available_sizes": ["XS", "S", "M", "L", "XL", "2XL", "3XL"],
        "colors": ["Black", "Dark Grey", "Carbon Heather"],
        "stock": 150,
        "is_featured": True,
        "is_new": False,
        "rating": 4.8,
        "reviews_count": 5467,
    },
    {
        "name": "Nike Pro Dri-FIT Tight",
        "sku": "PRO-TIGHT-008",
        "category": "Clothing",
        "subcategory": "Tights",
        "price": 55.00,
        "original_price": 70.00,
        "description": "Designed for high-intensity training, the Nike Pro Dri-FIT Tight features Dri-FIT technology to help you stay dry and comfortable. A wide waistband and flat seams provide a secure, chafe-free fit.",
        "image_url": "/static/images/placeholder.svg",
        "images": [
            "/static/images/placeholder.svg"
        ],
        "available_sizes": ["XS", "S", "M", "L", "XL", "2XL"],
        "colors": ["Black", "Dark Grey"],
        "stock": 200,
        "is_featured": False,
        "is_new": False,
        "is_sale": True,
        "rating": 4.6,
        "reviews_count": 3201,
    },
    {
        "name": "Nike Brasilia 9.5 Training Backpack",
        "sku": "BRAS-BAG-009",
        "category": "Accessories",
        "subcategory": "Bags",
        "price": 40.00,
        "original_price": 40.00,
        "description": "Store your gear in the Nike Brasilia 9.5 Training Backpack. Plenty of pockets and a large main compartment help you keep your gear organized. A sleeve fits most 15-inch laptops.",
        "image_url": "/static/images/placeholder.svg",
        "images": [
            "/static/images/placeholder.svg"
        ],
        "available_sizes": ["One Size"],
        "colors": ["Black/White", "Navy/White", "Grey/Black"],
        "stock": 300,
        "is_featured": False,
        "is_new": False,
        "rating": 4.5,
        "reviews_count": 7832,
    },
    {
        "name": "Nike Mercurial Superfly 9 Elite FG",
        "sku": "MSF9-ELITE-010",
        "category": "Shoes",
        "subcategory": "Football",
        "price": 275.00,
        "original_price": 275.00,
        "description": "Designed for speed, the Nike Mercurial Superfly 9 Elite FG features an ultra-thin Flyknit upper for a locked-in touch and explosive acceleration on firm ground surfaces.",
        "image_url": "/static/images/placeholder.svg",
        "images": [
            "/static/images/placeholder.svg"
        ],
        "available_sizes": ["6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11"],
        "colors": ["Crimson/Black", "Blue/Pink"],
        "stock": 45,
        "is_featured": True,
        "is_new": True,
        "rating": 4.8,
        "reviews_count": 1243,
    },
    {
        "name": "Nike Court Vision Low Next Nature",
        "sku": "CVLNN-011",
        "category": "Shoes",
        "subcategory": "Lifestyle",
        "price": 75.00,
        "original_price": 90.00,
        "description": "Simple and classic, the Nike Court Vision Low Next Nature is made with at least 20% recycled materials by weight. It brings a clean look that works anywhere and features a hooked lacing system.",
        "image_url": "/static/images/placeholder.svg",
        "images": [
            "/static/images/placeholder.svg"
        ],
        "available_sizes": ["6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "12"],
        "colors": ["White/Black", "Black/White"],
        "stock": 110,
        "is_featured": False,
        "is_new": False,
        "is_sale": True,
        "rating": 4.5,
        "reviews_count": 4523,
    },
    {
        "name": "Nike Dri-FIT Victory Golf Polo",
        "sku": "GOLF-POLO-012",
        "category": "Clothing",
        "subcategory": "Golf",
        "price": 75.00,
        "original_price": 75.00,
        "description": "The Nike Dri-FIT Victory Golf Polo delivers a clean look and moisture-wicking performance for the course. Made with at least 75% recycled polyester fibers.",
        "image_url": "/static/images/placeholder.svg",
        "images": [
            "/static/images/placeholder.svg"
        ],
        "available_sizes": ["S", "M", "L", "XL", "2XL"],
        "colors": ["White", "Black", "Navy", "Red"],
        "stock": 175,
        "is_featured": False,
        "is_new": False,
        "rating": 4.6,
        "reviews_count": 2341,
    },
]


def seed_products(db):
    existing = db.query(models.Product).count()
    if existing > 0:
        return
    for p in PRODUCTS:
        product = models.Product(**p)
        db.add(product)
    db.commit()


def run_seed():
    db = SessionLocal()
    try:
        seed_products(db)
        print(f"Seeded {len(PRODUCTS)} products")
    finally:
        db.close()


if __name__ == "__main__":
    run_seed()
