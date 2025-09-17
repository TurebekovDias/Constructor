import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { RouterLink, RouterModule } from "@angular/router";

@Component({
  selector: 'app-main.component',
  imports: [MatButtonModule, RouterLink, RouterModule],
  templateUrl: './main.component.html',
  styleUrl: './main.component.scss'
})
export class MainComponent {

}
