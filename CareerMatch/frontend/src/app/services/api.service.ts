import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';
import { Job, Applicant } from '../models';

@Injectable({ providedIn: 'root' })
export class ApiService {
  api = environment.apiUrl;
  constructor(private http: HttpClient) { }

  private authHeaders() {
    const token = localStorage.getItem('token');
    return token ? { headers: new HttpHeaders({ Authorization: `Bearer ${token}` }) } : {};
  }

  // Generic GET helper. `path` may be absolute or relative to API base.
  get<T = any>(path: string, includeAuth = true) {
    const url = path.startsWith('http') ? path : `${this.api}${path.startsWith('/') ? path : '/' + path}`;
    const opts = includeAuth ? this.authHeaders() : {};
    return this.http.get<T>(url, opts);
  }

  listJobs(): Observable<Job[]> { return this.http.get<Job[]>(`${this.api}/jobs`); }
  getJob(id: number): Observable<Job> { return this.http.get<Job>(`${this.api}/jobs/${id}`); }
  createJob(data: any): Observable<Job> { return this.http.post<Job>(`${this.api}/jobs`, data, this.authHeaders()); }
  apply(jobId: number, formData: FormData): Observable<Applicant> { return this.http.post<Applicant>(`${this.api}/jobs/${jobId}/apply`, formData); }
  getApplicants(jobId: number) { return this.http.get<Applicant[]>(`${this.api}/jobs/${jobId}/applicants`, this.authHeaders()); }
  login(username: string, password: string) { return this.http.post<any>(`${this.api}/auth/login`, { username, password }); }
  register(data: any) { return this.http.post<any>(`${this.api}/auth/register`, data); }
  updateJob(id: number, data: any): Observable<Job> {
    return this.http.put<Job>(`${this.api}/jobs/${id}`, data, this.authHeaders());
  }
}
