import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../services/api.service';
import { AuthService } from '../services/auth.service';
import { Job } from '../models';

@Component({
  selector: 'app-job-detail',
  templateUrl: './job-detail.component.html'
})
export class JobDetailComponent {
  job: Job | null = null;
  name = '';
  email = '';
  cv: File | null = null;

  constructor(private route: ActivatedRoute, private api: ApiService, public auth: AuthService) {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.api.getJob(id).subscribe(j => this.job = j);
  }

  onFile(e: any) { this.cv = e.target.files[0]; }

  apply() {
    if (!this.job || !this.cv) return alert('Provide name, email and CV');
    const fd = new FormData();
    fd.append('name', this.name);
    fd.append('email', this.email);
    fd.append('cv', this.cv, this.cv.name);
    this.api.apply(this.job.id, fd).subscribe(() => alert('Application sent'));
  }
}
