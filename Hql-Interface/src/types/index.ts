// API Types
export interface HqlRequest {
  hql: string;
  run: boolean;
  save: boolean;
  plan: boolean;
  start?: string; // ISO 8601 datetime string
  end?: string; // ISO 8601 datetime string
  retro?: boolean;
}

export interface HqlRunResponse {
  id: string;
}

export interface HqlRun {
  run_id: string;
  run_date: string;
  started: boolean;
  failed: boolean;
  completed: boolean;
  num_results: number;
  duration: number;
  results?: {
    // Data can be either a direct array or keyed by table name
    data?: Record<string, any>[] | Record<string, Record<string, any>[]>;
    schema?: Record<string, string> | Record<string, Record<string, string>>;
  };
  str_out?: string;
  hac?: any;
}

export interface Detection {
  id: string;
  title: string;
  description: string;
  author: string;
  status: string;
  schedule: string;
  hql?: string;
  src?: string;
}

export interface SchemaField {
  name: string;
  type: string;
  children?: SchemaField[];
}

export interface QueryResult {
  columns: string[];
  data: Record<string, any>[];
  duration?: number;
  rowCount: number;
}

export interface HacInitResponse {
  hql: string;
}

export interface SigmaConvertResponse {
  hql: string;
}

export interface RetroHuntResponse {
  ids: string[];
}

// UI State Types
export type Theme = 'light' | 'dark';

export interface QueryEditorState {
  query: string;
  isExecuting: boolean;
  results: QueryResult | null;
  error: string | null;
}
