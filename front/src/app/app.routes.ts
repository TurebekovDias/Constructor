import { Routes } from '@angular/router';
import { WelcomePageComponent } from './pages/welcome-page.component/welcome-page.component';
import { AboutUsComponent } from './pages/about-us.component/about-us.component';
import { AuthComponent } from './core/auth/auth.component/auth.component';
export const routes: Routes = [
   {
    path: '',
    component: WelcomePageComponent
   },
   {
    path: 'about-us',
    component: AboutUsComponent
   },
   {
    path: 'auth',
    component: AuthComponent
   }
];
