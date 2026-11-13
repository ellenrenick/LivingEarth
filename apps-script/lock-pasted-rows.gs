/**
 * Locks each row of the students' "Paste here" sheet as soon as something is
 * pasted into it, so pasted results cannot be changed afterward.
 *
 * Install once (in the students' paste-in sheet):
 *   1. Extensions > Apps Script. Delete any starter code and paste this file.
 *   2. Save. Open Triggers (clock icon) > Add Trigger.
 *   3. Function: lockEditedRows. Event source: From spreadsheet. Event type: On edit.
 *   4. Save and approve the permission prompt with your own account.
 *
 * It runs as the account that installs it, so only that account can edit a
 * locked row. Rows 1 and 2 (banner and header) are already locked by hand.
 */
var SHEET_NAME = 'Paste here';
var FIRST_DATA_ROW = 3;

function lockEditedRows(e) {
  var sh = e.range.getSheet();
  if (sh.getName() !== SHEET_NAME) return;

  var first = Math.max(e.range.getRow(), FIRST_DATA_ROW);
  var last = e.range.getLastRow();
  if (last < first) return;

  var range = sh.getRange(first, 1, last - first + 1, sh.getMaxColumns());
  var hasData = range.getValues().some(function (row) {
    return row.some(function (cell) { return cell !== ''; });
  });
  if (!hasData) return;

  var protection = range.protect().setDescription('Locked after paste');
  protection.addEditor(Session.getEffectiveUser());
  protection.removeEditors(protection.getEditors().filter(function (user) {
    return user.getEmail() !== Session.getEffectiveUser().getEmail();
  }));
  if (protection.canDomainEdit()) protection.setDomainEdit(false);
}
