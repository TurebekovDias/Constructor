import { Component, OnInit} from '@angular/core';
import { FormGroup, ReactiveFormsModule, Validators, FormBuilder } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { CommonModule } from '@angular/common';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-auth.component',
  imports: [CommonModule, ReactiveFormsModule, MatFormFieldModule, MatInputModule, MatButtonModule],
  templateUrl: './auth.component.html',
  styleUrl: './auth.component.scss'
})
export class AuthComponent {

  loginForm!: FormGroup;
  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {}
  ngOnInit(): void {
    this.loginForm = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
  }

  onSubmit(): void {
    if (this.loginForm.valid) {
      const { username, password } = this.loginForm.value;

            // Вызываем метод login из AuthService
            this.authService.login(username, password).subscribe({
                next: (response) => {
                    // Успешный вход: сервис уже сохранил токен
                    console.log('Успешный вход:', response);
                    // Перенаправляем пользователя на главную или в профиль
                    this.router.navigate(['/profile']); 
                },
                error: (err) => {
                    // Обработка ошибок (например, неверный логин/пароль)
                    console.error('Ошибка входа:', err.error.detail || 'Неизвестная ошибка');
                    // Можно показать сообщение пользователю
                }
            });
    }
  }
}
