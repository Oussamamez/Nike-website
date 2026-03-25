"""Update product images to use reliable, publicly accessible URLs."""
from database import SessionLocal
import models

IMAGES = {
    "AJ1-HIGH-001": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&q=80",
    "AF1-07-002":   "https://images.unsplash.com/photo-1600185365926-3a2ce3cdb9eb?w=500&q=80",
    "DUNK-LOW-003": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=500&q=80",
    "AM270-004":    "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=500&q=80",
    "VAPORFLY-005": "https://images.unsplash.com/photo-1556906781-9a412961a28c?w=500&q=80",
    "PEG40-006":    "https://images.unsplash.com/photo-1539185441755-769473a23570?w=500&q=80",
    "TF-HOODIE-007":"https://images.unsplash.com/photo-1556821840-3a63f15732ce?w=500&q=80",
    "PRO-TIGHT-008":"https://images.unsplash.com/photo-1519058082700-08a0b56da9b4?w=500&q=80",
    "BRAS-BAG-009": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500&q=80",
    "MSF9-ELITE-010":"https://images.unsplash.com/photo-1511556820780-d912e42b4980?w=500&q=80",
    "CVLNN-011":    "https://images.unsplash.com/photo-1515955656352-a1fa3ffcd111?w=500&q=80",
    "GOLF-POLO-012":"https://images.unsplash.com/photo-1537832816519-689ad163238b?w=500&q=80",
}

def run():
    db = SessionLocal()
    try:
        products = db.query(models.Product).all()
        updated = 0
        for p in products:
            if p.sku in IMAGES:
                p.image_url = IMAGES[p.sku]
                p.images = [IMAGES[p.sku]]
                updated += 1
        db.commit()
        print(f"Updated {updated} product images.")
    finally:
        db.close()

if __name__ == "__main__":
    run()
