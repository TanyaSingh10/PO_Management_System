from sqlalchemy import Column, Integer, String, Float, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from database import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact = Column(String)
    rating = Column(Float)

    orders = relationship("PurchaseOrder", back_populates="vendor")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sku = Column(String)
    unit_price = Column(DECIMAL)
    stock_level = Column(Integer)


class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id = Column(Integer, primary_key=True, index=True)
    reference_no = Column(String)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    total_amount = Column(DECIMAL)
    status = Column(String)

    vendor = relationship("Vendor", back_populates="orders")
    items = relationship("POItem", back_populates="po")


class POItem(Base):
    __tablename__ = "po_items"

    id = Column(Integer, primary_key=True, index=True)
    po_id = Column(Integer, ForeignKey("purchase_orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)

    po = relationship("PurchaseOrder", back_populates="items")
