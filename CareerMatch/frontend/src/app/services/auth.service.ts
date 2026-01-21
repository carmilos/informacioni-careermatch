import { Injectable } from '@angular/core';
import { ApiService } from './api.service';

@Injectable({ providedIn: 'root' })
export class AuthService {
  user: any = null;
  constructor(private api: ApiService) {
    const token = localStorage.getItem('token');
    if (token) this.fetchMe();
  }

  login(username: string, password: string) {
    return this.api.login(username, password).toPromise().then((res: any) => {
      localStorage.setItem('token', res.access_token);
      return this.fetchMe();
    });
  }

  register(email: string, password: string, is_hr = false) {
    return this.api.register({ email, password, is_hr }).toPromise();
  }

  fetchMe() {
    return this.api.http.get(`${this.api.api}/auth/me`, { headers: this.api['authHeaders']().headers }).toPromise().then((u: any) => { this.user = u; return u; });
  }

  logout() {
    localStorage.removeItem('token');
    this.user = null;
  }

  isHR() { return !!(this.user && this.user.is_hr); }
}
