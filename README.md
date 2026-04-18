# National Forest Trail App

A Flask backend for exploring NPS park data with client-side caching using Dexie.js (IndexedDB). Search results are stored locally on the device for fast, offline-capable lookups.

## Features

- Search NPS Parks and Trails
- Local caching with Dexie.js IndexedDB for offline access
- Mobile-friendly UI for iPhone Safari
- State-based filtering

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create an NPS API key at https://www.nps.gov/subjects/developer/get-started.htm
3. Set the API key in `.env`:
   ```text
   NPS_API_KEY=your_actual_nps_api_key_here
   ```
4. Run the app:
   ```bash
   python main.py
   ```

## Usage

1. Open `http://127.0.0.1:5000/` in a browser
2. Click "Sync Data" to download parks and trails from NPS and cache them locally
3. Search the local cache with keywords like `hiking`, `trail`, `park name`
4. Optionally filter by state code (e.g., `CA`, `OH`)

## API Endpoints

- `/api/parks` — retrieve NPS parks data
- `/api/trails` — retrieve NPS trail-related activities
- `/api/activities/parks` — retrieve NPS activities by park

Example:

```bash
curl "http://127.0.0.1:5000/api/trails?q=hiking&stateCode=CA&limit=100"
```

## Architecture

**Backend**: Flask + requests (Python)
- Proxies requests to NPS API (`developer.nps.gov/api/v1/`)
- Returns JSON responses

**Frontend**: Dexie.js + IndexedDB
- Stores parks and trails in browser IndexedDB
- Searches performed locally for instant results
- Syncs data on-demand via "Sync Data" button

## Technology Stack

- Flask, Python 3.9+, requests, python-dotenv
- Dexie.js, HTML5, CSS3
- IndexedDB (browser-based local storage)

## Notes

- Uses NPS API (National Parks only), not state parks or local trails
- For USGS trail data, the ArcGIS service integration requires public network access
