// PREMIUM PORTFOLIO - INTERACTIVE FEATURES
// Clean animations without cursor trail

// ==========================================
// ANIMATED PARTICLES BACKGROUND
// ==========================================
function createParticles() {
    const particlesContainer = document.getElementById('particles');
    const particleCount = 50;

    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        
        const size = Math.random() * 3 + 2;
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.top = `${Math.random() * 100}%`;
        
        const duration = Math.random() * 25 + 20;
        particle.style.animationDuration = `${duration}s`;
        
        const delay = Math.random() * 5;
        particle.style.animationDelay = `${delay}s`;
        
        const tx = (Math.random() - 0.5) * 250;
        const ty = (Math.random() - 0.5) * 250;
        particle.style.setProperty('--tx', `${tx}px`);
        particle.style.setProperty('--ty', `${ty}px`);
        
        particlesContainer.appendChild(particle);
    }
}

createParticles();

// ==========================================
// SMOOTH SCROLL
// ==========================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            const navbarHeight = document.querySelector('.navbar').offsetHeight;
            const targetPosition = targetElement.offsetTop - navbarHeight - 20;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// ==========================================
// NAVBAR SCROLL EFFECT & SCROLL HINT
// ==========================================
const navbar = document.querySelector('.navbar');
const scrollHint = document.getElementById('scrollHint');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 50) {
        navbar.style.background = 'rgba(1, 0, 13, 0.95)';
        navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
        
        // Hide scroll hint
        if (scrollHint) {
            scrollHint.classList.add('hidden');
        }
    } else {
        navbar.style.background = 'rgba(1, 0, 13, 0.85)';
        navbar.style.boxShadow = 'none';
        
        // Show scroll hint
        if (scrollHint) {
            scrollHint.classList.remove('hidden');
        }
    }
});

// ==========================================
// ACTIVE NAV LINK
// ==========================================
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 150) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// ==========================================
// SKIN CARD LIGHTBOX
// ==========================================
const skinCards = document.querySelectorAll('.skin-card');

skinCards.forEach((card, index) => {
    card.addEventListener('click', function() {
        const img = this.querySelector('.skin-image');
        const imgSrc = img.src;
        
        const lightbox = document.createElement('div');
        lightbox.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(1, 0, 13, 0.98);
            backdrop-filter: blur(20px);
            z-index: 10000;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            opacity: 0;
            transition: opacity 0.3s ease;
            padding: 40px;
        `;
        
        const lightboxImg = document.createElement('img');
        lightboxImg.src = imgSrc;
        lightboxImg.style.cssText = `
            max-width: 90%;
            max-height: 90%;
            border-radius: 20px;
            box-shadow: 0 20px 80px rgba(0, 0, 0, 0.8);
            transform: scale(0.95);
            transition: transform 0.3s ease;
        `;
        
        const closeBtn = document.createElement('div');
        closeBtn.innerHTML = '×';
        closeBtn.style.cssText = `
            position: absolute;
            top: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background: rgba(224, 255, 0, 0.1);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(224, 255, 0, 0.3);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 36px;
            color: #E0FF00;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 300;
        `;
        
        closeBtn.addEventListener('mouseenter', () => {
            closeBtn.style.background = 'rgba(224, 255, 0, 0.2)';
            closeBtn.style.transform = 'scale(1.1)';
        });
        
        closeBtn.addEventListener('mouseleave', () => {
            closeBtn.style.background = 'rgba(224, 255, 0, 0.1)';
            closeBtn.style.transform = 'scale(1)';
        });
        
        lightbox.appendChild(lightboxImg);
        lightbox.appendChild(closeBtn);
        document.body.appendChild(lightbox);
        document.body.style.overflow = 'hidden';
        
        setTimeout(() => {
            lightbox.style.opacity = '1';
            lightboxImg.style.transform = 'scale(1)';
        }, 10);
        
        const closeLightbox = () => {
            lightbox.style.opacity = '0';
            lightboxImg.style.transform = 'scale(0.95)';
            document.body.style.overflow = '';
            setTimeout(() => {
                document.body.removeChild(lightbox);
            }, 300);
        };
        
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox || e.target === closeBtn) {
                closeLightbox();
            }
        });
        
        const closeOnEsc = (e) => {
            if (e.key === 'Escape') {
                closeLightbox();
                document.removeEventListener('keydown', closeOnEsc);
            }
        };
        document.addEventListener('keydown', closeOnEsc);
    });
});

// ==========================================
// INTERSECTION OBSERVER FOR ANIMATIONS
// ==========================================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('.widget, .skin-card, .social-card').forEach(element => {
    observer.observe(element);
});

// ==========================================
// BUTTON RIPPLE EFFECT
// ==========================================
const buttons = document.querySelectorAll('.btn');

buttons.forEach(button => {
    button.addEventListener('click', function(e) {
        const rect = this.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const ripple = document.createElement('span');
        ripple.style.cssText = `
            position: absolute;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.5);
            transform: translate(-50%, -50%) scale(0);
            animation: rippleEffect 0.6s ease-out;
            pointer-events: none;
            left: ${x}px;
            top: ${y}px;
        `;
        
        this.style.position = 'relative';
        this.style.overflow = 'hidden';
        this.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
});

const style = document.createElement('style');
style.textContent = `
    @keyframes rippleEffect {
        to {
            transform: translate(-50%, -50%) scale(15);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// ==========================================
// LOADING ANIMATION
// ==========================================
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    }, 50);
});

// ==========================================
// CONSOLE BRANDING
// ==========================================
console.log('%c DAVA_WASAB ', 'background: #E0FF00; color: #01000D; font-size: 20px; font-weight: bold; padding: 10px 20px;');
console.log('%c Minecraft Designer • Premium Portfolio ', 'color: #F0FFD0; font-size: 14px; padding: 5px 0;');
console.log('%c DM me in Discord: Dava_Wasab ', 'color: #E0FF00; font-size: 12px;');
console.log('%c or with link: https://discord.com/users/1047829202705059840 ', 'color: #87C93D; font-size: 12px;');

// ==========================================
// GALLERY TABS
// ==========================================
const galleryTabs = document.querySelectorAll('.gallery-tab');
const galleryContainers = document.querySelectorAll('.gallery-container');

galleryTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const targetGallery = tab.getAttribute('data-gallery');
        
        // Remove active class from all tabs
        galleryTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        
        // Hide all galleries
        galleryContainers.forEach(container => {
            container.classList.remove('active');
        });
        
        // Show target gallery
        const targetContainer = document.getElementById(`gallery-${targetGallery}`);
        if (targetContainer) {
            targetContainer.classList.add('active');
        }
    });
});

