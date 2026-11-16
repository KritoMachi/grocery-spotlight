# Grocery Spotlight — Web Platform & Interactive MVP

This project contains the assets, landing page, and interactive mobile demo downloaded and assembled from Stitch Project **Company Landing Page MVP** (`558176700809783641`), Screen **Grocery Spotlight — Animated Landing Page** (`4a6fc0dff43448ff9581b4473590c861`).

---

## Project Structure

```
spotlight/
├── index.html                   # Main Company Landing Page
├── demo.html                    # Interactive Mobile App Simulator
├── prototype-animated-landing.html # Prototype screen variant
├── download_assets.py           # Asset download and extraction script
├── assets/
│   ├── logo-refined-mark.svg    # Vector brand mark
│   ├── logo-refined-mark.png    # Brand mark PNG
│   ├── logo-pin-produce.svg     # Secondary pin-produce logo SVG
│   ├── logo-pin-produce.png     # Secondary pin-produce logo PNG
│   ├── screenshot-animated-landing.png # Full-resolution screen capture
│   └── sweet-potatoes.jpg       # Product showcase imagery
└── .agents/
    └── mcp_config.json          # MCP configuration for Stitch API
```

---

## Features

### 1. Company Landing Page (`index.html`)
* **Hero Section**: Value proposition, conversion metrics, CTA buttons, and interactive phone showcase.
* **The Problem Statement**: 68% stale import and 1-in-4 recall unawareness statistics with transit drag and shelf comparison.
* **The Solution**: Side-by-side comparison between Industrial Supply Chains and the Grocery Spotlight live farm mesh model.
* **Target Audience Profiles**: Home cooks, safety-minded meal planners, and budget/eco shoppers.
* **Four Pillars of Produce Intelligence**:
  1. Regional Harvest Radar
  2. 1:1 Culinary Swap Engine
  3. Automated FDA Recall Safeguard
  4. Persistent Cart Swap Drawer
* **Beta Waitlist**: Responsive email signup form with instant feedback.
* **Team & Footer**: Core team presentation, deliverables, and newsletter subscription.

### 2. Interactive Mobile App Simulator (`demo.html`)
* **Seasonal Harvest**: Dynamic view for local farm produce availability.
* **Smart Swaps Engine**: 1:1 culinary substitutions with instant replacement.
* **Recall Bulletin**: Real-time pathogen alerts (Salmonella, Listeria) with safe alternatives.
* **Navigation**: Persistent floating link to return to the main landing page.

---

## Running Locally

To view the website in your browser, launch any static web server:

```powershell
python -m http.server 8085
```

Then open `http://localhost:8085` in your browser.
