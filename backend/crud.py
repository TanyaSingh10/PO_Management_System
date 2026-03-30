from sqlalchemy.orm import Session
import models, schemas

# 🔥 BUSINESS LOGIC
def calculate_total(items, db: Session):
    total = 0

    for item in items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        
        if not product:
            raise Exception(f"Product with id {item.product_id} not found")

        total += float(product.unit_price) * item.quantity

    tax = total * 0.05
    return total + tax

# ✅ CREATE PRODUCT
def create_product(db, product):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# ✅ CREATE PO
def create_po(db: Session, po: schemas.PurchaseOrderCreate):
    total = calculate_total(po.items, db)

    new_po = models.PurchaseOrder(
        reference_no=po.reference_no,
        vendor_id=po.vendor_id,
        total_amount=total,
        status="CREATED"
    )

    db.add(new_po)
    db.commit()
    db.refresh(new_po)

    # add items
    for item in po.items:
        db_item = models.POItem(
            po_id=new_po.id,
            product_id=item.product_id,
            quantity=item.quantity
        )
        db.add(db_item)

    db.commit()
    return new_po

# ✅ CREATE VENDOR
def create_vendor(db: Session, vendor: schemas.VendorCreate):
    db_vendor = models.Vendor(**vendor.dict())
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor

# 🔹 GET ALL VENDORS
def get_vendors(db):
    return db.query(models.Vendor).all()


# 🔹 GET ALL PRODUCTS
def get_products(db):
    return db.query(models.Product).all()


# 🔹 GET ALL PURCHASE ORDERS
def get_pos(db):
    return db.query(models.PurchaseOrder).all()
