// Renderiza cada HTML de ./piezas a PNG 2160x2700 (4:5 @2x) en ../png
// Uso: node render.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const src = path.join(__dirname, 'piezas');
  const out = path.join(__dirname, '..', 'png');
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  for (const f of fs.readdirSync(src).filter(f => f.endsWith('.html')).sort()) {
    await page.goto('file://' + path.join(src, f));
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(out, f.replace('.html', '.png')) });
    console.log('ok', f);
  }
  await browser.close();
})();
