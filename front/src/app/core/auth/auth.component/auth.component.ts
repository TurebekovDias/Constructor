import { Component } from '@angular/core';
import { MatTabsModule } from '@angular/material/tabs'
import { RegisterComponent } from '../register.component/register.component';
import { LoginComponent } from '../login.component/login.component';
interface AuthForm {
  email: string;
  password: string;
}

@Component({
  selector: 'app-auth.component',
  imports: [ MatTabsModule, RegisterComponent, LoginComponent ],
  templateUrl: './auth.component.html',
  styleUrl: './auth.component.scss'
})
export class AuthComponent {
  
}
