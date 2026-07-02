import type { DetectionDetail, DetectionMeta, HqlRun } from '../types'

const BASE = '/api'

export class ApiError extends Error {
  constructor(
    message: string,
    public status?: number,
  ) {
    super(message)
    this.name = 'ApiError'
  }
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${BASE}${path}`, init)
  if (!res.ok) {
    let detail = res.statusText
    try {
      const body = (await res.json()) as { detail?: string }
      if (body.detail) detail = body.detail
    } catch {
      // non-JSON error body, keep statusText
    }
    throw new ApiError(detail, res.status)
  }
  return (await res.json()) as T
}

function postJson<T>(path: string, body: unknown, signal?: AbortSignal): Promise<T> {
  return request<T>(path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
    signal,
  })
}

export function startRun(hql: string, signal?: AbortSignal): Promise<{ id: string }> {
  return postJson('/hql/runs', { hql, run: true, save: false, plan: false }, signal)
}

export function getRun(id: string, signal?: AbortSignal): Promise<HqlRun> {
  return request(`/hql/runs/${encodeURIComponent(id)}`, { signal })
}

const POLL_INTERVAL_MS = 1000
const POLL_CEILING_MS = 10 * 60 * 1000

/** Poll a run until completed/failed. Aborting the signal stops waiting. */
export async function pollRun(id: string, signal: AbortSignal): Promise<HqlRun> {
  const deadline = Date.now() + POLL_CEILING_MS
  for (;;) {
    const run = await getRun(id, signal)
    if (run.completed || run.failed) return run
    if (Date.now() > deadline) throw new ApiError('Timed out waiting for run after 10 minutes')
    await new Promise((resolve, reject) => {
      const t = setTimeout(resolve, POLL_INTERVAL_MS)
      signal.addEventListener(
        'abort',
        () => {
          clearTimeout(t)
          reject(new DOMException('Aborted', 'AbortError'))
        },
        { once: true },
      )
    })
  }
}

export function getDetections(): Promise<DetectionMeta[]> {
  return request('/detections')
}

export function getDetection(id: string): Promise<DetectionDetail> {
  return request(`/detections/${encodeURIComponent(id)}`)
}

// The backend reads the raw body, so this is not JSON
export function saveDetection(text: string): Promise<{ id: string }> {
  return request('/detections', {
    method: 'POST',
    headers: { 'Content-Type': 'text/plain' },
    body: text,
  })
}

export function initHac(hql: string): Promise<{ hql: string }> {
  return postJson('/hql/init_hac', { hql, run: false })
}

export function convertSigma(hql: string): Promise<{ hql: string }> {
  return postJson('/sigma/convert', { hql, run: false })
}

export function retroHunt(hql: string, start: string, end: string): Promise<{ ids: string[] }> {
  return postJson('/detections/retro', { hql, run: true, retro: true, start, end })
}
