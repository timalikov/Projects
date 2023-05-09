import { Component, Input } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  public username!: string;
  public password!: string;
  public errorMessage?: string;

  constructor(private authService: AuthService, private router: Router) {}

  login() {
    console.log(this.username);
    this.authService.login(this.username, this.password).subscribe((data) => {
      console.log(data)
        this.router.navigate(['']);
      },
      // (error) => {
      //   this.errorMessage = "Wrong email or password";
      // }
    );
  }
}
