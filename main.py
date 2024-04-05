from typing import Union

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from db import get_product, get_products, get_seller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/product/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="product.html", context={"id": id}
    )


@app.get("/seller/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="seller.html", context={"id": id}
    )


@app.get("/api/product")
async def read_products(id: Union[str, None] = None):
    if id is None:
        products = await get_products()
        if products is None:
            return {'data': None, 'error': {"message": "Products not found"}}
        return {'data': products, 'error': None}
    else:
        product = await get_product(id)
        if product is None:
            return {'data': None, 'error': {"message": "Product not found"}}
        return {'data': product, 'error': None}


@app.get("/api/seller")
async def read_products(id: Union[str, None] = None):
    if id is None:
        return {'data': None, 'error': {"message": "id parameter is required"}}
    else:
        product = await get_seller(id)
        if product is None:
            return {'data': None, 'error': {"message": "Seller not found"}}
        return {'data': product, 'error': None}
