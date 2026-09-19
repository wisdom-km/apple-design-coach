# Household Ledger (synthetic evaluation fixture)

This is a source-only React web fixture, used in Windows and macOS browsers.
Family users manually enter bills and import CSV weekly. CSV import and bulk
categorization must remain available. Keep the existing blue brand and React
component structure. New bill creation is the main daily task.

The form currently makes failed saves confusing. This excerpt is deliberately
not a complete application: no package manifest, server, renderer, or test runner
is supplied. Do not claim to have launched it. The save service can reject.

Entry: `src/BillForm.tsx`; shared styles: `src/tokens.css`.
