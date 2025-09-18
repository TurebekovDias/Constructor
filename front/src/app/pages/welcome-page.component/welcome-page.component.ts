import { Component } from '@angular/core';
import { FooterComponent } from '../../layout/footer/footer.component/footer.component';
import { MatButtonModule } from "@angular/material/button";

@Component({
  selector: 'app-welcome-page',
  imports: [FooterComponent, MatButtonModule],
  templateUrl: './welcome-page.component.html',
  styleUrl: './welcome-page.component.scss'
})
export class WelcomePageComponent {

}
