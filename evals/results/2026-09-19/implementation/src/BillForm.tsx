import { useRef, useState } from 'react';
import './tokens.css';

type Draft = { amount: string; category: string };
type Props = { saveBill: (draft: Draft) => Promise<void>; importCsv: () => void };

export function BillForm({ saveBill, importCsv }: Props) {
  const [draft, setDraft] = useState<Draft>({ amount: '', category: '' });
  const [notice, setNotice] = useState('');
  const [saving, setSaving] = useState(false);
  const saveInFlight = useRef(false);

  async function save() {
    if (saveInFlight.current) return;
    saveInFlight.current = true;
    setSaving(true);
    setNotice('');
    const pending = { ...draft };
    try {
      await saveBill(pending);
      setDraft({ amount: '', category: '' });
      setNotice('已保存');
    } catch {
      setNotice('保存失败，输入已保留。请再次点击“保存账单”重试。');
    } finally {
      saveInFlight.current = false;
      setSaving(false);
    }
  }

  return <section>
    <h1>家庭账单</h1>
    <nav aria-label="账单工具">
      <button onClick={importCsv}>导入 CSV</button>
      <a href="/bills/bulk-category">批量分类</a>
      <a href="/settings">设置</a>
    </nav>
    <label>金额<input value={draft.amount} disabled={saving}
      onChange={event => setDraft({ ...draft, amount: event.target.value })} /></label>
    <label>分类<input value={draft.category} disabled={saving}
      onChange={event => setDraft({ ...draft, category: event.target.value })} /></label>
    <button disabled={saving} onClick={save}>{saving ? '保存中…' : '保存账单'}</button>
    <p className="notice" role="status" aria-live="polite" aria-atomic="true">{notice}</p>
  </section>;
}
