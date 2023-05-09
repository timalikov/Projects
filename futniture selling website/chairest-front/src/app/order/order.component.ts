import { Component } from '@angular/core';
import { Furniture, User } from '../models';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent {
  product!: Furniture; // Replace with your product type
  user!: User; // Replace with your user type

  constructor(private http: HttpClient) { }

  buyProduct() {
    const purchaseData = {
      product: this.product,
      user: this.user
    };

    this.http.post('http://127.0.0.1:8000/order', purchaseData).subscribe(
      (response) => {
        console.log('Purchase successful');
      },
      (error) => {
        console.error('Error occurred during purchase', error);
      }
    );
  }
}
