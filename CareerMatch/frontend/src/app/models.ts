export interface Job {
  id: number;
  title: string;
  company?: string;
  location?: string;
  description?: string;
  owner_id?: number;
}

export interface Applicant {
  id: number;
  name: string;
  email: string;
  cv_path: string;
}
