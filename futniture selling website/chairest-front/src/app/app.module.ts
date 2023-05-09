import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { RegisterComponent } from './register/register.component';
import { FurnitureComponent } from './furniture/furniture.component';
import { CategoryDetailComponent } from './category-detail/category-detail.component';
import { CategoryListComponent } from './category-list/category-list.component';
import { OrderComponent } from './order/order.component';
import { AccountComponent } from './account/account.component';
import { FurnitureDetailComponent } from './furniture-detail/furniture-detail.component';
import { CategoryFurnitureListComponent } from './category-furniture-list/category-furniture-list.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import { CategoryService } from './category.service';
import { BannerComponent } from './banner/banner.component';
import {CommonModule} from "@angular/common";
import { CartComponent } from './cart/cart.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    RegisterComponent,
    FurnitureComponent,
    CategoryDetailComponent,
    CategoryListComponent,
    OrderComponent,
    AccountComponent,
    FurnitureDetailComponent,
    CategoryFurnitureListComponent,
    NavBarComponent,
    BannerComponent,
    CartComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    CommonModule,
    FormsModule,
  ],
  exports: [
    LoginComponent
  ],
  providers: [
    CategoryService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
export class RegisterModule { }
