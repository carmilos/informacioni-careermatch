import { Component } from '@angular/core';
import { AuthService } from './services/auth.service';

@Component({
  selector: 'app-root',
  template: `
  <div class="app-container">
    <header class="header">
      <div class="brand">
        <div class="logo">CM</div>
        <div>
          <div class="title">CareerMatch</div>
          <div class="muted">Find and post great jobs</div>
        </div>
      </div>
      <div class="nav-right">
        <div *ngIf="!auth.user" class="muted">Guest</div>
        <div *ngIf="auth.user" class="muted">{{auth.user.email}}</div>
        <button *ngIf="auth.user" class="button ghost" (click)="auth.logout()">Logout</button>
      </div>
    </header>

    <router-outlet></router-outlet>
  </div>
  `
})
export class AppComponent { constructor(public auth: AuthService){} }
