---
title: Media
---

<style>
/* ── Media browser — wiki-native styling ── */
.ub-media-tabs {
  display: flex; gap: 0; margin-bottom: 16px;
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
}
.ub-media-tabs button {
  padding: 8px 20px;
  border: 1px solid transparent; border-bottom: none;
  background: transparent;
  color: var(--md-default-fg-color--light);
  cursor: pointer;
  font-family: var(--md-code-font-family);
  font-size: 0.82rem;
  border-radius: 6px 6px 0 0;
  transition: color 0.15s, background 0.15s;
  position: relative; bottom: -1px;
}
.ub-media-tabs button:hover { color: var(--md-default-fg-color); }
.ub-media-tabs button.active {
  background: var(--md-code-bg-color);
  color: var(--md-accent-fg-color);
  border-color: var(--md-default-fg-color--lightest);
  border-bottom-color: var(--md-code-bg-color);
}

.ub-file-list {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 8px; overflow: hidden;
  background: var(--md-code-bg-color);
}
.ub-file-row {
  display: flex; flex-wrap: wrap; align-items: center;
  padding: 10px 16px; gap: 4px 12px;
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
  font-size: 0.82rem;
  transition: background 0.1s;
}
.ub-file-row:last-child { border-bottom: none; }
.ub-file-row:hover { background: var(--md-default-fg-color--lightest); }
.ub-file-row .ub-name {
  flex: 1 1 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  font-family: var(--md-code-font-family); font-size: 0.78rem;
  color: var(--md-default-fg-color); cursor: pointer;
}
.ub-file-row .ub-name:hover { color: var(--md-accent-fg-color); }
.ub-file-row .ub-meta { display: flex; gap: 12px; align-items: center; flex: 1; min-width: 0; }
.ub-file-row .ub-size {
  color: var(--md-default-fg-color--light); white-space: nowrap;
  font-family: var(--md-code-font-family); font-size: 0.75rem;
}
.ub-file-row .ub-date {
  color: var(--md-default-fg-color--light); white-space: nowrap; font-size: 0.75rem;
}
.ub-file-row .ub-actions { display: flex; gap: 6px; flex-shrink: 0; margin-left: auto; }

.ub-media-btn {
  padding: 4px 11px; border-radius: 4px;
  border: 1px solid var(--md-default-fg-color--lightest);
  background: var(--md-code-bg-color);
  color: var(--md-default-fg-color--light);
  cursor: pointer;
  font-family: var(--md-code-font-family); font-size: 0.75rem;
  transition: color 0.15s, border-color 0.15s;
  text-decoration: none; display: inline-block; line-height: 1.4;
}
.ub-media-btn:hover {
  color: var(--md-accent-fg-color);
  border-color: var(--md-accent-fg-color);
}
.ub-file-row .ub-actions .ub-media-btn {
  color: #00f0c2;
  border-color: rgba(0,240,194,0.25);
  transition: filter 0.15s, border-color 0.15s;
}
.ub-file-row .ub-actions .ub-media-btn:hover {
  filter: drop-shadow(0 0 6px rgba(0,240,194,0.9));
  border-color: #00f0c2;
}

