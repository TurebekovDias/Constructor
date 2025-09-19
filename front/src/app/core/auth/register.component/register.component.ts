import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
import { FormsModule } from '@angular/forms'
@Component({
  selector: 'app-register',
  imports: [ FormsModule ],
  templateUrl: './register.component.html',
  styleUrl: './register.component.scss'
})
export class RegisterComponent {
  credentials = { email: '', password: '' };

  constructor(private authService: AuthService) {}

  onSubmit() {
    this.authService.register(this.credentials).subscribe(
      () => alert('Регистрация успешна!'),
      error => console.error(error)
    );
  }
}
