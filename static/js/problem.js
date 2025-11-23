document.addEventListener('DOMContentLoaded', function() {
    // Try multiple selectors to find the form
    const form = document.querySelector('form[method="POST"]') || 
                 document.querySelector('form[method=POST]') ||
                 document.querySelector('form');
    
    console.log('Form found:', form); // Debug line
    
    if (form) {
        form.addEventListener('submit', async function(e) {
            e.preventDefault(); // Prevent page reload
            console.log('Form submit prevented'); // Debug line
            
            const code = document.getElementById('code').value;
            const formData = new FormData();
            formData.append('code', code);
            
            // Show loading state
            const submitButton = form.querySelector('input[type="submit"]');
            const originalValue = submitButton.value;
            submitButton.value = 'Testing...';
            submitButton.disabled = true;
            
            try {
                const response = await fetch(window.location.href, {
                    method: 'POST',
                    body: formData
                });
                
                // Clone the response so we can read it multiple times if needed
                const responseClone = response.clone();
                
                // Try to parse as JSON
                let data;
                const contentType = response.headers.get('content-type');
                
                if (contentType && contentType.includes('application/json')) {
                    try {
                        data = await response.json();
                    } catch (jsonError) {
                        // If JSON parsing fails, try text
                        const text = await responseClone.text();
                        data = {
                            tests: [],
                            error: text || "Unknown error occurred"
                        };
                    }
                } else {
                    // Not JSON, read as text
                    const text = await response.text();
                    data = {
                        tests: [],
                        error: text || "Unknown error occurred"
                    };
                }
                
                if (data.error) {
                    // Show error but still try to display any tests
                    console.error(data.error);
                }
                
                if (data.tests && data.tests.length > 0) {
                    // Update test cases section
                    updateTestCases(data.tests);
                    
                    // Check if all tests passed
                    if (data.all_passed) {
                        showSuccessPopup();
                    }
                } else {
                    // If no tests, show error message
                    alert(data.error || 'Unable to run tests');
                }
                
            } catch (error) {
                console.error(error);
                // Show error but don't break the page
                alert(error.message);
            } finally {
                submitButton.value = originalValue;
                submitButton.disabled = false;
            }
        });
    } else {
        console.error('Form not found!'); // Debug line
    }
    
    function updateTestCases(tests) {
        const container = document.querySelector('div[style*="max-height: 400px"]');
        if (!container) {
            console.error('Test cases container not found');
            return;
        }
        
        const ol = container.querySelector('ol');
        if (!ol) {
            console.error('OL element not found');
            return;
        }
        
        // Clear existing test results
        ol.innerHTML = '';
        
        tests.forEach(test => {
            const li = document.createElement('li');
            li.style.cssText = 'border-radius: 8px; padding: 12px; margin: 8px 0; background-color: #53A4F5;';
            
            let html = '';
            for (const [input_name, input_value] of Object.entries(test.input)) {
                html += `<p style="color:white; font-family: Consolata, sans-serif;"><strong>${input_name} =</strong> ${input_value}</p>`;
            }
            html += `<p style="color:white; font-family: Consolata, sans-serif;"><strong>expected =</strong> ${test.expected}</p>`;
            html += `<p style="color:white; font-family: Consolata, sans-serif;"><strong>result =</strong> ${test.actual}</p>`;
            
            if (test.passed) {
                html += '<div class="user-test-case"><h4 class="btn-container btn-resultp">PASSED</h4></div>';
            } else {
                html += '<div class="user-test-case"><h4 class="btn-container btn-resultf">FAILED</h4></div>';
            }
            
            li.innerHTML = html;
            ol.appendChild(li);
        });
    }

    function showSuccessPopup() {
        // Create popup overlay
        const overlay = document.createElement('div');
        overlay.id = 'success-popup-overlay';
        overlay.style.cssText = 'position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.7); z-index: 10000; display: flex; justify-content: center; align-items: center;';
        
        // Create popup content
        const popup = document.createElement('div');
        popup.id = 'success-popup';
        popup.style.cssText = 'background: white; padding: 30px; border-radius: 10px; text-align: center; max-width: 500px; position: relative;';
        
        // Add GIF
        const gif = document.createElement('img');
        gif.src = '/static/images/win.gif'; 
        gif.style.cssText = 'max-width: 100%; height: auto;';
         
        // Add close button
        const closeBtn = document.createElement('button');
        closeBtn.textContent = 'Close';
        closeBtn.className = 'btn-container';
        closeBtn.style.cssText = 'margin-top: 20px; cursor: pointer;';
        closeBtn.onclick = function() {
            document.body.removeChild(overlay);
        };
        
        // Assemble popup
        popup.appendChild(gif);
        popup.appendChild(closeBtn);
        overlay.appendChild(popup);
        
        // Add to page
        document.body.appendChild(overlay);
        
        // Close on overlay click (outside popup)
        overlay.onclick = function(e) {
            if (e.target === overlay) {
                document.body.removeChild(overlay);
            }
        };
        
        // Auto-close after 5 seconds (optional)
        setTimeout(() => {
            if (document.body.contains(overlay)) {
                document.body.removeChild(overlay);
            }
        }, 10000);
    }
});