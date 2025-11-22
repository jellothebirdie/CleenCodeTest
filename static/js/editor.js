document.addEventListener('DOMContentLoaded', () => {
  const codeInput = document.getElementById('code');
  const highlightCode = document.getElementById('highlight-code');
  const highlightLayer = document.getElementById('highlight-layer');
  const testBtn = document.getElementById('testBtn');
  const codeForm = document.getElementById('codeForm');

  if (!codeInput || !highlightCode || !highlightLayer) return;

  function escapeHtml(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function updateHighlight() {
    const code = codeInput.value;
    let highlighted = escapeHtml(code);

    // Process in order: first strings/comments, then keywords, then numbers
    // This prevents keywords inside strings from being highlighted
    
    // Highlight strings and comments by replacing them with placeholders
    const placeholders = [];
    let placeholderIndex = 0;
    
    // Protect triple-quoted strings first
    highlighted = highlighted.replace(/("""[\s\S]*?"""|'''[\s\S]*?''')/g, (match) => {
      const placeholder = `__PLACEHOLDER_${placeholderIndex}__`;
      placeholders[placeholderIndex] = '<span class="string">' + match + '</span>';
      placeholderIndex++;
      return placeholder;
    });
    
    // Protect single/double quoted strings
    highlighted = highlighted.replace(/("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')/g, (match) => {
      const placeholder = `__PLACEHOLDER_${placeholderIndex}__`;
      placeholders[placeholderIndex] = '<span class="string">' + match + '</span>';
      placeholderIndex++;
      return placeholder;
    });
    
    // Protect comments
    highlighted = highlighted.replace(/(#.*?$|\/\/.*?$)/gm, (match) => {
      const placeholder = `__PLACEHOLDER_${placeholderIndex}__`;
      placeholders[placeholderIndex] = '<span class="comment">' + match + '</span>';
      placeholderIndex++;
      return placeholder;
    });

    // Now highlight keywords (won't match inside protected strings/comments)
    highlighted = highlighted.replace(/\b(def|class|return|if|else|elif|for|while|in|import|from|as|with|try|except|pass|lambda|yield|function|const|let|var|async|await)\b/g,
      '<span class="keyword">$1</span>');

    // Highlight numbers
    highlighted = highlighted.replace(/\b(\d+)\b/g, '<span class="number">$1</span>');

    // Restore protected content
    for (let i = 0; i < placeholders.length; i++) {
      highlighted = highlighted.replace(`__PLACEHOLDER_${i}__`, placeholders[i]);
    }

    highlightCode.innerHTML = highlighted;
  }

  codeInput.addEventListener('input', updateHighlight);
  codeInput.addEventListener('scroll', () => {
    highlightLayer.scrollLeft = codeInput.scrollLeft;
    highlightLayer.scrollTop = codeInput.scrollTop;
  });

  // Initialize highlight
  updateHighlight();

  // Tab insertion and smart Enter indentation
  codeInput.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      e.preventDefault();
      const start = codeInput.selectionStart;
      const end = codeInput.selectionEnd;
      const value = codeInput.value;

      if (e.shiftKey) {
        // Unindent
        const selected = value.slice(start, end);
        if (start !== end) {
          const changed = selected.replace(/^(\t| {1,4})/gm, '');
          codeInput.value = value.slice(0, start) + changed + value.slice(end);
          codeInput.selectionStart = start;
          codeInput.selectionEnd = start + changed.length;
        } else {
          const lineStart = value.lastIndexOf('\n', start - 1) + 1;
          const line = value.slice(lineStart, start);
          if (/^(\t| {1,4})/.test(line)) {
            const newLine = line.replace(/^(\t| {1,4})/, '');
            codeInput.value = value.slice(0, lineStart) + newLine + value.slice(start);
            const newPos = lineStart + newLine.length;
            codeInput.selectionStart = codeInput.selectionEnd = newPos;
          }
        }
      } else {
        // Indent
        if (start !== end) {
          const selected = value.slice(start, end);
          const changed = selected.replace(/^/gm, '\t');
          codeInput.value = value.slice(0, start) + changed + value.slice(end);
          codeInput.selectionStart = start;
          codeInput.selectionEnd = start + changed.length;
        } else {
          codeInput.value = value.slice(0, start) + '\t' + value.slice(end);
          codeInput.selectionStart = codeInput.selectionEnd = start + 1;
        }
      }
      updateHighlight();
      return;
    }

    if (e.key === 'Enter') {
      e.preventDefault();
      const start = codeInput.selectionStart;
      const value = codeInput.value;
      const lineStart = value.lastIndexOf('\n', start - 1) + 1;
      const line = value.slice(lineStart, start);
      const indentMatch = line.match(/^\s*/);
      const indent = indentMatch ? indentMatch[0] : '';
      const addExtra = /[:({[\]]\s*$/.test(line) ? '\t' : '';
      const insert = '\n' + indent + addExtra;
      codeInput.value = value.slice(0, start) + insert + value.slice(codeInput.selectionEnd);
      const caret = start + insert.length;
      codeInput.selectionStart = codeInput.selectionEnd = caret;
      updateHighlight();
      return;
    }
  });

  // Console output handler
  const consoleOutput = document.getElementById('console-output');
  const clearBtn = document.getElementById('clearBtn');
  
  function addToConsole(message, type = 'log') {
    if (!consoleOutput) return;
    const line = document.createElement('div');
    line.className = type === 'error' ? 'console-error' : 'console-log';
    line.textContent = message;
    consoleOutput.appendChild(line);
    consoleOutput.scrollTop = consoleOutput.scrollHeight;
  }

  if (clearBtn) {
    clearBtn.addEventListener('click', (e) => {
      e.preventDefault();
      if (consoleOutput) {
        consoleOutput.innerHTML = '';
      }
    });
  }

  // Test button handler
  if (testBtn) {
    testBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const code = codeInput.value;
      
      // Clear console before running
      if (consoleOutput) {
        consoleOutput.innerHTML = '';
      }
      
      addToConsole('Running code...', 'log');
      
      // Send code to backend for execution
      fetch('/test/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'code=' + encodeURIComponent(code)
      })
      .then(response => response.text())
      .then(data => {
        if (data && data.trim()) {
          // Display the output from the backend
          const lines = data.trim().split('\n');
          lines.forEach(line => {
            addToConsole(line, 'log');
          });
        } else {
          addToConsole('Code executed with no output', 'log');
        }
      })
      .catch(error => {
        addToConsole('Error: ' + error.message, 'error');
      });
    });
  }
});
