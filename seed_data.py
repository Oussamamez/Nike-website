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
        "image_url": "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/99486859-0ff3-46b4-949b-2d16af2ad421/air-jordan-1-retro-high-og-shoes-X42mBG.png",
        "images": [
            "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/99486859-0ff3-46b4-949b-2d16af2ad421/air-jordan-1-retro-high-og-shoes-X42mBG.png"
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
        "image_url": "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/b7d9211d-1823-4fef-9e5e-1a5c24a94c47/air-force-1-07-shoes-WrLlWX.png",
        "images": [
            "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/b7d9211d-1823-4fef-9e5e-1a5c24a94c47/air-force-1-07-shoes-WrLlWX.png"
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
        "image_url": "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/9H2854301/dunk-low-retro-shoes-KP0NbP.png",
        "images": [
            "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/9H2854301/dunk-low-retro-shoes-KP0NbP.png"
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
        "image_url": "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/skwgyqlobah60fnnng1g/air-max-270-shoes-2V5C4p.png",
        "images": [
            "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/skwgyqlobah60fnnng1g/air-max-270-shoes-2V5C4p.png"
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
        "image_url": "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/b9d35476-18ea-4fe0-8b91-4d9cfb4de89b/zoomx-vaporfly-next-2-road-racing-shoes-FMpn71.png",
        "images": [
            "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/b9d35476-18ea-4fe0-8b91-4d9cfb4de89b/zoomx-vaporfly-next-2-road-racing-shoes-FMpn71.png"
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
        "image_url": "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/9af81c7b-b3c0-43a4-bc83-f92b7f6ba5b6/pegasus-40-road-running-shoes-Hnzj3t.png",
        "images": [
            "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/9af81c7b-b3c0-43a4-bc83-f92b7f6ba5b6/pegasus-40-road-running-shoes-Hnzj3t.png"
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
        "image_url": "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/i1-8e82af4b-99b4-41bc-b7c6-92e01a0c8b8b/sportswear-tech-fleece-mens-full-zip-hoodie-WjD0gq.png",
        "images": [
            "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/i1-8e82af4b-99b4-41bc-b7c6-92e01a0c8b8b/sportswear-tech-fleece-mens-full-zip-hoodie-WjD0gq.png"
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
        "image_url": "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/b97a9148-fa15-4a80-9bb7-5cd8e73c6b6c/pro-dri-fit-mens-tights-DF7B2g.png",
        "images": [
            "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/b97a9148-fa15-4a80-9bb7-5cd8e73c6b6c/pro-dri-fit-mens-tights-DF7B2g.png"
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
        "image_url": "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/19a6e162-c7c8-4e86-a05e-dac38e43f5d2/brasilia-9-5-training-backpack-medium-30l-JbgdgZ.png",
        "images": [
            "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/19a6e162-c7c8-4e86-a05e-dac38e43f5d2/brasilia-9-5-training-backpack-medium-30l-JbgdgZ.png"
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
        "image_url": "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/3e50e5cf-9df2-40eb-9d85-81a5e6db7bf7/mercurial-superfly-9-elite-firm-ground-soccer-cleats-ksPxbn.png",
        "images": [
            "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/3e50e5cf-9df2-40eb-9d85-81a5e6db7bf7/mercurial-superfly-9-elite-firm-ground-soccer-cleats-ksPxbn.png"
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
        "image_url": "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/71afd5de-abb5-4a5a-b7a9-a6be6f3ff93e/court-vision-low-next-nature-shoes-ggxtnb.png",
        "images": [
            "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/71afd5de-abb5-4a5a-b7a9-a6be6f3ff93e/court-vision-low-next-nature-shoes-ggxtnb.png"
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
        "image_url": "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/01c7b437-a61e-4aef-94d4-8ea6ffced26e/dri-fit-victory-solid-mens-golf-polo-Kc4GHn.png",
        "images": [
            "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/01c7b437-a61e-4aef-94d4-8ea6ffced26e/dri-fit-victory-solid-mens-golf-polo-Kc4GHn.png"
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
