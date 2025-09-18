import { Component } from '@angular/core';
import { RouterOutlet,  } from '@angular/router';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-root',
  imports: [ MatButtonModule],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  
}
