import { Injectable } from '@angular/core';
import { CartItem } from './cart.interface';
import { Furniture } from './models';

@Injectable({
  providedIn: 'root'
})
export class CartServiceService {

  cartItems: CartItem[] = [];

  constructor() { }

  addToCart(product: Furniture): void {
    const existingItem = this.cartItems.find(item => item.product.id === product.id);

    if (existingItem) {
      existingItem.quantity++;
    } else {
      const newItem: CartItem = {
        product: product,
        quantity: 1
      };
      this.cartItems.push(newItem);
    }
  }

  removeItemFromCart(item: CartItem): void {
    const itemIndex = this.cartItems.findIndex(cartItem => cartItem === item);
    if (itemIndex > -1) {
      this.cartItems.splice(itemIndex, 1);
    }
  }

  getCartItems(): CartItem[] {
    return this.cartItems;
  }

  getCartTotal(): number {
    let total = 0;
    for (const item of this.cartItems) {
      total += item.product.price * item.quantity;
    }
    return total;
  }

  clearCart(): void {
    this.cartItems = [];
  }
}
