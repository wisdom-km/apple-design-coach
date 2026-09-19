// Source-only regression checks. These execute the real save handler with state
// setters substituted; they do not render React, compile TSX, or test a screen reader.
// Run: node check-save.cjs
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const source = fs.readFileSync(path.join(__dirname, 'src/BillForm.tsx'), 'utf8');
const start = source.indexOf('  async function save() {');
const end = source.indexOf('\n  return <section>', start);
assert.ok(start >= 0 && end > start, 'Expected save handler boundary');
const createSave = new Function(
  'saveBill', 'draft', 'saveInFlight', 'setDraft', 'setNotice', 'setSaving',
  source.slice(start, end) + '\nreturn save;'
);

function fixture(saveBill) {
  const state = { draft: { amount: '128.50', category: '餐饮' }, notice: '', saving: false };
  const lock = { current: false };
  return {
    state,
    render: () => createSave(saveBill, state.draft, lock,
      value => { state.draft = value; },
      value => { state.notice = value; },
      value => { state.saving = value; })
  };
}

async function main() {
  let calls = 0;
  let rejectPending;
  let resolvePending;
  const submitted = [];
  const form = fixture(draft => {
    calls++;
    submitted.push(draft);
    return new Promise((resolve, reject) => { resolvePending = resolve; rejectPending = reject; });
  });
  const original = { ...form.state.draft };
  const save = form.render();
  const first = save();
  assert.equal(form.state.saving, true);
  assert.deepEqual(form.state.draft, original, 'Keep draft while saving');
  await save();
  await form.render()();
  assert.equal(calls, 1, 'Ignore repeated submission before and after rerender');
  rejectPending(new Error('Service unavailable'));
  await first;
  assert.deepEqual(form.state.draft, original, 'Keep draft after rejection');
  assert.equal(form.state.saving, false, 'Allow retry after rejection');
  assert.ok(form.state.notice.length > 2, 'Provide actionable failure feedback');

  const retry = form.render()();
  assert.equal(form.state.notice, '', 'Clear stale notice before another attempt');
  assert.equal(calls, 2);
  assert.deepEqual(submitted[1], original, 'Retry the retained draft');
  resolvePending();
  await retry;
  assert.deepEqual(form.state.draft, { amount: '', category: '' }, 'Clear only after success');
  assert.equal(form.state.saving, false);
  assert.ok(form.state.notice);

  const syncFailure = fixture(() => { throw new Error('Synchronous failure'); });
  await syncFailure.render()();
  assert.deepEqual(syncFailure.state.draft, original);
  assert.equal(syncFailure.state.saving, false);
  await syncFailure.render()();
  assert.deepEqual(syncFailure.state.draft, original, 'Keep draft after repeated failures');

  // Static JSX checks only: live-region attributes and existing controls.
  assert.match(source, /<p[^>]*role="status"[^>]*aria-live="polite"[^>]*aria-atomic="true"[^>]*>\{notice\}<\/p>/);
  assert.match(source, /onClick=\{importCsv\}/);
  assert.match(source, /href="\/bills\/bulk-category"/);
  assert.equal((source.match(/disabled=\{saving\}/g) || []).length, 3);
  assert.match(fs.readFileSync(path.join(__dirname, 'src/tokens.css'), 'utf8'), /--brand: #165dcc/);
  console.log('PASS: handler simulation (pending, rejection, retry, success, duplicate submission, repeated/synchronous failure).');
  console.log('PASS: static JSX live-region/controls and brand checks.');
  console.log('Not tested: TSX build, real React rendering, browser interaction, assistive-technology announcements, backend integration.');
}

main().catch(error => { console.error(error); process.exitCode = 1; });
