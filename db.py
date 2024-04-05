from typing import Optional, List

import psycopg2

from config import settings
from models import Product, Seller


def connect_db():
    return psycopg2.connect(database=settings.DB_NAME,
                            host=settings.DB_HOST,
                            user=settings.DB_USER,
                            password=settings.DB_PASSWORD)


async def get_seller(id: str) -> Optional[Seller]:
    conn = connect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM "Seller" 
            WHERE id = %s
            """, (id,))
        data = cursor.fetchone()

        if data is not None:
            data = Seller.from_tuple(data)
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        print("get product error", e)
        conn.rollback()
        conn.close()
        return None


async def get_product(id: str) -> Optional[Product]:
    conn = connect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT "Product".*, "Seller".name as sellerName FROM "Product" 
            INNER JOIN "Seller" ON "Seller"."id" = "Product"."sellerid"
            WHERE "Product".id = %s
            """, (id,))
        data = cursor.fetchone()

        if data is not None:
            data = Product.from_tuple(data)
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        print("get product error", e)
        conn.rollback()
        conn.close()
        return None


async def get_products() -> Optional[List[Product]]:
    conn = connect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT "Product".*, "Seller".name as sellerName FROM "Product" 
            INNER JOIN "Seller" ON "Seller"."id" = "Product"."sellerid"
            """)
        data = cursor.fetchall()

        if data is not None:
            data = [Product.from_tuple(data) for data in data]

        cursor.close()
        conn.close()
        return data
    except Exception as e:
        print("get product error", e)
        conn.rollback()
        conn.close()
        return None
