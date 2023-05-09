import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { tap } from 'rxjs/operators';
import {AuthToken} from "./models";

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private baseUrl = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) { }

  register(username: string, password: string, email: string): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}auth/register/`, { username, password, email })
      .pipe(tap(response => {
        const token = response.access;
        localStorage.setItem('token', token);
      }));
  }

  login(username: string, password: string): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}auth/login/`, { username, password })
      .pipe(tap(response => {
        const token = response.access;
        localStorage.setItem('token', token);
        const user = { username, password };
        localStorage.setItem('user', JSON.stringify(user));
      }));
  }


  // login(username: string, password: string):Observable<AuthToken>{
  //   console.log("hello im here")
  //   return this.http.post<AuthToken>(`${this.baseUrl}/login/`, {username, password});
  // }

  logout(): Observable<void> {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    return of(void 0);
  }

  isAuthenticated(): boolean {
    const token = localStorage.getItem('token');
    return !!token;
  }

  public getCurrentUser(): any {
    const user = localStorage.getItem('user');
    if (user) {
      return JSON.parse(user);
    }
    return null;
  }

  getToken(): string {
    return localStorage.getItem('token')!;
  }
}
