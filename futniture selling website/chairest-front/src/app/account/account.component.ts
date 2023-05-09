import { Component } from '@angular/core';
import { CategoryService } from '../category.service';

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css']
})
export class AccountComponent {
  user: any;
  isLoggedIn!: boolean;

  constructor(private categoryservice: CategoryService) { }

  ngOnInit() {
    this.categoryservice.getUserInfo().subscribe(
      response => {
        this.user = response;
        this.isLoggedIn = !!response;
      },
      error => {
        console.error('Error occurred while fetching user information:', error);
      }
    );
  }
}
