from fastapi import FastAPI

from app.routers import categories, products, users, cart, orders  # New
from fastapi.staticfiles import StaticFiles



# Создаём приложение FastAPI
app = FastAPI(
    title="FastAPI Интернет-магазин",
    version="0.1.0",
)
app.mount("/media", StaticFiles(directory="media"), name="media")

# Подключаем маршруты категорий и товаров
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(users.router)   # New
app.include_router(cart.router)
app.include_router(orders.router)  # ← Регистрация роутера заказов
# app.include_router(payments.router)  # ← Регистрация роутера оплаты


# Корневой эндпоинт для проверки
@app.get("/")
async def root():
    """
    Корневой маршрут, подтверждающий, что API работает.
    """
    return {"message": "Добро пожаловать в API интернет-магазина!"}
