import { Component, inject } from '@angular/core';
import { FooterComponent } from '../../layout/footer/footer.component/footer.component';
import { MatButtonModule } from "@angular/material/button";
import { MatDialog } from '@angular/material/dialog';
import { AuthComponent } from '../../core/auth/auth.component/auth.component';

@Component({
  selector: 'app-welcome-page',
  imports: [FooterComponent, MatButtonModule],
  templateUrl: './welcome-page.component.html',
  styleUrl: './welcome-page.component.scss'
})
export class WelcomePageComponent {
  readonly dialog = inject(MatDialog)
  openDialog() {
    this.dialog.open(AuthComponent, {
      width: '500px'
      
    })
  }
}