import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from "@angular/material/button";
import { MatIconModule } from "@angular/material/icon";
import { RouterLink } from "@angular/router";
import { MatDialog } from '@angular/material/dialog';
import { AuthComponent } from '../../../core/auth/auth.component/auth.component';
@Component({
  selector: 'app-header',
  imports: [CommonModule, MatSidenavModule, MatToolbarModule, MatButtonModule, MatIconModule, RouterLink],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {
  readonly dialog = inject(MatDialog)
  openDialog() {
    this.dialog.open(AuthComponent, {
      width: '500px'
      
    })
  }
}
