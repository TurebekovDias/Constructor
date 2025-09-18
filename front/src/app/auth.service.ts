import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

interface TokenResponse {
    access_token: string;
    token_type: string;
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://127.0.0.1:8000/main'; // Убедитесь, что это URL вашего FastAPI
  private TOKEN_KEY = 'access_token';

    constructor(
        private http: HttpClient,
        private router: Router
    ) { }

    login(username: string, password: string): Observable<TokenResponse> {
        // Форматирование данных для FastAPI (x-www-form-urlencoded)
        const body = new URLSearchParams();
        body.set('username', username);
        body.set('password', password);

        // Отправка запроса POST
        return this.http.post<TokenResponse>(`${this.apiUrl}/token`, body.toString())
            .pipe(
                // Сохраняем токен при получении успешного ответа
                tap(response => {
                    localStorage.setItem(this.TOKEN_KEY, response.access_token);
                })
            );
    }

    getToken(): string | null {
        return localStorage.getItem(this.TOKEN_KEY);
    }

    isLoggedIn(): boolean {
        return !!this.getToken();
    }

    logout(): void {
        localStorage.removeItem(this.TOKEN_KEY);
        this.router.navigate(['/login']);
    }
}
