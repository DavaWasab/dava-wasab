// ==========================================
// DAVAWASAB STYLESET - JAVASCRIPT
// UI Components Library Scripts
// ==========================================

// ==========================================
// PARTICLES BACKGROUND
// ==========================================
function createParticles() {
    const particlesContainer = document.getElementById('particles');
    if (!particlesContainer) return;
    
    const particleCount = 50;

    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        
        // Random size
        const size = Math.random() * 3 + 2;
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        
        // Random position
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.top = `${Math.random() * 100}%`;
        
        // Random animation duration
        const duration = Math.random() * 25 + 20;
        particle.style.animationDuration = `${duration}s`;
        
        // Random animation delay
        const delay = Math.random() * 5;
        particle.style.animationDelay = `${delay}s`;
        
        // Random movement direction
        const tx = (Math.random() - 0.5) * 250;
        const ty = (Math.random() - 0.5) * 250;
        particle.style.setProperty('--tx', `${tx}px`);
        particle.style.setProperty('--ty', `${ty}px`);
        
        particlesContainer.appendChild(particle);
    }
}

// ==========================================
// SMOOTH SCROLL
// ==========================================
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// ==========================================
// COPY TO CLIPBOARD
// ==========================================
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        // Show notification
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(224, 255, 0, 0.95);
            color: #01000D;
            padding: 16px 24px;
            border-radius: 12px;
            font-weight: 700;
            z-index: 9999;
            animation: slideIn 0.3s ease;
        `;
        notification.textContent = `Copied: ${text}`;
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy:', err);
    });
}

// Add copy functionality to code elements
function initCopyCode() {
    document.querySelectorAll('code').forEach(codeBlock => {
        codeBlock.style.cursor = 'pointer';
        codeBlock.title = 'Click to copy';
        
        codeBlock.addEventListener('click', function() {
            copyToClipboard(this.textContent);
        });
    });
}

// ==========================================
// WIDGET INTERACTIONS
// ==========================================
function initWidgetInteractions() {
    // Add ripple effect to widgets
    document.querySelectorAll('.widget').forEach(widget => {
        widget.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            ripple.style.cssText = `
                position: absolute;
                border-radius: 50%;
                background: rgba(224, 255, 0, 0.3);
                width: 20px;
                height: 20px;
                animation: ripple 0.6s ease-out;
                pointer-events: none;
            `;
            
            const rect = this.getBoundingClientRect();
            ripple.style.left = (e.clientX - rect.left - 10) + 'px';
            ripple.style.top = (e.clientY - rect.top - 10) + 'px';
            
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
}

// ==========================================
// ANIMATIONS
// ==========================================
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            transform: scale(15);
            opacity: 0;
        }
    }
    
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// ==========================================
// INITIALIZE
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
    console.log('%c DAVAWASAB STYLESET ', 'background: #E0FF00; color: #01000D; font-size: 20px; font-weight: bold; padding: 10px 20px;');
    console.log('%c UI Components Library Loaded ', 'color: #E0FF00; font-size: 14px;');
    
    // Initialize all features
    createParticles();
    initSmoothScroll();
    initCopyCode();
    initWidgetInteractions();
    
    console.log('%c ✓ All components initialized ', 'color: #87C93D; font-size: 12px;');
});

// ==========================================
// EXPORT FUNCTIONS
// ==========================================
window.DavaWasabStyleset = {
    createParticles,
    copyToClipboard,
    initSmoothScroll,
    initCopyCode,
    initWidgetInteractions
};
