import type {
  HqlRequest,
  HqlRunResponse,
  HqlRun,
  Detection,
  SchemaField,
  HacInitResponse,
  SigmaConvertResponse,
  RetroHuntResponse,
} from '../types';

const API_BASE = '/api';

class ApiError extends Error {
  constructor(public status: number, message: string) {
    super(message);
    this.name = 'ApiError';
  }
}

async function fetchApi<T>(
  endpoint: string,
  options?: RequestInit
): Promise<T> {
  const response = await fetch(`${API_BASE}${endpoint}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options?.headers,
    },
  });

  if (!response.ok) {
    const error = await response.text();
    throw new ApiError(response.status, error || response.statusText);
  }

  return response.json();
}

export const api = {
  // Execute HQL query
  executeQuery: async (hql: string, save = false): Promise<HqlRunResponse> => {
    const request: HqlRequest = {
      hql,
      run: true,
      save,
      plan: false,
    };
    return fetchApi<HqlRunResponse>('/hql/runs', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  },

  // Get query run by ID
  getRun: async (runId: string): Promise<HqlRun> => {
    return fetchApi<HqlRun>(`/hql/runs/${runId}`);
  },

  // Get all runs
  getRuns: async (): Promise<HqlRun[]> => {
    return fetchApi<HqlRun[]>('/hql/runs');
  },

  // Get all detections
  getDetections: async (): Promise<Detection[]> => {
    return fetchApi<Detection[]>('/detections');
  },

  // Get detection history
  getDetectionHistory: async (detectionId: string): Promise<any[]> => {
    return fetchApi<any[]>(`/detections/${detectionId}/history`);
  },

  // Get schema/fields
  getSchema: async (): Promise<SchemaField[]> => {
    return fetchApi<SchemaField[]>('/schema');
  },

  // Poll for run completion
  pollRunUntilComplete: async (
    runId: string,
    maxAttempts = 60,
    intervalMs = 1000
  ): Promise<HqlRun> => {
    for (let i = 0; i < maxAttempts; i++) {
      const run = await api.getRun(runId);
      if (run.completed || run.failed) {
        return run;
      }
      await new Promise((resolve) => setTimeout(resolve, intervalMs));
    }
    throw new Error('Query execution timeout');
  },

  // Initialize HAC for HQL query
  initHac: async (hql: string): Promise<HacInitResponse> => {
    const request: HqlRequest = {
      hql,
      run: false,
      save: false,
      plan: false,
    };
    return fetchApi<HacInitResponse>('/hql/init_hac', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  },

  // Convert Sigma rule to HQL
  convertSigma: async (hql: string): Promise<SigmaConvertResponse> => {
    const request: HqlRequest = {
      hql,
      run: false,
      save: false,
      plan: false,
    };
    return fetchApi<SigmaConvertResponse>('/sigma/convert', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  },

  // Retro hunt with date range
  retroHunt: async (hql: string, start: Date, end: Date): Promise<RetroHuntResponse> => {
    const request: HqlRequest = {
      hql,
      run: false,
      save: false,
      plan: false,
      start: start.toISOString(),
      end: end.toISOString(),
      retro: true,
    };
    return fetchApi<RetroHuntResponse>('/detections/retro', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  },
};

export { ApiError };
