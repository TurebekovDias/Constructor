import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { tap } from 'rxjs/operators';

interface AuthCredentials {
    email: string;
    password: string;
}

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private loggedIn = new BehaviorSubject<boolean>(false);
  isLoggedIn$ = this.loggedIn.asObservable();

  constructor(private http: HttpClient) {}

  login(credentials: AuthCredentials): Observable<any> {
    return this.http.post('YOUR_API_URL/login', credentials).pipe(
      tap((response: any) => {
        localStorage.setItem('authToken', response.token);
        this.loggedIn.next(true);
      })
    );
  }

  register(credentials: AuthCredentials): Observable<any> {
    return this.http.post('YOUR_API_URL/register', credentials);
  }

  logout(): void {
    localStorage.removeItem('authToken');
    this.loggedIn.next(false);
  }

  checkLoginStatus(): void {
    const token = localStorage.getItem('authToken');
    this.loggedIn.next(!!token);
  }
}