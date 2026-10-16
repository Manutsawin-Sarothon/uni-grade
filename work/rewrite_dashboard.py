from pathlib import Path

source = Path(__file__).resolve().parent.parent / 'uni-grade' / 'index.html'
content = source.read_text(encoding='utf-8')
start = content.index('const renderDashboard = () => {')
end = content.index('\nconst renderSubjectsList = () => {', start)
dashboard = r'''const renderDashboard = () => {
  const subjects = getSubjects(), termR = calcTermGPA(getTerm()), cum = calcCumGPA();
  const goal = appData.gpaTarget || 3.0;

  // Match the existing target planner's locked-score and remaining-credit rules.
  let completedCredits = 0, completedPoints = 0, remainingCredits = 0, remainingCount = 0;
  subjects.forEach(s => {
    const result = calcSubject(s), grade = scoreToGrade(result.score, s), credits = parseFloat(s.credits) || 0;
    if (s.quickMode && s.quickGrade === 'W') return;
    const assessed = (s.quickMode && s.quickGrade) || (!s.quickMode && (s.categories || []).some(c => c.items.some(i => i.locked && i.score !== '')));
    if (assessed && grade.gp !== null && grade.gp !== undefined) {
      completedCredits += credits;
      completedPoints += grade.gp * credits;
    } else {
      remainingCredits += credits;
      remainingCount++;
    }
  });
  const required = remainingCredits ? Math.max(0, (goal * (completedCredits + remainingCredits) - completedPoints) / remainingCredits) : null;
  const isReachable = required === null || required <= 4;
  const current = completedCredits ? completedPoints / completedCredits : null;
  const goalMessage = !subjects.length
    ? 'เพิ่มวิชาแรกเพื่อเริ่มวางแผนเกรดเป้าหมาย'
    : required === null
      ? (current !== null && current >= goal ? 'ถึงเป้าหมายแล้วในเทอมนี้' : 'ประเมินครบทุกวิชาแล้ว')
      : isReachable
        ? `ต้องทำ GP เฉลี่ย ${required.toFixed(2)} ใน ${remainingCount} วิชาที่เหลือ`
        : 'เป้าหมายนี้ต้องใช้ GP มากกว่า 4.00 ในวิชาที่เหลือ';

  const courseRows = subjects.map((s, index) => {
    const result = calcSubject(s), grade = scoreToGrade(result.score, s);
    const score = s.quickMode ? (s.quickGrade || '–') : result.score.toFixed(1);
    return `<button class="dashboard-course" type="button" onclick="window.switchView('subject', ${s.id})" aria-label="เปิดวิชา ${s.name}">
      <span class="course-index">${String(index + 1).padStart(2, '0')}</span>
      <span class="course-name">${s.name}<small>${s.credits} หน่วยกิต</small></span>
      <span class="course-score grade-letter">${score}</span>
      <span class="course-grade tag ${grade.letter}">${grade.letter}</span>
      <span class="course-arrow" aria-hidden="true">↗</span>
    </button>`;
  }).join('');

  const today = new Date(); today.setHours(0, 0, 0, 0);
  const deadlines = getAllDeadlines().filter(d => new Date(d.dl) >= today).slice(0, 3);
  const deadlineRows = deadlines.map(d => {
    const date = new Date(d.dl);
    const label = Number.isNaN(date.getTime()) ? d.dl : date.toLocaleDateString('th-TH', { day: 'numeric', month: 'short' });
    return `<button class="dashboard-deadline" type="button" onclick="window.switchView('subject', ${d.sId})">
      <span class="deadline-date">${label}</span><span class="deadline-detail"><strong>${d.item}</strong><small>${d.subj}</small></span><span aria-hidden="true">↗</span>
    </button>`;
  }).join('');

  document.getElementById('view-dashboard').innerHTML = `
    <section class="dashboard-goal ani" aria-label="สรุปเป้าหมายเกรด">
      <div class="goal-copy"><div class="goal-overline">เป้าหมาย GPA · ${getTerm().name}</div>
        <div class="goal-number grade-letter">${goal.toFixed(2)}</div>
        <p class="goal-message ${isReachable ? '' : 'goal-alert'}">${goalMessage}</p>
        <button class="goal-action" type="button" onclick="window.switchView('targets')">วางแผนให้ถึงเป้าหมาย <span aria-hidden="true">↗</span></button>
      </div>
      <div class="goal-aside"><div class="goal-aside-label">ผลที่ประเมินแล้ว</div><div class="goal-current grade-letter">${current === null ? '–' : current.toFixed(2)}</div><div class="goal-aside-foot">${completedCredits} จาก ${completedCredits + remainingCredits} หน่วยกิต</div><div class="goal-rule"></div><div class="goal-aside-label">GPA เทอมนี้</div><div class="goal-term grade-letter">${termR.gpa === null ? '–' : termR.gpa.toFixed(2)}</div></div>
    </section>
    <section class="dashboard-index ani" aria-label="รายวิชาในเทอมนี้">
      <div class="dashboard-section-head"><div><span class="section-counter">01 / COURSE INDEX</span><h2>รายวิชาในเทอมนี้</h2></div><button type="button" class="text-link" onclick="window.switchView('subjects')">ดูรายวิชาทั้งหมด ↗</button></div>
      ${subjects.length ? `<div class="dashboard-courses">${courseRows}</div>` : emptyStateHTML('book', 'ยังไม่มีรายวิชา', 'เพิ่มวิชาแรกเพื่อเริ่มวางแผนเป้าหมาย', `<button class="btn btn-accent" onclick="window.switchView('subjects'); document.getElementById('btn-add-subject').click();">เพิ่มรายวิชา</button>`)}
    </section>
    <section class="dashboard-side ani" aria-label="กำหนดการใกล้ถึง">
      <div class="dashboard-section-head"><div><span class="section-counter">02 / UPCOMING</span><h2>กำหนดการถัดไป</h2></div></div>
      ${deadlines.length ? `<div class="dashboard-deadlines">${deadlineRows}</div>` : '<p class="dashboard-empty">ยังไม่มีกำหนดการถัดไป</p>'}
      <button type="button" class="text-link" onclick="window.switchView('planner')">เปิดปฏิทิน ↗</button>
    </section>
    <section class="dashboard-history ani" aria-label="ภาพรวมผลการเรียน">
      <div class="dashboard-section-head"><div><span class="section-counter">03 / PROGRESS</span><h2>ภาพรวมผลการเรียน</h2></div><button type="button" class="text-link" onclick="window.switchView('analytics')">ดูการวิเคราะห์ ↗</button></div>
      <div class="history-content"><div class="history-stat"><span>GPA สะสม</span><strong class="grade-letter">${cum.gpa === null ? '–' : cum.gpa.toFixed(2)}</strong><small>${cum.credits} หน่วยกิตรวม</small></div><div class="history-chart"><canvas id="chart-dashboard-trend" aria-label="แนวโน้ม GPA รายเทอม"></canvas></div></div>
    </section>
  `;

  const ctx = document.getElementById('chart-dashboard-trend');
  if (ctx) {
    if (chartInstances.dashTrend) chartInstances.dashTrend.destroy();
    const labels = appData.terms.map(t => t.name);
    const data = appData.terms.map(t => { const r = calcTermGPA(t); return r.gpa !== null ? parseFloat(r.gpa.toFixed(2)) : null; });
    if (!data.some(value => value !== null)) {
      ctx.parentElement.innerHTML = '<p class="dashboard-empty">เมื่อมีผลการเรียน กราฟจะแสดงแนวโน้มที่นี่</p>';
      return;
    }
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    const textColor = chartTextColor(isDark);
    chartInstances.dashTrend = new Chart(ctx, { type: 'line', data: { labels, datasets: [{ label: 'GPA', data, borderColor: isDark ? '#83d9ab' : '#116b67', backgroundColor: isDark ? 'rgba(131,217,171,.12)' : 'rgba(17,107,103,.08)', borderWidth: 2, tension: 0.35, fill: true, pointBackgroundColor: isDark ? '#83d9ab' : '#116b67', pointBorderColor: '#fff', pointRadius: 4, pointBorderWidth: 2 }] }, options: { responsive: true, maintainAspectRatio: false, scales: { y: { min: 0, max: 4, border: { display: false }, grid: { color: 'var(--chart-grid)' }, ticks: { color: textColor, font: { family: "'DM Mono', monospace" } } }, x: { border: { display: false }, grid: { display: false }, ticks: { color: textColor, font: { family: "-apple-system, BlinkMacSystemFont, sans-serif", weight: 600 } } } }, plugins: { legend: { display: false }, tooltip: chartTooltip(isDark) } } });
  }
};
'''
source.write_text(content[:start] + dashboard + content[end:], encoding='utf-8')
