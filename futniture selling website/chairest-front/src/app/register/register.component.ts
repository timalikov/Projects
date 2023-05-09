import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';
import { User } from '../models';
import {HttpClient, HttpErrorResponse} from "@angular/common/http";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  public username?: string;
  public email?: string;
  public password?: string;
  errorMessage?: any;

  constructor(
    private http: HttpClient,
    private authService: AuthService,
    private router: Router
  ) { }

  register(): void {
    this.authService.register(this.username!, this.password!, this.email!)
      .subscribe(
        response => {
          localStorage.setItem('token', response.access);
          this.router.navigate(['/auth/login']);
        },
        (error: HttpErrorResponse) => {
          if (error.status === 400) {
            this.errorMessage = 'Invalid data provided. Please check your input and try again.';
          } else {
            this.errorMessage = 'An unexpected error occurred. Please try again later.';
          }
          console.error(error);
        }
      );
  }
}


