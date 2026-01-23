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
  cvText: string = '';
  showApply = false;

  constructor(private route: ActivatedRoute, private api: ApiService, public auth: AuthService) {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.api.getJob(id).subscribe(j => this.job = j);
  }

  onFile(e: any) { this.cv = e.target.files[0]; }

  canSeeApplicants() {
    return this.auth.isHR() && this.job && this.auth.user && this.job.owner_id === this.auth.user.id;
  }

  apply() {
    if (!this.job || (!this.cv && !this.cvText.trim())) return alert('Provide name, email and CV (file or text)');
    const fd = new FormData();
    fd.append('name', this.name);
    fd.append('email', this.email);
    if (this.cv) fd.append('cv', this.cv, this.cv.name);
    if (this.cvText && this.cvText.trim().length > 0) fd.append('cv_text', this.cvText);
    this.api.apply(this.job.id, fd).subscribe(() => alert('Application sent'));
  }
  
    resetApplyForm() {
      this.name = '';
      this.email = '';
      this.cv = null;
      this.cvText = '';
    }
  
    removeFile() {
      this.cv = null;
    }
  
    openApply() {
      this.resetApplyForm();
      this.showApply = true;
    }
  
    closeApply() {
      this.resetApplyForm();
      this.showApply = false;
    }
}
