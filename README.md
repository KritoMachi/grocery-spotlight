# Grocery Spotlight

Landing page and interactive demo for Grocery Spotlight, a grocery app that shows what's in season, suggests swaps, and alerts shoppers to produce recalls.

## Files

```
index.html                       # Landing page
demo.html                        # Interactive mobile app demo
prototype-animated-landing.html  # Earlier prototype (unused)
download_assets.py               # Asset download script (unused)
assets/                          # Logos and images
```

## Landing page

Sections: Home, Problem, Solution, Who It's For, Features, Waitlist, Team.

**Side rail.** The navigation is a slim dot rail on the right edge, with a progress line that fills as you scroll. It builds itself from the page: to add a section, give it an `id` and a `data-nav="Label"` attribute and it appears in the rail automatically.

```html
<section id="pricing" data-nav="Pricing"> ... </section>
```

## Waitlist setup (Google Sheets)

The waitlist form posts emails to `WAITLIST_ENDPOINT` in the script at the bottom of `index.html`. Until that is set, the form shows "Signups aren't open just yet" and nothing is stored.

1. Create a Google Sheet. In row 1 add the headers `timestamp`, `email`, `source`.
2. Open **Extensions → Apps Script** and paste:

   ```js
   function doPost(e) {
     const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
     sheet.appendRow([new Date(), e.parameter.email, e.parameter.source]);
     return ContentService.createTextOutput('ok');
   }
   ```

3. **Deploy → New deployment → Web app**. Execute as *Me*, access *Anyone*. Copy the web app URL.
4. Paste that URL into `WAITLIST_ENDPOINT` in `index.html`, commit, and push.

Emails then land in the sheet, where you can sort and filter them.

## Running locally

```bash
python -m http.server 8085
```

Then open http://localhost:8085. The site is published with GitHub Pages from `main`.
