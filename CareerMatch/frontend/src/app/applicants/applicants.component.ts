
import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../services/api.service';
import { Applicant } from '../models';

@Component({
  selector: 'app-applicants',
  templateUrl: './applicants.component.html',
  styleUrls: ['./applicants.component.css']
})
export class ApplicantsComponent {
  applicants: Applicant[] = [];
  jobId = 0;
  job: any = null;
  showCVModal = false;
  cvContent = '';

  constructor(private route: ActivatedRoute, private api: ApiService) {
    this.jobId = Number(this.route.snapshot.paramMap.get('id'));
    this.api.getJob(this.jobId).subscribe(j => this.job = j);
    this.load();
  }
  load() { this.api.getApplicants(this.jobId).subscribe(a => this.applicants = a); }

  getFilename(path: string): string {
    if (!path) return '';
    return path.split('/').pop()?.split('\\').pop() || path;
  }
  
  showCV(a: any) {
    if (!a.cv_path) return;
    // Učitaj sadržaj fajla kao tekst
    const filename = a.cv_path.split(/[\\/]/).pop();
    this.api.get(`/uploads/${filename}`, false).subscribe({
      next: (res: any) => {
        // Ako je tekstualni fajl, prikaži kao string
        if (typeof res === 'string') {
          this.cvContent = res;
        } else if (res instanceof Blob) {
          const reader = new FileReader();
          reader.onload = () => {
            this.cvContent = reader.result as string;
            this.showCVModal = true;
          };
          reader.readAsText(res);
          return;
        } else {
          this.cvContent = '[CV cannot be previewed]';
        }
        this.showCVModal = true;
      },
      error: () => {
        this.cvContent = '[Error loading CV]';
        this.showCVModal = true;
      }
    });
  }

  closeCV() {
    this.showCVModal = false;
    this.cvContent = '';
  }
}