// ==========================================
// DYNAMIC AGE CALCULATION
// ==========================================
function calculateAge() {
    const birthDate = new Date(2010, 7, 23); // August 23, 2010 (month is 0-indexed)
    const today = new Date();
    
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    
    // If birthday hasn't occurred this year yet, subtract 1
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    
    return age;
}

function updateAge() {
    const ageElement = document.querySelector('.stat-value');
    if (ageElement && ageElement.textContent.includes('Y.O.')) {
        const currentAge = calculateAge();
        ageElement.textContent = `${currentAge} Y.O.`;
    }
}

// ==========================================
// IMAGE PROTECTION
// ==========================================
// Disable right-click on images
document.addEventListener('contextmenu', (e) => {
    if (e.target.tagName === 'IMG') {
        e.preventDefault();
    }
});

// Disable dragging images
document.addEventListener('dragstart', (e) => {
    if (e.target.tagName === 'IMG') {
        e.preventDefault();
    }
});

// Disable image selection
const images = document.querySelectorAll('img');
images.forEach(img => {
    img.style.userSelect = 'none';
    img.style.webkitUserSelect = 'none';
    img.style.mozUserSelect = 'none';
    img.style.msUserSelect = 'none';
    img.setAttribute('draggable', 'false');
});

// ==========================================
// UTC+2 DIGITAL CLOCK
// ==========================================
function updateClock() {
    const clockElement = document.getElementById('utcClock');
    if (!clockElement) return;
    
    const now = new Date();
    // Get UTC time and add 2 hours
    const utcPlus2 = new Date(now.getTime() + (now.getTimezoneOffset() * 60000) + (2 * 3600000));
    
    const hours = String(utcPlus2.getHours()).padStart(2, '0');
    const minutes = String(utcPlus2.getMinutes()).padStart(2, '0');
    const seconds = String(utcPlus2.getSeconds()).padStart(2, '0');
    
    const timeString = `${hours}:${minutes}:${seconds}`;
    const timeElement = clockElement.querySelector('.clock-time');
    if (timeElement) {
        timeElement.textContent = timeString;
    }
}

// ==========================================
// INITIALIZE
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
    console.log('✨ Portfolio Loaded');
    console.log('🖼️ Gallery System Active');
    
    // Update age on load
    updateAge();
    
    // Check age daily (in case page stays open)
    setInterval(updateAge, 86400000); // 24 hours
    
    // Apply image protection to all images
    const allImages = document.querySelectorAll('img');
    allImages.forEach(img => {
        img.style.userSelect = 'none';
        img.setAttribute('draggable', 'false');
    });
    
    // Start clock
    updateClock();
    setInterval(updateClock, 1000); // Update every second
});
