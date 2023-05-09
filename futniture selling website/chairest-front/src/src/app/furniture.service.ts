import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Category, Furniture} from './models';

@Injectable({
  providedIn: 'root',
})
export class FurnitureService {
  private baseUrl = 'http://localhost:8000/';
  private furnitureUrl = 'category';

  constructor(private http: HttpClient) {}

  getFurnitureByCategory(id: number): Observable<Furniture[]>{
    return this.http.get<Furniture[]>(`${this.baseUrl}category/${id}/furniture`)
  }
}

