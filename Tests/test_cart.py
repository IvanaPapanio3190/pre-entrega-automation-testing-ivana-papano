from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_cart(login_in_driver):
    driver = login_in_driver

    # 1. Obtener nombre y PRECIO del primer producto en el catálogo
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text
    product_price = driver.find_elements(By.CLASS_NAME, "inventory_item_price")[0].text

    # 2. Agregar producto al carrito
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
    
    # Verificar contador carrito
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert contador_cart.text == "1", "La cantidad de productos no se agregaron correctamente"

    # 3. Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 4. Obtener el nombre y el precio del producto ya dentro del carrito
    cart_item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    cart_item_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

    # 5. Mostrar en consola para el Reporte HTML
    print(f"\n[INFO TP] Carrito verificado - Producto: {cart_item_name} | Precio: {cart_item_price}")

    # 6. Verificaciones
    assert cart_item_name == product_name, "El producto agregado no coincide en el nombre"
    assert cart_item_price == product_price, "El precio del producto cambió al entrar al carrito"