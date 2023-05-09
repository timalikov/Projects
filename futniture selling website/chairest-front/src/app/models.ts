import { Falsy } from "rxjs";

export interface User {
  id: number;
  username: string;
  email: string;
  password: string;
}
export interface Category {
  id: number;
  title: string;
  description: string;
  image: string;
}
export interface Furniture {
  id: number;
  title: string;
  description: string;
  image: string;
  price: number;
  category: Category;
  isExpanded: boolean;
}
export interface Order {
  id: number;
  user: User;
  address: string;
  phoneNumber: string;
  furniture: Furniture;
}

export interface AuthToken{
  access : string,
  refresh: string
}
