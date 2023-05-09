import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Category, Furniture} from './models';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {
  private baseUrl = 'http://localhost:8000/';

  constructor(private http: HttpClient) { }

  getCategories(): Observable<Category[]> {
    return this.http.get<Category[]>(`${this.baseUrl}category/`);
  }

  getCategory(id: number): Observable<Category> {
    return this.http.get<Category>(`${this.baseUrl}category/${id}/`);
  }

  getFurnitures(): Observable<Furniture[]>{
    return this.http.get<Furniture[]>(`${this.baseUrl}furniture/`)
  }

  getFurniture(id: number): Observable<Furniture[]> {
    return this.http.get<Furniture[]>(`${this.baseUrl}category/${id}/furniture/`);
  }
  getCategoryFurniture(id: number): Observable<Furniture[]> {
    return this.http.get<Furniture[]>(`${this.baseUrl}${id}/furniture/`);
  }
  getCategoryById(id: number): Observable<Category> {
    return this.http.get<Category>(`${this.baseUrl}/categories/${id}`);
  }

}
