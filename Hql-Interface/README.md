# HQL Interface

Web interface for HQL (Hunt Query Language) query execution and detection management.

## Features

- **Query Editor**: Monaco-based code editor with syntax highlighting
- **Results Table**: Sortable, filterable, paginated results display
- **Schema Explorer**: Browse available fields and data types
- **Detections Library**: View and manage scheduled detections
- **Theme Support**: Gruvbox light and dark themes
- **Real-time Execution**: Execute queries and poll for results

## Development

### Prerequisites

- Node.js 20.x or later
- npm

### Setup

```bash
cd Hql-Interface
npm install
```

### Run Development Server

```bash
npm run dev
```

The development server will start on http://localhost:5173 and proxy API requests to http://localhost:8081.

### Build for Production

```bash
npm run build
```

The built files will be in the `dist/` directory.

## Container Deployment

The interface is automatically built and served when using the Podman/Docker container:

```bash
# Build the container
podman build -t hql .

# Run the container
podman run -p 8081:8081 -v ./conf:/data/conf -v ./examples:/data/examples hql
```

Access the interface at http://localhost:8081

## API Endpoints

The frontend communicates with these backend API endpoints:

- `POST /api/hql/runs` - Execute a query
- `GET /api/hql/runs/:id` - Get query results by ID
- `GET /api/hql/runs` - List all query runs
- `GET /api/detections` - List all detections
- `GET /api/detections/:id/history` - Get detection run history
- `POST /api/detections` - Save a new detection
- `GET /api/schema` - Get available fields and types

## Architecture

- **Frontend**: React 18 + TypeScript + Vite
- **Styling**: Tailwind CSS with custom Gruvbox theme
- **Table**: TanStack Table for data grid
- **Editor**: Monaco Editor for code editing
- **Backend**: FastAPI serving both API and static files
