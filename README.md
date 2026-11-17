# CrossTrace

**Allergen cross-contamination monitoring for commercial kitchens.**

CrossTrace watches a kitchen counter through ceiling cameras and tracks every cook's hands. Each hand is **clean**, **unknown** or **contaminated**, and it carries the allergens it has touched (gluten, sugar, dairy). When an unsafe hand touches an allergen-free zone, the shift manager's phone receives an alert with a 4-second clip of the moment, so the problem can be handled before the food goes out.

Final project, Department of Information Systems · 2026–2027

| | |
|---|---|
| **Team** | Lama · Nadine · Qasem |
| **Supervisor** | Prof. Mor |
| **Client** | Caramel, Old Akko |

---

## Work plan

The project schedule is published as an interactive Gantt chart, in Hebrew and English:

**🔗 Live Gantt chart:** _link added after the first deployment_

It shows every task with its owner, time window, expected effort and completion criteria, together with milestones and the planned progress updates. Click any task to see its details.

### Timeline at a glance

| Phase | Period | Outcome |
|---|---|---|
| Part A | Nov 2026 – Feb 2027 | Requirements, test kitchen, camera setup, hand rules, first end-to-end alert, Part A report |
| Part B | Mar 2027 – Jun 2027 | Full mobile app, owner dashboard, wall screen, robustness, final evaluation, poster |
| Final presentation | 1 Jun 2027 | Live demonstration with measured results |

---

## How it works

```
Cameras ──Wi-Fi──► Kitchen computer ──internet──► Supabase ──push──► Mobile app
                   detection + hand rules                            Owner dashboard
                   wall screen (works offline)
```

1. **Zones.** The counter is divided into source zones (e.g. flour), protected zones (e.g. the gluten-free board), a sink and a door.
2. **Hands.** Every hand has its own state. A cook entering through the door starts as *unknown*; washing both hands together makes them *clean*; touching a source zone makes that hand *contaminated* with that zone's allergens.
3. **Violations.** An unknown or contaminated hand touching a protected zone that forbids what it carries triggers an alert. A hand that only passes over a zone does not count as a touch.
4. **Alerts.** The shift manager gets a push notification with the clip and can mark it as handled, item cleaned, or false alarm, directly from the notification.

## Technology

| Area | Stack |
|---|---|
| Computer vision | Python, OpenCV, YOLO11-pose, ByteTrack, MediaPipe, Depth Anything V2 |
| Kitchen server | FastAPI, WebSockets |
| Backend | Supabase (Postgres, Auth, Storage, Realtime, Edge Functions) |
| Mobile app | Expo (React Native), iOS and Android |
| Owner dashboard | Next.js, Tailwind CSS |

---

## Repository structure

```
CrossTrace/
├── gantt/
│   ├── tasks.json      Plan data: tasks, owners, dates, dependencies
│   ├── template.html   Gantt page template
│   └── build.py        Builds the page from the data
├── site/
│   └── index.html      Built Gantt page (deployed to Vercel)
└── vercel.json         Deployment settings
```

## Updating the Gantt

1. Edit `gantt/tasks.json`: dates, owners, or a task's `status` (`in_progress` or `done`).
2. Rebuild the page:
   ```bash
   python3 gantt/build.py
   ```
3. Commit and push. Vercel redeploys automatically.

No dependencies are required beyond Python 3.

## Deployment

The Gantt is a static page served from `site/` on Vercel.

- **First time:** import this repository at [vercel.com/new](https://vercel.com/new). The settings in `vercel.json` are picked up automatically; no build step is needed.
- **After that:** every push to `main` updates the live page.

---

© 2026 The CrossTrace team. All rights reserved.
