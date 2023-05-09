import { Component } from '@angular/core';
import { CartItem } from '../cart.interface';
import { CartServiceService } from '../cart-service.service';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent {
  cartItems: CartItem[];
  cartTotal: number;

  constructor(private cartService: CartServiceService) {
    this.cartItems = this.cartService.getCartItems();
    this.cartTotal = this.cartService.getCartTotal();
  }

  removeFromCart(item: CartItem) {
    this.cartService.removeItemFromCart(item);
  }

  redirectToTelegram() {
    const telegramMessageUrl = 'https://t.me/timalikov';
    window.location.href = telegramMessageUrl;
  }

  buyAll() {
    // Construct the Telegram URL with product details as query parameters
    const telegramBaseUrl = 'https://t.me/timalikov';
    const queryParams = this.constructQueryParams();
    const telegramMessageUrl = `${telegramBaseUrl}?${queryParams}`;

    // Redirect to the Telegram message URL
    window.location.href = telegramMessageUrl;
  }

  private constructQueryParams(): string {
    const params = [];

    for (const item of this.cartItems) {
      const { title, description, price } = item.product;
      const productInfo = `Product: ${title}, Price: ${price}, Description: ${description}`;
      params.push(encodeURIComponent(productInfo));
    }

    return params.join('&');
  }
}
