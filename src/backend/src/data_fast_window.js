/**
 * 仅供 fast_window_preload 使用的轻量 data 方法，避免引入 chat/mcp 等大依赖。
 * 只包含：saveFastInputWindowPosition, copyText, coderedirect
 */

function saveFastInputWindowPosition(position) {
  const configDoc = utools.db.get("config");
  if (configDoc) {
    const data = configDoc.data;
    data.config.fastWindowPosition = position;
    utools.db.put({
      _id: "config",
      data: data,
      _rev: configDoc._rev
    });
  }
}

function copyText(content) {
  utools.copyText(content);
}

async function coderedirect(label, payload) {
  utools.redirect(label, payload);
}

module.exports = {
  saveFastInputWindowPosition,
  copyText,
  coderedirect,
};
