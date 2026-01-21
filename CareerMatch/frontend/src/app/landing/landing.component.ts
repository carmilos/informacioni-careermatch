import { Component } from '@angular/core';
import { ApiService } from '../services/api.service';
import { AuthService } from '../services/auth.service';
import { Job } from '../models';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html'
})
export class LandingComponent {
  jobs: Job[] = [];
  showCreate = false;
  newJob = { title: '', company: '', location: '', description: '' };
  // auth fields
  loginEmail = '';
  loginPassword = '';
  registerEmail = '';
  registerPassword = '';

  constructor(private api: ApiService, public auth: AuthService) { this.load(); }

  load() { this.api.listJobs().subscribe(j => this.jobs = j); }

  toggleCreate() { this.showCreate = !this.showCreate; }

  create() {
    this.api.createJob(this.newJob).subscribe(() => { this.newJob = { title: '', company: '', location: '', description: '' }; this.showCreate = false; this.load(); });
  }

  doLogin() {
    this.auth.login(this.loginEmail, this.loginPassword).then(() => this.load());
  }

  doRegister() {
    this.auth.register(this.registerEmail, this.registerPassword, true).then(() => alert('Registered; now login'));
  }
}