.ub-media-status {
  position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); z-index: 900;
  padding: 9px 20px; border-radius: 6px;
  font-size: 0.84rem; font-family: var(--md-code-font-family);
  border-left: 3px solid; pointer-events: none; max-width: 90vw;
}
.ub-media-status:empty { display: none; }
.ub-media-status.ok { background: rgba(0,240,194,0.15); color: var(--md-accent-fg-color); border-color: var(--md-accent-fg-color); }
.ub-media-status.err { background: rgba(248,81,73,0.15); color: #f85149; border-color: #f85149; }

.ub-media-empty { padding: 48px; text-align: center; color: var(--md-default-fg-color--light); font-size: 0.9rem; }
.ub-media-loading { padding: 24px; text-align: center; color: var(--md-default-fg-color--light); font-size: 0.85rem; }

.ub-preview-overlay {
  position: fixed; inset: 0; z-index: 800; background: rgba(0,0,0,0.8);
  display: flex; align-items: center; justify-content: center; cursor: pointer;
}
.ub-preview-overlay img, .ub-preview-overlay video {
  max-width: 90vw; max-height: 85vh; border-radius: 8px; background: #000; cursor: default;
}
.ub-preview-overlay .ub-close-btn {
  position: absolute; top: 12px; right: 18px;
  color: var(--md-default-fg-color);
  font-size: 1.8rem; cursor: pointer; line-height: 1; background: none; border: none;
  font-family: var(--md-code-font-family);
}
.ub-preview-overlay .ub-close-btn:hover { color: var(--md-accent-fg-color); }

.ub-vault-login {
  display: inline-flex; align-items: center;
  color: var(--md-default-fg-color--lighter);
}
.ub-vault-login:hover { color: var(--md-accent-fg-color); }
[data-ub-editor="off"] .ub-vault-login { display: none; }
</style>

<div class="ub-media-header" style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px">
  <div style="display:flex;align-items:center;gap:12px">
    <span style="font-size:0.9rem;color:var(--md-default-fg-color--light)">Community media archive</span>
    <a class="ub-media-btn" href="https://nan-gogh.github.io/ultrabroken-media/editor/" target="_blank" rel="noopener">Video Editor ↗</a>
  </div>
</div>

<div id="ub-media-status" class="ub-media-status"></div>

<div class="ub-media-tabs" id="ub-media-tabs">
  <button class="active" onclick="ubSwitchTab('image/')">image/</button>
  <button onclick="ubSwitchTab('video/')">video/</button>
  <button onclick="ubSwitchTab('social/')">social/</button>
</div>

<div id="ub-file-list">
  <div class="ub-media-loading">Loading…</div>
</div>

<script>
(function() {
  var WORKER = 'https://ultrabroken-media.gl1tchcr4vt.workers.dev';
  var shareIcon = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 13.02 14.4" width="12" height="13" style="vertical-align:middle;fill:#00f0c2"><path d="M10.85,10.18c-.55,0-1.04.22-1.42.56l-5.16-3c.04-.17.07-.33.07-.51s-.03-.34-.07-.51l5.1-2.97c.39.36.9.59,1.48.59,1.2,0,2.17-.97,2.17-2.17s-.97-2.17-2.17-2.17-2.17.97-2.17,2.17c0,.17.03.34.07.51l-5.1,2.97c-.39-.36-.9-.59-1.48-.59-1.2,0-2.17.97-2.17,2.17s.97,2.17,2.17,2.17c.57,0,1.08-.22,1.48-.59l5.15,3c-.04.15-.06.31-.06.48,0,1.16.95,2.1,2.11,2.1s2.11-.94,2.11-2.1-.95-2.11-2.11-2.11"/></svg>';
  var currentPrefix = 'image/';
  var statusTimer = null;

  window.ubSwitchTab = function(prefix) {
    currentPrefix = prefix;
    document.querySelectorAll('#ub-media-tabs button').forEach(function(b) {
      b.classList.toggle('active', b.textContent.trim() === prefix);
    });
    ubLoadFiles();
  };

  function showStatus(msg, ok, duration) {
    var el = document.getElementById('ub-media-status');
    el.className = 'ub-media-status ' + (ok ? 'ok' : 'err');
    el.textContent = msg;
    if (statusTimer) clearTimeout(statusTimer);
    statusTimer = setTimeout(function() { el.textContent = ''; el.className = 'ub-media-status'; }, duration || 5000);
  }

  function ubLoadFiles() {
    var container = document.getElementById('ub-file-list');
    container.innerHTML = '<div class="ub-media-loading">Loading\u2026</div>';

    fetchAllFiles(currentPrefix).then(function(allFiles) {
      if (allFiles.length === 0) {
        container.innerHTML = '<div class="ub-media-empty">No files in ' + escHtml(currentPrefix) + '</div>';
        return;
      }
      var html = '<div class="ub-file-list">';
      for (var i = 0; i < allFiles.length; i++) {
        var f = allFiles[i];
        var name = f.key.slice(currentPrefix.length);
        var size = formatSize(f.size);
        var date = new Date(f.uploaded).toLocaleDateString();
        html += '<div class="ub-file-row">'
          + '<span class="ub-name" onclick="ubPreview(\'' + escAttr(f.key) + '\')" title="' + escHtml(f.key) + '">' + escHtml(name) + '</span>'
          + '<span class="ub-meta"><span class="ub-size">' + size + '</span>'
          + '<span class="ub-date">' + date + '</span></span>'
          + '<span class="ub-actions">'
          + '  <a class="ub-media-btn" href="' + WORKER + '/' + encodeURI(f.key) + '" download title="Download">&#1F87B;</a>'
          + '  <button class="ub-media-btn" onclick="ubCopyUrl(\'' + escAttr(f.key) + '\')" title="Copy URL">' + shareIcon + '</button>'
          + '</span></div>';
      }
      html += '</div>';
      container.innerHTML = html;
    }).catch(function() {
      container.innerHTML = '<div class="ub-media-empty">Error loading files</div>';
    });
  }

  function fetchAllFiles(prefix) {
    var allFiles = [];
    function page(cursor) {
      var params = new URLSearchParams({ prefix: prefix });
      if (cursor) params.set('cursor', cursor);
      return fetch(WORKER + '/api/list?' + params).then(function(res) {
        if (!res.ok) throw new Error('HTTP ' + res.status);
        return res.json();
      }).then(function(data) {
        allFiles = allFiles.concat(data.files);
        if (data.truncated && data.cursor) return page(data.cursor);
        return allFiles;
      });
    }
    return page(null);
  }

  function formatSize(bytes) {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1048576) return (bytes / 1024).toFixed(1) + ' KB';
    return (bytes / 1048576).toFixed(1) + ' MB';
  }

  function escHtml(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
  function escAttr(s) { return s.replace(/'/g, "\\'").replace(/"/g, '&quot;'); }

  window.ubCopyUrl = function(key) {
    var url = WORKER + '/' + key;
    navigator.clipboard.writeText(url).then(
      function() { showStatus('Copied: ' + url, true); },
      function() { showStatus('Failed to copy URL', false); }
    );
  };

  window.ubPreview = function(key) {
    var url = WORKER + '/' + key;
    var isVideo = /\.(mp4|mov|webm|mkv)$/i.test(key);
    var overlay = document.createElement('div');
    overlay.className = 'ub-preview-overlay';
    overlay.onclick = function(e) { if (e.target === overlay) closeOverlay(); };
    function closeOverlay() { if (overlay.parentNode) document.body.removeChild(overlay); document.removeEventListener('keydown', onKey); }
    function onKey(e) { if (e.key === 'Escape') closeOverlay(); }
    document.addEventListener('keydown', onKey);
    var close = document.createElement('button');
    close.className = 'ub-close-btn';
    close.innerHTML = '&times;';
    close.onclick = closeOverlay;
    overlay.appendChild(close);
    if (isVideo) {
      var vid = document.createElement('video');
      vid.controls = true; vid.autoplay = true; vid.playsInline = true; vid.muted = true;
      vid.onerror = function() {
        if (overlay.parentNode) {
          vid.remove();
          var msg = document.createElement('div');
          msg.style.cssText = 'text-align:center;color:var(--md-default-fg-color);padding:32px;';
          msg.innerHTML = '<p style="margin-bottom:12px;color:var(--md-default-fg-color--light);">This browser cannot play this video format.</p>'
            + '<a class="ub-media-btn" href="' + url + '" download style="font-size:0.85rem;padding:8px 18px;">Download to view</a>';
          overlay.appendChild(msg);
        }
      };
      vid.src = url;
      overlay.appendChild(vid);
    } else {
      var img = document.createElement('img');
      img.src = url; img.alt = key;
      overlay.appendChild(img);
    }
    document.body.appendChild(overlay);
  };

  // Inject login icon into editor row
  var actions = document.querySelector('.ub-page-actions');
  if (actions) {
    var login = document.createElement('a');
    login.href = WORKER + '/manage/';
    login.target = '_blank';
    login.rel = 'noopener';
    login.className = 'md-content__button ub-vault-login';
    login.title = 'Media Vault';
    login.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="width:1.2rem;height:1.2rem"><path fill="currentColor" d="M11 7L9.6 8.4l2.6 2.6H2v2h10.2l-2.6 2.6L11 17l5-5-5-5zm9 12h-8v2h8c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2h-8v2h8v14z"/></svg>';
    actions.appendChild(login);
  }

  ubLoadFiles();
})();
</script>
