const { chromium } = require('playwright-core');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', headless: true, args: ['--allow-file-access-from-files'] });
  const errors = [];
  for (const [name, width, height] of [['desktop', 1440, 900], ['mobile', 390, 844]]) {
    const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 1 });
    page.on('pageerror', error => errors.push(`${name}: ${error.message}`));
    await page.goto('file:///' + path.resolve(__dirname, '../uni-grade/index.html').replace(/\\/g, '/'));
    const skip = page.locator('#btn-onboard-skip');
    if (await skip.isVisible()) await skip.click();
    await page.locator('#btn-login-guest').click();
    await page.evaluate(() => {
      const data = { currentTermId: 1, userProfilePic: null, gpaTarget: 3.5, terms: [{ id: 1, name: 'เทอม 1', subjects: [
        { id: 1001, name: 'แคลคูลัสสำหรับวิศวกร', credits: 3, categories: [], quickMode: true, quickGrade: 'B+' },
        { id: 1002, name: 'ภาษาอังกฤษเชิงวิชาการ', credits: 3, categories: [], quickMode: true, quickGrade: null },
        { id: 1003, name: 'การออกแบบระบบ', credits: 3, categories: [], quickMode: true, quickGrade: null }
      ] }] };
      localStorage.setItem('st_data', JSON.stringify(data));
      localStorage.setItem('guest_mode', 'true');
      localStorage.setItem('onboarding_done_v2', 'true');
    });
    await page.reload();
    await page.locator('#btn-login-guest').click();
    await page.waitForTimeout(1000);
    console.log(name, await page.locator('#view-dashboard').innerText().then(s => s.slice(0, 350)));
    console.log(name, 'overflow', await page.evaluate(() => document.documentElement.scrollWidth - innerWidth));
    await page.screenshot({ path: path.resolve(__dirname, `dashboard-${name}.png`), fullPage: true });
    if (name === 'desktop') await page.locator('#dock-hide-grades').click();
    else await page.evaluate(() => document.body.classList.add('hide-grades'));
    await page.waitForTimeout(700);
    console.log(name, 'privacyMask', await page.locator('.goal-message').evaluate(el => getComputedStyle(el).filter));
    if (name === 'desktop') await page.locator('#dock-hide-grades').click();
    else await page.evaluate(() => document.body.classList.remove('hide-grades'));
    await page.locator('.goal-action').click();
    console.log(name, 'targetVisible', await page.locator('#view-targets').isVisible(), 'dashboardHidden', !(await page.locator('#view-dashboard').isVisible()));
    await page.waitForTimeout(900);
    await page.screenshot({ path: path.resolve(__dirname, `targets-${name}.png`), fullPage: true });
    console.log(name, 'targetCard', await page.locator('.target-course').first().boundingBox(), 'dock', await page.locator('.dock-container').boundingBox());
    await page.locator('.target-course').first().focus();
    await page.keyboard.press('Enter');
    console.log(name, 'courseVisible', await page.locator('#view-subject').isVisible());
    await page.close();
  }
  console.log('errors', errors);
  await browser.close();
})();
