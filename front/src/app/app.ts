import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MatButtonModule } from '@angular/material/button';
import { HeaderComponent } from "./layout/header/header.component/header.component";
import { WelcomePageComponent } from "./pages/welcome-page.component/welcome-page.component";

@Component({
  selector: 'app-root',
  imports: [MatButtonModule, RouterOutlet, HeaderComponent],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  
}
