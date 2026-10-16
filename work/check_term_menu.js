const { chromium } = require('playwright-core');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', headless: true, args: ['--allow-file-access-from-files'] });
  const errors = [];
  for (const [name, width, height] of [['desktop', 1440, 900], ['mobile', 390, 844]]) {
    const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 1 });
    page.on('pageerror', error => errors.push(`${name}: ${error.message}`));
    await page.goto('file:///' + path.resolve(__dirname, '../uni-grade/index.html').replace(/\\/g, '/'));
    if (await page.locator('#btn-onboard-skip').isVisible()) await page.locator('#btn-onboard-skip').click();
    await page.locator('#btn-login-guest').click();
    await page.evaluate(() => {
      localStorage.setItem('guest_mode', 'true');
      localStorage.setItem('onboarding_done_v2', 'true');
      localStorage.setItem('st_data', JSON.stringify({ currentTermId: 1, gpaTarget: 3.5, terms: [
        { id: 1, name: 'ภาคต้น 2569', subjects: [{ id: 10, name: 'แคลคูลัส', credits: 3, quickMode: true, quickGrade: 'B+', categories: [] }] },
        { id: 2, name: 'ภาคปลาย 2569', subjects: [] },
        { id: 3, name: 'ภาคฤดูร้อน 2569', subjects: [] }
      ] }));
    });
    await page.reload();
    await page.locator('#btn-login-guest').click();
    await page.locator('#term-trigger').click();
    await page.waitForTimeout(150);
    console.log(name, 'open', await page.locator('#term-list').isVisible(), 'expanded', await page.locator('#term-trigger').getAttribute('aria-expanded'));
    console.log(name, 'menu bounds', await page.locator('#term-list').boundingBox(), 'active', await page.locator('.term-item[aria-current="true"]').innerText());
    await page.locator('.term-menu-close').focus();
    await page.keyboard.press('Shift+Tab');
    console.log(name, 'focus wrap to last', await page.locator('.term-item').last().evaluate(el => el === document.activeElement));
    await page.keyboard.press('Tab');
    console.log(name, 'focus wrap to close', await page.locator('.term-menu-close').evaluate(el => el === document.activeElement));
    await page.screenshot({ path: path.resolve(__dirname, `term-menu-${name}.png`), fullPage: false });
    await page.keyboard.press('Escape');
    console.log(name, 'escape closed', !(await page.locator('#term-list').isVisible()));
    await page.locator('#term-trigger').click();
    await page.locator('.term-item[data-id="2"]').click();
    console.log(name, 'selected', await page.locator('#term-label').innerText(), 'closed', !(await page.locator('#term-list').isVisible()), 'overflow', await page.evaluate(() => document.documentElement.scrollWidth - innerWidth));
    await page.close();
  }
  console.log('errors', errors);
  await browser.close();
})();
