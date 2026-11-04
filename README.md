# Krioza Academy (`krioza_training`)

Training center management for **Odoo 20**: courses, sessions, trainers,
trainees and registrations. Built step by step in the YouTube course
"Odoo 20 module development" (Arabic).

## Features

- Courses with categories, trainers, seats and dates; sessions with calendar and kanban views
- Registrations with a workflow (draft, confirmed, done, cancelled) and chatter
- Security groups (Trainer, Manager) with record rules via `ir.access.csv`
- Server actions, automated actions and a scheduled email reminder before each session
- PDF certificate (QWeb report)
- Demo data and an Arabic translation (`i18n/ar.po`)
- Sales integration: create a sale order from a registration
- Public web pages (`/courses`) and a JSON endpoint
- External API example using JSON-2 (`examples/krioza_api_client.py`)
- Unit tests and an OWL dashboard

## Requirements

- Odoo 20 (Community)
- Python version required by your Odoo 20 installation
- Odoo apps: `base`, `mail`, `base_automation`, `sale`

## Installation

1. Clone this repository next to your Odoo addons:

   ```
   git clone https://github.com/AbdallatifTiyah/training-center-management.git
   ```

2. Add the repository folder to `addons_path` in your `odoo.conf`:

   ```
   addons_path = odoo/addons,training-center-management
   ```

3. Restart Odoo, update the apps list, and install **Krioza Academy**.

## Running the tests

```
python odoo/odoo-bin -c odoo.conf -d krioza_test -i krioza_training --test-tags /krioza_training --stop-after-init
```

## External API example

Edit `DB` and `API_KEY` in `examples/krioza_api_client.py`, then run it with
Python. Never commit a real API key.

## Get the code of an episode

Every episode is one commit with its own tag (`ep-01` ... `ep-33`), so you can get the exact code you see in the video:

- **ZIP, no Git needed:** `https://github.com/AbdallatifTiyah/training-center-management/archive/refs/tags/ep-05.zip` (change `ep-05` to your episode)
- **Browse online:** `https://github.com/AbdallatifTiyah/training-center-management/tree/ep-05`
- **Clone:** `git clone https://github.com/AbdallatifTiyah/training-center-management.git` then `git checkout ep-05`
- **What changed in an episode:** the *diff* link in the table below

## Use it on Windows (as in the course)

1. Download and extract the ZIP of your episode.
2. Copy the `krioza_training` folder into `~\odoo20\custom_addons\`.
3. Copy `setup\odoo.conf.example` to `~\odoo20\odoo.conf` and change the passwords.
4. Copy `setup\start_odoo.bat` (and `setup\upgrade_odoo.bat` from episode 3) to `~\odoo20\`.
5. Start Odoo with `start_odoo.bat`. After you change the code, update the module with `upgrade_odoo.bat`.

Each setup file appears in `setup\` from the episode that introduces it.

## Episodes

| # | الحلقة | Topic | Code | ZIP | Changes |
|---|---|---|---|---|---|
| 1 | تثبيت Odoo 20 على Windows من الصفر | Install Odoo 20 on Windows | [ep-01]

| 2 | واجهة Odoo من جوّا + أول موديول | Odoo UI tour and first module | [ep-02](https://github.com/AbdallatifTiyah/training-center-management/tree/ep-02) |
| 3 | أول Model: الدورات | First model: courses | [ep-03](https://github.com/AbdallatifTiyah/training-center-management/tree/ep-03) | 
