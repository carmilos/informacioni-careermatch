import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../services/api.service';
import { Applicant } from '../models';

@Component({
  selector: 'app-applicants',
  templateUrl: './applicants.component.html'
})
export class ApplicantsComponent {
  applicants: Applicant[] = [];
  jobId = 0;
  constructor(private route: ActivatedRoute, private api: ApiService) {
    this.jobId = Number(this.route.snapshot.paramMap.get('id'));
    this.load();
  }
  load() { this.api.getApplicants(this.jobId).subscribe(a => this.applicants = a); }
}
