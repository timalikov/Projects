import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { CategoryListComponent } from './category-list/category-list.component';
import { CategoryDetailComponent } from './category-detail/category-detail.component';
import { HomeComponent } from './home/home.component';
import { FurnitureComponent } from './furniture/furniture.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { OrderComponent} from "./order/order.component";
import { AccountComponent} from "./account/account.component";
import { AuthGuard } from './auth.guard';
import {FurnitureDetailComponent} from "./furniture-detail/furniture-detail.component";
import {CategoryFurnitureListComponent} from "./category-furniture-list/category-furniture-list.component";


const routes: Routes = [
  { path: '', component: HomeComponent},
  { path: 'auth/register', component: RegisterComponent },
  { path: 'auth/login', component: LoginComponent },
  { path: 'logout', redirectTo: '/login', pathMatch: 'full' },
  { path: 'category', component: CategoryListComponent},
  { path: 'category/:id', component: CategoryDetailComponent },
  { path: 'category/:id/furniture', component: CategoryFurnitureListComponent},
  { path: 'furniture', component: FurnitureComponent},
  { path: 'furniture/:id', component: FurnitureDetailComponent},
  { path: 'order/:id', component: OrderComponent },
  { path: 'account', component: AccountComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
