import { Routes } from '@angular/router';
import { WelcomePageComponent } from './pages/welcome-page.component/welcome-page.component';
import { AboutUsComponent } from './pages/about-us.component/about-us.component';
import { AuthComponent } from './core/auth/auth.component/auth.component';
import { WorkSpaceComponent } from './pages/work-space.component/work-space.component';
import { AuthGuard } from './core/guards/auth-guard';
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
   },
   {
    path: 'workspace',
    component: WorkSpaceComponent,
    canActivate: [AuthGuard]
   }
];
