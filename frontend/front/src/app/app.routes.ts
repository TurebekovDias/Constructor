import { Routes } from '@angular/router';
import { MainComponent } from './main.component/main.component'
import { WorkSpaceComponent } from './work-space.component/work-space.component';
import { AboutUsComponent } from './about-us.component/about-us.component';
import { AuthComponent } from './auth.component/auth.component';

export const routes: Routes = [
    {
        path: '',
        component: MainComponent,
        pathMatch: 'full'
    },
    {
        path: 'work-space',
        component: WorkSpaceComponent
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
        path: '**', redirectTo: '' 
    },
];
