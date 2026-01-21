import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { LandingComponent } from './landing/landing.component';
import { JobDetailComponent } from './job-detail/job-detail.component';
import { ApplicantsComponent } from './applicants/applicants.component';
import { routes } from './app.routes';
import { AuthService } from './services/auth.service';

@NgModule({
  declarations: [AppComponent, LandingComponent, JobDetailComponent, ApplicantsComponent],
  imports: [BrowserModule, FormsModule, HttpClientModule, RouterModule.forRoot(routes)],
  bootstrap: [AppComponent]
})
export class AppModule { }
