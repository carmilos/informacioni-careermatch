import { Routes } from '@angular/router';
import { LandingComponent } from './landing/landing.component';
import { JobDetailComponent } from './job-detail/job-detail.component';
import { ApplicantsComponent } from './applicants/applicants.component';

export const routes: Routes = [
  { path: '', component: LandingComponent },
  { path: 'jobs/:id', component: JobDetailComponent },
  { path: 'jobs/:id/applicants', component: ApplicantsComponent },
  { path: '**', redirectTo: '' }
];
